# !/usr/bin/env python
# coding=utf-8
# V1:Phantom,2015-11-26,C段信息收集工具，使用CENSYS的API接口，允许输入ip，进而查询C段信息
# V2：Phantom，2015-11-27，修改了输入方式，对无效的查询的输出进行修改
# V3:BlackWolf,2015-11-27,数据处理修改了输出数据的格式，细节微调，生成result.txt

import sys
import json
import requests
import re
#import ipaddress

URL_parameter = 'ipv4'

Data_parameter = 'netscreen sshd'  #参数输入
API_URL = "https://www.censys.io/api/v1"
UID = "2b5fb29e-7f37-4b05-a774-623750a985c8"
SECRET = "HSvoALc92fALeNSkBupaYjby7490vszD"

#result_view = ''  #查看单个详细结果
#res_view = requests.get(API_URL + "/view/"+URL_parameter+"/"+Data_parameter, auth=(UID, SECRET))

#Data_parameter = Data_parameter+'/24'  #C段
'''
payload示例：
           query：查询输入
           page：返回页面
           fields：返回的参数，可以对照网站上的参数列表进行设置
'''
page=range(118,822,1)
for pageid in page:
  try:
    payload = {"query": "125.69.85.19/24",
               "page": pageid,
               "fields": ["ip"]
    }
    
    payload["query"] = Data_parameter
    res_search = requests.post(API_URL + "/search/"+URL_parameter, data=json.dumps(payload), auth=(UID, SECRET))
    
    if res_search.json()["results"] == []:
        print 'the result is null'
        g = open('result.txt', 'a')
        g.writelines('the result is null')
    else:
        print res_search._content
        g = open('result.txt', 'a')
        json.dump(res_search.json(), g, indent=1)
    g.close()
  except:
    f2=open('error.txt','a')
    pageresult=str(pageid)
    f2.write(pageresult+'\n'+'error')
    f2.close()

  




