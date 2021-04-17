console.log('sing-up t')
$(function(){
  $('#signUpForm').submit(signUp);
});

function signUp(event){
  event.preventDefault();
  console.log('click')
}
