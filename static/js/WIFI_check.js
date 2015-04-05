function check(){

   if( connect_WIFI.SSID_text.value == ""){

      alert("Please select one of SSIDs");
      return false;

   }

   return true;

}
