console.log('ttt')
$(function(){
  $('.followButton').click(followMe)

})

function followMe(e){
    e.preventDefault();
    console.log('click')
    let button = $(this);
    let user_id = button.data('id')
    let data = {
      'to_user': user_id
    }

    console.log(data)


    $.ajax({
    url: button.data('href'),
    type: 'post',
    data: data,
    success: function(data){
    console.log('success', data)
    }
    })
    }
