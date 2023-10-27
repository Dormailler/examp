/* 주석1 */
#주석2
-- 주석3
select * from countries;
desc countries;
select country_name from countries;
select employee_id '사번' , first_name 성, last_name 이름, salary 급여 ,job_id 직종 from employees;
select salary*12 연봉 from employees;
desc employees;
select * from employees;
select employee_id 사번 , salary 급여 , first_name 성 , last_name 이름 from employees where salary between 10000 and 15000;
select employee_id 사번 , salary 급여 , first_name 성 , last_name 이름 from employees where employee_id in(100,200,300);
select first_name from employees where first_name like 'p%_';
select first_name, last_name from employees where last_name like '%ng';
select first_name, last_name from employees where last_name like '%er%';
select first_name, hire_date from employees;
select now();  -- from dual
select first_name, hire_date 
from employees 
where hire_date between '2006-01-01 00:00:00' and '2006-12-31 23:59:59';
select first_name, hire_date 
from employees 
where hire_date like '%-06-%';

select first_name, commission_pct from employees
where commission_pct is not null;

select job_id from employees;
select distinct job_id from employees;

-- 오라클 '||' MYSQL CONCAT
select concat("성은", last_name, "이고 이름은", first_name," 입니다.")
from employees;

select employee_id from employees order by employee_id desc;
select employee_id 사번 from employees order by 1;
select employee_id 사번 from employees order by 사번;

select first_name,salary from employees order by 2,first_name;

select first_name,commission_pct from employees
-- where commission_pct is not null 
order by 2 desc;

select * from employees order by employee_id limit 1,10; -- 인덱스1부터 10개

set @var1 = 1;
set @var2 = (@var1-1)*10;
select @var1,@var2;
select * from employees where employee_id = @var1;
 
 create table emp_copy
 (select first_name name , employee_id id, salary, department_id dept_id, hire_date from employees where salary >= 5000);
 
 select * from emp_copy;
 
set @var1 = 1; -- 변수 연결 정의
PREPARE myQuery
FROM 'select * from employees order by employee_id limit ?, 10';-- sql 정의 
EXECUTE myQuery USING @var1; -- 실행

select max(salary) from employees;
select max(salary) from employees where salary < 10000;

select max(salary),min(salary),sum(salary),avg(salary),count(salary) from employees;
select max(first_name),min(first_name),sum(first_name) from employees;
select max(hire_date) 최근입사일 ,min(hire_date) 최초입사일 ,sum(hire_date) from employees;
select count(department_id),count(commission_pct),count(*) from employees;
select * from employees where department_id is null;
select count(*) 총사원수, employee_id 사번 from employees; -- 레코드 개수가 달라서 실행불가
select sum(salary) from employees where department_id = 50;

select department_id 부서코드,sum(salary) 부서별총합 from employees
where department_id is not null
group by department_id
order by 2 desc ;

select department_id 부서코드,job_id 직종코드, sum(salary) 부서직종별총합 from employees
where department_id is not null
group by department_id,job_id
order by 3 desc ;

select department_id 부서코드, sum(salary) 부서직종별총합 from employees
where department_id is not null
group by department_id,job_id
having sum(salary) >= 50000
order by 2 desc ;

-- --과제-- -- 
select * from employees;

select first_name 이름 ,salary*12 연봉 from employees;
select first_name 이름 ,salary*12 연봉 from employees where department_id is null;
select first_name 이름 ,salary 급여, hire_date from employees 
where hire_date < '2004-01-01 00:00:00';
select department_id,department_name from departments;
select job_id,job_title from jobs;

select first_name, salary,department_id from employees
where department_id in (80,50) and salary >= 13000;

select first_name, salary,department_id,hire_date from employees
where hire_date > '2005-01-01 00:00:00' and salary between 1300 and 20000;

select first_name, salary,department_id,hire_date from employees
where hire_date like '2005%';
select first_name, salary,job_id from employees
where job_id like '%clerk%';

select first_name, salary,hire_date from employees
where hire_date like '%-12-%';	
select first_name, salary,hire_date from employees
where first_name like '%le%';	
select first_name, salary,hire_date from employees
where first_name like '%m';	
select last_name, salary,hire_date from employees
where last_name like '__d%';	
select last_name,commission_pct, salary from employees
where commission_pct is null;	
select * from employees
where commission_pct is not null and salary between 5000 and 17000
order by hire_date,salary;	
