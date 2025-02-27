import streamlit as st
import pandas as pd
import os
from io import BytesIO
st.set_page_config(page_title= "Data Sweeper" , layout='wide')
st.title("Data Sweeper...")
st.write("Transform you files between CSV and Excel formate with buit in data cleaning and visuliazastion")

uploaded_files = st.file_uploader("upload your files (CSV or Excel): ", type =["csv", "xlsx"], accept_multiple_files=True)


if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"unsuppoerted {file_ext}")
            continue
            # Dissplay about the files
        st.write(f"**file name** {file.name}")
        st.write(f"**file size** {file.size/1024}")


            # show 5 rows of our Dataframe
        st.write("preview the head of Dataframe")
        st.dataframe(df.head())

            # option for Data cleaning 
        st.subheader("Data Clean option")
        if st.checkbox(f"Clean data for {file.name}"):
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"removes duplicate from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("duplicates Removed!")

            with col2:
                if st.button(f"fill missing value for {file.name}"):
                    numeric_cols = df.select_dtypes(include=["number"]).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Missing values have been filled")
            
            # Choose specific columns
        st.subheader("select columns to convert")
        columns = st.multiselect(f"choos columns from {file.name}", df.columns, default=df.columns)
        df = df[columns]


        # create some  visualization
        st.subheader(" Data Visualization")
        if st.checkbox(f"show visualization for {file.name}"):
            st.bar_chart(df.select_dtypes(include="number").iloc[:,:2])


        # convert the file -> CSV to Excel

        st.subheader("Conversion option")
        conversion_type = st.radio(f"convert {file.name} to:", ["Csv" , "Excel"], key= file.name)
        if st.button(f"convert {file.name}"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer, index = False)
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv" 
            elif conversion_type == "Excel":
                 df.to_excel(buffer, index = False)
                 file_name = file.name.replace(file_ext, ".xlsx")
                 mime_type = "application.vnd.openxmlformats-officedocuments.spreadsheetml.sheet"
            buffer.seek(0)

        # download button
        st.download_button(

        )

