# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 11:01:44 2022

@author: tinch
"""

from pathlib import Path

import streamlit as st
from PIL import Image


#---PATH SETTINGS---

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "DSC_1141.jpg" #"profile-pic.png"

#--- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Martin Luis Peretti Ricart"
PAGE_ICON = ":wave:"
NAME = "MartΓ­n Luis Peretti Ricart"
DESCRIPTION =  """
Senior Valuation Analyst | π Excel & VBA Expert | Capital Markets | π Python 
| Data Modelling
"""
EMAIL = "mlpererettiricart@gmail.com"
SOCIAL_MEDIA = {
    "Linkedin": "https://linkedin.com/in/martin-luis-peretti-ricart-98668483",
    "GitHub": "https://github.com/tinchopr"
    }

ABOUT =  """
    
  βοΈ | π» I'm a tech lover β coffee savvy and a π§Ύ Public Accountant working 
   as a π Financial Senior Valuation Analyst 
  βοΈ | Participated in 1500+ valuations: 10+ Unicorns, 50+ PPAs & ASC 350, 10+ 
  βοΈ | Portfolio companies with 1B+ assets. 
  βοΈ | Excel & VBA expert, Python & Data Science, AI and ML enthusiast
  βοΈ | Automated and design complex reports with VBA (Excel + Word).
  βοΈ | Team team-player, target oriented.

"""

st.set_page_config(page_title = PAGE_TITLE, page_icon = PAGE_ICON)

st.title("Tincho's resume")

#LOAD CSS, PDF & PROFILE PIC

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    
with open(resume_file, "rb") as pdf_file:
    PDFByte = pdf_file.read()
    profile_pic = Image.open(profile_pic)

#--- HERO SECTION ---

col1, col2 = st.columns(2, gap="small")

with col1:
    st.image(profile_pic, width=230)
    
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label = "π Download resume",
        data = PDFByte,
        file_name = resume_file.name,
        mime="application/octet-stream",
        )
    
st.write("π¬", EMAIL)


#--- SOCIAL LINKS---
#st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
    
# --- ABOUT ME
st.write("#")
st.subheader("Soft Skills")
st.write(
    """   
    - π» | Tech lover
    - β | Coffee savvy
    - π | Team team-player, target oriented.
  """
    )
    
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
    - π | Public Accountant working as a Financial Senior Valuation Analyst. 
    - π | Business Combinations Β· Business Valuation Β· ASC 805 Β· IFRS.
    - π¦ | Participated in 1500+ valuations: 10+ Unicorns, 50+ PPAs & ASC 350.  
    - π’ | Assisted in 20+ Portfolio company valuations with 1B+ assets. 
    - πΈ | Excel & VBA expert: I've automated and design complex reports with VBA (Excel + Word).
    - π | Python & Data Science. 
    - ποΈ | Dabatabases and online services: Capital IQ, Refinitiv, Pithbook, GF Data,
           Deal Stats, Pratt Stats.

  """
    )
    
#  --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

#Job 1
st.write("π§")
st.write("01/2020 - Present")
st.write(
    """
    - βΆ | Responsible for valuation and transaction advisory engagements. 
    - βΆ | I have fulfilled 1000+ of engagements that include:
        - βΈ Goodwill impairment testing
        - βΈ Venture capital 
        - βΈ Private equity portfolios
        - βΈ Mergers and acquisitions
        - βΈ Raising capital
        - βΈ Deferred compensation 
        - βΈ Financial reporting
        - βΈ Estate and tax planning
        - βΈ Shareholder disputes
        
    - βΆ Assisted in the valuation of 8+ $1B companies from technology, 
      consumer discretionary and finanance sectors.
      
    """    
    )

    #Job 2
st.write("π§")
st.write("04/2017 - 01/2020")
st.write(
        """
        - βΆ Responsible for valuation and transaction advisory engagements. 
        - βΆ I have fulfilled hundreds of engagements that include:
            - βΈ Goodwill impairment testing
            - βΈ Venture capital 
            - βΈ Private equity portfolios
            - βΈ Mergers and acquisitions
            - βΈ Raising capital
            - βΈ Deferred compensation 
            - βΈ Financial reporting
            - βΈ Estate and tax planning
            - βΈ Shareholder disputes          
        """    
        )


    
    
    
    



























