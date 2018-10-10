# coding: utf-8

from flask import Flask, render_template, json, request, jsonify, url_for
from flask_bootstrap import Bootstrap
import time
import datetime
import subprocess
import os
import re
import base64

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploadedImgs'
bootstrap = Bootstrap(app)

news_example_body = '郇政华上大学的消息很快被妻子得知。“我爱人严厉反对，上大学耽误赚钱啊！” 郇政华说，得知自己年龄及家庭经济状况后，学校向其减免了6200元的学费和部分生活用品采购费用；校学生会还给他介绍了一份泥瓦匠的工作，周末上班，一天70块钱。“这些钱对我家来说远远不够。”郇政华不得不对现实做出妥协，但他仍然没有放弃求学，希望学校发新书时能给他寄一套过来，平时抽空学习、考试时去考试，籍此完成大学学业。郇政华上大学的消息很快被妻子得知。“我爱人严厉反对，上大学耽误赚钱啊！” 郇政华说，得知自己年龄及家庭经济状况后，学校向其减免了6200元的学费和部分生活用品采购费用；校学生会还给他介绍了一份泥瓦匠的工作，周末上班，一天70块钱。“这些钱对我家来说远远不够。”郇政华不得不对现实做出妥协，但他仍然没有放弃求学，希望学校发新书时能给他寄一套过来，平时抽空学习、考试时去考试，籍此完成大学学业。郇政华上大学的消息很快被妻子得知。“我爱人严厉反对，上大学耽误赚钱啊！” 郇政华说，得知自己年龄及家庭经济状况后，学校向其减免了6200元的学费和部分生活用品采购费用；校学生会还给他介绍了一份泥瓦匠的工作，周末上班，一天70块钱。“这些钱对我家来说远远不够。”郇政华不得不对现实做出妥协，但他仍然没有放弃求学，希望学校发新书时能给他寄一套过来，平时抽空学习、考试时去考试，籍此完成大学学业。郇政华上大学的消息很快被妻子得知。“我爱人严厉反对，上大学耽误赚钱啊！” 郇政华说，得知自己年龄及家庭经济状况后，学校向其减免了6200元的学费和部分生活用品采购费用；校学生会还给他介绍了一份泥瓦匠的工作，周末上班，一天70块钱。“这些钱对我家来说远远不够。”郇政华不得不对现实做出妥协，但他仍然没有放弃求学，希望学校发新书时能给他寄一套过来，平时抽空学习、考试时去考试，籍此完成大学学业。郇政华上大学的消息很快被妻子得知。“我爱人严厉反对，上大学耽误赚钱啊！” 郇政华说，得知自己年龄及家庭经济状况后，学校向其减免了6200元的学费和部分生活用品采购费用；校学生会还给他介绍了一份泥瓦匠的工作，周末上班，一天70块钱。“这些钱对我家来说远远不够。”郇政华不得不对现实做出妥协，但他仍然没有放弃求学，希望学校发新书时能给他寄一套过来，平时抽空学习、考试时去考试，籍此完成大学学业。郇政华上大学的消息很快被妻子得知。“我爱人严厉反对，上大学耽误赚钱啊！” 郇政华说，得知自己年龄及家庭经济状况后，学校向其减免了6200元的学费和部分生活用品采购费用；校学生会还给他介绍了一份泥瓦匠的工作，周末上班，一天70块钱。“这些钱对我家来说远远不够。”郇政华不得不对现实做出妥协，但他仍然没有放弃求学，希望学校发新书时能给他寄一套过来，平时抽空学习、考试时去考试，籍此完成大学学业。郇政华上大学的消息很快被妻子得知。“我爱人严厉反对，上大学耽误赚钱啊！” 郇政华说，得知自己年龄及家庭经济状况后，学校向其减免了6200元的学费和部分生活用品采购费用；校学生会还给他介绍了一份泥瓦匠的工作，周末上班，一天70块钱。“这些钱对我家来说远远不够。”郇政华不得不对现实做出妥协，但他仍然没有放弃求学，希望学校发新书时能给他寄一套过来，平时抽空学习、考试时去考试，籍此完成大学学业。郇政华上大学的消息很快被妻子得知。“我爱人严厉反对，上大学耽误赚钱啊！” 郇政华说，得知自己年龄及家庭经济状况后，学校向其减免了6200元的学费和部分生活用品采购费用；校学生会还给他介绍了一份泥瓦匠的工作，周末上班，一天70块钱。“这些钱对我家来说远远不够。”郇政华不得不对现实做出妥协，但他仍然没有放弃求学，希望学校发新书时能给他寄一套过来，平时抽空学习、考试时去考试，籍此完成大学学业。郇政华上大学的消息很快被妻子得知。“我爱人严厉反对，上大学耽误赚钱啊！” 郇政华说，得知自己年龄及家庭经济状况后，学校向其减免了6200元的学费和部分生活用品采购费用；校学生会还给他介绍了一份泥瓦匠的工作，周末上班，一天70块钱。“这些钱对我家来说远远不够。”郇政华不得不对现实做出妥协，但他仍然没有放弃求学，希望学校发新书时能给他寄一套过来，平时抽空学习、考试时去考试，籍此完成大学学业。郇政华上大学的消息很快被妻子得知。“我爱人严厉反对，上大学耽误赚钱啊！” 郇政华说，得知自己年龄及家庭经济状况后，学校向其减免了6200元的学费和部分生活用品采购费用；校学生会还给他介绍了一份泥瓦匠的工作，周末上班，一天70块钱。“这些钱对我家来说远远不够。”郇政华不得不对现实做出妥协，但他仍然没有放弃求学，希望学校发新书时能给他寄一套过来，平时抽空学习、考试时去考试，籍此完成大学学业。郇政华上大学的消息很快被妻子得知。“我爱人严厉反对，上大学耽误赚钱啊！” 郇政华说，得知自己年龄及家庭经济状况后，学校向其减免了6200元的学费和部分生活用品采购费用；校学生会还给他介绍了一份泥瓦匠的工作，周末上班，一天70块钱。“这些钱对我家来说远远不够。”郇政华不得不对现实做出妥协，但他仍然没有放弃求学，希望学校发新书时能给他寄一套过来，平时抽空学习、考试时去考试，籍此完成大学学业。郇政华上大学的消息很快被妻子得知。“我爱人严厉反对，上大学耽误赚钱啊！” 郇政华说，得知自己年龄及家庭经济状况后，学校向其减免了6200元的学费和部分生活用品采购费用；校学生会还给他介绍了一份泥瓦匠的工作，周末上班，一天70块钱。“这些钱对我家来说远远不够。”郇政华不得不对现实做出妥协，但他仍然没有放弃求学，希望学校发新书时能给他寄一套过来，平时抽空学习、考试时去考试，籍此完成大学学业。郇政华上大学的消息很快被妻子得知。“我爱人严厉反对，上大学耽误赚钱啊！” 郇政华说，得知自己年龄及家庭经济状况后，学校向其减免了6200元的学费和部分生活用品采购费用；校学生会还给他介绍了一份泥瓦匠的工作，周末上班，一天70块钱。“这些钱对我家来说远远不够。”郇政华不得不对现实做出妥协，但他仍然没有放弃求学，希望学校发新书时能给他寄一套过来，平时抽空学习、考试时去考试，籍此完成大学学业。郇政华上大学的消息很快被妻子得知。“我爱人严厉反对，上大学耽误赚钱啊！” 郇政华说，得知自己年龄及家庭经济状况后，学校向其减免了6200元的学费和部分生活用品采购费用；校学生会还给他介绍了一份泥瓦匠的工作，周末上班，一天70块钱。“这些钱对我家来说远远不够。”郇政华不得不对现实做出妥协，但他仍然没有放弃求学，希望学校发新书时能给他寄一套过来，平时抽空学习、考试时去考试，籍此完成大学学业。郇政华上大学的消息很快被妻子得知。“我爱人严厉反对，上大学耽误赚钱啊！” 郇政华说，得知自己年龄及家庭经济状况后，学校向其减免了6200元的学费和部分生活用品采购费用；校学生会还给他介绍了一份泥瓦匠的工作，周末上班，一天70块钱。“这些钱对我家来说远远不够。”郇政华不得不对现实做出妥协，但他仍然没有放弃求学，希望学校发新书时能给他寄一套过来，平时抽空学习、考试时去考试，籍此完成大学学业。郇政华上大学的消息很快被妻子得知。“我爱人严厉反对，上大学耽误赚钱啊！” 郇政华说，得知自己年龄及家庭经济状况后，学校向其减免了6200元的学费和部分生活用品采购费用；校学生会还给他介绍了一份泥瓦匠的工作，周末上班，一天70块钱。“这些钱对我家来说远远不够。”郇政华不得不对现实做出妥协，但他仍然没有放弃求学，希望学校发新书时能给他寄一套过来，平时抽空学习、考试时去考试，籍此完成大学学业。'

news = [
    {
        'news_link': 'news/1',
        'img': '//p9.pstatp.com/list/190x124/pgc-image/15360241463376f68781d3d',
        'title': unicode("奥运冠军夫妇现状：36岁杜丽当教练，宛如18少女，丈夫想再战奥运#", "utf8"),
        'content': unicode(news_example_body, "utf8"),
        'forward_counts': 120,
        'created_at': '2018-09-06 12:23:23',
        'user': {
            'img': '//p4.pstatp.com/large/6eee0001b0fd62c4ccda',
            'nick_name': unicode('新华社', "utf8"),
            'user_page': 'xx/xx'
        }
     },
    #
    # {
    #     'news_link': 'news/2',
    #     'img': '//p9.pstatp.com/list/190x124/pgc-image/15360241463376f68781d3d',
    #     'title': unicode("奥运冠军夫妇现状：36岁杜丽当教练，宛如18少女，丈夫想再战奥运#", "utf8"),
    #     'content': unicode(news_example_body, "utf8"),
    #     'forward_counts': 120,
    #     'created_at': '2018-09-06 12:23:23',
    #     'user': {
    #         'img': '//p4.pstatp.com/large/6eee0001b0fd62c4ccda',
    #         'nick_name': unicode('新华社', "utf8"),
    #         'user_page': 'xx/xx'
    #     }
    # },
    #
    # {
    #     'news_link': 'news/3',
    #     'img': '//p9.pstatp.com/list/190x124/pgc-image/15360241463376f68781d3d',
    #     'title': unicode("奥运冠军夫妇现状：36岁杜丽当教练，宛如18少女，丈夫想再战奥运#", "utf8"),
    #     'content': unicode(news_example_body, "utf8"),
    #     'forward_counts': 120,
    #     'created_at': '2018-09-06 12:23:23',
    #     'user': {
    #         'img': '//p4.pstatp.com/large/6eee0001b0fd62c4ccda',
    #         'nick_name': unicode('新华社', "utf8"),
    #         'user_page': 'xx/xx'
    #     }
    # },
    #
    # {
    #     'news_link': 'news/4',
    #     'img': '//p9.pstatp.com/list/190x124/pgc-image/15360241463376f68781d3d',
    #     'title': unicode("奥运冠军夫妇现状：36岁杜丽当教练，宛如18少女，丈夫想再战奥运#", "utf8"),
    #     'content': unicode(news_example_body, "utf8"),
    #     'forward_counts': 120,
    #     'created_at': '2018-09-06 12:23:23',
    #     'user': {
    #         'img': '//p4.pstatp.com/large/6eee0001b0fd62c4ccda',
    #         'nick_name': unicode('新华社', "utf8"),
    #         'user_page': 'xx/xx'
    #     }
    # },
    #
    # {
    #     'news_link': 'news/5',
    #     'img': '//p9.pstatp.com/list/190x124/pgc-image/15360241463376f68781d3d',
    #     'title': unicode("奥运冠军夫妇现状：36岁杜丽当教练，宛如18少女，丈夫想再战奥运#", "utf8"),
    #     'content': unicode(news_example_body, "utf8"),
    #     'forward_counts': 120,
    #     'created_at': '2018-09-06 12:23:23',
    #     'user': {
    #         'img': '//p4.pstatp.com/large/6eee0001b0fd62c4ccda',
    #         'nick_name': unicode('新华社', "utf8"),
    #         'user_page': 'xx/xx'
    #     }
    # },
]


@app.route("/")
def index():
    return render_template("index.html", news=news)


@app.route('/news/<int:id>')
def detailed_news(id):
    news_item = [news_item for news_item in news if news_item['news_link'] == 'news/'+str(id)][0]
    return render_template('detailed_news.html', title=news_item['title'], content=news_item['content'])


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


@app.route('/createNewsInBackend', methods=['POST'])
def create_news_in_backend():
    data = json.loads(request.get_data())
    add_new_article_to_cache(data)
    # save into ipfs
    file_hash = save_news_into_ipfs(data)
    get_news_from_ipfs(file_hash)
    # print('Successfully saved news into IPFS with HASH: {}'.format(corresponding_hash))
    return '200'


def _get_file_from_ipfs(hash, is_json=True):
    command = 'ipfs cat {}'.format(hash)
    subp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                            cwd="C:\Users\eyiszhe\Desktop\BCtrace\services\go-ipfs")
    stdout, stderr = subp.communicate()
    if subp.returncode != 0:
        print('===Error {} happened with command {}'.format(stderr, command))
    elif not stdout:
        print('===No return value get from IPFS, stdout was none!')
    else:
        result = stdout if not is_json else json.loads(stdout)
        print('get file {} from ipfs successfully with command {}'.format(result, command))
        return result


def get_news_from_ipfs(hash):
    result = _get_file_from_ipfs(hash)
    imgs_data = json.loads(result.get('imgs_data'))
    news_title = result.get('newsTitle')
    news_html = result.get('newsHtml')
    for img_name in imgs_data:
        img_data = base64.b64decode(imgs_data[img_name])
        with open('img1.png', "wb") as output_file:
            output_file.write(img_data)


def add_new_article_to_cache(article):
    news_id = len(news) + 1
    news_item = {
        'news_link': 'news/' + str(news_id),
        'img': '//p9.pstatp.com/list/190x124/pgc-image/15360241463376f68781d3d',
        'forward_counts': 120,
        'title': article['newsTitle'],
        'content': article['newsHtml'],
        'created_at': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        'user': {
            'img': '//p4.pstatp.com/large/6eee0001b0fd62c4ccda',
            'nick_name': unicode('新华社', "utf8"),
            'user_page': 'xx/xx'
        }
    }
    news.insert(0, news_item)


def _save_file_into_ipfs(path):
    command = 'ipfs add {}'.format(path)
    subp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                            cwd="C:\Users\eyiszhe\Desktop\BCtrace\services\go-ipfs")
    stdout, stderr = subp.communicate()
    if subp.returncode != 0:
        print('===Error happened: {}'.format(stderr))
    elif not stdout:
        print('===No return value get from IPFS, stdout was none!')
    else:
        hash = stdout.split()[1]
        print('saved {} into ipfs successfully, hash: {}'.format(path, hash))
        return hash


def save_news_into_ipfs(article):
    img_pattern = re.compile(r'/static/uploadedImgs/[0-9]{14}[.jpg.jpeg.png.bmp]{4,7}')
    img_links = img_pattern.findall(article['newsHtml'])
    imgs_data = {}
    cwd = os.getcwd()
    for img_link in img_links:
        split_str = '/' if '/' in img_link else '\\'
        img_name = img_link.split(split_str)[-1]
        complete_path = os.path.join(cwd, 'static', 'uploadedImgs', img_name)
        with open(complete_path, 'rb') as img:
            imgs_data[img_name] = base64.b64encode(img.read())

    file_path = os.path.join(cwd, 'newsHmtl.json')
    with open(file_path, 'w') as outfile:
        article['imgs_data'] = json.dumps(imgs_data)
        json.dump(article, outfile)
    file_hash = _save_file_into_ipfs(file_path)
    return file_hash


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