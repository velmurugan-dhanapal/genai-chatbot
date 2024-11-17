# app.py
import streamlit as st

def main():
    st.title('Hello, Streamlit on AWS ECS!')
    st.write("This app is deployed using ECS Fargate and AWS CodePipeline.")

if __name__ == "__main__":
    main()
