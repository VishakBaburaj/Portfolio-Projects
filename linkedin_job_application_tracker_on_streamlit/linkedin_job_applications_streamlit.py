# Importing libraries
import streamlit as st
import pandas as pd
from functions import process_linkedin_job_app_data, display_kpis, display_top_10_insights, display_daily_weekly_monthly_insights

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Setting the page title and layout
st.set_page_config(page_title = 'LinkedIn Job Application Tracker',
                   page_icon=None,
                   layout = 'centered', initial_sidebar_state="auto")

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Setting the sidebar options
options = ['About the App','LinkedIn Job Application Tracker']
selected_option = st.sidebar.selectbox('Select an option', options)

# Adding a horizontal line in the sidebar
st.sidebar.markdown('---')

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# If the selected option is "About", display the 'About the app' page
if selected_option == 'About the App':

    # Setting title of the page
    st.markdown('## About the app')

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# If the selected option is "LinkedIn", display the "LinkedIn Job Application Tracker" page
elif selected_option == 'LinkedIn Job Application Tracker':

    # Setting title of the page
    st.markdown('## LinkedIn Job Application Tracker')

    # Disabling the warning message
    st.set_option('deprecation.showfileUploaderEncoding', False)

    # Checkbox to load sample data
    load_sample_data_checkbox = st.checkbox('Load Sample Data')

    # Reading sample csv data
    df = pd.read_csv("C:/Users/visha/Documents/Projects/Portfolio Projects/linkedin_job_application_tracker_on_streamlit/sample_data/Job Applications.csv") 

    # If the sample data checkbox is selected upload the sample data
    if load_sample_data_checkbox:
        uploaded_file = df  # Display the sample data in the app

    # If the sample data checkbox is not selected upload the csv data
    elif uploaded_file := st.file_uploader('Choose the Job Application CSV file', type = 'csv'):

        # Reading the CSV file
        uploaded_file = pd.read_csv(uploaded_file)

    # When either data has been input
    if uploaded_file is not None:

        # Precessing the data
        data = process_linkedin_job_app_data(uploaded_file)

        # Adding a horizontal line
        st.write('---')

# ---------------------------------------------------------------------------------------------------------------------------------------------------

        display_kpis(data)

# ---------------------------------------------------------------------------------------------------------------------------------------------------

        display_top_10_insights(data)

# ---------------------------------------------------------------------------------------------------------------------------------------------------

        display_daily_weekly_monthly_insights(data)

# ---------------------------------------------------------------------------------------------------------------------------------------------------

