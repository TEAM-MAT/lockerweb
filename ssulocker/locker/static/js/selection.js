function selectBuilding(inp) {
  console.log(lockers);
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
}
const sectors = ["A", "B", "C", "D", "E", "F"];
let beforeSelected = "A";

function selectSector(inp) {
  for (i in sectors) {
    if (inp === sectors[i]) {
      const t = document.querySelectorAll(`td.sector${sectors[i]}`);
      t.forEach(function (t) {
        t.classList.remove("sectorDOWN");
      });
    } else {
      const t = document.querySelectorAll(`td.sector${sectors[i]}`);
      t.forEach(function (t) {
        t.classList.add("sectorDOWN");
      });
    }
  }
}
