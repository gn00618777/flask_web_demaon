function check(){

   var obj=document.getElementsByName("selection");

   if(obj[0].checked==false){

      alert("Start openVPN server not select");
      return false;

   }

}
