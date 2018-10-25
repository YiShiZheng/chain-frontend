import requests
import json, pprint

ADDRESS_OF_BACKEND = 'http://150.236.226.50:4000'
SUCCESS = 'success'
FAIL = 'fail'


def get_latest_news_from_blockchain():
    data = {"jsonrpc": "2.0", "method": "get_latest_newsletter", "params": [""], "id": 3}
    try:
        r = requests.post(ADDRESS_OF_BACKEND, data=json.dumps(data))
        return r.json()
    except Exception as e:
        print "!!!Error happened when fetch latest data from blockchin: {}".format(e)
        return None


def save_news_into_blockchain():
    data = {"jsonrpc": "2.0", "method": "get_block", "params": ["118"], "id": 3}
    try:
        r = requests.post(ADDRESS_OF_BACKEND, data=json.dumps(data))
        response = r.json()
    except Exception as e:
        print "!!!Error happened when save data into blockchain: {}".format(e)


def forward_news_in_blockchain():
    data = forward_data = {
        "jsonrpc": "2.0",
        "method": "forward_newsletter",
        "params": [
            "QmbKRxPw6odVUrcjcAxURJyLM4kuY7ck7GujVEXZwTqx6y",
            "ezbaowe",
            "QmbKRxPw6odVUrcjcAxURJyLM4kuY7ck7GujVEXZwTqx6y"
        ],
        "id": 2
    }
    try:
        r = requests.post(ADDRESS_OF_BACKEND, data=json.dumps(data))
        return r.json()
    except Exception as e:
        print "!!!Error happened when forward data in blockchain: {}".format(e)
        return None


def modified_news_in_blockchain():
    data = {
        "jsonrpc": "2.0",
        "method": "modify_newsletter",
        "params": [  # 1. new hash & uid & hash forward from & whatever
            "QmbKRxPw6odVUrcjcAxURJyLM4kuY7ck7GujVEXZwTqx6y",
            "ezbaowe",
            "QmbKRxPw6odVUrcjcAxURJyLM4kuY7ck7GujVEXZwTqx6y"
        ],
        "id": 2
    }
    try:
        r = requests.post(ADDRESS_OF_BACKEND, data=json.dumps(data))
        return r.json()
    except Exception as e:
        print "!!!Error happened when forward data in blockchain: {}".format(e)
        return None
