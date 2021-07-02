console.log('like')
$(function(){
$('#likeArticle').click(like)
$('#dislikeArticle').click(dislike)
$('.commentLike').click(likeComment)

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
  console.log('like1')
  let object_id = like_button.data('id')
  console.log(object_id)
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


    },
    error: function (data) {
        console.log('error', data)

    }})

}

//console.log('like')
//$(function(){
//$('#likeArticle').click(articleLikeRequest)
//$('#dislikeArticle').click(articleLikeRequest)
//$('.commentLike').click(commentLike)
//
//})
//
//function articleLikeRequest(e) {
//  let like = $(this);
//  let data = {
//    'object_id': like.data('id'),
//    'model': like.data('type'),
//    'vote': like.data('vote'),
//  }
//  $.ajax({
//    url: like.data('href'),
//    type: 'post',
//    data: data,
//    success: function (data) {
//      $('#articleLikeCount').text(' ' + data.like_count)
//      $('#articleDislikeCount').text(' ' + data.dislike_count)
//      switch (data.status) {
//        case 'liked':
//          liked_style();
//          break
//        case 'disliked':
//          dislike_status()
//          break
//        default:
//          default_status()
//          break
//      }
//    },
//    error: function (data) {
//      console.log(data, "Error")
//    }
//  })
//}
//
//function liked_style() {
//  $('#articleLikeIcon').removeClass('far', 'fa-thumbs-up')
//  $('#articleLikeIcon').addClass('fas', 'fa-thumbs-up')
//
//  $('#articleDislikeIcon').addClass('far', 'fa-thumbs-down')
//  $('#articleDislikeIcon').removeClass('fas', 'fa-thumbs-down')
//}
//
//function dislike_status() {
//  $('#articleLikeIcon').removeClass('fas', 'fa-thumbs-up')
//  $('#articleLikeIcon').addClass('far', 'fa-thumbs-up')
//
//  $('#articleDislikeIcon').addClass('fas', 'fa-thumbs-down')
//  $('#articleDislikeIcon').removeClass('far', 'fa-thumbs-down')
//
//}
//
//function default_status() {
//  $('#articleLikeIcon').removeClass('fas', 'fa-thumbs-up')
//  $('#articleLikeIcon').addClass('far', 'fa-thumbs-up')
//
//  $('#articleDislikeIcon').removeClass('fas', 'fa-thumbs-down')
//  $('#articleDislikeIcon').addClass('far', 'fa-thumbs-down')
//}
//
//
//function commentLike(e) {
//  e.preventDefault()
//  console.log('like')
//  let like = $(this);
//  let data = {
//    'object_id': like.data('id'),
//    'model': like.data('type'),
//    'vote': like.data('vote'),
//  }
//  console.log(data)
//  $.ajax({
//    url: like.data('href'),
//    type: 'post',
//    data: data,
//    success: function (data) {
//      console.log(data, "success")
//
//    },
//    error: function (data) {
//      console.log(data, "Error")
//    }
//  })
//}
