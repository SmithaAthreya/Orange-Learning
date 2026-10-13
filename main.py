#Program 9 Linear Regression (advanced learners)
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
#load the data file csv file
df=pd.read_csv("C://Users//A//Desktop//data.csv")
print(df)
#split data into features (x) and Target(y)
X=df[['HoursStudied']]
y=df['ExamScore']
#Train-Test split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
#Train the model
model=LinearRegression()
model.fit(X_train,y_train)
#Streamlit user interface
st.title("Exam predictor")
st.write("Enter hours studied to predict the exam score")
#user input
hours=st.number_input("Hours studies:",min_value=0.0,step=0.1)
if st.button("Predict Score"):
    predicted_score=model,predict([[hours]])[0]
    st.success(f"Predicted Score:{predicted_score: .2f}")
st.write("### Sample Training data")
st.dataframe(df)
