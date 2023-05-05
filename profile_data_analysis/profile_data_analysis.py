# Importing libraries
import streamlit as st
import pandas as pd
import plotly.express as px
# ---------------------------------------------------------------------------------------------------------------------------------------------------
# Setting the page title and layout
st.set_page_config(page_title = 'LinkedIn Data Analysis',
                   page_icon=None,
                   layout = 'centered', initial_sidebar_state="auto")
# ---------------------------------------------------------------------------------------------------------------------------------------------------
# Setting the first level sidebar options
options_level_1 = ['LinkedIn','Instagram']
selected_option_level_1 = st.sidebar.radio('Choose an application', options_level_1)

# Adding a horizontal line between the first and second level options
st.sidebar.markdown('---')

# If the selected option is "LinkedIn", display the second level of the sidebar
if selected_option_level_1 == 'LinkedIn':
    options_level_2_for_linkedin = ['LinkedIn Job Application', 'LinkedIn Connections']
    selected_option_level_2_for_linkedin = st.sidebar.radio('Choose an insight', options_level_2_for_linkedin)

    # Setting sidebar "LinkedIn" - "LinkedIn Job Application Tracker"
    if selected_option_level_2_for_linkedin  == 'LinkedIn Job Application':

        # Setting title of the page
        st.title('LinkedIn Job Application')

        st.set_option('deprecation.showfileUploaderEncoding', False)  # Disable warning message

        # Uploading the csv data
        uploaded_file = st.file_uploader('Upload the Job Application CSV file', type = 'csv')

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

            # Job application dashboard

            # Adding a horizontal line
            st.write('---')

# ---------------------------------------------------------------------------------------------------------------------------------------------------
            # Total jobs applied
            total_jobs_applied = len(data)

            # Displaying the total count of jobs applied as a KPI
            if total_jobs_applied >= 0:
                st.success(f"**Total Jobs Applied:** {total_jobs_applied}")
            else:
                st.error(f"**Total Jobs Applied:** {total_jobs_applied}")

            # Adding a horizontal line
            st.write('---')

# ---------------------------------------------------------------------------------------------------------------------------------------------------
            st.markdown('Daily applications sent')
            # Grouping the DataFrame by the date column and counting the number of applications for each day
            daily_applications = data.groupby('Date').size().reset_index(name='count')

            # Ploting the data using a line chart
            daily_applications_sent = px.line(daily_applications, x = 'Date', y = 'count', color_discrete_sequence=["#FF8C00"])

            # Displaying the chart using streamlit
            st.plotly_chart(daily_applications_sent, use_container_width=True)

            # Adding a horizontal line
            st.write('---')

# ---------------------------------------------------------------------------------------------------------------------------------------------------
            st.markdown('Top jobs titles applied')
            # Grouping the data by job title and counting the number of occurrences
            jobs_applied = data.groupby('Job Title').size().reset_index(name='count')

            # Sorting the data by count in descending order and selecting the top 10 rows
            top_jobs_applied = jobs_applied.sort_values("count", ascending=False).head(10)

            # Sorting the top jobs by count in descending order
            top_jobs_applied = top_jobs_applied.sort_values("count", ascending=True)

            # Plotting the horizontal bar chart using Plotly Express
            fig = px.bar(top_jobs_applied, x='count', y='Job Title', orientation='h', color='count')
            fig.update_layout(width=800, height=500)
            st.plotly_chart(fig)
# ---------------------------------------------------------------------------------------------------------------------------------------------------
    # Setting sidebar "LinkedIn" - "LinkedIn Connections Insights"
    elif selected_option_level_2_for_linkedin  == 'LinkedIn Connections':

        # Setting title of the page
        st.title('LinkedIn Connections')

        st.set_option('deprecation.showfileUploaderEncoding', False)  # Disable warning message



# If the selected option is "Instagram", display the second level of the sidebar
elif selected_option_level_1 == 'Instagram':
    options_level_2_for_instagram = ['Option 1', 'Option 2']
    selected_option_level_2_for_instagram = st.sidebar.radio('', options_level_2_for_instagram)

    # Setting sidebar "Instagram" - "Option 1"
    if selected_option_level_2_for_instagram  == 'Option 1':
        st.write('Coming Soon')


    # Setting sidebar "Instagram" - "Option 2"
    elif selected_option_level_2_for_instagram  == 'Option 2':
        st.write('Coming Soon')


