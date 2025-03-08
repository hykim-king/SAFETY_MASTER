<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt"%>
<c:set var="CP" value="${pageContext.request.contextPath}" />

<header id="header" class="mx-1 mt-4">
	<nav class="navbar navbar-expand-lg navbar-light bg-light">
		<div class="container">
				<div class="collapse navbar-collapse">
						<ul class="navbar-nav ms-auto">
								<li class="nav-item">
										<a class="nav-link" href="${pageContext.request.contextPath}/mypage">마이페이지</a>
								</li>
								<li class="nav-item">
					<c:choose>
								<c:when test="${empty sessionScope.user.name }">
								 <li  class="nav-item"><a class="nav-link" href="${pageContext.request.contextPath}/login/login.do">로그인</a></li>
								</c:when> 
							<c:otherwise>
								<li  class="nav-item"><a class="nav-link" href="${pageContext.request.contextPath}/logout">로그아웃</a></li>
							</c:otherwise>
						 </c:choose>
								</li>
						</ul>
				</div>
		</div>
</nav>
	<nav class="navbar navbar-expand-lg navbar-light">
		<div class="container-fluid">
			<a class="navbar-brand text-dark fs-2" href="${CP}/index">서울365
				안전포털</a>
			<button class="navbar-toggler" type="button"
				data-bs-toggle="collapse" data-bs-target="#navbarNav"
				aria-controls="navbarNav" aria-expanded="false"
				aria-label="Toggle navigation">
				<span class="navbar-toggler-icon"></span>
			</button>
			<div class="collapse navbar-collapse" id="navbarNav">
				<ul class="nav nav-pills">
					<!-- 재난 현황 메뉴 드롭다운  -->
					<li class="nav-item dropdown"><a
						class="nav-link text-dark fw-bolder" id="disasterDropdown"
						role="button"> 재난현황 </a>
						<ul class="dropdown-menu" aria-labelledby="disasterDropdown">
							<li><a class="dropdown-item" href="${CP}/rainfall/view">호우</a></li>
							<li><a class="dropdown-item" href="${CP}/waterlevel/view">홍수</a></li>
							<li><a class="dropdown-item" href="${CP}/earthquake/view">지진</a></li>
							<li><a class="dropdown-item" href="${CP}/typ/view">태풍</a></li>
							<li><a class="dropdown-item"
								href="${CP}/disastermessage/view">재난문자</a></li>
							<li><a class="dropdown-item"
								href="${CP}/disastermessage/safety_Index">재난안전통계</a></li>
						</ul></li>

					<!-- 날씨 메뉴 드롭다운  -->
					<li class="nav-item dropdown"><a
						class="nav-link text-dark fw-bolder" id="weatherDropdown"
						role="button"> 서울날씨 </a>
						<ul class="dropdown-menu" aria-labelledby="weatherDropdown">
							<li><a class="dropdown-item" href="${CP}/weather">날씨</a></li>
							<li><a class="dropdown-item" href="${CP}/air_quality">대기환경</a>
							</li>
						</ul></li>

					<!-- 재난안전시설 메뉴 드롭다운  -->
					<li class="nav-item dropdown"><a
						class="nav-link text-dark fw-bolder" id="facilitieDropdown"
						role="button"> 재난안전시설 </a>
						<ul class="dropdown-menu" aria-labelledby="facilitieDropdown">
							<li><a class="dropdown-item" href="${CP}/acmdfclty/view">지진
									옥외 대피 장소</a></li>
							<li><a class="dropdown-item" href="${CP}/hanpa/view">한파
									응급 대피소</a></li>
							<li><a class="dropdown-item" href="${CP}/faclt/view">비상
									대피 시설</a></li>
							<li><a class="dropdown-item" href="${CP}/ewsf/view">급수
									시설</a></li>
						</ul></li>

					<!-- 재난대비 메뉴 드롭다운 -->
					<li class="nav-item dropdown"><a
						class="nav-link text-dark fw-bolder" id="preparationDropdown"
						role="button"> 재난대비 </a>
						<ul class="dropdown-menu" aria-labelledby="preparationDropdown">
							<li><a class="dropdown-item" href="${CP}/siren">재난 경보 소리 테스트</a></li>
							<li><a class="dropdown-item" href="#">안전점검 퀴즈</a></li>
							<li><a class="dropdown-item" href="${CP}/checklist">생존
									필수품 추천 및 체크리스트</a></li>
							<li><a class="dropdown-item" href="${CP}/videopost/list">재난
									훈련 영상</a></li>
							<li><a class="dropdown-item"
								href="${CP}/disasterguide/finedust">자연재난 행동 요령 및 예방법</a></li>
						</ul></li>

					<!-- 시민안전보험 메뉴 드롭다운 -->
					<li class="nav-item dropdown"><a
						class="nav-link text-dark fw-bolder" id="insuranceDropdown"
						role="button"> 시민안전보험 </a>
						<ul class="dropdown-menu" aria-labelledby="insuranceDropdown">
							<li><a class="dropdown-item" href="${CP}/ins/intro.do">시민안전보험 소개</a></li>
							<li><a class="dropdown-item" href="${CP}/ins/getIns.do">시민안전보험 조회</a></li>
						</ul></li>
					<!-- 응급의료기관 -->
					<li class="nav-item dropdown"><a
						class="nav-link text-dark fw-bolder" id="medicalInstDropdown"
						role="button"> 응급의료기관 </a>
						<ul class="dropdown-menu" aria-labelledby="medicalInstDropdown">
							<li><a class="dropdown-item" href="${CP}/er_medi_inst/list">응급의료기관
									정보</a></li>
							<li><a class="dropdown-item"
								href="${CP}/er_medi_inst/er_bed">응급실 가용병상 현황</a></li>
						</ul></li>

					<!-- 재난안전게시판 -->
					<li class="nav-item dropdown"><a
						class="nav-link text-dark fw-bolder" id="boardDropdown"
						role="button"> 재난안전게시판 </a>
						<ul class="dropdown-menu" aria-labelledby="boardDropdown">
							<li><a class="dropdown-item" href="${CP}/board/doRetrieve.do?div=10">공지사항</a></li>
							<li><a class="dropdown-item" href="${CP}/board/doRetrieve.do?div=20">자유게시판</a></li>
							<li><a class="dropdown-item" href="${CP}/board/doRetrieve.do?div=30">통계자료실</a></li>
						</ul></li>
				</ul>
			</div>
		</div>
	</nav>
</header>

<!-- ✅ 마우스 오버 시 드롭다운 열리게 하는 JS -->
<script>
	document.addEventListener('DOMContentLoaded', function() {
		let dropdowns = document.querySelectorAll('.nav-item.dropdown');

		dropdowns.forEach(function(dropdown) {
			/* 마우스 오버시 이벤트 */
			dropdown.addEventListener('mouseover', function() {
				let menu = this.querySelector('.dropdown-menu');

				menu.classList.add('show');
			});

			/* 마우스 leave 시 이벤트 */
			dropdown.addEventListener('mouseout', function() {
				let menu = this.querySelector('.dropdown-menu');

				menu.classList.remove('show');
			});
		});
	});
</script>
