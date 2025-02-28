<%--
  Created by IntelliJ IDEA.
  User: acorn4
  Date: 2025-02-28
  Time: PM 4:52
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>사회재난 행동요령</title>
    <link rel="stylesheet" type="text/css" href="/assets/css/disasters_guide.css">
</head>
<body>
<div id="container" class="message">
    <div id="state_sub">
        <div class="historyTab">
            <ul>
                <li class="active"><a href="/disastermessage/view"><strong>재난문자</strong></a></li>
                <li class="active"><a href="/earthquake/view">지진</a></li>
                <li class="active"><a href="/typ/view">태풍</a></li>
                <li class="active"><a href="/disasterguide/natural">자연재난 행동요령</a></li>
                <li class="on"><a href="/disasterguide/social">사회재난 행동요령</a></li>
            </ul>
        </div>
        <div id="sidebar">
            <ul>
                <li><a href="/disasterguide/fineDust">화재</a></li>
                <li><a href="/disasterguide/typhoon">산불</a></li>
                <li><a href="/disasterguide/heatwave">전기-가스사고</a></li>
                <li><a href="/disasterguide/heavyRain">교통사고</a></li>
            </ul>
        </div>
    </div>
</div>
</body>
</html>
