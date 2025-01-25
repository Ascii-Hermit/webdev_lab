function changeColor() {
  const colorOptions = document.getElementsByName("color");

  for (let i = 0; i < colorOptions.length; i++) {
    if (colorOptions[i].checked) {
      document.body.style.backgroundColor = colorOptions[i].value;
    }
  }
}
