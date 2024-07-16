import streamlit as st

st.score = 0

@st.experimental_dialog("문제")
def vote(item):
    st.write(f"내가 가장 좋아하는 T1선수는?")
    st.reason = st.text_input("답 :")

    if st.button("제출하기"):
        st.switch_page("pages/2_Print.py")
    
if "vote" not in st.session_state:
    st.write("문제")
    if st.button("문제풀기"):
        vote("문제풀기")
        
if st.reason == "구마유시" :
    st.score += 50
else :
    st.score += 0