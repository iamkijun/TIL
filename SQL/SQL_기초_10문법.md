### 1. SELECT

SELECT 컬럼을 선택

- 컬럼 명을 선언하여 특정 컬럼만 볼 수 있음

FROM 테이블을 선택

LIMIT 나타내고자 하는 데이터 로우의 개수



### 2. ORDER BY

ORDER BY price

- price 순으로 오름차순해서 나타내기

ORDER BY price desc

- price 순으로 내림차순해서 나타내기

ORDER BY YEAR,MONTH,day

- 년,월,일 순으로 나타내기



### 3. COUNT

SELECT count(*)

- 행의 개수가 몇개인지 궁금할 때



### 4. GROUP BY

SELECT dong, count(*)

GROUP BY dong

- 동별로 아파트 매매건수를 보고 싶을 때



### 5. WHERE

WHERE dong='삼성동' or day=1

- 동이 삼성동이거나 1일인 데이터 조회

WHERE dong='삼성동' and day=1

- 동이 삼성동이면서 1일인 데이터 조회



### 6. CASE WHEN

그루핑을 할 때 많이 쓰인다.

```  mysql
SELECT price, YEAR, nm,
				case when price <= 10000 then '1억 이하'
						when price <= 30000 then '1억 ~ 3억이하'
						when price > 30000 then '3억 초과'
				end
FROM apt_list
```

```mysql
SELECT price, YEAR, nm,
				case when price <= 10000 then '1억 이하'
						when price <= 30000 then '1억 ~ 3억이하'
						ELSE '3억 초과'
				end
FROM apt_list
```

ELSE를 사용해도 됨



### 7. LIKE & NOT LIKE

``` mysql
SELECT *
FROM apt_list
WHERE nm LIKE '%자이%'
```

​	자이라는 단어가 포함된 데이터 조회

``` mysql
SELECT *
FROM apt_list
WHERE nm NOT LIKE '%자이%'
```

​	자이라는 단어가 포함되지 않은 데이터 조회

``` mysql
SELECT *
FROM apt_list
WHERE nm LIKE '%자이'
```

​	자이로 끝나는 데이터 조회



### 8. 서브쿼리

``` mysql
SELECT *
FROM (
	select dong, count(*) cnt
  from apt_list
  group by dong
)
where cnt>100
```

