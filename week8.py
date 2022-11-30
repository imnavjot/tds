# -*- coding: utf-8 -*-
"""WEEK8.ipynb"""


import streamlit as st
import decimal
from decimal import Decimal

st.title("Subtraction App using Streamlit")
 
# creates a horizontal line
st.write("---")
 
# input 1
num1 = st.number_input(label="Enter first number")
 
# input 2
num2 = st.number_input(label="Enter second number")
 
 
ans = 0
 
def calculate():
  ans = num1 - num2
  st.success(f"Answer = {ansa:.4f}")
 
if st.button("Subtract"):
    calculate()
