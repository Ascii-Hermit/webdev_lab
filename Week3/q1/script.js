const quizQuestions = [
  {
    question: "What does HTML stand for?",
    options: [
      "HyperText Markup Language",
      "Home Tool Markup Language",
      "Hyperlinks and Text Markup Language",
    ],
    correctAnswer: 0,
  },
  {
    question: "Which of these is used to define a function in JavaScript?",
    options: ["function", "def", "funct"],
    correctAnswer: 0,
  },
  {
    question: "What is the result of 5 + 10 + '20' in JavaScript?",
    options: ["1520", "15", "NaN"],
    correctAnswer: 0,
  },
  {
    question:
      "Which method is used to add an element to the end of an array in JavaScript?",
    options: ["push()", "pop()", "shift()"],
    correctAnswer: 0,
  },
];

let currentQuestionIndex = 0;
let score = 0;

function loadQuestion() {
  const question = quizQuestions[currentQuestionIndex];
  document.getElementById("question-container").textContent = question.question;

  const optionsContainer = document.getElementById("options-container");
  optionsContainer.innerHTML = "";
  question.options.forEach((option, index) => {
    const optionButton = document.createElement("button");
    optionButton.textContent = option;
    optionButton.onclick = () => checkAnswer(index);
    optionsContainer.appendChild(optionButton);
  });
}

function checkAnswer(selectedIndex) {
  const correctAnswer = quizQuestions[currentQuestionIndex].correctAnswer;
  if (selectedIndex === correctAnswer) {
    score++;
    document.getElementById("score").textContent = score;
  }
  document.getElementById("next-button").style.display = "block";
}

function nextQuestion() {
  currentQuestionIndex++;
  if (currentQuestionIndex < quizQuestions.length) {
    loadQuestion();
    document.getElementById("next-button").style.display = "none";
  } else {
    showFinalScore();
  }
}

function showFinalScore() {
  document.getElementById("question-container").textContent = "Quiz Complete!";
  document.getElementById("options-container").innerHTML = "";
  document.getElementById("next-button").style.display = "none";
  document.getElementById("score-container").style.display = "block";
}

loadQuestion();
document.getElementById("next-button").addEventListener("click", nextQuestion);
document.getElementById("next-button").style.display = "none";
