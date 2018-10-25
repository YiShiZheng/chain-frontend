# coding: utf-8
import time
import subprocess
import re
import base64
import json
import os

from news_in_blockchain import *
from news_cache import news_item


def init_global_news():
    respnse = get_latest_news_from_blockchain()
    news = []
    id = 0
    for item in respnse['result']:
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
    return {
            'news_link': news_item.get_news_link(),
            'img': news_item.get_img(),
            'title': news_item.get_title(),
            'content': news_item.get_content(),
            'forward_counts': news_item.get_forward_accounts(),
            'created_at': news_item.get_created_at(),
            'user': news_item.get_user()
        }


def update_cache(article, NEWS, NEWS_TO_DISPLAY):
    article['id'] = len(NEWS) + 1
    news = news_item(**article)
    NEWS.append(news_item(**article))
    NEWS_TO_DISPLAY.insert(0, _create_news_item_by_news_modle(news))


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

