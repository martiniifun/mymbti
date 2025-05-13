import streamlit as st

"""
간단 MBTI 추정 퀴즈 – Streamlit 예시
Run:
    streamlit run mbti_quiz_app.py
"""

st.set_page_config(page_title="MBTI Guess Quiz", page_icon="🧠", layout="centered")

st.title("🧠 MBTI 추정 퀴즈")
st.caption("몇 가지 쉽고 재미있는 질문으로 너의 MBTI 를 추정해볼게!")

# ----------------- 질문 정의 -----------------
QUESTIONS = [
    # E / I
    {
        "text": "친구들과 시간을 보내면 에너지가 어떻게 느껴져?",
        "choices": {
            "⚡ 완전 충전돼!": "E",
            "🔋 살짝 방전돼, 혼자 쉬어야 회복": "I",
        },
        "dim": "E",
    },
    {
        "text": "낯선 모임에 갔을 때 나는…",
        "choices": {
            "🎤 먼저 말 걸고 분위기를 리드해": "E",
            "👀 먼저 관찰하고 천천히 적응해": "I",
        },
        "dim": "E",
    },
    # S / N
    {
        "text": "프로젝트 계획할 때 나는 주로…",
        "choices": {
            "📋 구체적이고 현실적인 리스트부터!": "S",
            "🌈 큰 그림과 가능성부터 상상해": "N",
        },
        "dim": "S",
    },
    {
        "text": "설명서를 볼 때 내 스타일은?",
        "choices": {
            "📝 필요한 부분만 빠르게 찾는다": "S",
            "🌀 전체 맥락을 이해하려고 처음부터 끝까지 본다": "N",
        },
        "dim": "S",
    },
    # T / F
    {
        "text": "갈등 상황에서 내 결정 기준은…",
        "choices": {
            "⚖️ 논리적인 이유와 사실": "T",
            "💖 사람들의 감정과 조화": "F",
        },
        "dim": "T",
    },
    {
        "text": "칭찬을 받을 때 더 뿌듯한 말은?",
        "choices": {
            "🧠 '정말 똑똑하네!'": "T",
            "🤗 '정말 배려심 있네!'": "F",
        },
        "dim": "T",
    },
    # J / P
    {
        "text": "여행 계획은 어떻게 해?",
        "choices": {
            "📅 일정표를 미리 꼼꼼히 짜두는 편": "J",
            "🎒 즉흥적으로 현지에서 결정": "P",
        },
        "dim": "J",
    },
    {
        "text": "마감이 다가오면 나는…",
        "choices": {
            "✅ 미리미리 완료하고 여유": "J",
            "⏰ 데드라인이 있어야 집중돼": "P",
        },
        "dim": "J",
    },
]

# ----------------- 사용자 입력 -----------------
responses = {}
with st.form("quiz_form"):
    for idx, q in enumerate(QUESTIONS):
        responses[q["dim"] + str(idx)] = st.radio(
            f"**{idx + 1}. {q['text']}**",
            list(q["choices"].keys()),
            key=f"q{idx}",
        )

    submitted = st.form_submit_button("✨ 결과 보기")

# ----------------- 결과 계산 -----------------
if submitted:
    # 초기 점수
    score = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}

    for idx, q in enumerate(QUESTIONS):
        answer_text = responses[q["dim"] + str(idx)]
        trait = q["choices"][answer_text]
        score[trait] += 1

    # 각 차원 결정
    result = (
        ("E" if score["E"] >= score["I"] else "I") +
        ("S" if score["S"] >= score["N"] else "N") +
        ("T" if score["T"] >= score["F"] else "F") +
        ("J" if score["J"] >= score["P"] else "P")
    )

    st.success(f"🎉 너의 MBTI는 **{result}** (으)로 추정돼!")

    # 세부 점수 시각화
    st.write("### 세부 점수")
    traits = ["E", "I", "S", "N", "T", "F", "J", "P"]
    cols = st.columns(4)
    for i, trait in enumerate(traits):
        with cols[i % 4]:
            st.progress(score[trait] / 2, text=f"{trait} {score[trait]} / 2")

    st.write("---")
    st.info("👉 결과는 재미로만 보자! 정확한 MBTI 검사는 전문 검사를 추천해.")

st.caption("© 2025 Nomad Coder • Streamlit Demo")
