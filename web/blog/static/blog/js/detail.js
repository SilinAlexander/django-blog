$(function () {

$('#commentForm').submit(commentCreate)

});
function commentCreate(event){
    event.preventDefault();
    console.log('click')
    let form = $(this);
    let path = form.attr('action')
    console.log(path)
    let data = form.serialize()
    console.log(data)

}
console.log('blog-detail')
