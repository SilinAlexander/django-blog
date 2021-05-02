console.log('sing-up t')
$(function(){
  $('#signUpForm').submit(signUp);
});

function signUp(event){
  event.preventDefault();
  console.log('click')
  let form = $(this);
  let path = form.attr('action')
  console.log(path)
  let data = form.serialize()
  console.log(data)
  $.ajax(
  {
    url : path,
    type : 'post',
    data : data,
    success : function(data){
    let url = form.data('href');
    window.location.href = url
    },
    error : function(data){
      console.log(data, 'error')
      $('.help-block').remove()
      if ( data.responseJSON.first_name ){
         $('#firstNameGroup').addClass('has-error')
         $('#firstNameGroup').append(
         "<div class='help-block'>"+ data.responseJSON.first_name +"</div>"
      )}


      if ( data.responseJSON.last_name ){
      $('#lastNameGroup').addClass('has-error')
      $('#lastNameGroup').append(
        "<div class='help-block'>"+ data.responseJSON.last_name +"</div>"
      )
      }

      if (data.responseJSON.password1 ){
      $('#passwordGroup').addClass('has-error')
      $('#passwordGroup').append(
        "<div class='help-block'>"+ data.responseJSON.password1 +"</div>"
      )}

      if (data.responseJSON.password2 ){
      $('#passwordGroup').addClass('has-error')
      $('#passwordGroup').append(
        "<div class='help-block'>"+ data.responseJSON.password2 +"</div>"
      )}

      if (data.responseJSON.email ){
      $('#emailGroup').addClass('has-error')
      $('#emailGroup').append(
        "<div class='help-block'>"+ data.responseJSON.email +"</div>"
      )}





    }
  }
  )
}
