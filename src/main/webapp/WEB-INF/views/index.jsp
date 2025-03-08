<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt"%>
<c:set var="CP" value="${pageContext.request.contextPath}" />

<!DOCTYPE html>
<html>

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1200">
<link href="/assets/css/bootstrap.min.css" rel="stylesheet">
<link href="/assets/css/header.css" rel="stylesheet">
<link href="/assets/css/index.css" rel="stylesheet">
<link rel="stylesheet"
	href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
<title>Insert title here</title>
<script src="/assets/js/jquery_3_7_1.js"></script>
</head>
<link rel="icon" href="data:;base64,iVBORw0KGgo=">

<body>

	<div id="container" class="container">
		<!-- header-->
		<jsp:include page="/WEB-INF/views/template/header.jsp"></jsp:include>
		<!--// header-------------------------------------------------->


		<!-- main-->
		<main>
			<main>
				<div class="mt-5 weather-dashboard">
					<!-- 상단 헤더 -->
					<div
						class="header d-flex justify-content-between align-items-center">
						<h2>
							오늘 날씨 <span id="date"></span>
						</h2>
						<div
							class="d-flex justify-content-end align-items-center gap-3 me-5">
							<h3>서울특별시</h3>
							<div class="dropdown mb-1">
								<button class="btn btn-dark dropdown-toggle text-dark"
									type="button" id="dropdownMenuButton1"
									data-bs-toggle="dropdown" aria-expanded="false">${wc.gu_Nm}</button>
								<ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
									<li><a class="dropdown-item" href="${CP}/index/111123">종로구</a></li>
									<li><a class="dropdown-item" href="${CP}/index/111121">중구</a></li>
									<li><a class="dropdown-item" href="${CP}/index/111131">용산구</a></li>
									<li><a class="dropdown-item" href="${CP}/index/111181">은평구</a></li>
									<li><a class="dropdown-item" href="${CP}/index/111191">서대문구</a></li>
									<li><a class="dropdown-item" href="${CP}/index/111201">마포구</a></li>
									<li><a class="dropdown-item" href="${CP}/index/111142">성동구</a></li>
									<li><a class="dropdown-item" href="${CP}/index/111141">광진구</a></li>
									<li><a class="dropdown-item" href="${CP}/index/111152">동대문구</a></li>
									<li><a class="dropdown-item" href="${CP}/index/111151">중랑구</a></li>
									<li><a class="dropdown-item" href="${CP}/index/111161">성북구</a></li>
									<li><a class="dropdown-item" href="${CP}/index/111291">강북구</a></li>
									<li><a class="dropdown-item" href="${CP}/index/111171">도봉구</a></li>
									<li><a class="dropdown-item" href="${CP}/index/111311">노원구</a></li>
									<li><a class="dropdown-item" href="${CP}/index/111301">양천구</a></li>
									<li><a class="dropdown-item" href="${CP}/index/111212">강서구</a></li>
									<li><a class="dropdown-item" href="${CP}/index/111221">구로구</a></li>
									<li><a class="dropdown-item" href="${CP}/index/111281">금천구</a></li>
									<li><a class="dropdown-item" href="${CP}/index/111231">영등포구</a></li>
									<li><a class="dropdown-item" href="${CP}/index/111241">동작구</a></li>
									<li><a class="dropdown-item" href="${CP}/index/111251">관악구</a></li>
									<li><a class="dropdown-item" href="${CP}/index/111262">서초구</a></li>
									<li><a class="dropdown-item" href="${CP}/index/111261">강남구</a></li>
									<li><a class="dropdown-item" href="${CP}/index/111273">송파구</a></li>
									<li><a class="dropdown-item" href="${CP}/index/111274">강동구</a></li>
								</ul>
							</div>
						</div>
					</div>

					<!-- 현재 날씨 & 대기질 -->
					<div class="row mt-3 justify-content-center">
						<!-- 현재 날씨 -->
						<div class="col-md-5">
							<div class="card p-4 text-end">
								<p class="text-start">발표일 : ${wc_Dt}</p>
								<img class="rounded mx-auto d-block"
									src="https://openweathermap.org/img/wn/${wc.weather_Icon_Id}@2x.png"
									height="130" width="130">
								<p class="text-center fs-4 fw-bolder">${wc.weather_Desc}</p>
								<div
									class="d-flex justify-content-center align-items-center gap-2">
									<h1 class="pe-2 display-4">${wc.temp}°</h1>
									<p class="fs-5 text-danger">${wc.max_Temp}°</p>
									<p class="fs-5">/</p>
									<p class="fs-5 text-primary">${wc.min_Temp}°</p>
								</div>
								<div
									class="d-flex justify-content-center align-items-center gap-2 mt-2">
									<small>체감 <span class="fw-bolder">${wc.feels_Like_Temp}°</span></small>
									<small>습도 <span class="fw-bolder">${wc.humidity}%</span>
									</small> <small>풍속 <span class="fw-bolder">${wc.wind_Speed}m/s</span></small>
								</div>
							</div>
						</div>
						<!-- 대기질 정보 -->
						<div class="col-md-6">
							<div class="card p-4">
								<p class="text-start mb-0">발표일 : ${aqc_Dt}</p>
								<div class="row text-center">
									<div class="col-6 mt-4">
										<p class="fw-lighter">통합대기환경지수</p>
										<c:choose>
											<c:when test='${aqc.cai_Grade.equals("좋음")}'>
												<div class="border border-primary border-5 rounded-pill">
													<p class="mb-0 mt-1 pt-2 text-primary fw-bolder">${aqc.cai_Grade}</p>
													<p class="fw-bolder">${aqc.cai}</p>
												</div>
											</c:when>
											<c:when test='${aqc.cai_Grade.equals("보통")}'>
												<div class="border border-success border-5 rounded-pill">
													<p class="mb-0 mt-1 pt-2 text-success fw-bolder">${aqc.cai_Grade}</p>
													<p class="fw-bolder">${aqc.cai}</p>
												</div>
											</c:when>
											<c:when test='${aqc.cai_Grade.equals("나쁨")}'>
												<div class="border border-warning border-5 rounded-pill">
													<p class="mb-0 mt-1 pt-2 text-warning fw-bolder">${aqc.cai_Grade}</p>
													<p class="fw-bolder">${aqc.cai}</p>
												</div>
											</c:when>
											<c:when test='${aqc.cai_Grade.equals("매우나쁨")}'>
												<div class="border border-danger border-5 rounded-pill">
													<p class="mb-0 mt-1 pt-2 text-danger fw-bolder">${aqc.cai_Grade}</p>
													<p class="fw-bolder">${aqc.cai}</p>
												</div>
											</c:when>
											<c:otherwise>
												<div class="border border-dark border-5 rounded-pill">
													<p class="mb-0 mt-1 pt-2 text-dark fw-bolder">측정</p>
													<p class="fw-bolder">불가</p>
												</div>
											</c:otherwise>
										</c:choose>


									</div>
									<div class="col-6 mt-4">
										<p class="fw-lighter">미세먼지</p>
										<c:choose>
											<c:when test="${0 <= aqc.pm10_Conc && aqc.pm10_Conc <= 30}">
												<div class="border border-primary border-5 rounded-pill">
													<p class="mb-0 pt-2 text-primary fw-bolder">좋음</p>
													<p class="fw-bolder">${aqc.pm10_Conc}</p>
												</div>
											</c:when>
											<c:when test="${30 < aqc.pm10_Conc && aqc.pm10_Conc <= 80}">
												<div class="border border-success border-5 rounded-pill">
													<p class="mb-0 pt-2 text-success fw-bolder">보통</p>
													<p class="fw-bolder">${aqc.pm10_Conc}</p>
												</div>
											</c:when>
											<c:when test="${80 < aqc.pm10_Conc && aqc.pm10_Conc <= 150}">
												<div class="border border-warning border-5 rounded-pill">
													<p class="mb-0 pt-2 text-warning fw-bolder">나쁨</p>
													<p class="fw-bolder">${aqc.pm10_Conc}</p>
												</div>
											</c:when>
											<c:when test="${aqc.pm10_Conc > 150}">
												<div class="border border-danger border-5 rounded-pill">
													<p class="mb-0 pt-2 text-danger fw-bolder">매우나쁨</p>
													<p class="fw-bolder">${aqc.pm10_Conc}</p>
												</div>
											</c:when>
											<c:otherwise>
												<div class="border border-dark border-5 rounded-pill">
													<p class="mb-0 pt-2 text-dark fw-bolder">측정</p>
													<p class="fw-bolder">불가</p>
												</div>
											</c:otherwise>
										</c:choose>
									</div>
									<div class="col-6 mt-4">
										<p class="fw-lighter">초미세먼지</p>
										<c:choose>
											<c:when test="${0 <= aqc.pm25_Conc && aqc.pm25_Conc <= 15}">
												<div class="border border-primary border-5 rounded-pill">
													<p class="mb-0 pt-2 text-primary fw-bolder">좋음</p>
													<p class="fw-bolder">${aqc.pm25_Conc}</p>
												</div>
											</c:when>
											<c:when test="${15 < aqc.pm25_Conc && aqc.pm25_Conc <= 35}">
												<div class="border border-success border-5 rounded-pill">
													<p class="mb-0 pt-2 text-success fw-bolder">보통</p>
													<p class="fw-bolder">${aqc.pm25_Conc}</p>
												</div>
											</c:when>
											<c:when test="${35 < aqc.pm25_Conc && aqc.pm25_Conc <= 75}">
												<div class="border border-warning border-5 rounded-pill">
													<p class="mb-0 pt-2 text-warning fw-bolder">나쁨</p>
													<p class="fw-bolder">${aqc.pm25_Conc}</p>
												</div>
											</c:when>
											<c:when test="${aqc.pm25_Conc > 75}">
												<div class="border border-danger border-5 rounded-pill">
													<p class="mb-0 pt-2 text-danger fw-bolder">매우나쁨</p>
													<p class="fw-bolder">${aqc.pm25_Conc}</p>
												</div>
											</c:when>
											<c:otherwise>
												<div class="border border-dark border-5 rounded-pill">
													<p class="mb-0 pt-2 text-dark fw-bolder">측정</p>
													<p class="fw-bolder">불가</p>
												</div>
											</c:otherwise>
										</c:choose>
									</div>
									<div class="col-6 mt-4">
										<p class="fw-lighter">오존</p>
										<c:choose>
											<c:when test="${0 <= aqc.o3_Conc && aqc.o3_Conc <= 0.030}">
												<div class="border border-primary border-5 rounded-pill">
													<p class="mb-0 pt-2 text-primary fw-bolder">좋음</p>
													<p class="fw-bolder">${aqc.o3_Conc}</p>
												</div>
											</c:when>
											<c:when test="${0.030 < aqc.o3_Conc && aqc.o3_Conc <= 0.090}">
												<div class="border border-success border-5 rounded-pill">
													<p class="mb-0 pt-2 text-success fw-bolder">보통</p>
													<p class="fw-bolder">${aqc.o3_Conc}</p>
												</div>
											</c:when>
											<c:when test="${0.090 < aqc.o3_Conc && aqc.o3_Conc <= 0.150}">
												<div class="border border-warning border-5 rounded-pill">
													<p class="mb-0 pt-2 text-warning fw-bolder">나쁨</p>
													<p class="fw-bolder">${aqc.o3_Conc}</p>
												</div>
											</c:when>
											<c:when test="${aqc.o3_Conc > 0.150}">
												<div class="border border-danger border-5 rounded-pill">
													<p class="mb-0 pt-2 text-danger fw-bolder">매우나쁨</p>
													<p class="fw-bolder">${aqc.o3_Conc}</p>
												</div>
											</c:when>
											<c:otherwise>
												<div class="border border-dark border-5 rounded-pill">
													<p class="mb-0 pt-2 text-dark fw-bolder">측정</p>
													<p class="fw-bolder">불가</p>
												</div>
											</c:otherwise>
										</c:choose>
									</div>
								</div>
							</div>
						</div>
					</div>

					<!-- 5일간의 날씨 예보 -->
					<h3 class="text-start forecast-title mt-4 ms-1">5일 예보</h3>
					<div class="row justify-content-center gap-4">
						<c:forEach var="wf" items="${wf_List}">
							<div class="col-md-2 forecast-card">
								<div class="card text-center p-3">
									<p class="mb-0">${wf.week}</p>
									<p class="mt-1 mb-1">${wf.fcst_Dt}</p>
									<img class="rounded mx-auto d-block"
										src="https://openweathermap.org/img/wn/${wf.weather_Icon_Id}@2x.png" height="70"
										width="70">
									<div class="d-flex justify-content-center mt-0 mb-0 gap-1">
										<p class="fs-5 text-danger">${wf.max_Temp}°</p>
										<p class="fs-5">/</p>
										<p class="fs-5 text-primary">${wf.min_Temp}°</p>
									</div>
								</div>
							</div>
						</c:forEach>
					</div>
				</div>
			</main>

		</main>
		<!--// main---------------------------------------------------->


		<!-- footer-->
		<jsp:include page="/WEB-INF/views/template/footer.jsp"></jsp:include>
		<!--// footer-------------------------------------------------->
	</div>


	<script>
		// 오늘 날짜 자동 업데이트

		let day = new Date().toLocaleDateString('ko-KR');

		let dayOfWeek = new Date(day).getDay();
		let dayList = [ '일', '월', '화', '수', '목', '금', '토' ];
		let label = dayList[dayOfWeek];

		document.getElementById("date").innerText = day + "(" + label + ")";
	</script>

</body>
</html>