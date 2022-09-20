import streamlit as st
import pandas as pd
import numpy as np

st.title('LawDiktat Tool')

st.header('FAQs')

def answer(question_text, answer_vid, answer_text='answer'):
    vid = open(answer_vid, 'rb')
    vid_bytes = vid.read()

    with st.expander(question_text):
        col1, col2 = st.columns(2)
        col1.write(answer_text)
        col2.video(vid_bytes)


faqs = {'Question1':('answer1.mp4','This is the answer to question 1. Thank you for being patient.'),
        'Question2':('answer2.mp4','Now I am answering the question 2. I hope your query is resolved.'),
        'Question3':('answer3.mp4','This is a longer sentence to test my abilities. I hope I sound natural, just like a human. Answer 3.')}

for ques in faqs:
    answer(ques,faqs[ques][0],faqs[ques][1])