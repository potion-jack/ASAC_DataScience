use test_join;

select * from members; -- 영화 빌려간 사람들에 대한 정보
select * from movies;  -- 영화 관련 테이블
# id 는 각기 테이블에서 pk를 하지만 역할은 다름

# cross join
select * from movies cross join members;
select * from members cross join movies;
select * from members,movies;

# inner join : 빌려간 대여자 정보와 영화 정보를 같이 보기
select first_name, last_name, title 
from members as ME 
inner join movies as M
on ME.movie_id = M.id;

select ME.first_name, ME.last_name, M.title 
from members as ME 
inner join movies as M
on ME.movie_id = M.id;

select ME.first_name, ME.last_name, M.title 
	from movies as M
	inner join members as ME
	on ME.movie_id = M.id;

select * from movies M inner join members ME
	on M.id = ME.movie_id;
    
# left, right join
select * from movies M left join members ME
	on M.id = ME.movie_id
;


select * from movies M right join members ME
	on M.id = ME.movie_id
;

use sqldb;
select * from usertbl;
select * from buytbl;

# 구매이력이 있고, 회원 정보도 있는 테이블을 구성하자
select * from buytbl inner join usertbl
		on buytbl.userid = usertbl.userid
        order by buytbl.userid;

select usertbl.userid,usertbl.name,prodname,concat(mobile1,"-",mobile2) 
		from buytbl 
        inner join usertbl
		on buytbl.userid = usertbl.userid
        order by buytbl.userid;


### 
USE sqldb;
CREATE TABLE stdtbl 
( stdName    VARCHAR(10) NOT NULL PRIMARY KEY,
  addr	  CHAR(4) NOT NULL
);
CREATE TABLE clubtbl 
( clubName    VARCHAR(10) NOT NULL PRIMARY KEY,
  roomNo    CHAR(4) NOT NULL
);
CREATE TABLE stdclubtbl
(  num int AUTO_INCREMENT NOT NULL PRIMARY KEY, 
   stdName    VARCHAR(10) NOT NULL,
   clubName    VARCHAR(10) NOT NULL,
FOREIGN KEY(stdName) REFERENCES stdtbl(stdName),
FOREIGN KEY(clubName) REFERENCES clubtbl(clubName)
);
INSERT INTO stdtbl VALUES ('김범수','경남'), ('성시경','서울'), ('조용필','경기'), ('은지원','경북'),('바비킴','서울');
INSERT INTO clubtbl VALUES ('수영','101호'), ('바둑','102호'), ('축구','103호'), ('봉사','104호');
INSERT INTO stdclubtbl VALUES (NULL, '김범수','바둑'), (NULL,'김범수','축구'), (NULL,'조용필','축구'), (NULL,'은지원','축구'), (NULL,'은지원','봉사'), (NULL,'바비킴','봉사');

-- 3개의 테이블 join
select s.stdname, s.addr, sc.clubname, c.roomno 
	from stdtbl as s
		inner join stdclubtbl as sc on s.stdname = sc.stdname
        left join clubtbl as c on sc.clubname = c.clubname
	order by c.roomno;
		
select u.userid, u.name, b.prodname
	from usertbl u left outer join buytbl b
		on u.userid = b.userid;
        
select u.userid, u.name, b.prodname
	from usertbl as u 
		left outer join buytbl as b
		on u.userid = b.userid
	where b.prodname is null;
    
select s.stdname, s.addr, sc.clubname, c.roomno 
	from stdtbl as s
		left outer join stdclubtbl as sc on s.stdname = sc.stdname
        left join clubtbl as c on sc.clubname = c.clubname
	order by c.roomno;

select sc.clubname, s.stdname, s.addr, c.roomno 
	from stdtbl as s
		inner join stdclubtbl as sc on s.stdname = sc.stdname
        left join clubtbl as c on sc.clubname = c.clubname
	order by sc.clubname desc;

select sc.clubname, c.roomno, s.stdname, s.addr
	from clubtbl as c
		left outer join stdclubtbl as sc 
			on c.clubname = sc.clubname
        right outer join stdtbl as s 
			on s.stdname= sc.stdname
	order by sc.clubname desc;
    
select c.clubname,c.roomno,s.stdname,s.addr
	from stdtbl s 
		left outer join stdclubtbl sc
			on s.stdname = sc.stdname
		right outer join clubtbl c
		on sc.clubname = c.clubname
        ;

select s.stdname, s.addr ,c.clubname, c.roomno
	from stdtbl s 
		left outer join stdclubtbl sc
			on s.stdname = sc.stdname
		right outer join clubtbl c
			on sc.clubname = c.clubname
        ;
        
