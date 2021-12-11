function popupClose(inp) {
  const target = document.querySelector(`#${inp}`);
  target.classList.toggle("hidden");
}

function selectBuilding(inp) {
  const building = inp[0] + inp[1];
  const sector = inp[2];
  console.log(building, sector);
}
