import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

st.title("Welcome to Student Analysis Project")
st.set_page_config(page_title="Student Project")

with st.sidebar:
 uploaded_file= st.file_uploader(label="StackCircle",type=["csv"])
 selected=option_menu(menu_title="Menu",
                      options=["Raw Data","Student Result","Subject Analysis","Pass/Fail","Search","Topper"],  
                      icons=["table","grid","people","table","search ","trophy"]
                      
                      )

if uploaded_file:
  df=pd.read_csv(uploaded_file)
  if selected=="Raw Data":   
      st.dataframe(df)
  elif selected=="Student Result":
      total=df.groupby("Name")["Marks"].sum()
      average=df.groupby("Name")["Marks"].mean()
      st.dataframe({"Total":total,"Average":average})
  elif selected=="Subject Analysis":
      average=df.groupby("Subject")["Marks"].mean()
      st.dataframe({"Subject Avg":average})
  elif selected=="Pass/Fail":
     min_marks=st.slider(label="Please select min marks",min_value=1,max_value=100,value=40)
     df["Result"]=df["Marks"].apply(
        lambda x: "Pass" if x>=min_marks else "Fail"
     )
     st.dataframe(df)
  elif selected=="Search":
     text=st.text_input(label="Enter Student Name")
     filtered_data=df[df["Name"].str.lower()==text.lower()]
     st.dataframe(filtered_data)
  elif selected=="Topper":
     n=st.number_input(label="How many toppers you want",min_value=1,max_value=len(df))
     filtered_data=df.groupby("Name")["Marks"].sum().sort_values(ascending=False)
     st.dataframe(filtered_data.head(n))
else:
 st.error("Please upload file")



