function setTime(){

   var nowDate=new Date();
   var nowMonth=nowDate.getMonth();
   var nowDay=nowDate.getDay();
   var nowHour=nowDate.getHours();
   var nowMinute=nowDate.getMinutes();
   var nowYear=nowDate.getFullYear();

   var elem=document.getElementById("month");
   elem.value=nowMonth;

   var elem1=document.getElementById("day");
   elem1.value=nowDay;

   var elem2=document.getElementById("hour");
   elem2.value=nowHour;

   var elem3=document.getElementById("minute");
   elem3.value=nowMinute;

   var elem4=document.getElementById("year");
   elem4.value=nowYear;


  
}
