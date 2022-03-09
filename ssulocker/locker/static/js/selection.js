//preload images
let images = [];
function preload(arg) {
 for (let i = 0; i < arg.length; i++) {
  images[i] = arg[i];
  images[i].src = arg[i].src;
 }
}
preload([
 "https://i.imgur.com/mnesjq5.png",
 "https://i.imgur.com/f8kjHfc.png",
 "https://i.imgur.com/b9kaNKw.png",
 "https://i.imgur.com/gLjse84.png",
 "https://i.imgur.com/Lrqw5Nl.png",
 "https://i.imgur.com/OppfBtD.png",
 "https://i.imgur.com/E4pFw14.png",
]);

const floors = [0, 1, 2, 3, 4, 5, 6];
const sectors = ["A", "B", "C", "D", "E", "F", "G", "H", "I"];

function selectBuilding(inp) {
 console.log(inp);
 const building = inp[0] + inp[1];
 let floor = inp[2];
 let sector = inp[3];

 //선택한 층만 표시
 for (i in floors) {
  if (floor == floors[i]) {
   const t = document.querySelectorAll(`button.floor${floors[i]}`);
   t.forEach(function (t) {
    if (t.classList.contains(`sector${sector}`)) {
     t.classList.remove("sectorDOWN");
    } else {
     t.classList.add("sectorDOWN");
    }
   });
  } else {
   const t = document.querySelectorAll(`button.floor${floors[i]}`);
   t.forEach(function (t) {
    t.classList.add("sectorDOWN");
   });
  }
 }
 //선택한 구역만 표시

 sessionStorage.setItem("sector", inp);
 //사물함 배치도 변경
 const theImage = document.getElementById("lockermapImage");
 switch (inp) {
  case "HN1":
   theImage.src = "https://i.imgur.com/mnesjq5.png";
   break;
  case "HN3":
   theImage.src = "https://i.imgur.com/f8kjHfc.png";
   break;
  case "IS6":
   theImage.src = "https://i.imgur.com/b9kaNKw.png";
   break;
  case "IS4":
   theImage.src = "https://i.imgur.com/gLjse84.png";
   break;
  case "IS0":
   theImage.src = "https://i.imgur.com/Lrqw5Nl.png";
   break;
  default:
   theImage.src = "https://i.imgur.com/OppfBtD.png";
   break;
 }

 //사물함 목록 이름 변경
 if (floor == "0") floor = "B1";
 theSpan = document.querySelector("span#building-floor");
 let _building = "";
 let _floor = floor + "층";
 if (building === "HN") {
  _building = "형남공학관";
 } else if (building === "IS") {
  _building = "정보과학관";
 } else if (building === "CB") {
  _building = "문화관";
 } else {
  _building = _floor = "";
 }

 theSpan.innerText = `${_building} ${_floor}`;
 document.querySelector("span#userDep1").innerText = "";
}
