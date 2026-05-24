const timeDisplay = document.getElementById("time");

refreshTime();

function refreshTime() {
    const formatter = new Intl.DateTimeFormat("en-GB", {
        timeZone: "Europe/Stockholm",
        hour: "2-digit",
        minute: "2-digit",
        hour12: false,
        timeZoneName: "short",
    });

    const parts = formatter.formatToParts(new Date());

    const hour = parts.find(p => p.type === "hour").value;
    const minute = parts.find(p => p.type === "minute").value;
    const tz = parts.find(p => p.type === "timeZoneName").value;

    timeDisplay.textContent = `${hour}:${minute} ${tz}`;

}   setInterval(refreshTime, 1000);