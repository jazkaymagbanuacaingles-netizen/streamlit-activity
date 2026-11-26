import streamlit as st

st.set_page_config(page_title="My Profile", page_icon="👤")

col1, col2 = st.columns([1, 2])

with col1:
    st.image("jazkay.jpg.png", width=200)

with col2:
    st.title("Jazkay Magbanua Caingles")
    st.write("Student | Aspiring Developer")

st.header("About Me")
st.write("A Mechanical Engineering student who enjoys learning new things and working hard to achieve my goals..")

st.header("Skills")
st.write("- Python\n- Streamlit\n- GitHub")

st.header("Contact")
st.write("Email: jazkaymagbanuacaingles@gmail.com")
