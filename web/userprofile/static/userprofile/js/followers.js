console.log('ttt')
$(function(){
 $('#followersButton').click(followApi)
 $('#followingButton').click(followApi)

})


function followApi()  {
  let button = $(this);
  $('#followerModal').modal('show')
  $('#followModalTitle').text(button.text())
  $.ajax({
    url: button.attr("data-href"),
    type: "GET",
    success: function(data){
    console.log(data)
    followBodyRender(data)
    }
    })


  console.log(button.data('href'))
}

function followBodyRender(data) {
  user_list = data
  let body = $('#followModalBody')
  body.empty()
  $.each(user_list, function(i){ //Loop the array
   var templateString = `
      <div class="user">
        <p>
          <img src="${user_list[i].image}" class="avatar img-circle img-thumbnail" width=50px>
          <a href='${user_list[i].profile_url}'> ${user_list[i].full_name} </a>
          <button data-id='${user_list[i].id}' data-href='/follow/', class='followButton'>follow</button>
        </p>
      </div>
   `
   body.append(templateString);
  })
    $('.followButton').click(followMe)
}
