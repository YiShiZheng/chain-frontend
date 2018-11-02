function forwardNews(){
    var url = document.location.toString();
    var arrObj = url.split("/");
    var forwardFromId = arrObj.pop()
    var redirectUrl = '/forwardNews/' + forwardFromId
    window.location = redirectUrl;
}

$("#create_new_article_btn").click(function(){
    var newsHtml = $(".editormd-markdown-textarea").val();
    var newsTitle = $("input").val();
    console.error(newsTitle);
    $("#create_new_article_btn").attr("disabled","true");
    $.ajax({
        url: "/createNewsInBackend",
        type: "post",
        data:JSON.stringify({
            'newsTitle': newsTitle,
            'newsHtml': newsHtml,
        }),
        dataType:'JSON',
        success: function(return_code){
            // $("#create_article_form").prepend('<div class="alert alert-success" id="response-to-create">创建成功! 3秒之后跳转到主页面</div>');
            // setTimeout('displayInverval(2)', 1000)
            console.error('11111成功了！！');
            window.location = '/';
        },
        error: function(return_code){
            $("#create_new_article_btn").attr("disabled",false);
            console.error('失败!');
            alert('发布失败，原因：xxxxxx');
        }
    });
});

function traceNews(){
    var url = document.location.toString();
    var arrObj = url.split("/");
    var forwardFromId = arrObj.pop()
    var redirectUrl = '/bctrace/' + forwardFromId
    window.location = redirectUrl;
}