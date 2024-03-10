import streamlit as st
from PIL import Image
from fpdf import FPDF
import base64

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


with open("CV_PoojaMistry.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="Download Resume",
                    data=PDFbyte,
                    file_name="CV_PoojaMistry.pdf",
                    mime='application/octet-stream')

#####################
# Header 
st.write('''
# Pooja B. Mistry
##### *Portfolio* 
''')

image = Image.open('linkedin_headshot.png')
st.image(image, width=250)


st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Data & Business Analysis
- Programming, Business Intelligence
- Reporting development
- Python, Tableau, R, SQL
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #B38F13;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/poojabmistry/" target="_blank">Pooja Mistry</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

#####################
st.markdown('''
## Education
''')

txt('**Post Graduate Degree',
'2016-2018')
st.markdown('''
- bullet point 1
- bullet point 2
- bullet point 3
''')

txt('**Undergraduate degree',
'2012-2016')
st.markdown('''
- bullet point 1
- bullet point 2
- bullet point 3
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Experience 1',
'2021-Present')
st.markdown('''
- Warehouse science
''')

txt('**Experience 2',
'2020-2021')
st.markdown('''
- bullet point 1
- bullet point 2
- bullet point 3
''')


#####################
st.markdown('''
## Projects
''')
txt4('Company1', 'Project1')
txt4('Company1', 'Project1')
txt4('Company1', 'Project1')


#####################
st.markdown('''
## Skills
''')
txt3('Analysis','Skillist 1')
txt3('Business','Skillist 1')
txt3('Programming','Skillist 1')

#####################
st.markdown('''
## Links
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/poojabmistry/')
txt2('GitHub', 'github link')
