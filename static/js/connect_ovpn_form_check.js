function check(){

   if(form_table.ovpn_file.value==""){

       alert("The text is empty");
       return false;

   }
   if(document.getElementById("ovpn_list_label").innerHTML.match(new RegExp("\\b"+form_table.ovpn_file.value+"\\b"))==null){

      alert("Please select accurate ovpn file from list");
      return false;

   }
   return true;
}
