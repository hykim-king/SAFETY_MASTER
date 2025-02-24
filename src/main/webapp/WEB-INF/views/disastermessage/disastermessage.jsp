<%--
  Created by IntelliJ IDEA.
  User: acorn4
  Date: 2025-02-24
  Time: PM 2:07
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<html>
<head>
    <title>Title</title>
  <link rel="stylesheet" type="text/css" href="/assets/css/dismes.css">
</head>
<body>
<div id="container" class="message">
  <div id="state_sub">
    <div class="stateWrap">
      <strong>재난문자</strong>
      <ul>
        <li class="active"><a><strong>재난문자</strong></a></li>
        <li><a ><strong>과거재난기록</strong></a></li>
      </ul>
    </div>
  </div>
  <div>
    <div class="listWrap">
      <form name="searchForm" id="searchForm" method="get">
        <input type="hidden" id="sidoCds" name="sidoCds" value="">
        <input type="hidden" id="dtypes" name="dtypes" value="">
        <input type="hidden" id="page" name="page" value="1">

        <div class="searchArea">
          <a onclick="areaSelect()" id="smsAreaCd" data-code="">지역</a>
          <a id="smsDisasterCd" data-code="">재난종류</a>
          <input type="text" id="areaNm" name="areaNm" placeholder="지역검색" value="">
          <a  id="search">검색</a>
          <a id="reset">검색초기화</a>
        </div>
      </form>

      <table class="tableTypeE">
        <caption>지역 재난종류 등록일에대한 검색 결과 리스트</caption>
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
                <td>${list.disMesCon}</td>
                <td>${list.disMesCreateDt}</td>
              </tr>
          </c:forEach>
        </tbody>
      </table>
    </div>
  </div>

</body>
</html>
