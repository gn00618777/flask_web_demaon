function fcheck(){

    if(document.getElementById("tunnel_label").innerHTML.match(new RegExp("\\b"+connect_control_form.tunnel_name_to_be_connect.value+"\\b"))==null){

        alert("Please select a accurate tunnel name from list aaa");
        return false;
   }
    if(connect_control_form.tunnel_name_to_be_connect.value==""){

       alert("The text is empty");
       return false;
    }
   return true;
}
