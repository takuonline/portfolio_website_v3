
var drums=document.querySelectorAll(".drum").length;

for (var i=0; i<drums;i++) {
document.querySelectorAll("button")[i].addEventListener("click",
function ()  {
  makesound(this.innerHTML)
  anime(this.innerHTML)
})
}

function anime(key) {
var activebutton = document.querySelector("." + key);
activebutton.classList.add("pressed");
setTimeout(function(){
  activebutton.classList.remove("pressed");
},100)
}

document.addEventListener("keypress", function(event){
  makesound(event.key)
  anime(event.key)
})

function makesound(key){
  switch (key) {
    case "w":
      var tom1=new Audio("/static/drum-kit/sounds/tom-1.mp3");
      tom1.play();
      break;

    case "a":
    var tom2=new Audio("static/drum-kit/sounds/tom-2.mp3");
    tom2.play();
      break;

    case "s":
    var tom3=new Audio("static/drum-kit/sounds/tom-3.mp3");
    tom3.play();
      break;

    case "d":
    var tom4=new Audio("static/drum-kit/sounds/tom-4.mp3");
    tom4.play();
      break;

    case "j":
    var snare=new Audio("static/drum-kit/sounds/snare.mp3");
    snare.play();
      break;

    case "k":
    var crash=new Audio("static/drum-kit/sounds/crash.mp3");
    crash.play();
      break;

    case "l":
    var kickbass=new Audio("static/drum-kit/sounds/kick-bass.mp3");
    kickbass.play();
      break;
    default: console.log(key)
  }
}
