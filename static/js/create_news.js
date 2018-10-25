
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
            window.location = 'http://127.0.0.1:5000/';
        },
        error: function(return_code){
            $("#create_new_article_btn").attr("disabled",false);
            console.error('失败!');
            alert('发布失败，原因：xxxxxx');
        }
    });
});