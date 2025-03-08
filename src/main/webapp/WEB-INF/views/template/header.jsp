<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt"%>
<c:set var="CP" value="${pageContext.request.contextPath}" />

<header id="custom-header">

    <div class="custom-header-box">
        <div class="custom-header-content">
            <!-- 로고 -->
            <div class="custom-logo-container">
                <a class="custom-navbar-brand" href="${CP}/index">
                    <img src="${CP}/assets/images/logo/3652.png" alt="서울365 안전포털"
                        class="custom-logo-img">
                </a>
            </div>

            <!-- 네비게이션 메뉴 -->
            <nav class="custom-navbar">
                <ul class="custom-nav-pills">
                    <!-- 재난현황 메뉴 -->
                    <li class="custom-nav-item custom-dropdown">
                        <a class="custom-nav-link custom-dropdown-toggle" href="#">재난현황</a>
                        <ul class="custom-dropdown-menu">
                            <li><a class="custom-dropdown-item" href="#">홍수</a></li>
                            <li><a class="custom-dropdown-item" href="#">지진</a></li>
                            <li><a class="custom-dropdown-item" href="#">태풍</a></li>
                            <li><a class="custom-dropdown-item" href="#">재난문자</a></li>
                            <li><a class="custom-dropdown-item" href="#">재난안전통계</a></li>
                        </ul>
                    </li>

                    <!-- 서울날씨 메뉴 -->
                    <li class="custom-nav-item custom-dropdown">
                        <a class="custom-nav-link custom-dropdown-toggle" href="#">서울날씨</a>
                        <ul class="custom-dropdown-menu">
                            <li><a class="custom-dropdown-item" href="${CP}/weather">날씨</a></li>
                            <li><a class="custom-dropdown-item" href="${CP}/air_quality">대기환경</a></li>
                        </ul>
                    </li>

                    <!-- 재난안전시설 메뉴 -->
                    <li class="custom-nav-item custom-dropdown">
                        <a class="custom-nav-link custom-dropdown-toggle" href="#">재난안전시설</a>
                        <ul class="custom-dropdown-menu">
                            <li><a class="custom-dropdown-item" href="#">지진 옥외 대피 장소</a></li>
                            <li><a class="custom-dropdown-item" href="#">한파 응급 대피소</a></li>
                            <li><a class="custom-dropdown-item" href="#">비상 대피 시설</a></li>
                            <li><a class="custom-dropdown-item" href="#">급수 시설</a></li>
                        </ul>
                    </li>

                    <!-- 재난대비 메뉴 -->
                    <li class="custom-nav-item custom-dropdown">
                        <a class="custom-nav-link custom-dropdown-toggle" href="#">재난대비</a>
                        <ul class="custom-dropdown-menu">
                            <li><a class="custom-dropdown-item" href="#">재난 경보 소리 테스트</a></li>
                            <li><a class="custom-dropdown-item" href="#">안전점검 퀴즈</a></li>
                            <li><a class="custom-dropdown-item" href="#">생존 필수품 추천 및 체크리스트</a></li>
                            <li><a class="custom-dropdown-item" href="#">재난 훈련 영상</a></li>
                            <li><a class="custom-dropdown-item" href="#">자연재난 행동 요령 및 예방법</a></li>
                        </ul>
                    </li>

                    <!-- 시민안전보험 메뉴 -->
                    <li class="custom-nav-item custom-dropdown">
                        <a class="custom-nav-link custom-dropdown-toggle" href="#">시민안전보험</a>
                        <ul class="custom-dropdown-menu">
                            <li><a class="custom-dropdown-item" href="#">Feature 1</a></li>
                            <li><a class="custom-dropdown-item" href="#">Feature 2</a></li>
                            <li><a class="custom-dropdown-item" href="#">Feature 3</a></li>
                        </ul>
                    </li>

                    <!-- 응급의료기관 -->
                    <li class="custom-nav-item custom-dropdown">
                        <a class="custom-nav-link custom-dropdown-toggle" href="#">응급의료기관</a>
                        <ul class="custom-dropdown-menu">
                            <li><a class="custom-dropdown-item" href="${CP}/er_medi_inst/list">응급의료기관 정보</a></li>
                            <li><a class="custom-dropdown-item" href="${CP}/er_medi_inst/er_bed">응급실 가용병상 현황</a></li>
                        </ul>
                    </li>

                    <!-- 재난안전게시판 -->
                    <li class="custom-nav-item custom-dropdown">
                        <a class="custom-nav-link custom-dropdown-toggle" href="#">재난안전게시판</a>
                        <ul class="custom-dropdown-menu">
                            <li><a class="custom-dropdown-item" href="#">Feature 1</a></li>
                            <li><a class="custom-dropdown-item" href="#">Feature 2</a></li>
                            <li><a class="custom-dropdown-item" href="#">Feature 3</a></li>
                        </ul>
                    </li>
                </ul>
            </nav>
        </div>
    </div>
</header>

<!-- ✅ 마우스 오버 시 드롭다운 열리게 하는 JS -->
<script>
document.addEventListener('DOMContentLoaded', function() {
    let dropdowns = document.querySelectorAll('.custom-nav-item.custom-dropdown');

    dropdowns.forEach(function(dropdown) {
        let menu = dropdown.querySelector('.custom-dropdown-menu');

        dropdown.addEventListener('mouseenter', function() {
            menu.style.opacity = "1";
            menu.style.transform = "translateY(0)";
            menu.style.visibility = "visible";
        });

        dropdown.addEventListener('mouseleave', function() {
            menu.style.opacity = "0";
            menu.style.transform = "translateY(-10px)";
            menu.style.visibility = "hidden";
        });
    });
});

</script>
