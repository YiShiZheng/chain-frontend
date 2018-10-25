# coding: utf-8

import subprocess
import re
import base64
import json
import os


class news_item:
    def __init__(self, **kwargs):
        self._id = kwargs['id']
        self._link_to_detailed_info_page = 'news/{}'.format(self._id)
        self._img = '//p9.pstatp.com/list/190x124/pgc-image/15360241463376f68781d3d'
        self._hash = kwargs.get('hash')
        self._created_at = kwargs.get('timestamp')
        self._forward_counts = 120
        self._user_info = {
            'img': '//p4.pstatp.com/large/6eee0001b0fd62c4ccda',
            'nick_name': unicode('新华社', "utf8"),
            'user_page': 'xx/xx'
        }

        self._get_news_from_ipfs(**kwargs)

    def _get_file_from_ipfs(self, hash, is_json=True):
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
            print('get file from ipfs successfully with command {}'.format(command))
            return result

    def _get_news_from_ipfs(self, **kwargs):
        if self._hash:
            result = self._get_file_from_ipfs(self._hash)
            imgs_data = json.loads(result.get('imgs_data'))
            self._title = result.get('newsTitle')
            self._contnt = result.get('newsHtml')

            pwd = os.getcwd()
            for img_name in imgs_data:
                complete_path = os.path.join(pwd, 'static', 'uploadedImgs', img_name)
                img_data = base64.b64decode(imgs_data[img_name])
                with open(complete_path, "wb") as output_file:
                    output_file.write(img_data)
        else:
            self._title = kwargs.get('newsTitle')
            self._contnt = kwargs.get('newsHtml')

    def get_news_link(self):
        return self._link_to_detailed_info_page

    def get_img(self):
        return self._img

    def get_title(self):
        return self._title

    def get_content(self):
        return self._contnt

    def get_forward_accounts(self):
        return self._forward_counts

    def get_created_at(self):
        return self._created_at

    def get_user(self):
        return self._user_info


if __name__ == "__main__":
    a = {u'timestamp': 24, u'flag': u'SIGNED NEWSLETTER', u'hash': u'QmXajMJhh6E35TcP2gqhZp3sqdXm7tcPFp1LueLJk8nfdV', u'uid': u'wenbang'}
    b = news_item(**a)