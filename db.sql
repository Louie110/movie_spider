
-------douban中各字段含义----------
movie_name      电影名称
actor            演员
geners           电影类型
vote_count       投票数
rating_count     评分
----------------------------------

create table douban (
movie_name varchar(60),
actor varchar(10),
geners varchar(50),
rating_count int(10),
vote_count int(20)
) default charset=utf8;

---查看表结构
desc douban；




-------tencent中各字段含义----------
movie_name       电影名称
actor            演员
geners           电影类型
figure_count     播放次数
score            评分
----------------------------------

create table tencent (
movie_name varchar(60),
actor varchar(10),
score int(10),
figure_count int(20)
) default charset=utf8;

---查看表结构
desc tencent；


-------IMDB中各字段含义----------
imdb_name       电影名称
imdb_time       上映年份
imdb_type       电影类型
runtime         时长
meta_score      投票数
----------------------------------

create table IMDB (
imdb_name varchar(60),
imdb_time year(10),
imdb_type varchar(10),
runtime int(10),
meta_score int(10)
) default charset=utf8;