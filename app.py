import streamlit as st

st.title('Hello Streamlit!')
st.write('This is my first Streamlit app.')

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
st.pyplot(fig)
