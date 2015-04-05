function check(){

   if(pptp_server_form_table.server_name.value==""){

      alert("Please fill up the text of Server Name");
      return false;
  
   }

   if(pptp_server_form_table.server_ip.value==""){

      alert("Please fill up the text of IP Address for Server");
      return false;

   }
  
   if(pptp_server_form_table.clients_ip.value==""){

     alert("Please fill up the text of IP Aaddress to allocate");
     return false;     

   }

   return true;

}
