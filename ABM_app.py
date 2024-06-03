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
        
        # Sidebar for filtering
        st.sidebar.header("Filters")
        columns = df.columns.tolist()
        
        # Filter options
        filter_columns = st.sidebar.multiselect("Select columns to filter", columns)
        
        # Display filters and data
        if filter_columns:
            filters = {}
            for column in filter_columns:
                unique_values = df[column].unique()
                selected_values = st.sidebar.multiselect(f"Filter {column}", unique_values)
                if selected_values:
                    filters[column] = selected_values

            # Apply filters
            if filters:
                filtered_df = df
                for column, selected_values in filters.items():
                    filtered_df = filtered_df[filtered_df[column].isin(selected_values)]
                
                # Display the filtered dataframe
                st.write("Filtered Data:")
                st.dataframe(filtered_df)
            else:
                st.write("No filters applied.")
        else:
            st.write("No columns selected for filtering.")
else:
    st.write("No Excel files found in the current directory.")
