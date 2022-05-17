import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe
import os
from PIL import Image
import pandas as pd


st.set_page_config(layout="centered", page_icon="🎓", page_title="Diploma Generator")
st.title("🎓 Diploma PDF Generator")

##############################################



#Added by Azim
from datetime import date
today = date.today()


#Variable Names
datex = "w22"

#Program Variables
header = st.container()
login = st.container()
body = st.container()
owners = st.container()

#Reading the file
data = pd.read_csv("data/" + datex + ".csv",encoding='utf-8')
df = pd.DataFrame(data)

for i in range(len(df["Enrolment No"])):
    df['Enrolment No'][i] = df['Enrolment No'][i].lower()


#WebApp -- "LJ University Result"
sidebarContent = st.sidebar.radio("Menu", ["Semester Exam Report", "Milestone Leaderboard", "Program Resources"])


#SER
if (sidebarContent == "Semester Exam Report"):
    with(header):
        st.image('images/banner.png', use_column_width=True)
        st.markdown("<h1 style='text-align: center'><b>Semester Exam Report</b></h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center'><b>LJ Polytehnic</b></h1>", unsafe_allow_html=True)
        st.write("Last Updated On: " + datex + "-2022")
        st.write("#####")

    with(login):
        textInput = st.text_input("Enter your Enrolment No").lower()

        #Input Activity
        status = False
        for i in df["Enrolment No"]:
            if( i == textInput):
                status = True
        if(textInput != "" and status):
            tindex = df[df["Enrolment No"] == textInput].index[0] #Finding the index of the search Enrolment No
            st.title("Welcome " + str(df["Student Name"][tindex]) +" !")

            st.write("**Institution:** " + str(df["Institution"][tindex]))
            st.write("**Branch Code & Name:** " + str(df["BranchCode"][tindex]))
            st.write("**Subject 1:** " + str(df["Sub1"][tindex]) + "-" + str(df["Mark_1_TH"][tindex]) + "-" + str(df["Mark_1_PR"][tindex]) + "-" + str(df["Mark_1_OA"][tindex]))
            
            st.write("**SPI:** " + str(df["SPI"][tindex]))
            st.write("**CPI:** " + str(df["CPI"][tindex]))
            st.write("**CPI:** " + str(df["CPI"][tindex]))

            st.markdown("<hr>", unsafe_allow_html=True)


            
        elif (textInput != "" and status == False):
            st.error("No Entry Found")

    with(owners):
        st.write("####")
        st.markdown('<body class= "last" >Developed & Managed By: <a href="https://in.linkedin.com/in/mohammedazim-shaikh">MohammedAzim Shaikh</a></body>', unsafe_allow_html=True)
        #st.write("Developed & Managed By : MohammedAzim Shaikh")




########################################

st.write(
    "This app shows you how you can use Streamlit to make a PDF generator app in just a few lines of code!"
)

left, right = st.columns(2)

right.write("Here's the template we'll be using:")

right.image("template.png", width=300)

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("template.html")


left.write("Fill in the data:")
form = left.form("template_form")
student = form.text_input("Student name")
course = form.selectbox(
    "Choose course",
    ["Report Generation in Streamlit", "Advanced Cryptography"],
    index=0,
)
grade = form.slider("Grade", 1, 100, 60)
submit = form.form_submit_button("Generate PDF")

if submit:
    html = template.render(
        Sub1=str(df["Sub1"][tindex]),
        SPI=str(df["SPI"][tindex]),
        CPI=str(df["CPI"][tindex]),
        grade=f"{grade}/100",
        #date=date.today().strftime("%B %d, %Y"),
    )

    pdf = pdfkit.from_string(html, False)
    st.balloons()

    right.success("🎉 Your diploma was generated!")
    # st.write(html, unsafe_allow_html=True)
    # st.write("")
    right.download_button(
        "⬇️ Download PDF",
        data=pdf,
        file_name=str(df["Sub1"][tindex])+".pdf",
        mime="application/octet-stream",
    )