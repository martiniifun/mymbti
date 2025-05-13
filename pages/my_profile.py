import streamlit as st
import pandas as pd
import altair as alt
from datetime import date

# 👉 페이지 기본 설정
st.set_page_config(
    page_title="Nomad Coder – 프로필",
    page_icon="💻",
    layout="wide",
)

# =============== 사이드바 ===============
with st.sidebar:
    st.title("📬 Contact")
    st.markdown(
        """
        - ✉️ **Email**: you@example.com  
        - 🐙 **GitHub**: [github.com/you](https://github.com/you)  
        - 💼 **LinkedIn**: [linkedin.com/in/you](https://linkedin.com/in/you)  
        - 📝 **Blog**: [nomadlog.dev](https://nomadlog.dev)  
        """
    )

    st.write("---")
    st.markdown("### 🛠️ Tech Skills")
    skills = {
        "Python": 95,
        "JavaScript/TypeScript": 85,
        "Go": 70,
        "Rust": 60,
        "SQL": 80,
        "Docker/K8s": 75,
    }
    for skill, pct in skills.items():
        st.text(f"{skill} {pct}%")
        st.progress(pct / 100)

# =============== 히어로 섹션 ===============
col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://picsum.photos/300", width=250)  # 👉 프로필 사진 자리 (임시)
with col2:
    st.markdown("## 👋 안녕! 나는 **Nomad Coder** 🚀")
    st.write(
        """
        클라우드와 커피를 사랑하는 **프로그래머 & 디지털 노마드**.  
        글로벌 팀과 협업하며 **DevOps, 데이터 엔지니어링, AI 서비스**를 구축해왔어.  
        내가 뛰어든 문제는 늘 **'자동화'와 '확장성'**으로 해결하지! 🔧🔥
        """
    )
    st.download_button("📄 Download Résumé (PDF)", "(coming soon)", disabled=True)

st.write("---")

# =============== KPI Metrics ===============
st.markdown("### 🚀 Key Metrics")
kpi1, kpi2, kpi3 = st.columns(3)
with kpi1:
    st.metric("🏆 Years Experience", "8+", "↗︎")
with kpi2:
    st.metric("🌍 Countries Coded In", "12", "")
with kpi3:
    st.metric("💚 OSS Contributions", "350+", "↗︎ 12%")

st.write("---")

# =============== 커리어 타임라인 ===============
st.markdown("### 🗂️ Career Timeline")

timeline_df = pd.DataFrame(
    {
        "Role": [
            "Senior Backend Engineer",
            "Full‑stack Dev",
            "Data Engineer",
            "Freelance Nomad",
        ],
        "Start": [2018, 2020, 2022, 2024],
        "End": [2020, 2022, 2024, date.today().year],
    }
)

timeline_chart = (
    alt.Chart(timeline_df)
    .mark_bar()
    .encode(
        x="Start:O",
        x2="End:O",
        y=alt.Y("Role:N", sort="-x"),
        color="Role:N",
        tooltip=["Role", "Start", "End"],
    )
    .properties(height=200)
)

st.altair_chart(timeline_chart, use_container_width=True)

# =============== 기술 스택 차트 ===============
st.markdown("### 🧰 Tech Stack Proficiency")
stack_df = pd.DataFrame({"Stack": list(skills.keys()), "Proficiency": list(skills.values())})
stack_chart = (
    alt.Chart(stack_df)
    .mark_bar()
    .encode(
        y=alt.Y("Stack:N", sort="-x"),
        x="Proficiency:Q",
        color="Stack:N",
        tooltip=["Proficiency"],
    )
    .properties(height=250)
)

st.altair_chart(stack_chart, use_container_width=True)

# =============== 프로젝트 쇼케이스 ===============
st.markdown("### 💼 Featured Projects")
proj1, proj2, proj3 = st.columns(3)
with proj1:
    st.image("https://picsum.photos/200?grayscale")
    st.markdown("#### 📊 **AI‑Driven BI Dashboard**")
    st.caption("파이썬 + FastAPI + React")
with proj2:
    st.image("https://picsum.photos/seed/pic2/200")
    st.markdown("#### 🛳️ **K8s Fleet Manager**")
    st.caption("Golang + gRPC")
with proj3:
    st.image("https://picsum.photos/seed/pic3/200")
    st.markdown("#### 🤖 **ChatOps Assistant**")
    st.caption("LangChain + OpenAI")

st.write("---")

# =============== 자격증 뱃지 ===============
st.markdown("### 📜 Certifications & Badges")
cols = st.columns(6)
badges = ["aws", "gcp", "ckad", "cpp", "pytorch", "scrum"]
for col, badge in zip(cols, badges):
    col.image(f"https://img.shields.io/badge/{badge}-success?style=for-the-badge")

st.write("---")

# =============== 푸터 ===============
st.caption("© 2025 Nomad Coder · Made with Streamlit ❤️")
