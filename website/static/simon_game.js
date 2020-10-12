var gamePattern = [];
const buttonColors = ["red", "blue", "green", "yellow"];
var userClickedPattern =[];
var started = false;
var level =0;


function nextSequency(){
    let randomNumber=Math.floor(Math.random()*4);
    var randomChosenColor = buttonColors[randomNumber];
    $("#"+randomChosenColor).fadeOut(100).fadeIn(100);
    playSound(randomChosenColor)
    gamePattern.push(randomChosenColor);
    level++
    $("#level-title").html("Level " + level);

} 


$(".game-btn").on("click", function(){
    if (!started){
        setTimeout(nextSequency,500);
          started=true

          $(".game-btn").addClass("off")
          }
})

$(".simon-btn").on("click", function () {
 var userChosenColor = $(this).attr("id");
 userClickedPattern.push(userChosenColor);
 playSound(userChosenColor);
 animatePress(userChosenColor);
 checkAnswer(userClickedPattern.length-1)

})

function playSound (name){
   
    if (name==="blue"){
        var audioBlue = new Audio('/static/simon/sounds/blue.mp3');
        audioBlue.play();
    }else if (name ==="green"){
        var audioGreen = new Audio('/static/simon/sounds/green.mp3');
    audioGreen.play();
    }else if (name ==="red"){
        var audioRed = new Audio('/static/simon/sounds/red.mp3');
    audioRed.play();
    }else if (name ==="yellow"){
        var audioYellow = new Audio('/static/simon/sounds/yellow.mp3');
    audioYellow.play();
    }
   
}

function animatePress(currentColor){
 $("." + currentColor).addClass("pressed");
 setTimeout(function(){$("."+currentColor).removeClass("pressed")},100);
}



$(document).on('keypress',function() {
  if (!started){
    setTimeout(nextSequency,500);
      started=true
      }
  }
)

function checkAnswer(currentLevel){

    if (userClickedPattern[currentLevel]===gamePattern[currentLevel]){
        console.log("successss")
        if (userClickedPattern.length === gamePattern.length){
            setTimeout(nextSequency,1000)
            userClickedPattern=[]
        }

    } else {
        var audioWrong = new Audio('/static/simon/sounds/wrong.mp3');
        audioWrong.play();

        $(".simon-game-bg").addClass("game-over");

        setTimeout(function(){
            $(".simon-game-bg").removeClass("game-over")
        },100)

        $("#level-title").html("Game Over, press any key to restart")
        startOver()
    }
    
    

}

function startOver(){
     gamePattern = [];
userClickedPattern =[];

level = 0;
started=false
$(".game-btn").removeClass("off")
$(".game-btn").html("Play again?")
}