import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Jazkay | Mechanical Engineering", page_icon="⚙️", layout="wide")

# ---------- STYLE ----------
st.markdown("""
<style>
.hero {
background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
padding: 36px; border-radius: 20px; color: white;
}
.hero h1 { color: #ffffff; margin-bottom: 4px; }
.hero p { color: #cfe8ef; font-size: 18px; margin: 4px 0; }
.card {
background: #f4f8fa; border-left: 6px solid #2c5364;
padding: 14px 18px; border-radius: 10px; margin-bottom: 10px; color: #1b2a33;
}
.tag {
display: inline-block; background: #2c5364; color: white;
padding: 6px 14px; border-radius: 20px; margin: 4px; font-size: 15px;
}
</style>
""", unsafe_allow_html=True)

EMAIL = "jazkaymagbanuacaingles@gmail.com"
GITHUB = "https://github.com/jazkaymagbanuacaingles-netizen"

# ---------- SIDEBAR ----------
with st.sidebar:
    st.image("jazkay.jpg.png", width=200)
    st.title("Jazkay M. Caingles")
    st.caption("Bachelor of Science in Mechanical Engineering")
    st.divider()
    st.link_button("💻 My GitHub", GITHUB)
    st.link_button("📧 Email Me", f"mailto:{EMAIL}")
    st.divider()

    resume = f"""JAZKAY MAGBANUA CAINGLES
Bachelor of Science in Mechanical Engineering
Email: {EMAIL}

CAREER GOALS
- RME, PME, CPM, COSH

SKILLS
- Problem-solving
- Basic Mechanical Knowledge
- CAD (SolidWorks)
- Technical Drawing
- Teamwork and Collaboration
- Communication
- Time Management
"""
    st.download_button("📄 Download Resume", resume, file_name="Jazkay_Resume.txt")

# ---------- HERO ----------
st.markdown("""
<div class="hero">
<h1>⚙️ Jazkay Magbanua Caingles</h1>
<p>Bachelor of Science in Mechanical Engineering</p>
<p>Driven by passion, powered by engineering.</p>
</div>
""", unsafe_allow_html=True)
st.write("")

# ---------- TABS ----------
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    ["👩‍🎓 About", "🛠️ Skills", "🧮 Engineering Tools", "🖼️ Gallery", "📁 Projects", "📬 Contact"]
)

# ===== ABOUT =====
with tab1:
    st.subheader("Hello, I'm Jazkay!")
    st.markdown(
        '<div class="card">A Mechanical Engineering student who enjoys learning '
        'new things and working hard to achieve my goals.</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="card">🎓 <b>Course:</b> Bachelor of Science in Mechanical Engineering</div>',
        unsafe_allow_html=True,
    )

    st.subheader("🎯 Career Goals")
    st.write("Future **RME, PME, CPM, COSH**")
    goals = ["RME", "PME", "CPM", "COSH"]
    st.markdown("".join(f'<span class="tag">{g}</span>' for g in goals), unsafe_allow_html=True)

    st.write("")
    c1, c2 = st.columns(2)
    c1.metric("Favorite Tool", "SolidWorks")
    c2.metric("Goal", "Future RME")

    st.subheader("🎓 My Journey")
    st.markdown("""
- **Now:** Studying Mechanical Engineering and building my first web apps
- **Learning:** CAD modeling, technical drawing, and Python
- **Next:** Join engineering projects and internships
""")

# ===== SKILLS =====
with tab2:
    left, right = st.columns(2)

    with left:
        st.subheader("Technical Skills")
        technical = {
            "CAD (SolidWorks)": 80,
            "Technical Drawing": 85,
            "Basic Mechanical Knowledge": 75,
            "Python / Streamlit": 50,
        }
        for skill, level in technical.items():
            st.write(f"**{skill}**")
            st.progress(level)

    with right:
        st.subheader("Skill Chart")
        df = pd.DataFrame({"Skill": list(technical.keys()), "Level": list(technical.values())})
        st.bar_chart(df.set_index("Skill"))

    st.subheader("Soft Skills")
    soft = ["Problem-solving", "Teamwork and Collaboration", "Communication", "Time Management"]
    st.markdown("".join(f'<span class="tag">{s}</span>' for s in soft), unsafe_allow_html=True)

# ===== ENGINEERING TOOLS =====
with tab3:
    st.subheader("🧮 Interactive Engineering Tools")
    st.write("Two calculators I built with Python. Change the numbers and watch the results update.")

    tool = st.radio("Choose a tool", ["Beam Deflection", "Gear Ratio"], horizontal=True)

    if tool == "Beam Deflection":
        st.markdown("**Simply supported beam with a load at the center (rectangular cross-section)**")
        materials = {"Steel": 200, "Aluminum": 69, "Pine Wood": 10, "Concrete": 30}  # E in GPa

        a, b_, c = st.columns(3)
        with a:
            P = st.number_input("Load P (N)", 1.0, 100000.0, 1000.0, step=100.0)
            L = st.number_input("Span L (m)", 0.1, 20.0, 2.0, step=0.1)
        with b_:
            width = st.number_input("Width b (mm)", 5.0, 500.0, 50.0, step=5.0)
            height = st.number_input("Height h (mm)", 5.0, 500.0, 100.0, step=5.0)
        with c:
            mat = st.selectbox("Material", list(materials.keys()))

        E = materials[mat] * 1e9                      # Pa
        I = (width / 1000) * (height / 1000) ** 3 / 12  # m^4
        delta = P * L**3 / (48 * E * I)               # m
        M = P * L / 4                                 # N·m
        sigma = M * (height / 2000) / I / 1e6         # MPa

        m1, m2, m3 = st.columns(3)
        m1.metric("Max Deflection", f"{delta * 1000:.2f} mm")
        m2.metric("Max Bending Moment", f"{M:.0f} N·m")
import pandas as pd
import numpy as np

st.set_page_config(page_title="Jazkay | Mechanical Engineering", page_icon="⚙️", layout="wide")

# ---------- STYLE ----------
st.markdown("""
<style>
.hero {
background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
padding: 36px; border-radius: 20px; color: white;
}
.hero h1 { color: #ffffff; margin-bottom: 4px; }
.hero p { color: #cfe8ef; font-size: 18px; margin: 4px 0; }
.card {
background: #f4f8fa; border-left: 6px solid #2c5364;
padding: 14px 18px; border-radius: 10px; margin-bottom: 10px; color: #1b2a33;
}
.tag {
display: inline-block; background: #2c5364; color: white;
padding: 6px 14px; border-radius: 20px; margin: 4px; font-size: 15px;
}
</style>
""", unsafe_allow_html=True)

EMAIL = "jazkaymagbanuacaingles@gmail.com"
GITHUB = "https://github.com/jazkaymagbanuacaingles-netizen"

# ---------- SIDEBAR ----------
with st.sidebar:
    st.image("jazkay.jpg.png", width=200)
    st.title("Jazkay M. Caingles")
    st.caption("Mechanical Engineering Student")
    st.divider()
    st.link_button("💻 My GitHub", GITHUB)
    st.link_button("📧 Email Me", f"mailto:{EMAIL}")
    st.divider()

    resume = f"""JAZKAY MAGBANUA CAINGLES
Mechanical Engineering Student
Email: {EMAIL}

SKILLS
- Problem-solving
- Basic Mechanical Knowledge
- CAD (SolidWorks)
- Technical Drawing
- Teamwork and Collaboration
- Communication
- Time Management
"""
    st.download_button(
    "📄 Download Resume",
    resume,
    file_name="Jazkay_Resume.txt",
    key="download_resume_btn"
)

# ---------- HERO ----------
st.markdown("""
<div class="hero">
<h1>⚙️ Jazkay Magbanua Caingles</h1>
<p>Mechanical Engineering Student</p>
<p>Designing ideas into reality, one drawing at a time.</p>
</div>
""", unsafe_allow_html=True)
st.write("")

# ---------- TABS ----------
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["👩‍🎓 About", "🛠️ Skills", "🧮 Engineering Tools", "📁 Projects", "📬 Contact"]
)

# ===== ABOUT =====
with tab1:
    st.subheader("Hello, I'm Jazkay!")
    st.markdown(
        '<div class="card">A Mechanical Engineering student who enjoys learning '
        'new things and working hard to achieve my goals.</div>',
        unsafe_allow_html=True,
    )
    c1, c2, c3 = st.columns(3)
    c1.metric("Course", "BS Mechanical Eng.")
    c2.metric("Favorite Tool", "SolidWorks")
    c3.metric("Goal", "Future Engineer")

    st.subheader("🎓 My Journey")
    st.markdown("""
- **Now:** Studying Mechanical Engineering and building my first web apps
- **Learning:** CAD modeling, technical drawing, and Python
- **Next:** Join engineering projects and internships
""")

# ===== SKILLS =====
with tab2:
    left, right = st.columns(2)

    with left:
        st.subheader("Technical Skills")
        technical = {
            "CAD (SolidWorks)": 80,
            "Technical Drawing": 85,
            "Basic Mechanical Knowledge": 75,
            "Python / Streamlit": 50,
        }
        for skill, level in technical.items():
            st.write(f"**{skill}**")
            st.progress(level)

    with right:
        st.subheader("Skill Chart")
        df = pd.DataFrame({"Skill": list(technical.keys()), "Level": list(technical.values())})
        st.bar_chart(df.set_index("Skill"))

    st.subheader("Soft Skills")
    soft = ["Problem-solving", "Teamwork and Collaboration", "Communication", "Time Management"]
    st.markdown("".join(f'<span class="tag">{s}</span>' for s in soft), unsafe_allow_html=True)

# ===== ENGINEERING TOOLS =====
with tab3:
    st.subheader("🧮 Interactive Engineering Tools")
    st.write("Two calculators I built with Python. Change the numbers and watch the results update.")

    tool = st.radio("Choose a tool", ["Beam Deflection", "Gear Ratio"], horizontal=True)

    if tool == "Beam Deflection":
        st.markdown("**Simply supported beam with a load at the center (rectangular cross-section)**")
        materials = {"Steel": 200, "Aluminum": 69, "Pine Wood": 10, "Concrete": 30}  # E in GPa

        a, b_, c = st.columns(3)
        with a:
            P = st.number_input("Load P (N)", 1.0, 100000.0, 1000.0, step=100.0)
            L = st.number_input("Span L (m)", 0.1, 20.0, 2.0, step=0.1)
        with b_:
            width = st.number_input("Width b (mm)", 5.0, 500.0, 50.0, step=5.0)
            height = st.number_input("Height h (mm)", 5.0, 500.0, 100.0, step=5.0)
        with c:
            mat = st.selectbox("Material", list(materials.keys()))

        E = materials[mat] * 1e9                      # Pa
        I = (width / 1000) * (height / 1000) ** 3 / 12  # m^4
        delta = P * L**3 / (48 * E * I)               # m
        M = P * L / 4                                 # N·m
        sigma = M * (height / 2000) / I / 1e6         # MPa

        m1, m2, m3 = st.columns(3)
        m1.metric("Max Deflection", f"{delta * 1000:.2f} mm")
        m2.metric("Max Bending Moment", f"{M:.0f} N·m")
        m3.metric("Max Bending Stress", f"{sigma:.1f} MPa")

        x = np.linspace(0, L, 100)
        xs = np.where(x <= L / 2, x, L - x)
        y = P * xs * (3 * L**2 - 4 * xs**2) / (48 * E * I)
        curve = pd.DataFrame({"Position (m)": x, "Deflection (mm)": -y * 1000}).set_index("Position (m)")
        st.line_chart(curve)

        with st.expander("📘 Formulas used"):
            st.latex(r"\delta_{max} = \frac{PL^3}{48EI}")
            st.latex(r"M_{max} = \frac{PL}{4}, \quad I = \frac{bh^3}{12}, \quad \sigma = \frac{Mc}{I}")

    else:
        st.markdown("**Simple gear pair**")
        a, b_, c = st.columns(3)
        with a:
            driver = st.number_input("Driver gear teeth", 5, 200, 20)
        with b_:
            driven = st.number_input("Driven gear teeth", 5, 200, 60)
        with c:
            rpm = st.number_input("Input speed (RPM)", 1, 10000, 1500)

        ratio = driven / driver
        m1, m2, m3 = st.columns(3)
        m1.metric("Gear Ratio", f"{ratio:.2f} : 1")
        m2.metric("Output Speed", f"{rpm / ratio:.0f} RPM")
        m3.metric("Torque Multiplier", f"{ratio:.2f}x")

        if ratio > 1:
            st.info("Speed reduction: the output turns slower but with more torque.")
        elif ratio < 1:
            st.info("Speed increase: the output turns faster but with less torque.")
        else:
            st.info("1:1 ratio: speed and torque stay the same.")

# ===== PROJECTS =====
with tab4:
    st.subheader("📁 Projects")
    with st.expander("🌐 Personal Profile Web App (this page!)", expanded=True):
        st.write("Built with Python and Streamlit, version controlled on GitHub, and deployed on Streamlit Community Cloud.")
        st.write("**Tools:** Python, Streamlit, GitHub, Codespaces")
    with st.expander("⚙️ SolidWorks Design Project"):
        st.write("Describe one of your CAD models or class projects here.")
        st.write("**Tools:** SolidWorks, Technical Drawing")
    with st.expander("🤝 Group Project"):
        st.write("Describe a team project and your role in it.")

# ===== CONTACT =====
with tab5:
    st.subheader("Let's connect!")
    st.markdown(f'<div class="card">📧 {EMAIL}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="card">💻 GitHub: <a href="{GITHUB}">{GITHUB}</a></div>', unsafe_allow_html=True)

    st.subheader("Leave a message")
    name = st.text_input("Your name")
    msg = st.text_area("Your message")
    if st.button("Send"):
        if name and msg:
            st.toast("Message received!", icon="✅")
            st.success(f"Thanks, {name}! Nice to meet you.")
        else:
            st.warning("Please enter your name and a message.")

    if st.button("🎉 Click for a surprise"):
        st.balloons()

st.divider()
st.caption("Built with Python and Streamlit • Deployed on Streamlit Community Cloud")
