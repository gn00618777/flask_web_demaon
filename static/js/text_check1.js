function fcheck1(){

   if(document.getElementById("tunnel_label").innerHTML.match(new RegExp("\\b"+connect_control_form1.tunnel_name_to_be_disconnect.value+"\\b"))==null){
       alert("Please select a accurate tuneel from list");
       return false;
   }
   if(connect_control_form1.tunnel_name_to_be_disconnect.value==""){
      alert("The text is empty");
      return false;
   }
   return true;
}
