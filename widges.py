import streamlit as st

st.title("Widges")

if st.button('Subscribe'):
    st.write('like this video too')

name = st.text_input("Name")
st.write(name)

address = st.text_area("Enter your address")
st.write(address)

st.date_input("Ente a date")
st.time_input("Enter a time")

if st.checkbox("You accept T&C",value=False):
    st.write('Thank you')

v1 = st.radio('colour',['g','r','b'], index=1)
v2 = st.selectbox('colour',['g','r','b'], index=0)

st.write(v1,v2)

v3 = st.multiselect('colour',['g','r','b'])
st.write(v3)

st.slider("age",min_value=10,max_value=80,value=30,step=10)

st.number_input("numbers",min_value=10.0,max_value=80.0,value=30.0,step=10.0)

img = st.file_uploader("Upload a file")
st.image(img)
