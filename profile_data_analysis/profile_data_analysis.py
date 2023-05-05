# Importing libraries
import streamlit as st
import pandas as pd
import altair as alt
# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Setting the page title and layout
st.set_page_config(page_title = 'LinkedIn Data Analysis',
                   page_icon=None,
                   layout = 'centered', initial_sidebar_state="auto")

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Data Processing Function for LinkedIn Job Application Data
def process_linkedin_job_app_data(uploaded_file):
    # Reading the CSV file
    data = pd.read_csv(uploaded_file)
    # Droping sensitive data
    data = data[['Application Date', 'Company Name', 'Job Title']]
    # Droping duplicate rows
    data.drop_duplicates(keep='first', inplace=True)
    # Splitting the date and time column into separate columns
    split_df = data['Application Date'].str.split(' ', expand=True)
    # Assigning new column names
    split_df.columns = ['Date', 'Time', 'AM/PM']
    # Replacing missing or null values with NaN
    split_df = split_df.replace('', pd.NA)
    # Concatenating the split DataFrame with the original DataFrame
    data = pd.concat([data, split_df], axis=1)
    # Droping the 'Application Date', 'Time' and 'AM/PM' columns in place
    data.drop(columns=['Application Date', 'Time', 'AM/PM'], inplace=True)
    # Converting the 'Date' column to a datetime data type
    data['Date'] = pd.to_datetime(data['Date'])
    # Droping the index column from the DataFrame
    data = data.reset_index(drop=True)
    return data

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Setting the first level sidebar options
options_level_1 = ['LinkedIn','Instagram']
selected_option_level_1 = st.sidebar.radio('Choose an application', options_level_1)

# Adding a horizontal line between the first and second level options
st.sidebar.markdown('---')

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# If the selected option is "LinkedIn", display the second level of the sidebar
if selected_option_level_1 == 'LinkedIn':
    options_level_2_for_linkedin = ['LinkedIn Job Application', 'LinkedIn Connections']
    selected_option_level_2_for_linkedin = st.sidebar.radio('Choose an insight', options_level_2_for_linkedin)

    # Setting sidebar "LinkedIn" - "LinkedIn Job Application"
    if selected_option_level_2_for_linkedin  == 'LinkedIn Job Application':

        # Setting title of the page
        st.markdown('## LinkedIn Job Application')

        st.set_option('deprecation.showfileUploaderEncoding', False)  # Disable warning message

        # Uploading the csv data
        uploaded_file = st.file_uploader('Upload the Job Application CSV file', type = 'csv')

        # After uploading the csv data
        if uploaded_file is not None:

            # Precessing the data
            data = process_linkedin_job_app_data(uploaded_file)

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

            # Grouping the data by job title and counting the number of occurrences
            jobs_applied = data.groupby('Job Title').size().reset_index(name='count')

            # Sorting the data by count in descending order and selecting the top 10 rows
            top_jobs_applied = jobs_applied.sort_values("count", ascending=False).head(10)

            # Creating the chart
            chart = alt.Chart(top_jobs_applied).mark_bar().encode(
                x=alt.X('count:Q', title='Count of Jobs Applied'),
                y=alt.Y('Job Title:O', title='Job Title', sort='-x'),
                color=alt.Color('count:Q', legend=None)
            ).properties(
                title='Top 10 Job Titles Applied'
            )

            # Adding labels for the count of jobs applied
            text = chart.mark_text(
                align='left',
                baseline='middle',
                dx=5,
                fontSize=18
            ).encode(
                text='count:Q'
            )

            # Displaying the chart and the count of jobs applied
            st.altair_chart(chart + text, use_container_width=True)

            # Adding a horizontal line
            st.write('---')

# ---------------------------------------------------------------------------------------------------------------------------------------------------
            
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
                alt.Chart(source)
                .mark_line(point="transparent")
                .encode(x=alt.X(x, title="Date", axis=alt.Axis(labelFontSize=15, titleFontSize=15)), 
                        y=alt.Y(y, title="Count of Jobs Applied", axis=alt.Axis(labelFontSize=15, titleFontSize=15))
                        )
                .transform_calculate(color='datum.delta < 0 ? "red" : "lightblue"') # doesn't show red for negative delta
            )
            points = (
                lines.transform_filter(hover)
                .mark_circle(size=50)
                .encode(color=alt.Color("color:N", scale=None))
            )
            tooltips = (
                alt.Chart(source)
                .mark_rule(opacity=0)
                .encode(
                    x=x,
                    y=y,
                    tooltip=[y, x],
                )
                .add_selection(hover)
            )

            daily_app_chart = (lines + points + tooltips).interactive().configure_view(strokeWidth=0)

            st.write(f"###### Daily Job Applications Sent")
            st.altair_chart(daily_app_chart, use_container_width=True)

# ---------------------------------------------------------------------------------------------------------------------------------------------------
    # Setting sidebar "LinkedIn" - "LinkedIn Connections Insights"
    elif selected_option_level_2_for_linkedin  == 'LinkedIn Connections':

        # Setting title of the page
        st.title('LinkedIn Connections')

        st.set_option('deprecation.showfileUploaderEncoding', False)  # Disable warning message



# If the selected option is "Instagram", display the second level of the sidebar
elif selected_option_level_1 == 'Instagram':
    options_level_2_for_instagram = ['Option 1', 'Option 2']
    selected_option_level_2_for_instagram = st.sidebar.radio('Choose an insight', options_level_2_for_instagram)

    # Setting sidebar "Instagram" - "Option 1"
    if selected_option_level_2_for_instagram  == 'Option 1':
        st.write('Coming Soon')


    # Setting sidebar "Instagram" - "Option 2"
    elif selected_option_level_2_for_instagram  == 'Option 2':
        st.write('Coming Soon')


