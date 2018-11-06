# _*_ coding: utf-8 _*_

#import related library
import requests
import pymysql
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
    print('开始解析页面')
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
    return info_list

# add data to the database
def mysql_con(host,user,passwd,dbase,port,charset,info):
    print('开始连接数据库')
    db = pymysql.connect(
        host = host, 
        user = user,
        passwd = passwd,
        database = dbase,
        port = port,
        charset = charset)
    with db.cursor() as cursor:
        cursor.execute('drop table if exists Douban')
        sql = """create table Douban (
            name varchar(50),
            director varchar(50),
            origin varchar(50),
            run_time varchar(50),
            meta_score varchar(10),
            movie_type varchar(100),
            vote_count varchar(20)
        )default charset=utf8;"""
        cursor.execute(sql)
        for i in range(len(info)):
            sets = ''
            for value in range(len(info[i]['movie_type'])):
                sets += info[i]['movie_type'][value]
                if value !=  max(range(len(info[i]['movie_type']))):   
                    sets += '/'
                else:
                    pass
            print(sets)
            sqls = "INSERT INTO Douban (name,director,run_time,meta_score,movie_type,vote_count) VALUES (info[i]['name'],info[i]['director'],info[i]['run_time'],info[i]['meta_score'],sets,info[i]['vote_count']);"
            try:
                cursor.execute(sqls)
                db.commit()
                print('已将数据成功导入数据库')
            except Exception as e:
                print('错误详情内容:',e)       
            finally:
                cursor.close()
                db.close()
    print('连接成功')

# main function 
def main():
    url = 'https://movie.douban.com/top250'
    result =  get_content(url)
    print(result)
    urls = get_link(result)
    info = get_info(urls)
    mysql_con('localhost','root','643521','movies',3306,'utf8',info)
    
if __name__ == '__main__':
    main()