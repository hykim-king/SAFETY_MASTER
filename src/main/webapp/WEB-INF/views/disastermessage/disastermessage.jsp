<%--
  Created by IntelliJ IDEA.
  User: acorn4
  Date: 2025-02-24
  Time: PM 2:07
  To change this template use File | Settings | File Templates.
--%>
<%@ page import="com.pcwk.ehr.cmn.StringUtil" %>
<%@ page import="com.pcwk.ehr.cmn.SearchVO" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%
  /**
   *
   * @param maxNum : 총 글수
   * @param currentPageNo: 현재 페이지번호
   * @param rowPerPage : 페이지 사이즈 (10,20,...100)
   * @param bottomCount: 10/5
   * @param url : 서버 호출 URL
   * @param scriptName : 자바스크립트 함수명
   * @return "html 텍스트"
   */
  int bottomCount = 10;
  int pageSize    = 10;
  int pageNo      = 0;

  int maxNum      = Integer.parseInt(request.getAttribute("totalCnt").toString()) ;//총 글수

  //out.print("****:"+maxNum);
  SearchVO  paramVO     = (SearchVO)request.getAttribute("search");
  pageSize  = paramVO.getPageSize();
  pageNo    = paramVO.getPageNo();

  //out.print("pageSize****:"+pageSize);
  //out.print("pageNo****:"+pageNo);

  String cp = request.getContextPath();
  String pageHtml =
          StringUtil.renderingPager(maxNum,
                  pageNo,
                  pageSize,
                  bottomCount,
                  cp+"/disastermessage/view", "pageDoRetrieve");

%>
<%@ include file="../../template/footer.jsp" %>
<%@ include file="../../template/header.jsp" %>
<html>
<head>
    <title>재난문자</title>
  <link rel="stylesheet" type="text/css" href="/assets/css/dismes.css">
</head>
<body>
<div id="container" class="message">
  <div id="state_sub">
    <div class="historyTab">
      <ul>
        <li class="on"><a href="/disastermessage/view"><strong>재난문자</strong></a></li>
        <li class="active"><a href="/earthquake/view">지진</a></li>
        <li class="active"><a href="/typ/view">태풍</a></li>
        <li class="active"><a href="/disasterguide/finedust">자연재난 행동요령</a></li>
        <li class="active"><a href="/disasterguide/fire">사회재난 행동요령</a></li>
      </ul>
    </div>
  </div>
  <div>

    <div class="listWrap">
      <form action = "#" class="search-form" name = "userForm" id = "userForm" method = "get" enctype="application/x-www-form-urlencoded">
        <input type ="hidden" name = "pageNo" id = "pageNo"> <!-- 히든할 것들은 form 바로 밑에 주는 게 암묵적 약속 -->
        <div class="search-group">
          <select name="searchDiv" id="searchDiv">
            <option id="" value="10" <c:if test="${10 == search.searchDiv}">selected</c:if>>검색 항목을 선택하세요</option>
            <option value="20" <c:if test="${20 == search.searchDiv}">selected</c:if>>지역</option>
            <option value="30" <c:if test="${30 == search.searchDiv}">selected</c:if>>재난종류</option>
          </select>


          <input type="search" name="searchWord" id="searchWord" value="${search.searchWord}" placeholder="검색어를 입력하세요">
          <select name = "pageSize" id = "pageSize">
            <option value = "10" <c:if test = "${10 == search.pageSize}">selected</c:if> >10</option>
            <option value = "20" <c:if test = "${20 == search.pageSize}">selected</c:if> >20</option>
            <option value = "30" <c:if test = "${30 == search.pageSize}">selected</c:if> >30</option>
            <option value = "40" <c:if test = "${40 == search.pageSize}">selected</c:if> >40</option>
            <option value = "50" <c:if test = "${50 == search.pageSize}">selected</c:if> >50</option>
            <option value = "100"<c:if test = "${100 == search.pageSize}">selected</c:if> >100</option>
          </select>
          <input type="button" value="조회" id="doRetrieveBtn">
          <input type="button" value="검색초기화" id="reset">
        </div>
      </form>
<%--      <form name="searchForm" id="searchForm" method="get">--%>
<%--        <input type="hidden" id="sidoCds" name="sidoCds" value="">--%>
<%--        <input type="hidden" id="dtypes" name="dtypes" value="">--%>
<%--        <input type="hidden" id="page" name="page" value="1">--%>

<%--        <div class="searchArea">--%>
<%--          <a onclick="areaSelect()" id="smsAreaCd" data-code="">지역</a>--%>
<%--          <a id="smsDisasterCd" data-code="">재난종류</a>--%>
<%--          <input type="text" id="areaNm" name="areaNm" placeholder="지역검색" value="">--%>
<%--          <a  id="search">검색</a>--%>
<%--          <a id="reset">검색초기화</a>--%>
        </div>
      </form>

      <table class="tableTypeE">
        <colgroup>
          <col width="80"><col width="300"><col width="127"><col width="533"><col width="140">
        </colgroup>
        <thead>
        <tr>
          <th>번호</th>
          <th>지역</th>
          <th>재난종류</th>
          <th>재난내용</th>
          <th>등록일</th>
        </tr>
        </thead>


        <tbody>
        <c:forEach var="list" items="${list}">

                <td>${list.disMesNum}</td>
                <td>${list.disMesArea}</td>
                <td>${list.disMesType}</td>
                <td><a href="/disastermessage/Detail?disMesNum=${list.disMesNum}">${list.disMesCon}</a></td>
                <td>${list.disMesCreateDt}</td>
              </tr>

          </c:forEach>
        </tbody>
      </table>
    </div>

    <br>
    <% out.print(pageHtml); %>
  </div>
  <script src="/assets/js/dismes/dismes_page.js"></script> <!-- 여기에 스크립트 파일 경로 -->
</body>
</html>
