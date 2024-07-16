import time
import numpy as np
import pandas as pd
import streamlit as st

_LOREM_IPSUM = """
공덕현 '나' 에 대한 소개
"""

Q_like = '''
Q.내가 좋아하는 게임은?'''

A_like = '''
A.롤'''

Q_music = '''
Q.내가 좋아하는 음악은? '''

A_music = '''
시간을 거슬러'''


def stream_data():
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)
    for word in Q_like.split(" "):
        yield word + "\n"
        time.sleep(0.02)
    for word in A_like.split("ln"):
        yield word + "\n"
        time.sleep(0.02)
    for word in Q_music.split(" "):
        yield word + "\n"
        time.sleep(0.02)
    for word in A_music.split(" "):
        yield word + "\n"
        time.sleep(0.02)

if st.button("Stream data"):
    st.write_stream(stream_data)

import streamlit as st

st.numname = st.text_input("학번이름 입력하세요", "1101 공덕현")
if st.button("Next"):
    st.switch_page("pages/1_Button.py")


