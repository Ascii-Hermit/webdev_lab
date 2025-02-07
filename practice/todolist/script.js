document.addEventListener("DOMContentLoaded", function () {
  document
    .querySelectorAll("#tasklist input[type='checkbox']")
    .forEach((checkbox) => {
      checkbox.addEventListener("change", function () {
        this.parentElement.classList.toggle("completed");
      });
    });
});

function addTask() {
  let taskInput = document.getElementById("taskinput");
  let li = document.createElement("li");
  let checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.onclick = function () {
    this.parentElement.classList.toggle("completed");
  };
  let span = document.createElement("span");
  span.textContent = taskInput.value.trim();
  li.appendChild(checkbox);
  li.appendChild(span);
  document.getElementById("tasklist").appendChild(li);
  taskInput.value = "";
}
