import streamlit as st
import datetime
import pandas as pd

# 1. Input Widgets
## 1. Text Input
name = st.text_input(label='Nama lengkap', value='')
st.write('Nama: ', name)

## 2. Text Area
## It uses for multiline text
text = st.text_area('Feedback')
st.write('Feedback: ', text)

## 3. Number Input
number = st.number_input(label='Umur')
st.write('Umur: ', int(number), ' tahun')

## 4. Date Input
date = st.date_input(label='Tanggal lahir', min_value=datetime.date(1900, 1, 1))
st.write('Tanggal lahir:', date)

## 5. File Uploader
uploaded_file = st.file_uploader('Choose a CSV file')
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

## 6. Camera Input
picture = st.camera_input('Take a picture')
if picture:
    st.image(picture)

# 2. Button Widgets
## 1. Button
if st.button('Say hello'):
    st.write('Hello there')

## 2. Checkbox
agree = st.checkbox('I agree')
if agree:
    st.write('Welcome to MyApp  ')

## 3. Radio button
genre = st.radio(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary'),
    horizontal=False
)

## 4. Select box
genre = st.selectbox(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

## 5. Multiselect
genre = st.multiselect(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

## 6. Slider
values = st.slider(
    label='Select a range of values',
    min_value=0, max_value=100, value=(0, 100))
st.write('Values:', values)