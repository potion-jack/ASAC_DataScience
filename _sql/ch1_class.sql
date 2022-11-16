select * from tcity;
select name, popu from tcity;

select * from tstaff;
select name, depart, grade from tstaff;

select * from tcity;
select name as "도시명",area as "면적(제곱km)",popu as "인구(만명)" from tcity;

select name as "도시명",popu*10000 as "인구(명)" from tcity;

select name as "이름",area as "면적",popu as "인구", popu*10000/area as "인구밀도" from tcity;

select name from tcity where area>1000;

select name, area from tcity where area > 1000;

select name from tcity where popu < 10;

select * from tcity where region like "전_";

select name from tstaff where salary > 400;

select * from tstaff where score is not null;

select * from tcity where popu > 100 and area > 700;

select * from tcity where region = '경기' and ;