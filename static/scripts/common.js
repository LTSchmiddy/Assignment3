
let selected_item = -1;

function open_selected_item(item_id) {
    set_item_button(item_id);

    $.post("/panes/item_view", {'id': item_id}, (data, status)=>{
        // $.post("/panes/item_view", (data, status)=>{
        if (status !== 'success') {
            return;
        }
        selected_item = item_id;
        $('#full_item_view').html(data);

        // set_item_button();

    });



}

function set_item_button(item_id) {
    let selectables = $("#sidebar-content")[0].getElementsByClassName('item_button');

        let selected_class = "list_item_id_" + item_id;

        for (let i = 0; i < selectables.length; i++) {
            let item = selectables[i];

            if (item.id === selected_class) {
                item.classList.add('item_button-active');

            } else {
                item.classList.remove('item_button-active');
            }
        }
}

function delete_item(item_id) {
        $.post("/api/delete", {'id': item_id}, (data, status)=>{
        if (status !== 'success') {
            return;
        }
        selected_item = item_id;
        console.log(data);
        $('#full_item_view').html("");
        load_item_list();
    });
}

function new_item() {
        $.post("/api/create", {}, (data, status)=>{
        if (status !== 'success') {
            return;
        }
        selected_item = data;
        open_selected_item(selected_item)
        load_item_list();
    });
}

function checkBrowser(){
    let c = navigator.userAgent.search("Chrome");
    let f = navigator.userAgent.search("Firefox");
    let m8 = navigator.userAgent.search("MSIE 8.0");
    let m9 = navigator.userAgent.search("MSIE 9.0");
    let browser = "";

    if (c > -1) {
        browser = "Chrome";
    } else if (f > -1) {
        browser = "Firefox";
    } else if (m9 > -1) {
        browser ="MSIE 9.0";
    } else if (m8 > -1) {
        browser ="MSIE 8.0";
    }
    return browser;
}

let firefox_datetime;


/*
function seconds_to_timecode(val) {
    let retVal = "";

    let hours = 0;
    let minutes = 0;
    let seconds = 0;

    // Hours:
    if (val >= 3600) {
        hours = Math.floor(val / 3600);
        retVal += hours.toString() + ":";
        val = val % 3600;
    }

    // Minutes
    if (val >= 60) {
        minutes = Math.floor(val / 60);
        if (hours > 0 && minutes < 10){
            retVal += "0" + minutes.toString() + ":";
        } else {
            retVal += minutes.toString() + ":";
        }

        val = val % 60;
    } else {
        retVal += "0:";
    }

    seconds = Math.floor(val)

    if (val < 10){
        retVal += "0" + seconds.toString();
    } else {
        retVal += seconds.toString();
    }

    return {
        hours: hours,
        minutes: minutes,
        seconds: seconds,
        timecode: retVal
    };
}*/