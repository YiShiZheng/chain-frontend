# coding: utf-8
import time
import subprocess
import re
import base64
import json
import os
import time

from news_in_blockchain import *
from news_cache import news_item


def init_hot_news(NEWS_TO_DISPLAY):
    result = []
    count = 0
    for news_item in NEWS_TO_DISPLAY:
        if count == 10:
            break;
        count += 1
        result.append({
            'title': news_item['title'],
            'link': news_item['news_link'],
            'action': news_item['action'],
            'created_at': news_item['created_at']
        })
    return result


def init_global_news():
    # response = get_latest_news_from_blockchain()
    response = {u'jsonrpc': u'2.0', u'id': 3, u'result': [{u'timestamp': 24, u'flag': u'SIGNED NEWSLETTER', u'hash': u'QmXajMJhh6E35TcP2gqhZp3sqdXm7tcPFp1LueLJk8nfdV', u'uid': u'wenbang', u'action': u'create'}, {u'timestamp': 22968323, u'flag': u'SIGNED NEWSLETTER', u'hash': u'QmbKRxPw6odVUrcjcAxURJyLM4kuY7ck7GujVEXZwTqx6y', u'uid': u'ezbaowe', u'action': u'create'}, {u'timestamp': 4248528480L, u'flag': u'SIGNED NEWSLETTER', u'hash': u'QmbGQFRtJ6HdN89oyadQTnvKzUPxjRL11v4aDekhCvwMDU', u'uid': u'zak', u'source_hash': u'QmbKRxPw6odVUrcjcAxURJyLM4kuY7ck7GujVEXZwTqx6y', u'action': u'create'}]}
    news = []
    id = 0
    for item in response['result']:
        item['id'] = id
        news.append(news_item(**item))
        id += 1
    return news


def format_news_in_local_cache(news):
    result = []
    for news_item in news:
        result.append(_create_news_item_by_news_modle(news_item))
    return result


def _create_news_item_by_news_modle(news_item):
    created_at = news_item.get_created_at()
    created_at = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(created_at)))
    return {
            'news_link': news_item.get_news_link(),
            'img': news_item.get_img(),
            'title': news_item.get_title(),
            'content': news_item.get_content(),
            'forward_counts': news_item.get_forward_accounts(),
            'created_at': created_at,
            'user': news_item.get_user(),
            'action': news_item.get_action(),
            'hash': news_item.get_hash(),
            'index_img': news_item.get_index_img_name()
        }


def update_cache(article, NEWS, NEWS_TO_DISPLAY, timestamp):
    article['id'] = len(NEWS)
    article['timestamp'] = timestamp
    new_news = news_item(**article)
    NEWS.append(new_news)
    NEWS_TO_DISPLAY.insert(0, _create_news_item_by_news_modle(new_news))


def _save_file_into_ipfs(path):
    command = 'ipfs add {}'.format(path)
    subp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                            cwd="C:\Users\eyiszhe\Desktop\BCtrace\services\go-ipfs")
    stdout, stderr = subp.communicate()
    if subp.returncode != 0:
        print('===Error happened when saving news into ipfs: {}'.format(stderr))
    elif not stdout:
        print('===No return value got from IPFS, stdout was none!')
    else:
        hash = stdout.split()[1]
        print('saved news into ipfs successfully, hash: {}'.format(hash))
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


def get_traced_news(news_id, NEWS, NEWS_TO_DISPLAY):
    news = [news_item for news_item in NEWS_TO_DISPLAY if news_item['news_link'] == 'news/'+str(news_id)][0]
    # news = [news_item for news_item in NEWS if news_item.get_id() == news_id][0]
    response = get_traced_in_blockchain(news['hash'])
    result = []
    for news in response['result']:
        current_news = [news_item for news_item in NEWS_TO_DISPLAY if news_item['hash'] == news['hash']][0]
        complete_link = 'http://127.0.0.1:5000/' + current_news['news_link']
        result.append({'action': current_news['action'],
                       'link': complete_link,
                       'uid': current_news['user']['nick_name'],
                       'created_at': current_news['created_at'],
                       'title': current_news['title']})
    return result
