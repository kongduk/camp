import streamlit as st

answer = st.radio(
    "나에대한 설명으로 옳지않은 것은?",
    ["나는 중1때부터 T1팬이었다.", "내가 불수있는 악기중에는 소금이있다.", "나의 생일은 3월달이다.", "내가 가장 오래한 게임은 롤이다.", "나는 운동중 농구를 가장 좋아한다."],
    index=None,
)
if answer == "내가 가장 오래한 게임은 롤이다." :
    st.score +=50
else :
    st.score +=0

if st.button("Next"):
    st.switch_page("pages/3_result.py")


