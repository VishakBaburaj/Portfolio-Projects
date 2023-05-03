
# Importing libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Setting the page title and layout
st.set_page_config(page_title = 'LinkedIn Data Analysis',
                   layout = 'centered')

# Setting the sidebar header
st.sidebar.header("Sidebar Header")

# Setting the sidebar options
options = ['Option 1','Option 2', 'Option 3']
add_sidebar = st.sidebar.radio('', options)

# Setting sidebar "option 1"
if add_sidebar == 'Option 1':

    # Setting title of the page
    st.title('LinkedIn Data Analysis')

    st.set_option('deprecation.showfileUploaderEncoding', False)  # Disable warning message

    # Uploading the csv data
    uploaded_file = st.file_uploader('Choose a CSV file', type = 'csv')

    # After uploading the csv data
    if uploaded_file is not None:

        # Reading the CSV file
        data = pd.read_csv(uploaded_file)

        # Processing the data

        # Droping sensitive data
        data = data[['Application Date',
                    'Company Name', 
                    'Job Title']]
        
        # Droping duplicate rows
        data.drop_duplicates(keep = 'first', inplace = True)

        # Splitting the date and time column into separate columns
        split_df = data['Application Date'].str.split(' ', expand = True)

        # Assigning new column names
        split_df.columns = ['Date', 'Time', 'AM/PM']

        # Replacing missing or null values with NaN
        split_df = split_df.replace('', pd.NA)

        # Concatenating the split DataFrame with the original DataFrame
        data = pd.concat([data, split_df], axis=1)

        # Droping the 'Application Date', 'Time' and 'AM/PM' columns in place
        data.drop(columns = ['Application Date', 'Time', 'AM/PM'], inplace = True)

        # Converting the 'Date' column to a datetime data type
        data['Date'] = pd.to_datetime(data['Date'])

        # Droping the index column from the DataFrame
        data = data.reset_index(drop=True)

        # Visualizing the data

        # Grouping the DataFrame by the date column and count the number of applications for each day
        daily_applications = data.groupby('Date').size().reset_index(name='count')

        # Ploting the data using a line chart
        daily_applications_sent = px.line(daily_applications, x = 'Date', y = 'count')

        # Displaying the chart using streamlit
        st.plotly_chart(daily_applications_sent, use_container_width=True)





