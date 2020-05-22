def blogsMardViewed(articleId,ip,port):
    url = "https://count.cnblogs.com/blog/post/"+articleId
    parsed = urlparse(url)
    header1["Referer"]="https://www.cnblogs.com/hekbobo/articles/%s.html" % (articleId)
    header1["Origin"]=parsed.hostname
    header1["User-Agent"] =useragent[random.randint(0,len(useragent))]
    r = requests.put(url, proxies=proxies, timeout = 5,headers=header1)        
    print(r.url)
    print(r.reason)
    
    
 #blog("12909012","58.61.154.153",8080)
