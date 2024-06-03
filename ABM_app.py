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

import pandas as pd
df = pd.read_excel("ALL local authorities pipeline")
        
# Display the dataframe
st.write("Data from Excel file:")
st.dataframe(df)
