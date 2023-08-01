function displayDateTime() {

    const clock = document.querySelector('.clock');

    // Assigning time values to constants
    const tick = () => {
        const now = new Date();
        let h = now.getHours();
        let m = now.getMinutes();
        let s = now.getSeconds();
        let am_pm = "";
        /* Twelve-hour clock */
        if (h >= 12) {
            h -= 12;
            am_pm = "PM";
        };

        if (h == 0) {
            h = 12;
            am_pm = "AM";
        };
        /* Single digit correction*/
        if (h < 10) {
            h = "0" + h;
        }
        if (m < 10) {
            m = "0" + m;
        }
        if (s < 10) {
            s = "0" + s;
        }
        var today = new Date();
        var date = (today.getMonth() + 1) + '-' + today.getDate() + '-' + today.getFullYear();

        // Defining html for digital clock
        const html =
            `
            ${h}:${m}:${s}
            <span>${am_pm}</span>
            <p style="font-size: medium; text-align: center;">${date}</p>
            `;
        //printing html code inside div.clock
        clock.innerHTML = html;
    };
    //refreshing clock every 1 second
    setInterval(tick, 1000);
}