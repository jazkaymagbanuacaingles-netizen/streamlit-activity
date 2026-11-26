import streamlit as st

st.set_page_config(page_title="Jazkay | Mechanical Engineering", page_icon="⚙️", layout="wide")

st.markdown("""
<style>
.hero {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    padding: 40px;
    border-radius: 20px;
    color: white;
}
.hero h1 { color: #ffffff; margin-bottom: 4px; }
.hero p { color: #cfe8ef; font-size: 18px; margin: 4px 0; }
.card {
    background: #f4f8fa;
    border-left: 6px solid #2c5364;
    padding: 14px 18px;
    border-radius: 10px;
    margin-bottom: 10px;
    color: #1b2a33;
}
.tag {
    display: inline-block;
    background: #2c5364;
    color: white;
    padding: 6px 14px;
    border-radius: 20px;
    margin: 4px;
    font-size: 15px;
}
</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
col1, col2 = st.columns([1, 3])

with col1:
    st.image("jazkay.jpg.png", use_container_width=True)

with col2:
    st.markdown("""
    <div class="hero">
        <h1>⚙️ Jazkay Magbanua Caingles</h1>
        <p>Mechanical Engineering Student</p>
        <p>Designing ideas into reality, one drawing at a time.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ---------- TABS ----------
tab1, tab2, tab3 = st.tabs(["👩‍🎓 About Me", "🛠️ Skills", "📬 Contact"])

with tab1:
    st.subheader("Hello, I'm Jazkay!")
    st.markdown(
        '<div class="card">A Mechanical Engineering student who enjoys learning new things '
        'and working hard to achieve my goals.</div>',
        unsafe_allow_html=True,
    )
    c1, c2, c3 = st.columns(3)
    c1.metric("Course", "Bachelor of Science in Mechanical Engineering.")
    c2.metric("Favorite Tool", "SolidWorks")
    c3.metric("Goal", "Future RME")

with tab2:
    st.subheader("Technical Skills")
    technical = {
        "CAD (SolidWorks)": 80,
        "Technical Drawing": 85,
        "Basic Mechanical Knowledge": 75,
    }
    for skill, level in technical.items():
        st.write(f"**{skill}**")
        st.progress(level)

    st.subheader("Soft Skills")
    soft = ["Problem-solving", "Teamwork and Collaboration", "Communication", "Time Management"]
    tags = "".join(f'<span class="tag">{s}</span>' for s in soft)
    st.markdown(tags, unsafe_allow_html=True)

with tab3:
    st.subheader("Let's connect!")
    st.markdown('<div class="card">📧 jazkaymagbanuacaingles@gmail.com</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="card">💻 GitHub: '
        '<a href="https://github.com/jazkaymagbanuacaingles-netizen">jazkaymagbanuacaingles-netizen</a></div>',
        unsafe_allow_html=True,
    )
    if st.button("🎉 Click for a surprise"):
        st.balloons()
        st.success("Thanks for visiting my profile!")

st.divider()
st.caption("Built with Python and Streamlit • Deployed on Streamlit Community Cloud")
