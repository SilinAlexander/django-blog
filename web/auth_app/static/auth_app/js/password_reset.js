console.log('passwordReset')
$(function(){
  $('#passwordResetForm').submit(passwordReset);
});
function passwordReset(e){
e.preventDefault();
console.log('click')

}
