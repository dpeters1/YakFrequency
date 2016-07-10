// default time range is [-5h : current time]
var CurrentDate = new Date();
var startDate = new Date(CurrentDate.getFullYear(), CurrentDate.getMonth(), CurrentDate.getDate()-CurrentDate.getDay()); //Default range is current week
var endDate = new Date(CurrentDate.getFullYear(), CurrentDate.getMonth(), CurrentDate.getDate()-CurrentDate.getDay()+7, 12, 59, 59);
var timeBounds = { // Stores values of sliders
    hourMin: CurrentDate.getHours()-5,
    hourMax: CurrentDate.getHours(),
    dayMin: CurrentDate.getDay(),
    dayMax: CurrentDate.getDay(),
    startStamp : startDate.getTime(),
    endStamp : endDate.getTime(),
    invertHour: false,
    invertDay: false,
    university: "Carleton"
};
if(CurrentDate.getHours() < 5){ //if it's earlier than 5am, include previous day's yaks in default load
    timeBounds.hourMin = timeBounds.hourMax;
    timeBounds.hourMax += 19;
    document.getElementById('invertHour').checked = true;
    timeBounds.invertHour = true;
    timeBounds.dayMin -= 1;
    if(timeBounds.dayMin < 0){
        timeBounds.dayMax = 6;
        timeBounds.dayMin = 0;
        document.getElementById('invertDay').checked = true;
        timeBounds.invertDay = true;
    }
}
var weekday = new Array(7);
weekday[0]=  "Sunday";
weekday[1] = "Monday";
weekday[2] = "Tuesday";
weekday[3] = "Wednesday";
weekday[4] = "Thursday";
weekday[5] = "Friday";
weekday[6] = "Saturday";

$("#basicSlider").rangeSlider({
    defaultValues:{min: timeBounds.hourMin, max: timeBounds.hourMax},
    bounds: {min: 0, max: 23},
    formatter:function(val){
        integerVal = Math.round(val);
        if (integerVal > 12){
            return integerVal.toString()-12 + " PM";
        }
        else if (integerVal == 12){
            return "12 PM";
        }
        else if (integerVal == 0){
            return "12 AM";
        }
        else{
            return integerVal.toString() + " AM";
        }
    }
});
$("#daySlider").rangeSlider({
    defaultValues:{min: timeBounds.dayMin-0.25, max: timeBounds.dayMax+0.25},
    bounds: {min: 0, max: 6},
    formatter:function(val){
        return weekday[Math.round(val)];
    }
});
$("#dateSlider").dateRangeSlider({
    defaultValues:{min: startDate, max: endDate},
    bounds: {min: new Date(2016, 2, 20), max: new Date(CurrentDate.getFullYear(), CurrentDate.getMonth(), CurrentDate.getDate()-CurrentDate.getDay()+7, 12, 59, 59)},

    formatter:function(val){
        var dispDate = new Date(val.getFullYear(), val.getMonth(), val.getDate()-val.getDay());
        var days = dispDate.getDate(),
          month = dispDate.getMonth() + 1,
          year = dispDate.getFullYear();
        return days + "/" + month + "/" + year;
    }
});

$("#basicSlider").bind("valuesChanged", function(e, data){
    timeBounds.hourMin = (Math.round(data.values.min));
    timeBounds.hourMax = (Math.round(data.values.max));

    returnDate();
});

$("#daySlider").bind("valuesChanged", function(e, data){
    timeBounds.dayMin = Math.round(data.values.min);
    timeBounds.dayMax = Math.round(data.values.max);

    returnDate();
});

$("#dateSlider").bind("valuesChanged", function(e, data){
    var dayValues = $("#daySlider").rangeSlider("values");
    startDate = new Date(data.values.min.getFullYear(), data.values.min.getMonth(), data.values.min.getDate()-data.values.min.getDay());
    endDate = new Date(data.values.max.getFullYear(), data.values.max.getMonth(), data.values.max.getDate()-data.values.max.getDay());

    returnDate();
});

$('#invertHour').change(function() {
    if($(this).is(":checked")) {
        timeBounds.invertHour = true;
    }
    else{
        timeBounds.invertHour = false;
    }

    returnDate();
});

$('#invertDay').change(function() {
   if($(this).is(":checked")) {
        timeBounds.invertDay = true;
    }
    else{
        timeBounds.invertDay = false;
    }
    returnDate();
});

function returnDate() {
    $('#cloud').jQCloud('update', [{text: "Loading...", weight: "10"}], {
            autoResize: true
        });
    endDate = new Date(endDate.getFullYear(), endDate.getMonth(), endDate.getDate()); // Remove hh:mm:ss  
    timeBounds.startStamp = startDate.getTime(); // Convert to timestamp for js to python date object
    timeBounds.endStamp = endDate.getTime();
    $.ajax({
      type: "POST",
      contentType: "application/json; charset=utf-8",
      url: "/timeData",
      data: JSON.stringify(timeBounds),
      success: function (data) {
    
        var updateWords = []

        try {
            for(i=0;i<30;i++){
                updateWords.push({text: data.yaks[i][0], weight: data.yaks[i][1]})
                $('#cloud').jQCloud('update', updateWords);
            }
        } catch (e) {
            if (e instanceof TypeError) {
                $('#cloud').jQCloud('update', [{text: "No posts in selected time range", weight: "3"},
                    {text: "[Error]", weight: "4"}], {autoResize: true
        });
        }
    }
        
        console.log(data.hourMin);
        console.log(data.hourMax);
        console.log(data.dayMin);
        console.log(data.dayMax);
        console.log(new Date(data.startDate*1000));
        console.log(new Date(data.endDate*1000));
        console.log(data.invertHour);
        console.log(data.invertDay);
        console.log(data.university);
    },
    dataType: "json"
});
}

/// University Selectors

$(document).ready(function() {
    $("#radio1").click(function(){
        timeBounds.university = "Acadia";
        returnDate();
    }); 
    $("#radio2").click(function(){
        timeBounds.university = "Carleton";
        returnDate();
    }); 
    $("#radio3").click(function(){
        timeBounds.university = "Mcgill";
        returnDate();
    }); 
    $("#radio4").click(function(){
        timeBounds.university = "Ottawa";
        returnDate();
    }); 
    $("#radio5").click(function(){
        timeBounds.university = "Queens";
        returnDate();
    }); 
    $("#radio6").click(function(){
        timeBounds.university = "Toronto";
        returnDate();
    }); 
    $("#radio7").click(function(){
        timeBounds.university = "Waterloo";
        returnDate();
    }); 
    $("#radio8").click(function(){
        timeBounds.university = "Western";
        returnDate();
    }); 
});