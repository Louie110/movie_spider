# _*_ coding: utf-8 _*_

#import related library
import requests
from bs4 import BeautifulSoup

#get the content of url
def get_content(url):
    try:
        html = requests.get(url)
    except Exception:
        print('url 请求失败')
    else:
        return html.content

#parse page,extract the links
def get_link(content):
    soup = BeautifulSoup(content,'html.parser')
    try:
        result = soup.find_all('div',class_ = 'item')
    except:
        print('解析页面错误，请检查')
    else:
        pass
    link_list = []
    for link in result:
        bref = link.find('a').get('href')
        link_list.append(bref)
    return link_list

#extract the field which we need 
def get_info(urls):
    info_list = []
    for url in urls:
        info_dic = {}
        req = requests.get(url)
        soup = BeautifulSoup(req.content,'html.parser')
        info_dic['name'] = soup.find('h1').text.strip().split(' ')[0]
        info_dic['director'] = soup.find('span',class_ = 'attrs').text
        type_list = soup.find_all('span',property = 'v:genre')
        ts = []
        for types in type_list:
            ts.append(types.text)
        info_dic ['movie_type'] = ts
        info_dic['run_time'] = soup.find('span',property = 'v:runtime').text
        info_dic['meta_score'] = soup.find('strong',class_ = 'll rating_num').text
        info_dic['vote_count'] = soup.find('span',property = 'v:votes').text
        if '\n' in info_dic['name']:
            info_dic['name'].replace('\n','')
        else:
            pass
        info_list.append(info_dic)
    print(info_list)

#main faction
def main():
    url = 'https://movie.douban.com/top250'
    result =  get_content(url)
    urls = get_link(result)
    get_info(urls)

if __name__ == '__main__':
    main()