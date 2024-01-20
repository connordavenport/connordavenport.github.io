function rotateClockHands() {
  const now = new Date();
  const hours = now.getHours() % 12; // Convert to 12-hour format
  const minutes = now.getMinutes();
  const seconds = now.getSeconds();
  const milliseconds = now.getMilliseconds();

  const hourHand = document.getElementById('hour-hand');
  const minuteHand = document.getElementById('minute-hand');
  const secondHand = document.getElementById('second-hand');

  const hourRotation = 30 * hours + 0.5 * minutes; // 30 degrees per hour, 0.5 degrees per minute
  const minuteRotation = 6 * minutes; // 6 degrees per minute
  const secondRotation = (6 / 1000) * (1000 * seconds + milliseconds); // 6 degrees per second, 1 degree per 166.6 milliseconds

  hourHand.style.transform = `translateX(-50%) rotate(${hourRotation}deg)`;
  minuteHand.style.transform = `translateX(-50%) rotate(${minuteRotation}deg)`;
  secondHand.style.transform = `translateX(-50%) rotate(${secondRotation}deg)`;

  // Call the function again after a short interval
  const remainingMilliseconds = 1000 - milliseconds;
  setTimeout(rotateClockHands, remainingMilliseconds);
}

// Start the clock rotation
rotateClockHands();