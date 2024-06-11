import streamlit as st
#import panda as pd

name=st.text_input("enter your name:")
fname=st.text_input("enter your father name:")
adr=st.text_area("enter your text....")
classdata= st.selectbox("enter your class:",(1,2,3,4,5,6))

button=st.button("Done")
if button:
    st.markdown(f"""
    Name : {name}
    Father name : {fname}
    address : {adr}
    class : {classdata}""")