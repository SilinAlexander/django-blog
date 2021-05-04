console.log('confirm')
$(function(){
  verify_email()
});
function verify_email()
{
    console.log('verify_email')
    console.log(window.location.pathname)
    let path = window.location.pathname
    let objects = path.split('/')
    console.log(objects[3])
    $.ajax({
    url: $('#verifyConfirm').data('href'),
    type: 'post',
    data: {'key': objects[3]},
    success: function(data){
    let url = $('#successVerify').data('href');
    window.location.href = url
    console.log(data)

    },
     error : function(data){
      console.log(data, 'error')
      }
    })

}
