import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

col1, col2, col3 = st.columns([1, 3, 1]) 
with col2:
    st.title("MYP Data Analysis")

option_grade = st.selectbox("Select the Grade Level",("Grade 6","Grade 7","Grade 8","Grade 9","Grade 10"))
option = st.selectbox(
    "Select the subject from the list",
    ("English L&L", "German L&L", "English LA", "German LA",
     "French LA","Spanish LA","Individuals and Societies",
     "Science","Math","Visual Arts","PHE",
     "Performing Arts","Design","Music")
)
if option == "English L&L" or option == "German L&L":
    criteria = ["A: Analysing", "B: Organizing", "C: Producing text", "D: Using language"]
elif option == "German LA" or option == "English LA" or option == "French LA" or option == "Spanish LA":
    criteria = ["A: Listening", "B: Reading", "C: Speaking", "D: Writing"]
elif option == "Math":
    criteria = ["A: Knowing and understanding", "B: Investigating patterns", "C: Communicating", "D: Applying mathematics in real-life contexts"]
elif option == "Individuals and Societies":
    criteria = ["A: Knowing and understanding", "B: Investigating", "C: Communicating", "D: Thinking critically"]
elif option == "Science":
    criteria = ["A: Knowing and understanding", "B: Inquiring and designing", "C: Processing and evaluating", "D: Reflecting on the impacts of science"]
elif option == "Design":
    criteria = ["A: Inquiring and analysing", "B: Developing ideas", "C: Creating the solution", "D: Evaluating"]
elif option == "PHE":
    criteria = ["A: Knowing and understanding", "B: Planning for performance", "C: Applying and performing", "D: Reflecting and improving performance"]
else:
    criteria = ["A: Investigating", "B: Developing", "C: Creating or performing", "D: Evaluating"]

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file, header=6) 
    for criterion in criteria:
        if criterion in df.columns:
            grade_counts = df[criterion].value_counts()
            fig, ax = plt.subplots(figsize=(5, 5))
            ax.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%', startangle=140)
            ax.set_title(f"{option_grade} Distribution for {criterion}")
            st.pyplot(fig)
        else:
            st.warning(f"Column '{criterion}' not found in the uploaded file.")
            
      
    final_column = df.iloc[:, 10]
    grade_counts = final_column.value_counts()
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%', startangle=140)
    ax.set_title(f"{option_grade} Distribution for Final Level of achievement")
    st.pyplot(fig)
    buf = io.BytesIO()
    fig.savefig(buf, format="png",bbox_inches="tight", pad_inches=0.5)
    buf.seek(0)
            
    
    st.download_button(
    label="Download Chart as Image",
    data=buf,
    file_name=f"{option_grade}_{criterion}.png",
    mime="image/png"
    )
            
   
        
    
