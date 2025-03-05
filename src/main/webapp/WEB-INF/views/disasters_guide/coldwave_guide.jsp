<%@ page contentType="text/html;charset=UTF-8" language="java" %>

<%@ include file="../../template/header.jsp" %>
<html>
<head>
    <title>자연재난 행동요령</title>
    <link rel="stylesheet" type="text/css" href="/assets/css/disasters_guide.css">
    <link rel="stylesheet" type="text/css" href="/assets/css/bootstrap.min.css">
</head>
<style>
    #sidebar{
        height: 374.6%;!important;
    }
</style>
<body>
<div >
    <!-- 여기에 본문 내용이 들어갑니다 -->
        <div id="sidebar">
            <ul>
                <li><a href="/disasterguide/finedust">미세먼지</a></li>
                <li><a href="/disasterguide/typhoon">태풍</a></li>
                <li><a href="/disasterguide/heatwave">폭염</a></li>
                <li><a href="/disasterguide/heavyrain">호우</a></li>
                <li><a href="/disasterguide/flood">홍수</a></li>
                <li><a href="/disasterguide/coldwave">한파</a></li>
                <li><a href="/disasterguide/snowstorm">대설</a></li>
            </ul>
        </div>
        <!-- 컨텐츠 영역 -->
        <div class="content4">
            <div class="card-section">
                <img class="card-img" src="https://www.junggu.seoul.kr/safety/img/card/card8_1.jpg">
                <img class="card-img" src="https://www.junggu.seoul.kr/safety/img/card/card8_2.jpg">
                <img class="card-img" src="https://www.junggu.seoul.kr/safety/img/card/card8_3.jpg">
                <img class="card-img" src="https://www.junggu.seoul.kr/safety/img/card/card8_4.jpg">
            </div>
        </div>

</div>
</body>
</html>
<%@ include file="../../template/footer.jsp" %>