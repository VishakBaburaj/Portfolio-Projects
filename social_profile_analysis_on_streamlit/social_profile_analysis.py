# Importing libraries
import streamlit as st
import pandas as pd
import altair as alt
from functions import process_linkedin_job_app_data, display_kpis, display_top_10_insights

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Setting the page title and layout
st.set_page_config(page_title = 'LinkedIn Job Application Tracker',
                   page_icon=None,
                   layout = 'centered', initial_sidebar_state="auto")

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Setting the sidebar options
options = ['About','LinkedIn Job Application Tracker']
selected_option = st.sidebar.selectbox('Select an option', options)

# Adding a horizontal line undernead the sidebar
st.sidebar.markdown('---')

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# If the selected option is "About", display the 'About the app' page
if selected_option == 'About':
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
    df = pd.read_csv("C:/Users/visha/Documents/Projects/Portfolio Projects/social_profile_analysis_on_streamlit/sample_data/Job Applications.csv") 

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

        # Selecting the trend
        trend_options = ['Daily Application Trend', 'Weekly Applications Trend', 'Monthly Application Trend']
        selected_trend = st.radio('###### Select a trend:', trend_options)

# ---------------------------------------------------------------------------------------------------------------------------------------------------
        if selected_trend == 'Daily Application Trend':
            # Grouping the DataFrame by the date column and counting the number of applications for each day
            daily_applications = data.groupby('Date').size().reset_index(name='count')

            # Daily trend line chart
            source = daily_applications
            x = 'Date'
            y = 'count'
            # color = 'keywords'
            selector = alt.selection_single(encodings=['x', 'y'])
            hover = alt.selection_single(
                fields=[x],
                nearest=True,
                on="mouseover",
                empty="none",
            )

            lines = (
                alt.Chart(source).mark_line(point="transparent").encode(
                    x=alt.X(x, title="Date", axis=alt.Axis(labelFontSize=15, titleFontSize=15)), 
                    y=alt.Y(y, title="Count of Applications sent", axis=alt.Axis(labelFontSize=15, titleFontSize=15))
                    ).transform_calculate(color='datum.delta < 0 ? "red" : "lightblue"') # doesn't show red for negative delta
            )
            points = (
                lines.transform_filter(hover).mark_circle(size=50).encode(
                color=alt.Color("color:N", scale=None))
            )
            tooltips = (
                alt.Chart(source).mark_rule(opacity=0).encode(
                    x=x,
                    y=y,
                    tooltip=[x, y],
                ).add_selection(hover)
            )

            daily_applications_chart = (lines + points + tooltips).interactive().configure_view(strokeWidth=0)

            st.write(f"#### Daily Job Applications Trend")
            st.altair_chart(daily_applications_chart, use_container_width=True)

# ---------------------------------------------------------------------------------------------------------------------------------------------------
        elif selected_trend == 'Weekly Applications Trend':
            st.write('You clicked Button 2!')

# ---------------------------------------------------------------------------------------------------------------------------------------------------

        elif selected_trend == 'Monthly Application Trend':
            # Group the data by year and month, and count the number of applications per month
            monthly_applications = data.groupby(['Year', 'Month'])['Date'].count().reset_index()
            monthly_applications = monthly_applications.rename(columns={'Date': 'Count'})

            # Create a new column that combines the Year and Month columns
            monthly_applications['YearMonth'] = pd.to_datetime(monthly_applications['Year'].astype(str) + ' ' + monthly_applications['Month'], format='%Y %B')
            monthly_applications = monthly_applications.sort_values('YearMonth')

            st.write(f"#### Monthly Job Applications Trend")

            # Creating a dropdown filters for year
            monthly_applications_selected_year = st.selectbox('Select year:', options=monthly_applications['Year'].unique(), index=0)

            # Creating the year filters
            monthly_applications_year_filter = monthly_applications[monthly_applications['Year'] == monthly_applications_selected_year]

            # Creating the bar chart
            monthly_applications_chart = alt.Chart(monthly_applications_year_filter).mark_bar().encode(
                x=alt.X('Month:N', title='Month', sort=None),
                y=alt.Y('Count:Q', title='Count of Applications Sent'),
                color=alt.Color('Count:Q', title='Year', legend=None),
                tooltip=['Year:N', 'Month:N', 'Count:Q']
            )
                
            # Add labels to the bars
            monthly_applications_text = monthly_applications_chart.mark_text(
                align='center',
                baseline='bottom',
                dy=-5,
                fontSize=18
            ).encode(
                text='Count:Q'
            )

            # Displaying the chart
            st.altair_chart((monthly_applications_chart + monthly_applications_text), use_container_width=True)
