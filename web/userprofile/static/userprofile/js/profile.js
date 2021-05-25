console.log('ttt')
$(function(){
$('#fileUpload').on('change', changeAvatar)

}
)



function passwordChange(event){
    event.preventDefault();
    console.log('click')
    let form = $(this);
    let path = form.attr('action')
    console.log(path)
    let data = form.serialize()
    console.log(data)

    $.ajax({
    url: path,
    type: 'post',
    data: data,
    success: function(data){
    location.reload()
    },
    error: function(data){
    console.log('error', data)
    }


    })
}



function changeAvatar(e){
   e.preventDefault();
   console.log('ddd')
   let form = $(this)
   path = form.data('href')
   console.log(path)
   let data = new FormData()
   let file = form[0].files
   console.log(file)
   data.append('image', file[0])

   $.ajax({
   url: path,
   type: 'post',
   data: data,
   contentType: false,
   processData: false,
   success: function(data){
   console.log('success', data)
   },
   error: function(data){
   console.log('error', data)
   }



   })


}
