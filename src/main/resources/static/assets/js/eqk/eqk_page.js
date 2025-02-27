// URL 파라미터에서 특정 값을 가져오는 함수
function getQueryParameter(name) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(name);
}

// 페이지 로드 시 searchDiv와 searchWord에 맞는 상태를 반영
window.onload = function() {
    const searchDiv = getQueryParameter('searchDiv');
    const searchWord = getQueryParameter('searchWord');

    // searchDiv에 맞는 항목에 'on' 클래스를 추가
    if (searchDiv === '10') {
        document.getElementById('listDate').classList.add('on');
    } else if (searchDiv === '20') {
        document.getElementById('listMng').classList.add('on');
    }

    // 'year' select 태그에서 searchWord에 해당하는 연도 선택
    if (searchWord) {
        document.getElementById('year').value = searchWord;
    }
};

// 연도 선택 시 해당 연도에 맞는 데이터 조회
function changeYear() {
    const year = document.getElementById('year').value;
    const currentSearchDiv = getQueryParameter('searchDiv'); // 기존에 선택된 searchDiv 값 가져오기
    let newUrl = '/earthquake/view?searchWord=' + year;

    // searchDiv 값이 있을 경우, 그대로 유지하면서 새 URL 생성
    if (currentSearchDiv) {
        newUrl += '&searchDiv=' + currentSearchDiv;
    }

    // 새로운 URL로 리디렉션
    window.location.href = newUrl;
}

// 클릭 시 선택된 항목 변경
function changeSelection(value) {
    const currentSearchWord = getQueryParameter('searchWord'); // 기존에 선택된 searchWord 값 가져오기
    let newUrl = '/earthquake/view?searchDiv=' + value;

    // searchWord 값이 있을 경우, 그대로 유지하면서 새 URL 생성
    if (currentSearchWord) {
        newUrl += '&searchWord=' + currentSearchWord;
    }

    // 새로운 URL로 리디렉션
    window.location.href = newUrl;
}

// // 데이터 예시 (실제는 JSP에서 데이터베이스에서 추출하여 삽입해야 합니다)
// var earthquakeData = [
//     { year: '2025', magnitudeRange: '2.0 - 2.9', count: 12 },
//     { year: '2025', magnitudeRange: '3.0 - 3.9', count: 8 },
//     { year: '2025', magnitudeRange: '5.0 ~', count: 2 },
//     { year: '2024', magnitudeRange: '2.0 - 2.9', count: 15 },
//     { year: '2024', magnitudeRange: '3.0 - 3.9', count: 7 },
//     { year: '2024', magnitudeRange: '5.0 ~', count: 3 },
//     { year: '2023', magnitudeRange: '2.0 - 2.9', count: 12 },
//     { year: '2023', magnitudeRange: '3.0 - 3.9', count: 8 },
//     { year: '2023', magnitudeRange: '5.0 ~', count: 2 },
//     { year: '2022', magnitudeRange: '2.0 - 2.9', count: 15 },
//     { year: '2022', magnitudeRange: '3.0 - 3.9', count: 7 },
//     { year: '2022', magnitudeRange: '5.0 ~', count: 3 },
//     { year: '2021', magnitudeRange: '2.0 - 2.9', count: 12 },
//     { year: '2021', magnitudeRange: '3.0 - 3.9', count: 8 },
//     { year: '2021', magnitudeRange: '5.0 ~', count: 2 },
//     { year: '2020', magnitudeRange: '2.0 - 2.9', count: 15 },
//     { year: '2020', magnitudeRange: '3.0 - 3.9', count: 7 },
//     { year: '2020', magnitudeRange: '5.0 ~', count: 3 },
//     { year: '2019', magnitudeRange: '2.0 - 2.9', count: 12 },
//     { year: '2019', magnitudeRange: '3.0 - 3.9', count: 8 },
//     { year: '2019', magnitudeRange: '5.0 ~', count: 2 },
//     { year: '2018', magnitudeRange: '2.0 - 2.9', count: 15 },
//     { year: '2018', magnitudeRange: '3.0 - 3.9', count: 7 },
//     { year: '2018', magnitudeRange: '5.0 ~', count: 3 },
//     { year: '2017', magnitudeRange: '2.0 - 2.9', count: 12 },
//     { year: '2017', magnitudeRange: '3.0 - 3.9', count: 8 },
//     { year: '2017', magnitudeRange: '5.0 ~', count: 2 },
//     { year: '2016', magnitudeRange: '2.0 - 2.9', count: 15 },
//     { year: '2016', magnitudeRange: '3.0 - 3.9', count: 7 },
//     { year: '2016', magnitudeRange: '4.0 - 4.9', count: 7 },
//     { year: '2016', magnitudeRange: '5.0 ~', count: 3 },
// ];
//
// /// 고유 연도 리스트
// var years = [...new Set(earthquakeData.map(item => item.year))];
//
// // 규모 범위 설정
// var magnitudeRanges = ['2.0 - 2.9', '3.0 - 3.9', '4.0 - 4.9', '5.0 ~'];
//
// // 각 연도별 규모 범위별 지진 수량을 합산
// var dataset = magnitudeRanges.map(range => {
//     return {
//         label: range,
//         data: years.map(year => {
//             return earthquakeData.filter(item => item.year === year && item.magnitudeRange === range)
//                 .reduce((sum, item) => sum + item.count, 0);
//         }),
//         backgroundColor: range === '2.0 - 2.9' ? 'rgb(69,100,237)' :
//             range === '3.0 - 3.9' ? 'rgb(241,189,58)' :
//                 range === '4.0 - 4.9' ? 'rgb(237,101,43)' : 'rgb(239,43,43)',
//         borderColor: 'black',
//         borderWidth: 1,
//         borderRadius: 8,  // 여기서 radius를 설정
//     };
// });
//
// // 차트 그리기
// var ctx = document.getElementById('earthquakeChart').getContext('2d');
// var earthquakeChart = new Chart(ctx, {
//     type: 'bar',
//     data: {
//         labels: years, // X축 레이블: 연도
//         datasets: dataset // Y축 데이터: 규모별 데이터셋
//     },
//     options: {
//         maxBarThickness: 20,
//         responsive: true,
//         maintainAspectRatio: false,
//         scales: {
//             x: {
//                 title: {
//                     display: true
//                 },
//                 stacked: true,  // 막대가 쌓이는 차트
//                 grid: {
//                     offset: true
//                 }
//             },
//             y: {
//                 beginAtZero: true,
//                 stacked: true, // 막대가 쌓이는 차트
//                 title: {
//                     display: true
//                 }
//             }
//         },
//         plugins: {
//             legend: {
//                 position: 'top',
//             }
//         },
//     },
// });


