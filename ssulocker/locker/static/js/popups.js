function popupClose(inp) {
  const target = document.querySelector(`#${inp}`);
  target.classList.toggle("hidden");
}
