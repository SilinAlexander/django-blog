console.log('ttt')
$(function(){
 $('#followersButton').click(followApi)
 $('#followingButton').click(followApi)

})


function followApi()  {
  let button = $(this);

  console.log(button.data('href'))
}
