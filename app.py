
import streamlit as st

st.set_page_config(page_title="SourceQR Helper", page_icon="🔎", layout="centered")

st.title("🔎 SourceQR 문구 & 정책 미리보기")

tab2, tab1 = st.tabs(["개인정보처리방침 미리보기", "sourceQR 문구 미리보기"])

with tab2:
    st.subheader("개인정보처리방침(privacy.html)")
    st.caption("아래에 파일을 업로드하거나, 자동으로 감지된 파일을 미리봅니다.")

    uploaded = st.file_uploader("privacy.html 업로드", type=["html", "htm"])
    html_content = None

    if uploaded is not None:
        html_content = uploaded.read().decode("utf-8", errors="ignore")
    else:
        # 샘플: /mnt/data/privacy.html 같은 경로를 자동 탐지
        default_paths = ["privacy.html", "/mnt/data/privacy.html", "./privacy.html"]
        for p in default_paths:
            try:
                with open(p, "r", encoding="utf-8") as f:
                    html_content = f.read()
                    st.info(f"자동으로 파일을 찾았습니다: {p}")
                    break
            except Exception:
                continue

    if html_content:
        st.components.v1.html(html_content, height=800, scrolling=True)
    else:
        st.warning("미리볼 HTML이 없습니다. 파일을 업로드해 주세요.")

with tab1:
    st.subheader("QR 앱 소개 문구 추천")
    st.caption("원문: “QR을 스캔하여 QR 내용을 읽는 앱”")

    tone = st.radio(
        "톤 & 스타일을 선택하세요",
        ["프로페셔널", "친절한/사용자 중심", "기술 지향", "보안 강조"],
        horizontal=True,
    )

    suggestions = {
        "프로페셔널": [
            "스마트 QR 인식 & 정보 확인 앱",
            "QR 스캔 기반 안전한 정보 열람 서비스",
            "실시간 QR 코드 판독 및 정보 제공 앱",
            "QR 인증 및 데이터 확인 솔루션",
            "신뢰할 수 있는 QR 코드 리더",
        ],
        "친절한/사용자 중심": [
            "찍고 바로 확인하는 똑똑한 QR 리더",
            "누구나 쉽게 쓰는 빠른 QR 스캐너",
            "한 번의 스캔으로 필요한 정보까지",
            "간편하게 스캔하고 안심하고 확인하세요",
            "가볍고 빠른 QR 코드 도우미",
        ],
        "기술 지향": [
            "온디바이스 실시간 QR 디코딩 & 컨텍스트 제공",
            "저지연 QR 판독과 메타데이터 분석",
            "정확한 QR 파싱과 결과 시각화",
            "멀티 포맷 QR/바코드 인식 엔진",
            "스캔 후 즉시 데이터 처리/출력",
        ],
        "보안 강조": [
            "QR 진위 확인과 안전한 정보 열람",
            "출처 검증 기반의 신뢰 가능한 QR 리더",
            "위험 링크 차단 및 안전 스캔",
            "오프라인에서도 개인정보 없는 안전 판독",
            "검증 가능한 QR 인증 뷰어",
        ],
    }

    selected = suggestions[tone]
    st.write("### 추천 문구")
    for i, s in enumerate(selected, start=1):
        st.write(f"{i}. {s}")

    st.divider()
    st.write("### 내 문구 다듬기")
    base = st.text_area(
        "초안을 붙여 넣으면 톤에 맞춰 다듬어 드립니다",
        "QR을 스캔하여 QR 내용을 읽는 앱",
    )
    if st.button("톤에 맞게 다듬기", type="primary"):
        # 간단한 톤 변환 규칙 (실제 모델 대체용)
        if tone == "프로페셔널":
            out = f"{base.replace('앱', '솔루션')} · 실시간 인식과 정확한 정보 제공"
        elif tone == "친절한/사용자 중심":
            out = f"한 번 찍고 바로 확인! {base.replace('앱', '도우미')}"
        elif tone == "기술 지향":
            out = f"온디바이스 디코딩 · 저지연 판독 · 정확한 결과 — {base}"
        else:
            out = f"출처 검증과 안전한 열람을 지원하는 {base}"
        st.success(out)
        st.download_button("문구 다운로드(.txt)", data=out, file_name="tagline.txt")
