//preload images
let images = [];
function preload(arg) {
 for (let i = 0; i < arg.length; i++) {
  images[i] = arg[i];
  images[i].src = arg[i].src;
 }
}
preload([
 "https://i.imgur.com/b9kaNKw.png",
 "https://i.imgur.com/gLjse84.png",
 "https://i.imgur.com/Lrqw5Nl.png",
 "https://i.imgur.com/f8kjHfc.png",
 "https://i.imgur.com/mnesjq5.png",
 "https://i.imgur.com/zxOx1fD.png",
 "https://i.imgur.com/swXCbhD.png",
 "https://i.imgur.com/OppfBtD.png",
]);

const floors = [0, 1, 2, 3, 4, 5, 6];
const sectors = ["A", "B", "C", "D", "E", "F", "G", "H", "I"];

function selectBuilding(inp) {
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
 selectedImage(inp);
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

function selectedImage(inp) {
 let floorSector = inp.slice(0, 3);
 const theImage = document.getElementById("lockermapImage");
 switch (floorSector) {
  case "IS0":
   theImage.src = "https://i.ibb.co/dQbFNN2/IS0.jpg";
   break;
  case "IS1":
   theImage.src = "https://i.ibb.co/THrqxCc/IS1.jpg";
   break;
  case "IS2":
   theImage.src = "https://i.ibb.co/4Z43DGZ/IS2.jpg";
   break;
  case "IS3":
   theImage.src = "https://i.ibb.co/9VG8xKZ/IS3.png";
   break;
  case "IS4":
   theImage.src = "https://i.ibb.co/x745qfD/IS4.jpg";
   break;
  case "IS5":
   theImage.src = "https://i.ibb.co/Kh6fP6n/IS5.jpg";
   break;
  case "IS6":
   theImage.src = "https://i.ibb.co/QFPpr48/IS6.png";
   break;
  case "HN0":
   theImage.src = "https://i.ibb.co/C0xg5Sx/HN0.png";
   break;
  case "HN1":
   theImage.src = "https://i.ibb.co/Zmxy3gD/HN1.png";
   break;
  case "HN3":
   theImage.src = "https://i.ibb.co/hfFHgg4/HN3.png";
   break;
  case "HN4":
   theImage.src = "https://i.ibb.co/7pf4YMc/HN4.png";
   break;
 }
}
