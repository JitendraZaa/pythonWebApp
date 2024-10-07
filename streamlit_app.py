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
@description   POC for Python Web application using Streamlit 
'''

import streamlit as st

# --- Page Setup ---
about_page = st.Page( 
    title="About Me",
    icon=":material/account_circle:", 
    page="views/about_me.py",
    default=True ,
)

project_1_page = st.Page(
    title="Sales Dashboard",
    icon=":material/bar_chart:", 
    page="views/sales_dashboard.py", 
)

project_2_page = st.Page(
    title="Chat Bot",
    icon=":material/smart_toy:", 
    page="views/chatbot.py", 
)

## --- Navigation Setup [Without Sections] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

## --- Navigation Setup [With Sections]using Dictionary Data type ---
pg = st.navigation(
    {
        "Info" : [about_page],
        "Projects" : [project_1_page, project_2_page]
    }
)

# --- SHARED ON ALL PAGES ---
st.logo("assets/Shivasoft_logo.jpeg")
st.sidebar.markdown("Made with ❤️ by [JZ](https://jitendrazaa.com)")

# --- Run Navigation ---
pg.run() 
 