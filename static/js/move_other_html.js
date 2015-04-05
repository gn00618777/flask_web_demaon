function autoclick(name){

     if(document.all){
        document.getElementById(name).click();
     }
     else{
        var evt = document.createEvent("MouseEvents");
        evt.initEvent("click", true, true);
        document.getElementById(name).dispatchEvent(evt);
    }
}
