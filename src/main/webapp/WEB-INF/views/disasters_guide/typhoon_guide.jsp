<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>자연재난 행동요령</title>
    <link rel="stylesheet" type="text/css" href="/assets/css/disasters_guide.css">
    <link rel="stylesheet" type="text/css" href="/assets/css/bootstrap.min.css">
    <style>
        #sidebar{
            height: 468.3%!important;
        }
    </style>
</head>
<body>
<div class="container">
    <!-- header-->
    <jsp:include page="/WEB-INF/views/template/header.jsp"></jsp:include>
    <!--// header-------------------------------------------------->
</div>
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
                <img class="card-img" src="https://www.junggu.seoul.kr/safety/img/card/card4_1.jpg">
                <img class="card-img" src="https://www.junggu.seoul.kr/safety/img/card/card4_2.jpg">
                <img class="card-img" src="https://www.junggu.seoul.kr/safety/img/card/card4_3.jpg">
                <img class="card-img" src="https://www.junggu.seoul.kr/safety/img/card/card4_4.jpg">
                <img class="card-img" src="https://www.junggu.seoul.kr/safety/img/card/card4_5.jpg">
            </div>
        </div>

</div>

 <div class="container">
      <!-- footer-->
      <jsp:include page="/WEB-INF/views/template/footer.jsp"></jsp:include>
      <!--// footer-------------------------------------------------->
    </div>
</body>
</html>
