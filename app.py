import streamlit as st

# 1. 웹 페이지 기본 설정
st.set_page_config(page_title="LoL 패치 하이라이트", page_icon="🔥", layout="centered")

# 2. 메인 헤더
st.title("🔥 롤 핵심 패치 모아보기")
st.markdown("과거부터 현재까지, 협곡을 뒤흔든 주요 패치와 이슈들을 한눈에 확인하세요.")
st.divider()

# 3. 데이터 구조화 (패치 버전별로 데이터를 나누어 관리합니다)
# 💡 나중에 새로운 패치가 나오면 이 딕셔너리의 맨 위에 추가만 하시면 됩니다.
patch_history = {
    "14.6 패치 (최신)": [
        {
            "title": "스몰더 - 처형 기준 너프",
            "type": "너프",
            "isHot": True,
            "description": "후반 캐리력이 지나치게 높았던 스몰더의 Q 스킬 처형 기준이 대폭 낮아집니다. 이제 예전만큼 쉽게 펜타킬을 쓸어담기는 힘들 것입니다.",
            "stats": "Q 처형 기준치: 225 스택 ➔ 275 스택"
        },
        {
            "title": "서포터 아이템 골드 수급 하향",
            "type": "너프",
            "isHot": True,
            "description": "서포터 아이템의 골드 수급량이 줄어들어 시야 장악 타이밍이 늦어집니다. 바텀 라인전의 스노우볼 속도에 큰 영향을 미칠 핵심 패치입니다.",
            "stats": "퀘스트 완료 골드 요구치 증가"
        }
    ],
    "14.5 패치": [
        {
            "title": "트위스티드 페이트 - AD 트페의 몰락",
            "type": "너프",
            "isHot": True,
            "description": "AD 트페가 협곡 생태계를 파괴하던 시대가 막을 내렸습니다. 핵심 데미지 계수가 크게 깎였습니다.",
            "stats": "E 스킬 추가 공격력 계수: 75% ➔ 50%"
        },
        {
            "title": "렉사이 - 브루저로 완벽한 포지션 변경",
            "type": "버프",
            "isHot": False,
            "description": "암살자에서 전사(브루저)로 확실히 자리 잡을 수 있도록 체력 회복과 유틸성이 대폭 상향되었습니다.",
            "stats": "W(돌출) 에어본 범위 증가, 패시브 체력 회복량 증가"
        }
    ],
    "14.4 패치": [
        {
            "title": "아우렐리온 솔 - 협곡의 재앙",
            "type": "버프",
            "isHot": True,
            "description": "Q 스킬의 마나 소모량이 줄어들고 스택 쌓기가 너무 쉬워지면서, 후반 왕귀 타이밍이 비정상적으로 앞당겨졌던 논란의 패치입니다.",
            "stats": "Q 스킬 초당 마나 소모량 감소"
        }
    ]
}

# 4. 사용자가 패치 버전을 선택할 수 있는 드롭다운 메뉴
selected_patch = st.selectbox(
    "📌 확인하고 싶은 패치 버전을 선택하세요:", 
    list(patch_history.keys())
)

st.subheader(f"💡 {selected_patch} 주요 이슈")
st.markdown("<br>", unsafe_allow_html=True)

# 5. 선택된 패치의 데이터만 화면에 렌더링
for item in patch_history[selected_patch]:
    with st.container():
        # 버프/너프에 따른 색상 및 텍스트 설정
        if item["type"] == "버프":
            type_badge = "🔵 **버프**"
        else:
            type_badge = "🔴 **너프**"
            
        hot_badge = "🔥 **HOT 이슈**" if item["isHot"] else ""
        
        # 컨텐츠 출력
        st.markdown(f"### {item['title']}")
        st.markdown(f"{type_badge} &nbsp;&nbsp; {hot_badge}")
        st.write(item["description"])
        st.info(f"**수치 변화:** {item['stats']}")
        st.divider() # 각 항목 사이에 얇은 선을 그어 가독성을 높입니다.
