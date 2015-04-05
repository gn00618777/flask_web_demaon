function rcheck(){


    if(document.getElementById("list_label").innerHTML.match(new RegExp("\\b"+remove_html_form.tunnel_be_remove.value+"\\b"))==null){
       alert("Please select a tunnel to be remove from list");
       return false;
    }
    if(remove_html_form.tunnel_be_remove.value==""){

        alert("The text is empty");
        return false;
    }

    return true;
}
