//console.log('like')
$(function(){
$('#like_article').click(like)
$('#dislike_article').click(dislike)

})
function like(e){
  let like_button = $(this);
  e.preventDefault();
  console.log('like')
  let object_id = like_button.data('id')
  console.log(object_id)
  let vote = 1
  console.log(vote)
  let model = like_button.data('type')
  console.log(model)
  let data ={
  'object_id':  like_button.data('id'),
  'vote': 1,
  'model': like_button.data('type')
  }
  $.ajax({
  url: like_button.data('href'),
  type: "POST",
    dataType: 'json',
    data: data,
    success: function (data) {
        console.log('success', data)
    },
    error: function (data) {
        console.log('error', data)

    }

  })
}
function dislike(e){
  let dislike_button = $(this);
  e.preventDefault();
  console.log('dislike')
}
