// default time range is [-5h : current time]
var CurrentDate = new Date();
var startDate = new Date(CurrentDate.getFullYear(), CurrentDate.getMonth(), CurrentDate.getDate()-CurrentDate.getDay());
var endDate = new Date(CurrentDate.getFullYear(), CurrentDate.getMonth(), CurrentDate.getDate()-CurrentDate.getDay()+7);
var timeBounds = { // Stores values of sliders
    hourMin: CurrentDate.getHours()-5,
    hourMax: CurrentDate.getHours(),
    dayMin: CurrentDate.getDay(),
    dayMax: CurrentDate.getDay(),
    startStamp : startDate.getTime(),
    endStamp : endDate.getTime(),
    invertHour: false,
    invertDay: false
};
if(CurrentDate.getHours() < 5){ //if it's earlier than 5am, include previous day's yaks in default load
    timeBounds.hourMin = timeBounds.hourMax;
    timeBounds.hourMax += 20;
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
    //bounds: {min: new Date(2016, 2, 20), max: new Date(endDate.getFullYear(), endDate.getMonth(), endDate.getDate()-endDate.getDay()+7)},
    bounds: {min: new Date(2016, 2, 6), max: new Date(2016, 7, 21)},
    step: {days: 7}
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
    startDate.setDate(data.values.min.getDate());
    endDate.setDate(data.values.max.getDate());
    startDate.setMonth(data.values.min.getMonth());
    endDate.setMonth(data.values.max.getMonth());

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
    timeBounds.startStamp = startDate.getTime(); // Convert to timestamp for js to python date object
    timeBounds.endStamp = endDate.getTime();
    $.ajax({
      type: "POST",
      contentType: "application/json; charset=utf-8",
      url: "/timeData",
      data: JSON.stringify(timeBounds),
      success: function (data) {
    
        var updateWords = []
        for(i=0;i<30;i++){
            updateWords.push({text: data.yaksup[1][i], weight: data.yaksup[0][i]})
        }
        $('#cloud').jQCloud('update', updateWords, {
            autoResize: true
        });
    
        console.log(data.yaksup);
        console.log(data.hourMin);
        console.log(data.hourMax);
        console.log(data.dayMin);
        console.log(data.dayMax);
        console.log(data.startDate);
        console.log(data.endDate);
        console.log(data.invertHour);
        console.log(data.invertDay);
    },
    dataType: "json"
});
}
