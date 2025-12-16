console.log("Tracker loaded!");

// 🔥 Track scroll depth
document.addEventListener("scroll", function () {
    let scrollPercent = Math.round(
        (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100
    );

    if (scrollPercent % 25 === 0) {
        sendEvent("scroll", scrollPercent + "%");
    }
});

// 🔥 Track time spent
let secondsSpent = 0;
setInterval(() => {
    secondsSpent++;
    sendEvent("time_spent", secondsSpent);
}, 5000); // every 5 sec

// 🔥 Track button clicks
document.getElementById("signupBtn").addEventListener("click", () => {
    sendEvent("button_click", "signupBtn");
});

// 🔥 Track form submissions
document.getElementById("contactForm").addEventListener("submit", (e) => {
    e.preventDefault();
    sendEvent("form_submit", "contact_form");
    alert("Form submitted & event tracked!");
});

// 🔥 Function to send event to Flask backend
function sendEvent(eventType, eventValue) {
    fetch(`/track-event?type=${eventType}&value=${eventValue}&page=${window.location.pathname}`)
        .then(res => res.json())
        .then(data => console.log("Event logged:", data))
        .catch(err => console.error("Error sending event:", err));
}
