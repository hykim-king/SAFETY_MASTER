# SAFETY_MASTER

----

## 테이블 설계

### 재난문자  
![재난문자.png](img%2F%EC%9E%AC%EB%82%9C%EB%AC%B8%EC%9E%90.png)

### 지진
![지진.png](img%2F%EC%A7%80%EC%A7%84.png)  

### 태풍  
![태풍.png](img%2F%ED%83%9C%ED%92%8D.png)  

## 알로리즘 추가 기능  
<mark>재난안전지수</mark>
- 재난빈도점수, 양수량, 기타요소에 가중치를 곱해 더하여 서울권 지역의 안전지수 정보를 제공한다.

### 지수 계산 방법
1. 각 항목에 대한 점수: 각 구별로 재난 빈도수, 날씨, 범죄율 등을 점수화 (예: 1~10점).  
2. 가중치 부여: 각 항목에 대한 가중치를 설정 중요한 항목일수록 높은 가중치 부여.
3. 안전지수 = (재난빈도점수 x 가중치) + (급수시설 x 가중치) + (기타요소점수 x 가중치)
4. <mark>최근 6개월 기준 서울 총 재난 건수 2908건 서울특별시 총 24개 구 평균121건   최다 : 중구-463 , 최소 : 은평구 - 60 </mark>


### 참고 테이블 

#### 급수시설 
![급수시설.png](img%2F%EA%B8%89%EC%88%98%EC%8B%9C%EC%84%A4.png)
 
#### 재난문자  
![재난문자.png](img%2F%EC%9E%AC%EB%82%9C%EB%AC%B8%EC%9E%90.png)  

```sql
<select id="safetyIndex">
    SELECT COUNT(*)*1000 AS totalCnt
    FROM DISASTER_MESSAGE
    WHERE DIS_MES_AREA LIKE '%' || #{searchWord} || '%'
      AND TO_TIMESTAMP(DIS_MES_DT, 'YYYY/MM/DD HH24:MI:SS.FF') >= SYSTIMESTAMP - INTERVAL '99' DAY - INTERVAL '99' DAY - INTERVAL '99' DAY - INTERVAL '68' DAY
</select>

<select id="safetyIndex_EWSF">
    SELECT PUMP_TON_
    FROM EWSF
    WHERE SGG LIKE '%' || #{searchWord} || '%'
</select>

<select id="item_count">
    SELECT
    COUNT(CASE WHEN DIS_MES_TYPE LIKE '%' || '먼지' || '%' THEN 1 END) AS dust_count,
    COUNT(CASE WHEN DIS_MES_TYPE LIKE '%' || '폭염' || '%' THEN 1 END) AS heat_wave_count,
    COUNT(CASE WHEN DIS_MES_TYPE LIKE '%' || '호우' || '%' THEN 1 END) AS heavy_rain_count,
    COUNT(CASE WHEN DIS_MES_TYPE LIKE '%' || '한파' || '%' THEN 1 END) AS cold_wave_count,
    COUNT(CASE WHEN DIS_MES_TYPE LIKE '%' || '대설' || '%' THEN 1 END) AS heavy_snow_count,
    COUNT(CASE WHEN DIS_MES_TYPE LIKE '%' || '산불' || '%' THEN 1 END) AS wildfire_count,
    COUNT(CASE WHEN DIS_MES_TYPE LIKE '%' || '풍랑' || '%' THEN 1 END) AS storm_count,
    COUNT(CASE WHEN DIS_MES_TYPE LIKE '%' || '전염병' || '%' THEN 1 END) AS epidemic_count,
    COUNT(CASE WHEN DIS_MES_TYPE LIKE '%' || '산사태' || '%' THEN 1 END) AS landslide_count
    FROM DISASTER_MESSAGE
    WHERE DIS_MES_AREA LIKE '%' || #{searchWord} || '%'
    AND TO_TIMESTAMP(DIS_MES_DT, 'YYYY/MM/DD HH24:MI:SS.FF') >= SYSTIMESTAMP - INTERVAL '99' DAY - INTERVAL '99' DAY - INTERVAL '99' DAY - INTERVAL '68' DAY
</select>
```
