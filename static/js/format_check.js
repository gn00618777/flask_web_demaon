function check(){

   if( upload_form.file.value == "" ){

       alert("Please select one of files");
       return false;
      
   }

   if( upload_form.file.value.match(".tar\\b") != null){

       return true;   

   } 
   else {

       alert("The file must be made out of \".tar\""); 
       return false;  

   }
}
