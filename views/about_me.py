'''
Copyright  2024 IBM, Author - Jitendra Zaa

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

       https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

        https://wwww.jitendraZaa.com

@date          October 2024
@author        Jitendra Zaa
@email         jitendra.zaa@ibm.com | jitendra.zaa+30@gmail.com
@description   TBD
'''

import streamlit as st

from forms.contact import contact_form

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/JZProfile.jpeg", width=230)

with col2:
    st.title("Jitendra Zaa", anchor=False)
    st.write(
        "Salesfprce CTA."
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - 15+ years in Salesforce, CTA
    - Java, Python, C#
    - Devops Expert
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Programming: Python (Scikit-learn, Pandas), SQL, VBA
    - Data Visualization: PowerBi, MS Excel, Plotly
    - Modeling: Logistic regression, linear regression, decision trees
    - Databases: Postgres, MongoDB, MySQL
    """
)