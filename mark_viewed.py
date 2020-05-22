# -*- coding: utf-8 -*-
import sys
import requests
import webbrowser
import random

import time
from urllib.parse import urlparse

proxies={
    'http':'http://'+proxy,
    'https':'https://'+proxy,
}

header1 = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
  "Referer":"https://www.cnblogs.com/xuanyuan/p/12935503.html","Origin":"https://www.cnblogs.com/","Connection":"close"} 

useragent = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
        "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.94",
         "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36",
          "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1",
          "Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M032 Build/IML74K) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/4.1 Mobile Safari/533.1",
          "MQQBrowser/38 (iOS 4; U; CPU like Mac OS X; zh-cn)",
          "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/14.14263"
]

def blogsMardViewed(url,ip,port):
    parsed = urlparse(url)
    beginIndex = url.find('articles')
    endIndex = url.find('.html')
    if beginIndex != -1 :
        articleId = url[beginIndex+9:endIndex]
    else:
        print("地址有错")
        return
    
    countUrl = "https://count.cnblogs.com/blog/post/"+articleId
    header1["Referer"]=url
    header1["Origin"]=parsed.hostname
    header1["User-Agent"] =useragent[random.randint(0,len(useragent) -1 )]
    try:
        if len(ip)== 0:            
            r = requests.put(countUrl, proxies=proxies, timeout = 5,headers=header1)        
        else:
            proxies['https'] ='https://%s:%s' %(ip, str(port))
            proxies['http'] = 'http://%s:%s' % (ip , str(port))
            r = requests.put(countUrl, proxies=proxies, timeout = 5,headers=header1)        
        print(r.url)
        print(r.reason)
    except Exception as identifier:
        print(str(identifier))
    
#blogsMark_viewed("https://www.cnblogs.com/xuanyuan/p/12935503.html","58.61.154.153",8080)
