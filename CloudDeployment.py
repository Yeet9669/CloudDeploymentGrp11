# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:11:46 2024

@author: Computer
"""

import streamlit as st
st.title("Finals Exam: Cloud Deployment")

file = st.file_uploader("Upload File Here", type = ["png","jpeg","jpg"])
if file is not None: 
    st.image(file)