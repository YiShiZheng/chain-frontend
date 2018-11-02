import requests
import json, pprint

ADDRESS_OF_BACKEND_TO_GET = 'http://150.236.223.144:4000'
ADDRESS_OF_BACKEND_TO_OTHER = 'http://150.236.223.167:4001'
SUCCESS = 'success'
FAIL = 'fail'


def get_latest_news_from_blockchain():
    data = {"jsonrpc": "2.0", "method": "get_latest_newsletter", "params": [""], "id": 3}
    try:
        r = requests.post(ADDRESS_OF_BACKEND_TO_GET, data=json.dumps(data))
        return r.json()
    except Exception as e:
        print "!!!Error happened when fetch latest data from blockchin: {}".format(e)
        return None


def save_news_into_blockchain(request_data):
    # 1.hash  2.uid 3.timestamp
    params = [request_data['hash'], request_data['uid'], request_data['timestamp']]
    data = {"jsonrpc": "2.0", "method": "submit_newsletter", "params": params, "id": 0}
    try:
        requests.post(ADDRESS_OF_BACKEND_TO_OTHER, data=json.dumps(data))
    except Exception as e:
        print "!!!Error happened when save data into blockchain: {}".format(e)
    print "===Save news {} into blockchain successfully".format(request_data['hash'])


def forward_news_in_blockchain(request_data):
    # 1. new hash 2. uid 3. hash forward from 4. timestamp
    params = [request_data['hash'], request_data['forward_from'],  request_data['uid'], request_data['timestamp']]
    data = {"jsonrpc": "2.0", "method": "forward_newsletter", "params": params, "id": 2}
    try:
        requests.post(ADDRESS_OF_BACKEND_TO_OTHER, data=json.dumps(data))
    except Exception as e:
        print "!!!Error happened when forward data in blockchain: {}".format(e)
    print "===Forward news {}  from {} into blockchain successfully".format(request_data['hash'], request_data['forward_from'])


def modified_news_in_blockchain(request_data):
    # 1. new hash 2. uid 3. hash forward from 4. timestamp
    params = [request_data['hash'], request_data['forward_from'], request_data['uid'], request_data['timestamp']]
    data = {"jsonrpc": "2.0", "method": "modify_newsletter", "params": params, "id": 2}
    try:
        requests.post(ADDRESS_OF_BACKEND_TO_OTHER, data=json.dumps(data))
    except Exception as e:
        print "!!!Error happened when forward data in blockchain: {}".format(e)
    print "===Modified news {}  from {} into blockchain successfully".format(request_data['hash'], request_data['forward_from'])


def get_news_count_in_blockchain():
    # return {'result': {'msg': '2'}}
    data = {"jsonrpc": "2.0", "method": "get_newsletter_count", "params": [""], "id": 0}
    try:
        r = requests.post(ADDRESS_OF_BACKEND_TO_GET, data=json.dumps(data))
        return r.json()
    except Exception as e:
        print "!!!Error happened when forward data in blockchain: {}".format(e)
        return None


def get_block_count_in_blockchain():
    data = {"jsonrpc": "2.0", "method": "get_block_count", "params": [""], "id": 0}
    try:
        r = requests.post(ADDRESS_OF_BACKEND_TO_GET, data=json.dumps(data))
        return r.json()
    except Exception as e:
        print "!!!Error happened when forward data in blockchain: {}".format(e)
        return None


def get_traced_in_blockchain(current_hash):
    data = {
        "jsonrpc": "2.0",
        "method": "get_traces_by_url",
        "params": [current_hash],
        "id": 0
    }
    try:
        r = requests.post(ADDRESS_OF_BACKEND_TO_GET, data=json.dumps(data))
        return r.json()
    except Exception as e:
        print "!!!Error happened when trying to trace history in blockchain: {}".format(e)
        return None

