<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<html>
<head>
    <title>과거지진</title>
    <link rel="stylesheet" href="styles.css"> <!-- 스타일시트 추가 (선택적) -->
</head>
<body>
<div class="historyTab">
    <ul>
        <li class="on"><a href="/info/history/earthquake">지진</a></li>
        <li><a href="/info/history/typhoon">태풍</a></li>
    </ul>
</div>
<div class="earthquakeList">
    <div class="leftArea">
        <div class="titArea">
            <strong>지진 발생 목록</strong>
            <link rel="stylesheet" type="text/css" href="/assets/css/eqk.css">
            <div class="selectArea">
                <select class="selectTypeA" style="width:170px;" name="year" id="year" onchange="changeYear()">
                    <option value="">선택</option>
                    <option value="2025" ${searchWord == '2025' ? 'selected' : ''}>2025</option>
                    <option value="2024" ${searchWord == '2024' ? 'selected' : ''}>2024</option>
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
        </div>
        <div class="mapArea" id="tmpMapArea">
            <!-- 여기서 지진 발생지도를 표시할 수 있습니다. -->
        </div>
    </div>

    <div class="rightArea">
        <div class="topArea">
            <ul id="sortList">
                <li class="on"><a href="javascript:;" id="listDate">최신순</a></li>
                <li><a href="javascript:;" id="listMng">규모순</a></li>
            </ul>
        </div>
        <div class="tableArea">
            <div class="titArea">
                <div class="tableSet">
                    <span>발생시각</span>
                    <span>규모</span>
                    <span>위/경도</span>
                    <span>위치</span>
                </div>
            </div>
            <ul class="tableList scr1" id="getEarthquakeList">
                <c:forEach var="earthquake" items="${list}">
                    <li>
                        <span>${earthquake.eqkReportTime}</span>
                        <span>${earthquake.eqkMt}</span>
                        <span>${earthquake.eqkLat}, ${earthquake.eqkLon}</span>
                        <span>${earthquake.eqkLoc}</span>
                    </li>
                </c:forEach>
            </ul>
        </div>
    </div>
</div>

<script>
    // 연도 선택 시 해당 연도에 맞는 데이터 조회
    function changeYear() {
        const year = document.getElementById('year').value;
        if (year) {
            // 여기에 선택된 연도에 맞는 지진 데이터를 서버에서 가져오는 로직을 작성할 수 있습니다.
            window.location.href = '/earthquake/view?searchWord=' + year;
        }
    }
</script>
</body>
</html>
