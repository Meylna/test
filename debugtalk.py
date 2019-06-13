from jsonschema import validate
from os import path
import json

def get_base_url(type):
    base_url = ""
    if type == 1:
        base_url = "http://dev.collectivedynamic.com"
    elif type == 2:
        base_url =  "http://dev.collectivedynamic.com:30010"
    elif type == 3:
        base_url = "http://admin-dev.collectivedynamic.com:30010"
    else:
        base_url = "http://passport-dev.collectivedynamic.com:30010"
    return base_url


def get_headers(type):
    headers = {}
    if type == 1:  # 1表示创建 APP的请求URL
      headers =  {
        'content-type': "application/json; charset=UTF-8",
        'metadata': "iOS Debug_in2_32_10.300000_3.2.0",
        'device-id': "2970AEBB-F2E0-45A1-B135-BB6FF400B6D2",
        'referer': "https://app.yingtu.co/",
        'appversion': "3.2.0",
        'user-id': "415675474554856856",
        'token': "74717458584859545",
        'connection': "Keep-Alive",
        'accept-encoding': "gzip",
        'user-agent': "okhttp/3.8.1",
        'host': "dev.collectivedynamic.com"
      }

    elif type == 2:  # 2表示创建 联盟后台的请求URL
      headers = {
            'Accept': "application/json, text/plain, */*",
            'Content-Type': "application/json",
            'Origin': "http://quntidongli.oss-cn-shanghai.aliyuncs.com",
            'Referer': "http://quntidongli.oss-cn-shanghai.aliyuncs.com/v2/test/index.html",
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
            'Host': "dev.collectivedynamic.com:30010",
            'accept-encoding': "gzip, deflate"
        }
    elif type == 3:
      headers = {
            'Accept': "application/json, text/plain, */*",
            'Content-Type': "application/json",
            'Origin': "http://admin.ingtube.com",
            'Referer': "http://admin.ingtube.com/v5/test/index.html",
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
            'Host': "admin-dev.collectivedynamic.com:30010",
        }

    elif type == 4:  # 小二后台、联盟后台登录
        headers = {
            'Accept': "application/json, text/plain, */*",
            'Content-Type': "application/json",
            'Origin': "http://admin.ingtube.com",
            'Referer': "http://admin.ingtube.com/v5/test/index.html",
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
            'Host': "passport-dev.collectivedynamic.com:30010",
         }
    return headers


def alter_validate_response(response,validate_path):
    d = path.dirname(__file__)
    data = json.loads(response.content)
   # print(data)
    validate_path = d+"/"+validate_path
    shema_data = {}
    with open(validate_path,'r') as load_f:
        shema_data = json.load(load_f)

    try:
      eq = validate(data,shema_data)
      response.status_code = 0
    except Exception:
        pass
