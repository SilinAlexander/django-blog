//console.log('like')
$(function(){
$('#like_article').click(like)
$('#dislike_article').click(dislike)
$('#likeButtonComment').click(likeComment)

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
        $('#articleLikeCount').text(data.like_count)
        $('#articleDislikeCount').text(data.dislike_count)

//        like_button.find('[data-count="like"]').text(data.like_count)
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
  let object_id = dislike_button.data('id')
  console.log(object_id)
  let vote = -1
  console.log(vote)
  let model = dislike_button.data('type')
  console.log(model)
  let data ={
  'object_id':  dislike_button.data('id'),
  'vote': -1,
  'model': dislike_button.data('type')
  }
  $.ajax({
  url: dislike_button.data('href'),
  type: "POST",
    dataType: 'json',
    data: data,
    success: function (data) {
        console.log('success', data)
//        dislike_button.find('[data-count="dislike"]').text(data.dislike_count)
        $('#articleLikeCount').text(data.like_count)
        $('#articleDislikeCount').text(data.dislike_count)
    },
    error: function (data) {
        console.log('error', data)

    }

  })
}

function likeComment(e){
  let like_button = $(this);
  e.preventDefault();
  console.log('like')
  let object_id = like_button.data('id')
  console.log(object_id)

}
