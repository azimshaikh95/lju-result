import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader, Template
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe
import os
from PIL import Image
import pandas as pd

import base64

def image_file_path_to_base64_string(filepath: str) -> str:
  '''
  Takes a filepath and converts the image saved there to its base64 encoding,
  then decodes that into a string.
  '''
  with open(filepath, 'rb') as f:
    return base64.b64encode(f.read()).decode()


st.set_page_config(layout="centered", page_icon="🎓", page_title="LJ Result App")
#st.title("🎓 LJ University Result App")

##############################################



#Added by Azim
from datetime import date
today = date.today()


#Variable Names
datex = "w22"
lastupdated = "01-01-2022 05:00 PM"

#Program Variables
header = st.container()
login = st.container()
body = st.container()
owners = st.container()

#Reading the file
data = pd.read_csv("data/" + datex + ".csv",encoding='utf-8')
df = pd.DataFrame(data)


for i in range(len(df["EnrolmentNo"])):
    df['EnrolmentNo'][i] = df['EnrolmentNo'][i].lower()


#WebApp -- "LJ University Result"
# sidebarContent = st.sidebar.radio("Menu", ["Semester Exam Report", "Milestone Leaderboard", "Program Resources"])


#SER
# if (sidebarContent == "Semester Exam Report"):
    # with(header):
        st.image('ljulogo.png', use_column_width=True)
        st.markdown("<h1 style='text-align: center'><b>Semester Exam Report</b></h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center'><b>LJ Polytehnic</b></h1>", unsafe_allow_html=True)
        st.write("Last Updated On: " + lastupdated )
        st.write("#####")

    # with(login):
        textInput = st.text_input("Enter your Enrolment No").lower()

        #Input Activity
        status = False
        for i in df["EnrolmentNo"]:
            if( i == textInput):
                status = True
        if(textInput != "" and status):
            tindex = df[df["EnrolmentNo"] == textInput].index[0] #Finding the index of the search EnrolmentNo
            st.header("Welcome " + str(df["StudentName"][tindex]).title() +" !")

            # st.write("**Institution:** " + str(df["InstituteCode"][tindex]))
            # st.write("**Branch Code & Name:** " + str(df["BranchCode"][tindex]))
            # st.write("**Subject 1:** " + str(df["Sub1"][tindex]) + "-" + str(df["Mark_1_TH"][tindex]) + "-" + str(df["Mark_1_PR"][tindex]) + "-" + str(df["Mark_1_OA"][tindex]))
            
            # st.write("**SPI:** " + str(df["SPI"][tindex]))
            # st.write("**CPI:** " + str(df["CPI"][tindex]))
            # st.write("**CPI:** " + str(df["CPI"][tindex]))

            # st.markdown("<hr>", unsafe_allow_html=True)
            # st.markdown("<table><tr><td>" + str(df["InstituteCode"][tindex]) + "<td>2<td>3</tr></table>", unsafe_allow_html=True)
            
            st.markdown("<style>#lju {border-collapse: collapse;  width: 100%;}</style>", unsafe_allow_html=True)
            
            
            st.markdown("<table id=lju><tbody><tr><th>Institute&amp;Name:</td><td>" + str(df["InstituteCode"][tindex]) + "</td></tr><tr><th>ExamName:</td><td>" + str(df["ExamName"][tindex]) + "</td></tr><tr><th>ExamMonth&amp;Year:</td><td>" + str(df["ExamMonthYear"][tindex]) + "</td></tr><tr><th>Semester:</td><td>" + str(df["Semester"][tindex]) + "</td></tr><tr><th>SeatNo:</td><td>" + str(df["SeatNo"][tindex]) + "</td></tr><tr><th>EnrolmentNo:</td><td>" + str(df["EnrolmentNo"][tindex]) + "</td></tr><tr><th>StudentName:</td><td>" + str(df["StudentName"][tindex]) + "</td></tr><tr><th>ProgramCode&amp;Name:</td><td>" + str(df["ProgramCode"][tindex]) + "</td></tr><tr><th>BranchCode&amp;Name:</td><td>" + str(df["BranchCode"][tindex]) + "</td></tr><tbody></table>&nbsp;&nbsp;", unsafe_allow_html=True)
            
            st.markdown("<table id=lju><tbody ><tr><th>Subject Code and Name</th><th>Theory Grade</th><th>Practical Grade</th><th>Overall Grade</th></tr><tr><td>" + str(df["Sub1"][tindex]) + "</td><td>" + str(df["Mark_1_TH"][tindex]) + "</td><td>" + str(df["Mark_1_PR"][tindex]) + "</td><td>" + str(df["Mark_1_OA"][tindex]) + "</td></tr><tr><td>" + str(df["Sub2"][tindex]) + "</td><td>" + str(df["Mark_2_TH"][tindex]) + "</td><td>" + str(df["Mark_2_PR"][tindex]) + "</td><td>" + str(df["Mark_2_OA"][tindex]) + "</td></tr><tr><td>" + str(df["Sub3"][tindex]) + "</td><td>" + str(df["Mark_3_TH"][tindex]) + "</td><td>" + str(df["Mark_3_PR"][tindex]) + "</td><td>" + str(df["Mark_3_OA"][tindex]) + "</td></tr><tr><td>" + str(df["Sub4"][tindex]) + "</td><td>" + str(df["Mark_4_TH"][tindex]) + "</td><td>" + str(df["Mark_4_PR"][tindex]) + "</td><td>" + str(df["Mark_4_OA"][tindex]) + "</td><tr><td>" + str(df["Sub5"][tindex]) + "</td><td>" + str(df["Mark_5_TH"][tindex]) + "</td><td>" + str(df["Mark_5_PR"][tindex]) + "</td><td>" + str(df["Mark_5_OA"][tindex]) + "</td></tr><tr><td>" + str(df["Sub6"][tindex]) + "</td><td>" + str(df["Mark_6_TH"][tindex]) + "</td><td>" + str(df["Mark_6_PR"][tindex]) + "</td><td>" + str(df["Mark_6_OA"][tindex]) + "</td></tr><tr><td>" + str(df["Sub7"][tindex]) + "</td><td>" + str(df["Mark_7_TH"][tindex]) + "</td><td>" + str(df["Mark_7_PR"][tindex]) + "</td><td>" + str(df["Mark_7_OA"][tindex]) + "</td></tr><tr><td>" + str(df["Sub8"][tindex]) + "</td><td>" + str(df["Mark_8_TH"][tindex]) + "</td><td>" + str(df["Mark_8_PR"][tindex]) + "</td><td>" + str(df["Mark_8_OA"][tindex]) + "</td></tr><tr><td>" + str(df["Sub9"][tindex]) + "</td><td>" + str(df["Mark_9_TH"][tindex]) + "</td><td>" + str(df["Mark_9_PR"][tindex]) + "</td><td>" + str(df["Mark_9_OA"][tindex]) + "</td></tr><tr><td>" + str(df["Sub10"][tindex]) + "</td><td>" + str(df["Mark_10_TH"][tindex]) + "</td><td>" + str(df["Mark_10_PR"][tindex]) + "</td><td>" + str(df["Mark_10_OA"][tindex]) + "</td></tr></tbody></table>&nbsp;&nbsp;",unsafe_allow_html=True)
            
            
            st.markdown("<table id=lju><tbody><tr><td>SPI:</td><td>" + str(df["SPI"][tindex]) +" </td></tr><tr><td>CPI:</td><td>" + str(df["CPI"][tindex]) +"</td></tr><tr><td>CGPA:</td><td>" + str(df["CGPA"][tindex]) +"</td></tr><tr><td>Status:</td><td>" + str(df["Status"][tindex]) +"</td></tr><tr><td>Current Backlog:</td><td>" + str(df["CurrentBacklog"][tindex]) +"</td></tr><tr><td>Total Backlog:</td><td>" + str(df["TotalBacklog"][tindex]) +"</td></tr><tr><td>Declaration Date:</td><td>" + str(df["DeclarationDate"][tindex]) +"</td></tr></tbody></table>",unsafe_allow_html=True)

            
        elif (textInput != "" and status == False):
            st.error("No Entry Found")

    # with(owners):
        st.write("####")
        st.markdown('<body class= "last" >Developed & Managed By: <a href="https://in.linkedin.com/in/mohammedazim-shaikh">MohammedAzim Shaikh</a></body>', unsafe_allow_html=True)
        st.write("...")
        
# col1, col2, col3, col4 = st.columns([3, 1, 1, 1])

# with col1:
    # st.write("**Subject Code and Name**")
    # st.write( str(df["Sub1"][tindex]) )

# with col2:
    # st.write("**Theory Grade**")
    # st.write( str(df["Mark_1_TH"][tindex]) )

# with col3:
    # st.write("**Practical Grade**")
    # st.write( str(df["Mark_1_PR"][tindex]) )
    
# with col4:
    # st.write("**Overall Grade**")
    # st.write( str(df["Mark_1_OA"][tindex]) )
    
    
  



########################################

    st.write("  \n  This app shows you how you can use Streamlit to make a PDF generator app in just a few lines of code!")

    left, right = st.columns(2)

    right.write("Here's the template we'll be using:")

    right.image("ljulogo.png", width=300)

    env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
    template = env.get_template("template.html")


    left.write("Fill in the data:")
    form = left.form("template_info")

    submit = form.form_submit_button("Generate PDF")

    if submit:
        html = template.render(
            InstituteCode=str(df["InstituteCode"][tindex]),
            ExamName=str(df["ExamName"][tindex]),
            ExamMonthYear=str(df["ExamMonthYear"][tindex]),
            Semester=str(df["Semester"][tindex]),
            SeatNo=str(df["SeatNo"][tindex]),
            EnrolmentNo=str(df["EnrolmentNo"][tindex]),
            StudentName=str(df["StudentName"][tindex]),
            ProgramCode=str(df["ProgramCode"][tindex]),
            BranchCode=str(df["BranchCode"][tindex]),
            Sub1=str(df["Sub1"][tindex]),
            Mark_1_TH=str(df["Mark_1_TH"][tindex]),
            Mark_1_PR=str(df["Mark_1_PR"][tindex]),
            Mark_1_OA=str(df["Mark_1_OA"][tindex]),
            Sub2=str(df["Sub2"][tindex]),
            Mark_2_TH=str(df["Mark_2_TH"][tindex]),
            Mark_2_PR=str(df["Mark_2_PR"][tindex]),
            Mark_2_OA=str(df["Mark_2_OA"][tindex]),
            Sub3=str(df["Sub3"][tindex]),
            Mark_3_TH=str(df["Mark_3_TH"][tindex]),
            Mark_3_PR=str(df["Mark_3_PR"][tindex]),
            Mark_3_OA=str(df["Mark_3_OA"][tindex]),
            Sub4=str(df["Sub4"][tindex]),
            Mark_4_TH=str(df["Mark_4_TH"][tindex]),
            Mark_4_PR=str(df["Mark_4_PR"][tindex]),
            Mark_4_OA=str(df["Mark_4_OA"][tindex]),
            Sub5=str(df["Sub5"][tindex]),
            Mark_5_TH=str(df["Mark_5_TH"][tindex]),
            Mark_5_PR=str(df["Mark_5_PR"][tindex]),
            Mark_5_OA=str(df["Mark_5_OA"][tindex]),
            Sub6=str(df["Sub6"][tindex]),
            Mark_6_TH=str(df["Mark_6_TH"][tindex]),
            Mark_6_PR=str(df["Mark_6_PR"][tindex]),
            Mark_6_OA=str(df["Mark_6_OA"][tindex]),
            Sub7=str(df["Sub7"][tindex]),
            Mark_7_TH=str(df["Mark_7_TH"][tindex]),
            Mark_7_PR=str(df["Mark_7_PR"][tindex]),
            Mark_7_OA=str(df["Mark_7_OA"][tindex]),
            Sub8=str(df["Sub8"][tindex]),
            Mark_8_TH=str(df["Mark_8_TH"][tindex]),
            Mark_8_PR=str(df["Mark_8_PR"][tindex]),
            Mark_8_OA=str(df["Mark_8_OA"][tindex]),
            Sub9=str(df["Sub9"][tindex]),
            Mark_9_TH=str(df["Mark_9_TH"][tindex]),
            Mark_9_PR=str(df["Mark_9_PR"][tindex]),
            Mark_9_OA=str(df["Mark_9_OA"][tindex]),
            Sub10=str(df["Sub10"][tindex]),
            Mark_10_TH=str(df["Mark_10_TH"][tindex]),
            Mark_10_PR=str(df["Mark_10_PR"][tindex]),
            Mark_10_OA=str(df["Mark_10_OA"][tindex]),
            SPI=str(df["SPI"][tindex]),
            CPI=str(df["CPI"][tindex]),
            CGPA=str(df["CGPA"][tindex]),
            Status=str(df["Status"][tindex]),
            CurrentBacklog=str(df["CurrentBacklog"][tindex]),
            TotalBacklog=str(df["TotalBacklog"][tindex]),
            DeclarationDate=str(df["DeclarationDate"][tindex]),              
        )

        pdf = pdfkit.from_string(html, False)
        st.balloons()
           
      

        right.success("🎉 Your diploma was generated!")
         #st.write(html, unsafe_allow_html=True)
         #st.write("")
        right.download_button(
            "⬇️ Download PDF",
            data=pdf,
            file_name=str(df["EnrolmentNo"][tindex]) + "-" + str(df["ExamName"][tindex]) + ".pdf",
            mime="application/octet-stream",
        )
