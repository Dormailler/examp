desc emp_copy;
select count(*) from emp_copy;
desc employees;
select * from emp_copy;
select count(*) from employees;

insert into emp_copy(name,id,salary,dept_id,hire_date) values ('홍길동',100,5000,10,'2023-03-28 00:00:00');
insert into emp_copy values ('홍사원',300,5000,10,'2023-03-28 00:00:00');
insert into emp_copy(id,hire_date) values (301,now());
insert into emp_copy values (null,302,null,null,now());
select * from emp_copy where id >= 300;

INSERT into emp_copy values 
('김부장',303,10000,50,'2023-03-28 00:00:00'),
('김차장',304,10000,50,'2023-03-28 00:00:00'),
('김이사',305,10000,50,'2023-03-28 00:00:00'),
('김신입',306,10000,50,'2023-03-28 00:00:00');
select * from emp_copy where id >= 300;


insert ignore into emp_copy values ('박부장',307,20000,80,'2023');
insert into emp_copy values ('최부장',308,20000,70,now());
select * from emp_copy where id >= 300;

-- oracle sequence / mysql auto_increment
create table product
(code int not null primary key auto_increment, name varchar(50) , price decimal(10,2));

desc product;

insert into product(name,price) values("멀티컴퓨터",100000),("캠프모니터",10000),("자바마우스",1000);
insert into product values(93,"멀티컴퓨터",100000);
insert into product(name,price) values("멀티컴퓨터",100000),("캠프모니터",10000),("자바마우스",1000);
select * from product;

-- update(emp_copy)

update emp_copy set id = 310 where name = '홍길동';
update emp_copy set salary = salary + 1000, dept_id = 100 where name= '홍길동';
select * from emp_copy;

-- 홍길동의 입사일을 jack의 입사일로 변경
update emp_copy 
set hire_date = (select * from (select hire_date from emp_copy where name ='jack') as t) 
where name= '홍길동';
select * from emp_copy;

-- 홍길동과 같은 부서원의 급여 1000 인상
update emp_copy 
set salary = salary+1000 
where dept_id = (select * from (select dept_id from emp_copy where name='홍길동')as a);
select * from emp_copy;

select @@autocommit;
set autocommit = false;

start transaction;
delete from emp_copy where id=307;
select * from emp_copy;
commit;
rollback;
-- char(10) 고정/ varchar(10) 최대10/ unicode 자바2바이트 , mysql 영문 1바이트 한글 3바이트 
-- oracle char(10) -> byte
-- 날짜 date,time,datetime

select length('mysql'),length('마이'),char_length('마이');

set @var1 = 5;
set @var2 = @var1+10;
select @var1, @var2;

set @var1 = 50;
select @var1, @var2;
select * from emp_copy where dept_id = @var1;

set @var1 = 1;
prepare myquery from 'select * from employees order by employee_id limit ?, 10 ' ;
execute myquery using @var1;

-- 자동형변환alter
select 100+200 sum;
select '100'+'200'; -- 문자가 숫자로만 이루어지면 정수 자동형변환 
select concat('100','200'); -- 문자열 덧셈
select concat(100,200); -- 문자열 덧셈
select 12 > '2222abc'; -- 문자가 숫자 변환,2222

select * from employees where department_id is null;

select first_name, ifnull(department_id, '부서미배정') from employees;

select  if(1>0 , "그렇다","아니다");
select nullif(100,100), nullif(100,200),  nullif(200,100);

select salary from employees order by 1;
select salary 급여, case
when salary >= 20000 then '임원'
when salary >= 19000 then '부장'
when salary >= 10000 then '과장'
when salary >= 5000 then '대리'
else '사원'end 직급 from employees;

select truncate(1234.5678,1);  -- 소수점 0자리 잘라냄(반올림x)

select salary,truncate(salary/5000,0) from employees;

select salary 급여, case truncate(salary/5000,0)
when 4  then '임원'
when 3  then '부장'
when 2  then '과장'
when 1  then '대리'
else '사원'end 직급 from employees;

select salary,salary*12 + salary*ifnull(commission_pct,0) 연봉 from employees;

select length('숫자'),char_length('숫자'),bit_length('숫자');

select name from emp_copy
where char_length(name) = 3;

select ('1'+'2'), concat('1','2'), concat_ws('-','1','2');

-- 문자찾기 함수
select elt(2,'일이','삼','넷'); -- 2번쨰 문자열 출력
select field('일이','일이','삼','넷'); -- 인덱스 번호찾기 
select find_in_set('일이','일이,삼,넷'); -- 한 문자열에서 문자열 번호찾기
select instr('일이 삼 넷','일이'); -- 한 문자열에서 문자열 번호찾기 	
select locate('이','일이삼넷'); -- 한 문자열에서 문자열 번호찾기
select substring('이것이 mysql이다.',5,5); -- 앞번호 index부터 뒤번호만큼 문자열 출력
select substring('이것이 mysql이다.',5); -- 끝까지

select first_name, hire_date from employees where hire_date like '2006%';

select first_name, substring(hire_date,1,4) from employees where hire_date like '2006%';

select first_name, hire_date from employees where substring(hire_date,1,4) = 2006;
select first_name, hire_date from employees where instr(hire_date,2006) = 1;
select first_name, hire_date from employees where year(hire_date) = 2006;

select first_name, hire_date from employees where substring(hire_date,6,2) = 06;
select first_name, hire_date from employees where instr(hire_date,'-06-') = 5;
select first_name, hire_date from employees where month(hire_date) = 06;
select instr(hire_date,06) from employees;

select truncate(1234.5678,0),round(1234.5678,0), format(1234.5678,0); -- 잘라내기 vs 반올림

select insert('abcde',2,3,'xxxxx'); -- 2번부터 3개 삭제하고 뒤에 문자열 추가
select repeat('*',8); 

set @pw = 'abc123가나다'; 
set @lpw =  char_length(@pw);
select insert (@pw,1,@lpw,repeat('*',@lpw));
select replace(@pw, @pw, repeat('*',@lpw));

select left(@pw,3),right(@pw,3),upper(@pw),lower(@pw);
select salary, lpad(salary,15,'-') ,rpad(salary,15,'-') from employees;

set @sns = "    재밌어요.웃겨요.    ";
select char_length(@sns), char_length(ltrim(@sns)), char_length(rtrim(@sns)),char_length(trim(@sns));
set @sns = "ㅋㅋㅋㅋ재밌어요.웃겨요.ㅋㅋㅋㅋ";
select @sns,  trim(leading 'ㅋ' from @sns), trim(trailing 'ㅋ' from @sns),trim(both 'ㅋ' from @sns);

select round(avg(salary),0) 반올림급여평균,truncate(avg(salary),0) 버림급여평균 from employees;
select employee_id 사번,
case mod(employee_id,2)
when 0  then "청팀"
else "백팀"
end 팀명 from employees;

-- 날짜시간함수 보통 now와 sysdate사용
select now(), sysdate(), current_date(), curdate(), current_time(), curtime(), current_timestamp();
-- date,time 추출
select now(),date(now()),time(now());
select now(),year(now()),month(now()),day(now());

select date_format(now(), '%Y:%m:%d %H:%i:%s'); -- y 연도 m 월 d 일 H 시 i 분 s 초
select date_format(now(), '%m');

select date_format('20230328123456' , '%Y:%m:%d %H:%i:%s');

select weekday(now()), dayofweek(now());
-- weekday 0~ (월요일~) dayofweek 1~ (일요일~)
 
 select now() 현재시작,
 case weekday(now())
 when 0 then '월요일'
 when 1 then '화요일'
 when 2 then '수요일'
 else '목금토일중 하나'
 end 요일;
 
 select curdate() 오늘날짜, adddate(curdate(),interval 1 day) 내일날짜, subdate(curdate(),interval 1 day) 어제날짜,
adddate(curdate(),interval 1 month) 한달후, adddate(curdate(),interval 1 year) 1년후 ;

select addtime(now(), '2:01:01');
select datediff('20230228',now());

select timediff(time(now()), '020101');
select period_diff('202303','202203');

select date_format(now(),"%Y%m");
select date_format(hire_date ,"%Y%m") from employees;
select period_diff(date_format(now(),"%Y%m"),date_format(hire_date ,"%Y%m")) from employees;
select hire_date, datediff(now(),hire_date) 입사경과일수,truncate(datediff(now(),hire_date)/7,0) 입사경과주수,
truncate(datediff(now(),hire_date)/365,0) 입사경과년수,
period_diff(date_format(now(),"%Y%m"),date_format(hire_date ,"%Y%m")) 입사경과월수 from employees;

select cast(123.5678 as signed integer), convert(123.5678 , signed integer), format(123.5678, 1);
-- json 항목 갯수 짝수가 되야함 (키-값)
select json_object(id,ifnull(name,'없음'),ifnull(salary,0), hire_date) from emp_copy;
select json_object("ID",id,"NAME",name,"SALARY",salary,"HIRE_DATE",hire_date) from emp_copy;
show variables like 'lower_case_table_names'; -- 대소문자 구분 여부 1구분x
select json_object(id,ifnull(name,'미정'),ifnull(salary,0),hire_date),
json_object(id, ifnull(name,'미정'), ifnull(salary,0),hire_date) from emp_copy;

desc employees;
desc departments;

select first_name, salary, e.department_id, department_name
from employees e /*inner*/ join departments d
on e.department_id = d.department_id;

-- 부서코드,부서이름, 부서장사번, 부서장이름
select d.department_id 부서코드 ,department_name 부서이름 , d.manager_id 부서장사번 , first_name 부서장이름
from employees e /*inner*/ join departments d
on d.manager_id = e.employee_id;

select * from departmentt;

desc locations;

select department_name, d.location_id, l.location_id,city
from departments d join locations l
on d.location_id = l.location_id;

select * from employees where department_id is null;