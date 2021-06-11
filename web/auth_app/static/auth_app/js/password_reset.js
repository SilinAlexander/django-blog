console.log('passwordReset')
$(function(){
  $('#passwordResetForm').submit(passwordReset);
});
function passwordReset(e){
e.preventDefault();
//console.log('click')
//console.log('reset_password')
    console.log(window.location.pathname)
    let path = window.location.pathname
    let form = $(this);
    let objects = path.split('/')
//    console.log(objects)
    console.log(form.serialize())
    let data = {
      'new_password1': $("[name='new_password1']").val(),
      'new_password2': $("[name='new_password2']").val(),
      'uid': objects[3],
      'token': objects[4],


    }
    console.log($("[name='new_password1']").val())
//    let data2 = {
//      ...data,
//      ...form.serialize(),
//    }
//    console.log(data2)
//    const newObj = Object.assign({}, data, form.serialize());
//
//    console.log(newObj);
//    for (let item of form.serializeArray()){
//      console.log(item)
//    }

    console.log(data)
    $.ajax({
    url: form.attr('action'),
    type: 'post',
    data: data,
    success: function(data){
    let url = form.data('success');
    window.location.href = url
    console.log(data)

    },
     error : function(data){
      console.log(data, 'error')
      }
    })
}
