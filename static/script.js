// dashboard functionality

const updateTime = () => {
    const now = new Date();
    const formattedDate = now.toISOString().substring(0, 19).replace('T', ' ');
    document.getElementById('current-time').innerText = formattedDate;
};

setInterval(updateTime, 1000); // Update time every second
