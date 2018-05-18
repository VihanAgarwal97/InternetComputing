/*Variable to hold all the times*/
var times = [];

/*Generate all the time options*/
generateOptions();

/*Create an event object*/
function EventItem(name, location, day, start, end, duration) {
    var obj = new Object();

    obj.name = name;
    obj.location = location;
    obj.day = day;
    obj.start = start;
    obj.end = end;
    obj.duration = duration;

    obj.createEvent = function () {
        var eventdiv = $("<div>", {"class": "event-item"});
        eventdiv.append("<strong>" + name + "</strong>" + "<br>");
        eventdiv.append(location + "<br>");
        eventdiv.append(start + " - " + end);
        obj.stylize(eventdiv);
        return eventdiv;
    }

    obj.addEvent = function() {
        $("#"+day).append(obj.createEvent())
    }

    obj.stylize = function(div) {
        var top = (times.indexOf(start)/96)*500;
        div.css("top",top);
        var height= duration/96 * 500;
        div.css("height",height);
    }

    return obj;
}

/*Display the event creation form when add event button is clicked*/
$("#new_event_button").on("click",function () {
    $("#add_event_form").css("display","block");
});


/*Generate the drop down options for the event start and end time*/
function generateOptions() {
    var value=0;
    var dt = new Date(1970, 0, 1, 0, 0, 0, 0);
    var counter=0;
    while (dt.getDate() == 1) {
        var point = dt.toLocaleTimeString('en-US');
        dt.setMinutes(dt.getMinutes() + 15);
        times[counter]=point;
        counter+=1;
    }
    for(i=0;i<96;i++){
        var timeOption = $("<option value=" + value + "> "+ times[i] + "</option>");
        var timeOption1 = $("<option value=" + value + "> "+ times[i] + "</option>");
        $("#eve_end").append(timeOption);
        $("#eve_start").append(timeOption1);
        value+=1;
    }
}

/*Submits the event to the calendar if it's a valid event*/
function submitEvent() {
    var name=$("#eve_name").val();
    var location=$("#eve_location").val();
    var day=$("#eve_day").val();
    var start=times[$("#eve_start").val()];
    var end=times[$("#eve_end").val()];
    var duration = $("#eve_end").val() - $("#eve_start").val();
    if(duration<=0) {
        alert("You entered an invalid time. Please check the time.");
    } else {
        var event = EventItem(name, location, day, start, end, duration);
        event.addEvent();
        $("#add_event_form").css("display","none");
        $("#eve_name").val("");
        $("#eve_location").val("");
        $("#eve_day").val("");
        $("#eve_start").val("");
        $("#eve_end").val("");
    }
}
