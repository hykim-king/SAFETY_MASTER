<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/functions" prefix="fn" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt" %>

<html>
<head>
    <title>${video.videoTitle}</title>
    <link rel="stylesheet" type="text/css" href="/assets/css/videodetail.css">
</head>
<body>

<div class="video-detail-container">
    <h1 class="video-title">${video.videoTitle}</h1>
    
    <p class="video-date">작성일: 
        <fmt:formatDate value="${video.videoUploaded}" pattern="yyyy-MM-dd HH:mm"/>
    </p>

    <!-- 유튜브 영상 ID 가져오기 -->
    <c:set var="videoId" value="${video.videoOriginalUrl}" />

    <!-- 📌 영상 플레이어 -->
    <div class="video-player">
        <iframe width="800" height="450" 
                src="https://www.youtube.com/embed/${videoId}" 
                frameborder="0" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                referrerpolicy="strict-origin-when-cross-origin" 
                allowfullscreen>
        </iframe>
    </div>

    <!-- 📌 영상 설명 -->
    <div class="video-description">
        <p>${video.videoDescription}</p>
    </div>

    <!-- 🔙 목록으로 돌아가기 버튼 -->
    <div class="back-button">
        <a href="<c:url value='/videopost/list' />">목록으로 돌아가기</a>
    </div>
</div>

</body>
</html>
