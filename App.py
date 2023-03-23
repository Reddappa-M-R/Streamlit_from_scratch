import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plotly import graph_objs as go
from sklearn.linear_model import LinearRegression

data = pd.read_csv("Salary_Data.csv")

x = np.array(data["YearsExperience"]).reshape(-1,1)
lr = LinearRegression()
lr.fit(x,np.array(data["Salary"]))

st.title("Salary Predicter")

nav = st.sidebar.radio("Navigation", ["Home","Prediction","Contribute"])
if nav == "Home":
    st.image("Sal.jfif", width = 500)
    if st.checkbox("Show table"):
        st.table(data)

    val = st.slider("Filter data using years",0,20)
    data=data.loc[data["YearsExperience"]>=val]
    
    graph = st.selectbox("What kind of graph ?", ["Non-Interactive","Interactive"])
    if graph == "Non-Interactive":
        fig, ax = plt.subplots()
        ax.scatter(data['YearsExperience'],data['Salary'])
        plt.title('Scatter')
        plt.ylim(0)
        plt.xlabel("Years of Experience")
        plt.ylabel("Salary")
        st.pyplot(fig)

    if graph == "Interactive":
        layout = go.Layout(
            xaxis = dict(range=[0,16]),
            yaxis = dict(range=[0,100000])

        )
        fig = go.Figure(data=go.Scatter(x=data["YearsExperience"],y=data["Salary"],mode="markers"), layout = layout)
        st.plotly_chart(fig)




if nav == "Prediction":
    st.header("Know your Salary")
    val = st.number_input("Enter your exp",0.00,20.00,step=0.5)
    val = np.array(val).reshape(1,-1)
    pred = lr.predict(val)[0]
    if st.button("Predict"):
        st.success(f"Your predicted salary is {round(pred)}")


if nav == "Contribute":
    st.header("Contribute to our dataset")
    ex = st.number_input("Enter your experience",0.0,20.0)
    sal = st.number_input("Enter your salary",0.0, 100000.0,step=1000.0)
    if st.button("Submit"):
        #to_add = {"YearsExperience":ex,"Salary":sal}
        #to_add = pd.DataFrame(to_add)
        #to_add.to_csv("Data\\Salary_Data",mode=a,header =False,index=False)
        st.success("Submitted")

