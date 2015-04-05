function check(){

   if(tunnel_table.tunnel_name.value==""){
       alert("Please fill up the entry of Tunnel name");
       return false;
   }
   if(tunnel_table.server_ip.value==""){
       alert("Please fill up the entry of Server IP");
       return false;
   }
   if(tunnel_table.server_name.value==""){
       alert("Please fill up the entry of Server Name");
       return false;
   }
   if(tunnel_table.user_name.value==""){
       alert("Please fill up the entry of User name");
       return false;
   }
   if(tunnel_table.user_password.value==""){
      alert("Please fill up the entry of Login with Password");
      return false;
   }
  // if(tunnel_table.route_commands.value==""){
  //     alert("Please fill up the entry of Other Route Commands");
  //     return false;
  // }
  // if(!tunnel_table.encryption1_type[0].checked && !tunnel_table.encryption1_type[1].checked && !tunnel_table.encryption1_type[2].checked){
  //    alert("Please select one of 128-bit encryption of items");
  //    return false;
  // }

   return true;
}
