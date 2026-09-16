function showLoadingMessage(message) {
  document.getElementById("status").innerHTML = message;
}
function fetchSchoolEventData(callback) {
  callback("Loading school event data... Please wait.");

  return new Promise(function(resolve) {
    setTimeout(function() {
      let schoolEvent = {
        eventName: "Annual Science Fair",
        date: "31 September 2026",
        time: "1:00 PM",
        venue: "School Auditorium",
        coordinator: "Miss Battle-Axe",
        participants: 150,
        isRegistrationOpen: true
      };
      resolve(schoolEvent);
    }, 2000);
  });
}

async function showSchoolEvent() {
  let eventData = await fetchSchoolEventData(showLoadingMessage);
  document.getElementById("status").innerHTML = "Event data loaded successfully!";
  let jsonText = JSON.stringify(eventData, null, 2);
  let parsedEvent = JSON.parse(jsonText);
  let eventMessage = "";

  eventMessage += "<p><strong>Event Name:</strong> " + parsedEvent.eventName + "</p>";
  eventMessage += "<p><strong>Date:</strong> " + parsedEvent.date + "</p>";
  eventMessage += "<p><strong>Time:</strong> " + parsedEvent.time + "</p>";
  eventMessage += "<p><strong>Venue:</strong> " + parsedEvent.venue + "</p>";
  eventMessage += "<p><strong>Coordinator:</strong> " + parsedEvent.coordinator + "</p>";
  eventMessage += "<p><strong>Participants:</strong> " + parsedEvent.participants + "</p>";

  if (parsedEvent.isRegistrationOpen === true) {
    eventMessage += "<p><strong>Registration:</strong> Open</p>";
  } else {
    eventMessage += "<p><strong>Registration:</strong> Closed</p>";
  }

  document.getElementById("eventDetails").innerHTML = eventMessage;
  document.getElementById("jsonOutput").textContent = jsonText;
}