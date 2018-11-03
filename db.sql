


-------movie中各字段含义----------
name           电影名称
director       导演
origin         所属网站
movie_type     电影类型
runtime         时长
meta_score      评分
movie_type      电影类型
vote_count      投票数
----------------------------------

create table movie (
name varchar(50),
director varchar(50),
origin varchar(20),
runtime int(10),
meta_score int(10),
movie_type varchar(10),
vote_count int(10)
) default charset=utf8;