var currentDate = new Date();
var startH = currentDate.getHours()-5;
var stopH = startH+5;
var startDay = currentDate.getDay()-1;
var stopDay = startDay+1;
var startDate = currentDate.getDate()-currentDate.getDay();
var stopDate = startDate+7;
var startMonth = currentDate.getMonth();
var stopMonth = currentDate.getMonth();
var weekday = new Array(7);
weekday[0]=  "Sunday";
weekday[1] = "Monday";
weekday[2] = "Tuesday";
weekday[3] = "Wednesday";
weekday[4] = "Thursday";
weekday[5] = "Friday";
weekday[6] = "Saturday";

$("#basicSlider").rangeSlider({
defaultValues:{min: currentDate.getHours(), max: currentDate.getHours()+5},
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
defaultValues:{min: currentDate.getDay()-1, max: currentDate.getDay()},
bounds: {min: 0, max: 6},
formatter:function(val){
return weekday[Math.round(val)];
}
});
var currentWeekDay = currentDate.getDate()-currentDate.getDay();
$("#dateSlider").dateRangeSlider({
defaultValues:{min: new Date(2016, 2, currentWeekDay), max: new Date(2016, 2, currentWeekDay+7)},
bounds: {min: new Date(2016, 2, 6), max: new Date(2016, 6, 31)},
step: {days: 7}
});
$("#daySlider").bind("valuesChanged", function(e, data){
startDay = Math.round(data.values.min);
stopDay = Math.round(data.values.max);
//alert(startDay + " " + stopDay);
});
$("#basicSlider").bind("valuesChanged", function(e, data){
startH = Math.round(data.values.min);
stopH = Math.round(data.values.max);
//alert(startH + " " + stopH);
});
$("#dateSlider").bind("valuesChanged", function(e, data){
startDate = data.values.min.getDate()+startDay;
stopDate = data.values.max.getDate()-7+stopDay;
startMonth = data.values.min.getMonth()+1;
stopMonth = data.values.max.getMonth()+1;
if (stopDate <= 0){
var checkDate = new Date(2016, stopMonth, 0);
stopDate += checkDate.getDate()-1;
stopMonth -= 1;
}
//alert(startDate + " " + stopDate);
//alert(startMonth + " " + stopMonth);
});