# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 20:32:52 2018

@author: win
"""
import urllib
import logging
import random


logger=logging.getLogger('basicHmtlLogger')

#定制日志输出格式

formatter=logging.Formatter('%(asctime)s %(levelname)s %(message)s')

#创建日志：文件日志，终端日志

file_handler=logging.FileHandler('basicHmtlLogger.log')
file_handler.setFormatter(formatter)


#设置默认的日志级别
logger.setLevel(logging.ERROR)

#把文件日志和终端日志添加到日志处理器中
logger.addHandler(file_handler)


PROXY_RANGE=2
PROXY_RANGE_MIN=1
PROXY_RANGE_MAX=10

def downloadHtml(url,headers=[],proxy={},
                 num_retries=10,timeout=10,decodeInfo='utf-8'):
    
    """
    """
    #动态地使用服务器
    html=None
    if random.randint(1,10)>=1:
        logger.info('No Proxy')
        proxy=None
        
    proxy=urllib.request.ProxyHandler(proxy)
    
    opener=urllib.request.build_opener(proxy)

#把opener装载进urllib库中，准备使用
    opener.addheaders=headers
    urllib.request.install_opener(opener)
    try:
        response=urllib.request.urlopen(url)
        html=response.read().decode(decodeInfo)
    except UnicodeDecodeError:
        #1.会出现解码错误
        logger.error('UnicodeDecodeError')
    except urllib.error.URLError or urllib.error.HTTPError as e:
        logger.error('urllib error')
        if hasattr(e,'code') and 400<=e.code <500:
            logger.error('Client error')#客户端的问题，通过分析日志来分析
        elif hasattr(e,'code') and 500<=e.code <600:
            html=downloadHtml(url,headers,proxy,
                 num_retries-1,timeout,decodeInfo)
            if num_retries<0:
                return html
    except:
        logger.error('Downloaderror')
        
    return html
    


if __name__=="__main__":
    
    url='http://www.baidu.com'
    headers=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5514.400 QQBrowser/10.1.1681.400')]
    proxy={}
    num_retries=10
    timeout=10
    decodeInfo='utf-8'
    
    print(downloadHtml(url,headers,proxy={},
                 num_retries=10,timeout=10,decodeInfo='utf-8'))

#当不用日志时，记得要remove
    logger.removeHandler(file_handler)
    logger.removeHandler(consle_handler)


































