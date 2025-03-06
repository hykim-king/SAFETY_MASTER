<%@ page
         pageEncoding="UTF-8"%>

<header id="header" class="mx-1 mt-4">
    <nav class="navbar navbar-expand-lg navbar-light ">
        <div class="container-fluid">
            <a class="navbar-brand text-dark fs-2" href="#">서울365 안전포털</a>
            <button class="navbar-toggler" type="button"
                    data-bs-toggle="collapse" data-bs-target="#navbarNav"
                    aria-controls="navbarNav" aria-expanded="false"
                    aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="nav nav-pills">

                    <!-- 재난 현황 메뉴 드롭다운  -->
                    <li class="nav-item dropdown"><a class="nav-link text-dark fw-bolder"
                                                     href="#" id="disasterDropdown" role="button"> 재난현황 </a>
                        <ul class="dropdown-menu" aria-labelledby="disasterDropdown">
                            <li><a class="dropdown-item" href="#">홍수</a></li>
                            <li><a class="dropdown-item" href="/earthquake/view">지진</a></li>
                            <li><a class="dropdown-item" href="/typ/view">태풍</a></li>
                            <li><a class="dropdown-item" href="/disastermessage/view">재난문자</a></li>
                            <li><a class="dropdown-item" href="#">재난안전통계</a></li>
                            <li><a class="dropdown-item" href="/disastermessage/safety_Index">재난안전지수</a></li>

                        </ul></li>

                    <!-- 날씨 메뉴 드롭다운  -->
                    <li class="nav-item dropdown"><a class="nav-link text-dark fw-bolder"
                                                     href="#" id="weatherDropdown" role="button"> 서울날씨 </a>
                        <ul class="dropdown-menu" aria-labelledby="weatherDropdown">
                            <li><a class="dropdown-item" href="#">날씨</a></li>
                            <li><a class="dropdown-item" href="#">대기오염</a></li>
                            <li><a class="dropdown-item" href="#">미세먼지주의보발령내역</a></li>
                        </ul></li>

                    <!-- 재난안전시설 메뉴 드롭다운  -->
                    <li class="nav-item dropdown"><a class="nav-link text-dark fw-bolder"
                                                     href="#" id="facilitieDropdown" role="button"> 재난안전시설 </a>
                        <ul class="dropdown-menu" aria-labelledby="facilitieDropdown">
                            <li><a class="dropdown-item" href="#">지진 옥외 대피 장소</a></li>
                            <li><a class="dropdown-item" href="#">한파 응급 대피소</a></li>
                            <li><a class="dropdown-item" href="#">비상 대피 시설</a></li>
                            <li><a class="dropdown-item" href="/ewsf/view">급수 시설</a></li>
                        </ul></li>

                    <!-- 재난대비 메뉴 드롭다운 -->
                    <li class="nav-item dropdown"><a class="nav-link text-dark fw-bolder"
                                                     href="#" id="preparationDropdown" role="button"> 재난대비 </a>
                        <ul class="dropdown-menu" aria-labelledby="preparationDropdown">
                            <li><a class="dropdown-item" href="#">재난 경보 소리 테스트</a></li>
                            <li><a class="dropdown-item" href="#">안전점검 퀴즈</a></li>
                            <li><a class="dropdown-item" href="#">생존 필수품 추천 및 체크리스트</a></li>
                            <li><a class="dropdown-item" href="#">재난 훈련 영상</a></li>
                            <li><a class="dropdown-item" href="/disasterguide/finedust">자연재난 행동 요령 및 예방법</a></li>
                            <li><a class="dropdown-item" href="/disasterguide/fire">사회재난 행동 요령 및 예방법</a></li>
                        </ul></li>

                    <!-- 시민안전보험 메뉴 드롭다운 -->
                    <li class="nav-item dropdown"><a class="nav-link text-dark fw-bolder"
                                                     href="#" id="insuranceDropdown" role="button"> 시민안전보험 </a>
                        <ul class="dropdown-menu" aria-labelledby="insuranceDropdown">
                            <li><a class="dropdown-item" href="#">Feature 1</a></li>
                            <li><a class="dropdown-item" href="#">Feature 2</a></li>
                            <li><a class="dropdown-item" href="#">Feature 3</a></li>
                        </ul></li>


                    <!-- 응급의료기관 -->
                    <li class="nav-item dropdown"><a class="nav-link text-dark fw-bolder"
                                                     href="#" id="medicalInstDropdown" role="button"> 응급의료기관 </a>
                        <ul class="dropdown-menu" aria-labelledby="medicalInstDropdown">
                            <li><a class="dropdown-item" href="#">응급의료기관 정보</a></li>
                            <li><a class="dropdown-item" href="#">응급실 가용병상 현황</a></li>
                        </ul></li>

                    <!-- 재난안전게시판 -->
                    <li class="nav-item dropdown"><a class="nav-link text-dark fw-bolder"
                                                     href="#" id="boardDropdown" role="button"> 재난안전게시판 </a>
                        <ul class="dropdown-menu" aria-labelledby="boardDropdown">
                            <li><a class="dropdown-item" href="#">Feature 1</a></li>
                            <li><a class="dropdown-item" href="#">Feature 2</a></li>
                            <li><a class="dropdown-item" href="#">Feature 3</a></li>
                        </ul></li>


                </ul>
            </div>
        </div>
    </nav>
</header>

<!-- ✅ 마우스 오버 시 드롭다운 열리게 하는 JS -->
<script>
    document.addEventListener("DOMContentLoaded", function() {
        let dropdowns = document.querySelectorAll(".nav-item.dropdown");

        dropdowns.forEach(function(dropdown) {

            /* 마우스 오버시 이벤트 */
            dropdown.addEventListener("mouseover", function() {

                let menu = this.querySelector(".dropdown-menu");

                menu.classList.add("show");
            });

            /* 마우스 leave 시 이벤트 */
            dropdown.addEventListener("mouseout", function() {
                let menu = this.querySelector(".dropdown-menu");

                menu.classList.remove("show");


            });

        });
    });
</script>

