import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Write
## 1. Show basic web app
st.write(
    """
    ## My first app
    Hello, para calon praktisi data masa depan!
    """
)

## 2. Show dataframe
st.write(pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
}))

## 3. Same as write()
st.markdown(
    """
    ## My first app
    Hello, para calon praktisi data masa depan!
    """
)

## 4. Show title
st.title('Belajar Analisis Data')

## 5. Show sub-header
st.subheader('Pengembangan Dashboard')

## 6. Show caption. It usually uses for small text
st.caption('Copyright (c) 2023')

## 7. Show code
code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language='python')

## 8. Show (normal) text
st.text('Halo, calon praktisi data masa depan.')

## 9. Show latex (mathematical expression)
st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")

# 2. Data Display
## 1. Show dataframe
df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})

st.dataframe(data=df, width=500, height=150)

## 2. Show static table
df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
st.table(data=df)

## 3. Show metric
st.metric(label="Temperature", value="28 °C", delta="1.2 °C")

## 4. Show JSON
st.json({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})

# 3. Chart
x = np.random.normal(15, 5, 250)
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)