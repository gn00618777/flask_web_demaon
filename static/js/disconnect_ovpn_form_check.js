function dcheck(){

   if(form_table1.ovpn_file_from_text.value==""){

       alert("The text is empty");
       return false;

   }
   if(document.getElementById("ovpn_list_label").innerHTML.match(new RegExp("\\b"+form_table1.ovpn_file_from_text.value+"\\b"))==null){

      alert("Please select accurate ovpn file from list ");
      return false;
   }

   return true;

}
