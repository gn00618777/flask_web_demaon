function check(){

    if(add_account_table.ppp_account.value==""){

       alert("Please fill up the text of Account");
       return false;       

    }
    if(add_account_table.ppp_password.value==""){

       alert("Please fill up the text of Password");
       return false;
    }

    return true;
}
