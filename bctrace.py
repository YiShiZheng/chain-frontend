# coding: utf-8

from flask import Flask, render_template, json, request, jsonify, url_for
from flask_bootstrap import Bootstrap
import datetime

from news_operation.news_operate import *
from news_operation.news_in_blockchain import *

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploadedImgs'
bootstrap = Bootstrap(app)

NEWS = init_global_news()
NEWS_TO_DISPLAY = format_news_in_local_cache(NEWS)


@app.route("/")
def index():
    global NEWS, NEWS_TO_DISPLAY
    return render_template("index.html", news=NEWS_TO_DISPLAY)


@app.route('/news/<int:id>')
def detailed_news(id):
    global NEWS_TO_DISPLAY
    news_item = [news_item for news_item in NEWS_TO_DISPLAY if news_item['news_link'] == 'news/'+str(id)][0]
    return render_template('detailed_news.html', title=news_item['title'], content=news_item['content'])


@app.route('/bctrace/<int:news_id>')
def trace_news(news_id):
    return render_template('bctrace.html', news_id=news_id)


@app.route('/createNews')
def create_news():
    return render_template('create_news.html')


@app.route('/forwardNews')
def forward_news():
    return render_template('create_news.html')


@app.route('/createNewsInBackend', methods=['POST'])
def create_news_in_backend():
    data = json.loads(request.get_data())
    global NEWS, NEWS_TO_DISPLAY
    update_cache(data, NEWS, NEWS_TO_DISPLAY)
    file_hash = save_news_into_ipfs(data)
    return '200'


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('editormd-image-file')
    if not file:
        res = {
            'success': 0,
            'message': u'图片格式异常'
        }
    else:
        ex = os.path.splitext(file.filename)[1]
        filename = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + ex
        basedir = os.path.abspath(os.path.dirname(__file__))
        file.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], filename))
        res = {
            'success': 1,
            'message': u'图片上传成功',
            'url': url_for('static', filename=os.path.join('uploadedImgs/', filename))
        }
    return jsonify(res)


if __name__ == "__main__":
    # set FLASK_ENV=development
    app.run()