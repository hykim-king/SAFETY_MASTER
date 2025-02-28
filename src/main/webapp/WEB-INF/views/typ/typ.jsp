<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions" %>

<html>
<head>
  <title>태풍</title>
  <link rel="stylesheet" type="text/css" href="/assets/css/typ.css">
</head>
<body>
<div class="historyTab">
  <ul>
    <li class="active"><a href="/disastermessage/view"><strong>재난문자</strong></a></li>
    <li class="active"><a href="/earthquake/view">지진</a></li>
    <li class="on"><a href="/typ/view">태풍</a></li>
    <li class="active"><a href="/disasterguide/natural">자연재난 행동요령</a></li>
    <li class="active"><a href="/disasterguide/social">사회재난 행동요령</a></li>
  </ul>
</div>

<div class="earthquakeList">
  <div class="leftArea" style="margin-top: 45px">
    <div class="selectArea">
      <select class="selectTypeA" style="width:170px;" name="year" id="year" onchange="changeYear()">
        <option value="">선택</option>
        <option value="2023" ${searchWord == '2023' ? 'selected' : ''}>2023</option>
        <option value="2022" ${searchWord == '2022' ? 'selected' : ''}>2022</option>
        <option value="2021" ${searchWord == '2021' ? 'selected' : ''}>2021</option>
        <option value="2020" ${searchWord == '2020' ? 'selected' : ''}>2020</option>
        <option value="2019" ${searchWord == '2019' ? 'selected' : ''}>2019</option>
        <option value="2018" ${searchWord == '2018' ? 'selected' : ''}>2018</option>
        <option value="2017" ${searchWord == '2017' ? 'selected' : ''}>2017</option>
        <option value="2016" ${searchWord == '2016' ? 'selected' : ''}>2016</option>
      </select>
    </div>
    <div class="tableArea" style="margin-top: 30px;">
      <!-- 차트가 그려질 캔버스 -->
      <canvas id="typhoonChart" width="400" height="400"></canvas>
    </div>
  </div>

  <div class="rightArea">
    <div class="topArea">
      <ul>
        <li><a id="all" href="#" onclick="changeSelection('10')">전체</a></li>
        <li><a id="landing" href="#" onclick="changeSelection('20')">상륙</a></li>
        <li><a id="directly" href="#" onclick="changeSelection('30')">직접</a></li>
      </ul>
    </div>
    <div class="tableArea">
      <div class="titArea">
        <div class="tableSet">
          <span>태풍명</span>
          <span>시작일시</span>
          <span>종료일시</span>
          <span>한반도 영향</span>
          <span>지속시간</span> <!-- Add a new column for duration -->
        </div>
      </div>
      <ul class="tableList scr1">
        <c:if test="${empty typ}">
          <div class="noneData">데이터가 없습니다</div>
        </c:if>
        <!-- 태풍 정보 출력 -->
        <c:forEach var="typ" items="${typ}">
          <li onclick="displayTyphoonData('${typ.typKorName}', '${typ.typSt}', '${typ.typEd}', ${typ.typMinPressure}, ${typ.typMaxWind})">
            <span>${typ.typKorName}</span>
            <span>${typ.typSt}</span>
            <span>${typ.typEd}</span>
            <span>${typ.typEff}</span>
            <span>${fn:substring(typ.typSt, 0, 10)} - ${fn:substring(typ.typEd, 0, 10)}</span>
          </li>
        </c:forEach>
      </ul>
    </div>
  </div>
</div>

<script src="/assets/js/typ/typ_page.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>

  const ctx = document.getElementById('typhoonChart').getContext('2d');


  let typhoonChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: [],
      datasets: [
        {
          label: '최소 기압 (kPa)',
          data: [],
          backgroundColor: 'rgba(75, 192, 192, 0.2)',
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1
        },
        {
          label: '최대 풍속 (m/s)',
          data: [],
          backgroundColor: 'rgba(255, 99, 132, 0.2)',
          borderColor: 'rgba(255, 99, 132, 1)',
          borderWidth: 1
        },
        {
          label: '태풍 존재일 (일)',
          data: [],
          backgroundColor: 'rgba(153, 102, 255, 0.2)',
          borderColor: 'rgba(153, 102, 255, 1)',
          borderWidth: 1
        }
      ]
    },
    options: {
      responsive: true,
      scales: {
        x: {
          title: {
            display: true,
            text: '시작일시 - 종료일시'
          }
        },
        y: {
          title: {
            display: true,
            text: '단위 (kPa / m/s / 일)'
          },
          beginAtZero: true, // Y축이 0부터 시작하게 설정
          min: 0, // Y축의 최소 값
          max: 120 // Y축의 최대 값
        }
      }
    }
  });

  function displayTyphoonData(name, startDate, endDate, minPressure, maxWind) {

    const days = endDate - startDate;


    const labels = [`${startDate} - ${endDate}`];
    const minPressureData = [minPressure / 10];
    const maxWindData = [maxWind];
    const durationData = [days];


    typhoonChart.data.labels = labels;
    typhoonChart.data.datasets[0].data = minPressureData ;
    typhoonChart.data.datasets[1].data = maxWindData;
    typhoonChart.data.datasets[2].data = durationData;


    typhoonChart.update();
  }
</script>






</body>
</html>
