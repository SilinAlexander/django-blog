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
      console.log(data)
    },
    error : function(data){
      console.log(data, 'error')
      $('.help-block').remove()
      if (typeof data.responseJSON.first_name !== 'undefined'){
      $('#firstNameGroup').addClass('has-error')
      $('#firstNameGroup').append(
        "<div class='help-block'>"+ data.responseJSON.first_name +"</div>"
      )
      }




    }
  }
  )
}
