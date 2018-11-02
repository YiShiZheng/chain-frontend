
$("#create_news_btn").click(function(){
    $("#create_news_btn").attr("disabled","true");
    var newsHtml = $(".editormd-markdown-textarea").val();
    var newsTitle = $("input").val();
    var action = $("#create_news_btn").text();
    if (action === '发布'){
        actionType = 1;
        forwardFromId = 0;
    }
    else if (action === '转发'){
        actionType = 0;
        var url = document.location.toString();
        var arrObj = url.split("/");
        forwardFromId = arrObj.pop()

    }
    $.ajax({
        url: "/createNewsInBackend",
        type: "post",
        data:JSON.stringify({
            'newsTitle': newsTitle,
            'newsHtml': newsHtml,
            'actionType': actionType,
            'forwardFromId': forwardFromId,
        }),
        dataType:'JSON',
        success: function(return_code){
            // $("#create_article_form").prepend('<div class="alert alert-success" id="response-to-create">创建成功! 3秒之后跳转到主页面</div>');
            // setTimeout('displayInverval(2)', 1000)
            console.error('11111成功了！！');
            window.location = '/';
        },
        error: function(return_code){
            $("#create_news_btn").attr("disabled",false);
            console.error('失败!'+return_code);
            // alert('发布失败，原因：xxxxxx');
            window.location = '/';
        }
    });
});