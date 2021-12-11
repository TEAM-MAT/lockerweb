function popupClose(id) {
  const target = document.querySelector(`#${id}`);
  console.log(id);
  target.classList.toggle("hidden");
}
