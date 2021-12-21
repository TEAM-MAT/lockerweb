const departments = [
  { id: "EIE", name: "전자정보공학부" },
  { id: "CS", name: "컴퓨터학부" },
  { id: "GM", name: "글로벌미디어학부" },
  { id: "SW", name: "소프트웨어학부" },
  { id: "AIC", name: "AI융합학부" },
];
const userDepartmentSpan1 = document.querySelector("span#userDepartment1");
const userDepartmentSpan2 = document.querySelector("span#userDepartment2");
for (i in departments) {
  const t = departments[i];
  if (userDepartmentSpan1.innerText === t.id) {
    userDepartmentSpan1.innerText = t.name;
    userDepartmentSpan2.innerText = t.name;
  }
}

function popupClose(inp) {
  const target = document.querySelector(`#${inp}`);
  target.classList.toggle("hidden");
}

function selectBuilding(inp) {
  const building = inp[0] + inp[1];
  const floor = inp[2];


  theSpan = document.querySelector("span#building-floor");
  let _building = "";
  let _floor = floor;

  if (building === "HN") {
    _building = "형남공학관";
  } else if (building === "IS") {
    _building = "정보과학관";
  } else if (building === "CB") {
    _building = "문화관";
  } else {
    _building = null;
  }
  theSpan.innerText = `${_building} ${_floor}구역 사물함 목록`;
  document.querySelector("span#userDepartment1").innerText = "";
}
