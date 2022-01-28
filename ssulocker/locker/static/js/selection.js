//images, preload
let images = [];

function preload() {
  for (let i = 0; i < preload.arguments.lenght; i++) {
    images[i] = new Image();
    images[i].src = preload.arguments.src;
  }
}

preload(
  "https://i.imgur.com/mnesjq5.png",
  "https://i.imgur.com/f8kjHfc.png",
  "https://i.imgur.com/b9kaNKw.png",
  "https://i.imgur.com/gLjse84.png",
  "https://i.imgur.com/Lrqw5Nl.png",
  "https://i.imgur.com/OppfBtD.png"
);

const floors = [0, 1, 2, 3, 4, 5, 6];
const sectors = ["A", "B", "C", "D", "E", "F", "G", "H", "I"];

for (i in floors) {
  if (floors[i] === 1) {
    const t = document.querySelectorAll(`button.floor${floors[i]}`);
    t.forEach(function (t) {
      t.classList.remove("sectorDOWN");
    });
  } else {
    const t = document.querySelectorAll(`button.floor${floors[i]}`);
    t.forEach(function (t) {
      t.classList.remove("sectorDOWN");
    });
  }
}
function selectBuilding(inp) {
  console.log(inp);
  const building = inp[0] + inp[1];
  const floor = inp[2];

  //사물함 목록 이름 벼경
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
  //선택한 층만 표시
  for (i in floors) {
    if (floor == floors[i]) {
      const t = document.querySelectorAll(`button.floor${floors[i]}`);
      t.forEach(function (t) {
        t.classList.remove("floorDOWN");
      });
    } else {
      const t = document.querySelectorAll(`button.floor${floors[i]}`);
      t.forEach(function (t) {
        t.classList.add("floorDOWN");
      });
    }
  }
  //사물함 배치도 변경
  const theImage = document.getElementById("lockermapImage");
  switch (inp) {
    case "HN1":
      theImage.src = "https://i.imgur.com/mnesjq5.png";
      console.log("HN1");
      break;
    case "HN3":
      theImage.src = "https://i.imgur.com/f8kjHfc.png";
      console.log("HN3");
      break;
    case "IS6":
      theImage.src = "https://i.imgur.com/b9kaNKw.png";
      console.log("IS6");
      break;
    case "IS4":
      theImage.src = "https://i.imgur.com/gLjse84.png";
      console.log("IS4");
      break;
    case "IS0":
      theImage.src = "https://i.imgur.com/Lrqw5Nl.png";
      console.log("IS0");
      break;
    default:
      theImage.src = "https://i.imgur.com/OppfBtD.png";
      console.log("basic");
      break;
  }
  //모든 구역 표시
  for (i in sectors) {
    const t = document.querySelectorAll(`button.sector${sectors[i]}`);
    t.forEach(function (t) {
      t.classList.remove("sectorDOWN");
    });
  }
}

function selectSector(inp) {
  //선택한 구역만 표시
  for (i in sectors) {
    if (inp === sectors[i]) {
      const t = document.querySelectorAll(`button.sector${sectors[i]}`);
      t.forEach(function (t) {
        t.classList.remove("sectorDOWN");
      });
    } else {
      const t = document.querySelectorAll(`button.sector${sectors[i]}`);
      t.forEach(function (t) {
        t.classList.add("sectorDOWN");
      });
    }
  }
  sessionStorage.setItem("sector", inp);
}
