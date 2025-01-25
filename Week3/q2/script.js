function updateClockAndGreeting() {
  const currentDate = new Date();
  const hours = currentDate.getHours();
  const minutes = currentDate.getMinutes();
  const seconds = currentDate.getSeconds();

  const formattedTime = `${hours}:${minutes < 10 ? "0" + minutes : minutes}:${
    seconds < 10 ? "0" + seconds : seconds
  }`;

  document.getElementById("clock").textContent = formattedTime;

  let greetingMessage = "";
  if (hours >= 0 && hours < 12) {
    greetingMessage = "Good Morning!";
  } else if (hours >= 12 && hours < 17) {
    greetingMessage = "Good Afternoon!";
  } else if (hours >= 17 && hours < 21) {
    greetingMessage = "Good Evening!";
  } else {
    greetingMessage = "Good Night!";
  }

  document.getElementById("greeting").textContent = greetingMessage;
}

updateClockAndGreeting();
setInterval(updateClockAndGreeting, 1000);
