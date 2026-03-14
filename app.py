<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LoL 패치 하이라이트 - 한눈에 보는 핵심 패치</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* 부드러운 스크롤과 기본 다크 테마 배경 설정 */
        body {
            background-color: #0f172a;
            color: #f8fafc;
            font-family: 'Pretendard', sans-serif;
        }
        .card-hover {
            transition: transform 0.2s ease-in-out;
        }
        .card-hover:hover {
            transform: translateY(-5px);
        }
    </style>
</head>
<body class="min-h-screen p-6">

    <header class="max-w-4xl mx-auto mb-10 text-center">
        <h1 class="text-4xl font-bold mb-2 text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-500">
            패치 14.6 하이라이트
        </h1>
        <p class="text-slate-400">이번 패치에서 가장 논란이 되거나 주목해야 할 핵심 변경점</p>
    </header>

    <main class="max-w-4xl mx-auto">
        <div id="patch-container" class="grid grid-cols-1 md:grid-cols-2 gap-6">
            </div>
    </main>

    <script>
        // 가독성을 높이기 위해 데이터를 분리하여 관리합니다.
        // 향후 백엔드나 DB와 연결하기 쉬운 구조입니다.
        const patchData = [
            {
                title: "스몰더 - 처형 기준 너프",
                type: "너프",
                typeColor: "bg-red-500/20 text-red-400 border-red-500/50",
                isHot: true,
                description: "후반 캐리력이 지나치게 높았던 스몰더의 Q 스킬 처형 기준이 대폭 낮아집니다. 이제 예전만큼 쉽게 펜타킬을 쓸어담기는 힘들 것입니다.",
                stats: "Q 처형 기준치: 225 스택 -> 275 스택"
            },
            {
                title: "갈리오 - 딜탱 브루저로 재탄생?",
                type: "버프",
                typeColor: "bg-blue-500/20 text-blue-400 border-blue-500/50",
                isHot: true,
                description: "기본 데미지는 낮아졌지만, 스킬 쿨타임이 대폭 감소하고 패시브 활용도가 높아졌습니다. 지속 교전에 강한 딜탱 포지션으로 떡상할 가능성이 높습니다.",
                stats: "패시브 쿨타임 감소, Q 스킬 쿨타임: 12~8초 -> 10~7초"
            },
            {
                title: "무한의 대검 - 치명타 원딜의 희망",
                type: "버프",
                typeColor: "bg-blue-500/20 text-blue-400 border-blue-500/50",
                isHot: false,
                description: "치명타 피해량이 증가하여 침체되어 있던 전통적인 치명타 기반 원거리 딜러들이 다시 등장할 수 있는 발판이 마련되었습니다.",
                stats: "치명타 피해량: 40% -> 50%"
            },
            {
                title: "서포터 아이템 골드 수급 하향",
                type: "너프",
                typeColor: "bg-red-500/20 text-red-400 border-red-500/50",
                isHot: true,
                description: "서포터 아이템의 골드 수급량이 줄어들어 시야 장악 타이밍이 늦어집니다. 바텀 라인전의 스노우볼 속도에 큰 영향을 미칠 핵심 패치입니다.",
                stats: "퀘스트 완료 골드 요구치 증가"
            }
        ];

        // 데이터를 HTML 카드로 변환하여 화면에 출력하는 함수
        function renderPatchNotes() {
            const container = document.getElementById('patch-container');
            
            patchData.forEach(item => {
                // HOT 이슈일 경우 불꽃 마크 추가
                const hotBadge = item.isHot ? `<span class="bg-orange-500 text-white text-xs font-bold px-2 py-1 rounded ml-2 animate-pulse">🔥 HOT 이슈</span>` : '';

                const cardHTML = `
                    <div class="bg-slate-800 border border-slate-700 rounded-xl p-6 shadow-lg card-hover">
                        <div class="flex items-center justify-between mb-4">
                            <h2 class="text-xl font-bold text-white flex items-center">
                                ${item.title}
                            </h2>
                        </div>
                        <div class="mb-4 flex items-center">
                            <span class="border px-3 py-1 rounded-full text-sm font-semibold ${item.typeColor}">
                                ${item.type}
                            </span>
                            ${hotBadge}
                        </div>
                        <p class="text-slate-300 text-sm leading-relaxed mb-4">
                            ${item.description}
                        </p>
                        <div class="bg-slate-900 rounded-lg p-3 border-l-4 border-slate-500 text-sm text-slate-400">
                            <strong>수치 변화:</strong> ${item.stats}
                        </div>
                    </div>
                `;
                container.innerHTML += cardHTML;
            });
        }

        // 페이지가 로드되면 렌더링 함수 실행
        window.onload = renderPatchNotes;
    </script>
</body>
</html>
