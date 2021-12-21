const departments = [
  { id: "EIE", name: "전자정보공학부" },
  { id: "CS", name: "컴퓨터학부" },
  { id: "GM", name: "글로벌미디어학부" },
  { id: "SW", name: "소프트웨어학부" },
  { id: "AIC", name: "AI융합학부" },
];
const userDepSpan1 = document.querySelector("span#userDep1");
const userDepSpan2 = document.querySelector("span#userDep2");
for (i in departments) {
  const t = departments[i];
  if (userDepSpan1.innerText === t.id) {
    userDepSpan1.innerText = t.name;
    userDepSpan2.innerText = t.name;
  }
}

const floorSpan = document.querySelectorAll("span.floor");
floorSpan.forEach(function (t) {
  if (t.innerText == "0") {
    t.innerText = "B1";
  }
});
