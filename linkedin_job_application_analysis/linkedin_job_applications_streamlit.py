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
options = ['About','LinkedIn Job Application Tracker']
selected_option = st.sidebar.selectbox('Select an option', options)

# Adding a horizontal line in the sidebar
st.sidebar.markdown('---')

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# If the selected option is "About", display the 'About the app' page
if selected_option == 'About':

    # Setting title of the page
    st.markdown('## About LinkedIn Job Application Tracker')

    st.write('---')

    st.markdown('#### Goal:')

    st.write('''The LinkedIn Job Application Tracker is a tool deployed to 
            help job seekers keep track of their job applications on LinkedIn. 
            It allows users to track their progress, and get insights into their job search. 
            The goal of the tool is to help job seekers stay organized and motivated 
            throughout their job search process.''')

    st.markdown('#### Methodology:')

    st.write('''The "LinkedIn Job Application Tracker" page allows users to upload their job application data from LinkedIn 
            and get insights into their job search, such as key performance indicators, and daily / weekly / monthly insights.
            The data is stored in a CSV file and is uploaded, processed and displayed in the "LinkedIn Job Application Tracker" page.''')
    
    st.markdown('#### Links:')

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write('##### [Github](https://github.com/VishakBaburaj/)')

    with col2:
        st.write('##### [LinkedIn](https://www.linkedin.com/in/vishakbaburaj/)')

    with col3:
        st.write('##### [Portfolio](https://vishakbaburaj.carrd.co/)')

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# If the selected option is "LinkedIn", display the "LinkedIn Job Application Tracker" page
elif selected_option == 'LinkedIn Job Application Tracker':

    # Setting title of the page
    st.markdown('## LinkedIn Job Application Tracker')

    st.write('---')

    # Disabling the warning message
    st.set_option('deprecation.showfileUploaderEncoding', False)

    # Checkbox to load sample data
    load_sample_data_checkbox = st.sidebar.checkbox('Load Sample Data')

    # Reading sample csv data
    df = pd.read_csv("C:/Users/visha/Documents/Projects/Portfolio Projects/linkedin_job_application_analysis/sample_data/Job Applications.csv") 

    # If the sample data checkbox is selected upload the sample data
    if load_sample_data_checkbox:
        uploaded_file = df  # Display the sample data in the app

    # If the sample data checkbox is not selected upload the csv data
    elif uploaded_file := st.sidebar.file_uploader('Choose the Job Application CSV file', type = 'csv'):

        # Reading the CSV file
        uploaded_file = pd.read_csv(uploaded_file)

    elif st.markdown('##### Upload Job Application CSV file or Load Sample Data'):

        st.markdown('''This dashboard is designed to work exclusively with the Job Application data on LinkedIn. 
                To access your data, you will need to request an archive from LinkedIn by following the instructions 
                provided in this [link](https://www.linkedin.com/help/linkedin/answer/a1339364/downloading-your-account-data?lang=en).
                \n It usually takes approximately 24 hours to receive your data. However, in the interim, 
                you can experiment with the job application sample data that is readily available on the app. 
                Simply load the sample data by clicking on the "Load Sample Data" checkbox in the sidebar.''')

    # When either data has been input
    if uploaded_file is not None:

        # Precessing the data
        data = process_linkedin_job_app_data(uploaded_file)

# ---------------------------------------------------------------------------------------------------------------------------------------------------

        display_kpis(data)

# ---------------------------------------------------------------------------------------------------------------------------------------------------

        display_top_10_insights(data)

# ---------------------------------------------------------------------------------------------------------------------------------------------------

        display_daily_weekly_monthly_insights(data)

# ---------------------------------------------------------------------------------------------------------------------------------------------------

