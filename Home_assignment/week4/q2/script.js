window.onload = function () {
  let text = document.querySelector(".sliding-text");

  setTimeout(() => {
    text.style.left = "50%";
    text.style.transform = "translate(-50%, -50%)";
  }, 1000);
};
