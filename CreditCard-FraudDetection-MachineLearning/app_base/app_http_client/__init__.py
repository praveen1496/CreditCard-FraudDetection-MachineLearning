# coding:utf8
import requests
from traceback import format_exc

from app_base.utils import json_dumps_util, json_loads_utf8_util


def http_client(url, params, time_out=30, method='post', result_type='json', headers=None, protocol='http'):
    result = ''
    try:
        if not url.startswith('%s://' % protocol):
            url = '%s://%s' % (protocol, url)
        if method.lower() == 'post':
            r = requests.post(url, params, timeout=time_out, headers=headers)
        else:
            r = requests.get(url, params=params, timeout=time_out, headers=headers)
        result = r.text
        if result_type.lower() == 'json':
            result = json_loads_utf8_util(r.text)
    except Exception as e:
        print 'http client error:', e
        print 'http client error:', format_exc()
    finally:
        return result


def http_client_json(url, params, time_out=30, result_type='json', headers=None, protocol='http'):
    result = ''
    try:
        if not url.startswith('%s://' % protocol):
            url = '%s://%s' % (protocol, url)
        r = requests.post(url, json_dumps_util(params), timeout=time_out, headers=headers)
        result = r.text
        if result_type.lower() == 'json':
            result = json_loads_utf8_util(r.text)
    except Exception as e:
        print 'http client error:', e
        print 'http client error:', format_exc()
    finally:
        return result


if __name__ == '__main__':
    http_client('127.0.0.1:9000', {})
