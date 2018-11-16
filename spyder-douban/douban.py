 # -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 14:58:08 2018

@author: win
"""

import basicSpider
from bs4 import BeautifulSoup

def get_html(url):
    """
    获取当前页面网页源码信息
    
    """
    headers=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5514.400 QQBrowser/10.1.1681.400')]
    proxy={"http":"182.129.243.84:9000"}
    
    html=basicSpider.downloadHtml(url,headers,proxy=proxy,)
    return html


def get_movie_all(html):
    """
    获取当前页面所有的电影列表信息
    
    """
    soup=BeautifulSoup(html,'html.parser')#
    movie_list=soup.find_all('div',class_='bd doulist-subject')#
    return movie_list
    
    
         
def get_movie_one(movie):
    """
    获取电影的详细信息
    
    """
    
    result=""
    soup=BeautifulSoup(str(movie),'html.parser')#
    
    title=soup.find_all('div',class_='title')

    soup_title=BeautifulSoup(str(title[0]),'html.parser')
    for line in soup_title.stripped_strings:

        result+=line
        
    try:
        score=soup.find_all('span',class_='rating_nums')
        score_=BeautifulSoup(str(score[0]),'html.parser')
        for line in score_.stripped_strings:
            result+="|| 评分:"
            result+=line+'\n' 
    except:
        result+="|| 评分:5.0分"
    
    abstract=soup.find_all('div',class_='abstract')
    abstract_info=BeautifulSoup(str(abstract[0]),'html.parser')
    for line in abstract_info.stripped_strings:
        result+="||"
        result+=line+'\n'
    print(result)    
    return result
  

    
def save_file(movieInfo):
    #写文件用的是追加的方式
    with open('doubanMovie.txt','a') as f:
        f.write(movieInfo)



if __name__=="__main__":
    url='https://www.douban.com/doulist/3516235/?start=225&sort=seq&sub_type='
    html=get_html(url)
    movie_list=get_movie_all(html)
    #将参数传进get_movie_one 
    for it in movie_list:
        save_file(get_movie_one(it))

        
   
    
    



#正则表达式 匹配电影名‘<div class="title">[\s\S]*?/>([\s\S]*?)</a>’


























































