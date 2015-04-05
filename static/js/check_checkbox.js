function check(){

   var check=document.getElementsByTagName("input")
   var sel=false;
   
   for(var i=0;i<check.length;i++){
  
       if(check[i].name=="account" && check[i].checked){
  
          sel=true;
          break;       
 
       }  
   }
   if(!sel) alert("At least select one of accounts");

   return sel;
}
