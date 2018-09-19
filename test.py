# coding: utf-8

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

news = [
    {
        'news_link': 'news/2',
        'img': '//p9.pstatp.com/list/190x124/pgc-image/15360241463376f68781d3d',
        'title': unicode("奥运冠军夫妇现状：36岁杜丽当教练，宛如18少女，丈夫想再战奥运#", "utf8"),
        'forward_counts': 120,
        'created_at': '2018-09-06 12:23:23',
        'user': {
            'img': '//p4.pstatp.com/large/6eee0001b0fd62c4ccda',
            'nick_name': unicode('新华社', "utf8"),
            'user_page': 'xx/xx'
        }
     },

    {
        'aaa': '这是一条测试新闻',
        'img': '//p9.pstatp.com/list/190x124/pgc-image/15360241463376f68781d3d',
        'title': unicode("奥运冠军夫妇现状：36岁杜丽当教练，宛如18少女，丈夫想再战奥运#", "utf8"),
        'forward_counts': 120,
        'created_at': '2018-09-06 12:23:23',
        'user': {
            'img': '//p4.pstatp.com/large/6eee0001b0fd62c4ccda',
            'nick_name': unicode('新华社', "utf8"),
            'user_page': 'xx/xx'
        }
    },

    {
        'aaa': '这是一条测试新闻',
        'img': '//p9.pstatp.com/list/190x124/pgc-image/15360241463376f68781d3d',
        'title': unicode("奥运冠军夫妇现状：36岁杜丽当教练，宛如18少女，丈夫想再战奥运#", "utf8"),
        'forward_counts': 120,
        'created_at': '2018-09-06 12:23:23',
        'user': {
            'img': '//p4.pstatp.com/large/6eee0001b0fd62c4ccda',
            'nick_name': unicode('新华社', "utf8"),
            'user_page': 'xx/xx'
        }
    },

    {
        'aaa': '这是一条测试新闻',
        'img': '//p9.pstatp.com/list/190x124/pgc-image/15360241463376f68781d3d',
        'title': unicode("奥运冠军夫妇现状：36岁杜丽当教练，宛如18少女，丈夫想再战奥运#", "utf8"),
        'forward_counts': 120,
        'created_at': '2018-09-06 12:23:23',
        'user': {
            'img': '//p4.pstatp.com/large/6eee0001b0fd62c4ccda',
            'nick_name': unicode('新华社', "utf8"),
            'user_page': 'xx/xx'
        }
    },

    {
        'aaa': '这是一条测试新闻',
        'img': '//p9.pstatp.com/list/190x124/pgc-image/15360241463376f68781d3d',
        'title': unicode("奥运冠军夫妇现状：36岁杜丽当教练，宛如18少女，丈夫想再战奥运#", "utf8"),
        'forward_counts': 120,
        'created_at': '2018-09-06 12:23:23',
        'user': {
            'img': '//p4.pstatp.com/large/6eee0001b0fd62c4ccda',
            'nick_name': unicode('新华社', "utf8"),
            'user_page': 'xx/xx'
        }
    },
]


@app.route("/")
def index():
    return render_template("index.html", news=news)


@app.route('/news/<int:id>')
def detailed_news(id):
    return render_template('detailed_news.html', id=id)


@app.route('/bctrace/<int:news_id>')
def trace_news(news_id):
    return render_template('bctrace.html', news_id=news_id)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/createNews')
def create_news():
    # show the post with the given id, the id is an integer
    return render_template('create_news.html')


if __name__ == "__main__":
    # set FLASK_ENV=development
    app.run()