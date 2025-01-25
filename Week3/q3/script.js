function calculateGrade() {
  var subject1 = parseFloat(document.getElementById("subject1").value);
  var subject2 = parseFloat(document.getElementById("subject2").value);
  var subject3 = parseFloat(document.getElementById("subject3").value);
  var subject4 = parseFloat(document.getElementById("subject4").value);

  if (
    isNaN(subject1) ||
    isNaN(subject2) ||
    isNaN(subject3) ||
    isNaN(subject4)
  ) {
    alert("Please enter valid marks for all subjects.");
    return;
  }

  var average = (subject1 + subject2 + subject3 + subject4) / 4;

  document.getElementById("average").textContent = average.toFixed(2);

  var grade = "";
  if (average > 90) {
    grade = "A";
  } else if (average > 80) {
    grade = "B";
  } else if (average > 70) {
    grade = "C";
  } else if (average > 60) {
    grade = "D";
  } else {
    grade = "F";
  }

  document.getElementById("grade").textContent = grade;
}
