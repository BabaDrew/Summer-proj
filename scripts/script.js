let sidebaron = false;


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


        let month = now.getMonth()+1;
        let day = now.getDate();
        if (month < 10) {
            month = "0" + month;
        }

        if (day < 10) {
            day = "0" + day;
        }
        var date = month + '-' + day + '-' + today.getFullYear();

        // Defining html for digital clock
        const html =
            `
            <p>${h}:${m}:${s} ${am_pm}</p>
            <p>${date}</p>
            `;
        //printing html code inside div.clock
        clock.innerHTML = html;
    };
    //refreshing clock every 1 second
    setInterval(tick, 1000);
}

function openCloseNav() {
    if (!sidebaron) {
        document.getElementById("mySidebar").style.width = "250px";
        document.getElementById("main").style.marginLeft = "250px";
        sidebaron = true;
    } else {
        document.getElementById("mySidebar").style.width = "0";
        document.getElementById("main").style.marginLeft= "0";
        sidebaron = false;
    }

}