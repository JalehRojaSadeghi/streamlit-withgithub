import streamlit.components.v1 as components
import streamlit as st
from PIL import Image

# Load the HTML file in Streamlit
st.sidebar.title('Choose your favorite output')
option=st.sidebar.selectbox('select graph',('network','at risk projects', 'graph'))


if option=='network':
    
    HtmlFile = open('ABM.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height=500)
    
if option == 'at risk projects':
    image = Image.open('ABM_atriskprojects.jpg')
    st.image(image, use_column_width=True)

if option == 'graph':
    image = Image.open('ABM_graph.jpg')
    st.image(image, use_column_width=True)


###
import pandas as pd
import requests
from io import BytesIO

# Function to load the Excel file from a GitHub URL
def load_excel_from_github(url):
    response = requests.get(url)
    response.raise_for_status()  # Check that the request was successful
    return pd.read_excel(BytesIO(response.content))

# Input URL for the Excel file in the GitHub repository (raw file)
url = st.text_input("https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2FJalehRojaSadeghi%2Fstreamlit-withgithub%2Fmain%2FALL%2520local%2520authorities%2520pipeline.xlsx&wdOrigin=BROWSELINK")
#df = load_excel_from_github(url)
#st.dataframe(df)
###

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})
st.dataframe(df)
