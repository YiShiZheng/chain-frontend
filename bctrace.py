# coding: utf-8

from flask import Flask, render_template, json, request, jsonify, url_for
from flask_bootstrap import Bootstrap
import datetime

from news_operation.news_operate import *
from news_operation.news_in_blockchain import *
from random import randint

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploadedImgs'
bootstrap = Bootstrap(app)

NEWS = init_global_news()
NEWS_TO_DISPLAY = format_news_in_local_cache(NEWS)
HOT_NEWS = init_hot_news(NEWS_TO_DISPLAY)


# mock variable
UID_LIST = ['XinHuaShe', 'ZhongXinWang', 'HuanQiuRiBao', 'FengHuangShe', 'QingNianShe']


@app.route("/")
def index():
    global NEWS, NEWS_TO_DISPLAY
    return render_template("index.html", news=NEWS_TO_DISPLAY, hot_news=HOT_NEWS)


@app.route('/news/<int:id>')
def detailed_news(id):
    global NEWS_TO_DISPLAY
    news_item = [news_item for news_item in NEWS_TO_DISPLAY if news_item['news_link'] == 'news/'+str(id)][0]
    return render_template('detailed_news.html', title=news_item['title'], content=news_item['content'])


@app.route('/bctrace/<int:news_id>')
def trace_news(news_id):
    global NEWS, NEWS_TO_DISPLAY
    traced_news = get_traced_news(news_id, NEWS, NEWS_TO_DISPLAY)
    return render_template('bctrace.html', traced_news=traced_news)


@app.route('/createNews')
def create_news():
    return render_template('create_news.html', btn_name=u'发布', raw_data='', title='')


@app.route('/forwardNews/<int:id>')
def forward_news(id):
    global NEWS_TO_DISPLAY
    news_item = [news_item for news_item in NEWS_TO_DISPLAY if news_item['news_link'] == 'news/' + str(id)][0]
    return render_template('create_news.html', btn_name=u'转发', raw_data=news_item['content'], title=news_item['title'])


@app.route('/createNewsInBackend', methods=['POST'])
def create_news_in_backend():
    data = json.loads(request.get_data())
    timestamp = time.time()
    data_in_ipfs = {'newsHtml': data['newsHtml'], 'newsTitle': data['newsTitle']}
    # different actions based on actionType
    global NEWS, NEWS_TO_DISPLAY
    current_hash = save_news_into_ipfs(data_in_ipfs)
    data['hash'] = current_hash
    uid = UID_LIST[randint(0, len(UID_LIST)-1)]
    data['uid'] = uid
    if data['actionType'] == 0:
        # direct or modify
        forward_from_id = int(data['forwardFromId'])
        news_item_forward_from = [news_item for news_item in NEWS if news_item.get_id() == forward_from_id][0]
        previous_hash = news_item_forward_from.get_hash()
        request_data = {'hash': current_hash, 'uid': uid, 'forward_from': previous_hash, 'timestamp': timestamp}
        if current_hash != previous_hash:
            data['action'] = 'modify'
            modified_news_in_blockchain(request_data)
        else:
            data['action'] = 'forward'
            forward_news_in_blockchain(request_data)
    elif data['actionType'] == 1:
        # create
        data['action'] = 'create'
        reuqest_data = {'hash': current_hash, 'uid': uid, 'timestamp': timestamp}
        save_news_into_blockchain(reuqest_data)
    update_cache(data, NEWS, NEWS_TO_DISPLAY, timestamp)
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


@app.route('/getNewsCount', methods=['GET'])
def get_news_count():
    result = get_news_count_in_blockchain()
    response = result['result']['msg']
    return response


@app.route('/getBlockCount', methods=['GET'])
def get_block_count():
    result = get_block_count_in_blockchain()
    response = result['result']['msg']
    return response


if __name__ == "__main__":
    # set FLASK_ENV=development
    # app.run(host='150.236.221.221', port=5000, debug=True)
    app.run()