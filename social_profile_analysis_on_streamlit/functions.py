# Importing libraries
import pandas as pd
import streamlit as st
import altair as alt

#------------------------------------------------------------------------------------------------------------------------------------------------
# Processing the data
def process_linkedin_job_app_data(data):

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
    # Droping the index from the DataFrame
    data = data.reset_index(drop=True)
    # Extracting weekday, month and year from Date into separate columns
    data['Weekday'] = data['Date'].dt.day_name()
    data['Month'] = data['Date'].dt.strftime('%B')
    data['Year'] = data['Date'].dt.year

    return data

#------------------------------------------------------------------------------------------------------------------------------------------------
# Displaying the KPIs
def display_kpis(data):

    # Divide the screen into two equal parts
    col1, col2 = st.columns(2)

    # Total jobs applied KPI
    total_jobs_applied = len(data)

    # Displaying the total count of jobs applied as a KPI in the first column
    if total_jobs_applied >= 0:
        col1.success(f"**Total Jobs Applied:** {total_jobs_applied}")
    else:
        col1.error(f"**Total Jobs Applied:** {total_jobs_applied}")

    # Average jobs applied per day KPI
    # Calculating the number of days over which the jobs were applied
    num_days = (data['Date'].max() - data['Date'].min()).days + 1

    # Calculating the average jobs applied per day
    average_jobs_per_day = total_jobs_applied / num_days

    # Displaying the average jobs applied per day as a KPI in the second column
    if average_jobs_per_day >= 0:
        col2.success(f"**Average Jobs Applied Per Day:** {average_jobs_per_day:.0f}")
    else:
        col2.error(f"**Average Jobs Applied Per Day:** {average_jobs_per_day:.0f}")

    # Adding a horizontal line
    st.write('---')

#------------------------------------------------------------------------------------------------------------------------------------------------
# Displaying the top 10 insights
def display_top_10_insights(data):

    # Selecting the job roles and companies
    top_10_options = ['Top 10 Job Roles Applied', 'Top 10 Companies Applied']
    selected_top_10_options = st.radio('###### Select an insight:', top_10_options)

    # Displaying the selected options
    if selected_top_10_options == 'Top 10 Job Roles Applied':
        # Grouping the data by job title and counting the number of occurrences
        jobs_applied = data.groupby('Job Title').size().reset_index(name='count')

        # Sorting the data by count in descending order and selecting the top 10 rows
        top_jobs_applied = jobs_applied.sort_values("count", ascending=False).head(10)

        # Creating the chart
        top_jobs_applied_chart = alt.Chart(top_jobs_applied).mark_bar().encode(
            x=alt.X('count:Q', title='Count of Jobs Applied'),
            y=alt.Y('Job Title:O', title='Job Titles', sort='-x'),
            color=alt.Color('count:Q', legend=None),
            tooltip=['Job Title:O', 'count:Q']
        )

        # Adding labels for the count of jobs applied
        top_jobs_applied_text = top_jobs_applied_chart.mark_text(
            align='left',
            baseline='middle',
            dx=5,
            fontSize=18
        ).encode(
            text='count:Q'
        )

        st.write(f"#### Top 10 Job Roles Applied")

        # Displaying the chart and the count of jobs applied
        st.altair_chart(top_jobs_applied_chart + top_jobs_applied_text, use_container_width=True)

        # Adding a horizontal line
        st.write('---')

    #----------------------------------------------------------------------------------------------------------------------------------------------
    
    elif selected_top_10_options == 'Top 10 Companies Applied':

        # Grouping the data by company name and counting the number of occurrences
        companies_applied = data.groupby('Company Name').size().reset_index(name='count')

        # Sorting the data by count in descending order and selecting the top 10 rows
        top_companies_applied = companies_applied.sort_values("count", ascending=False).head(10)

        # Creating the chart
        top_companies_applied_chart = alt.Chart(top_companies_applied).mark_bar().encode(
            x=alt.X('count:Q', title='Count of Companies Applied'),
            y=alt.Y('Company Name:O', title='Company Names', sort='-x'),
            color=alt.Color('count:Q', legend=None),
            tooltip=['Company Name:O', 'count:Q']
        )

        # Adding labels for the count of companies applied
        top_companies_applied_text = top_companies_applied_chart.mark_text(
            align='left',
            baseline='middle',
            dx=5,
            fontSize=18
        ).encode(
            text='count:Q'
        )

        st.write(f"#### Top 10 Companies Applied")

        # Displaying the chart and the count of companies applied
        st.altair_chart(top_companies_applied_chart + top_companies_applied_text, use_container_width=True)

        # Adding a horizontal line
        st.write('---')

#------------------------------------------------------------------------------------------------------------------------------------------------
# Displaying daily, weekly and monthly insights
def display_daily_weekly_monthly_insights(data):
    
    # Selecting the insights
    daily_weekly_monthly_options = ['Daily Job Application Trend', 'Weekly Job Application Trend', 'Monthly Job Application Trend']
    selected_daily_weekly_monthly_options = st.radio('###### Select an insight:', daily_weekly_monthly_options)

    # Displaying the selected options
    if selected_daily_weekly_monthly_options == 'Daily Job Application Trend':
        # Grouping the data by date and counting the number of occurrences
        daily_jobs_applied = data.groupby('Date').size().reset_index(name='count')

        # Sorting the data by count in descending order
        daily_jobs_applied = daily_jobs_applied.sort_values("count", ascending=False)

        # Creating the chart
        # Daily trend line chart
        source = daily_jobs_applied
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

        daily_application_chart = (lines + points + tooltips).interactive().configure_view(strokeWidth=0)

        st.write(f"#### Daily Job Application Trend")
        st.altair_chart(daily_application_chart, use_container_width=True)

# ---------------------------------------------------------------------------------------------------------------------------------------------------

    elif selected_daily_weekly_monthly_options == 'Weekly Job Application Trend':
        st.write(f"#### Weekly Job Application Trend")

# ---------------------------------------------------------------------------------------------------------------------------------------------------

    elif selected_daily_weekly_monthly_options == 'Monthly Job Application Trend':
        # Group the data by year and month, and count the number of applications per month
        monthly_jobs_applied = data.groupby(['Year', 'Month'])['Date'].count().reset_index()
        monthly_jobs_applied = monthly_jobs_applied.rename(columns={'Date': 'Count'})

        # Create a new column that combines the Year and Month columns
        monthly_jobs_applied['YearMonth'] = pd.to_datetime(monthly_jobs_applied['Year'].astype(str) + ' ' + monthly_jobs_applied['Month'], format='%Y %B')
        monthly_jobs_applied = monthly_jobs_applied.sort_values('YearMonth')

        st.write(f"#### Monthly Job Application Trend")

        # Creating a dropdown filters for year
        monthly_jobs_applied_selected_year = st.selectbox('Select year:', options=monthly_jobs_applied['Year'].unique(), index=0)

        # Creating the year filters
        monthly_jobs_applied_year_filter = monthly_jobs_applied[monthly_jobs_applied['Year'] == monthly_jobs_applied_selected_year]

        # Creating the bar chart
        monthly_application_chart = alt.Chart(monthly_jobs_applied_year_filter).mark_bar().encode(
            x=alt.X('Month:N', title='Month', sort=None),
            y=alt.Y('Count:Q', title='Count of Applications Sent'),
            color=alt.Color('Count:Q', title='Year', legend=None),
            tooltip=['Year:N', 'Month:N', 'Count:Q']
        )
            
        # Add labels to the bars
        monthly_application_text = monthly_application_chart.mark_text(
            align='center',
            baseline='bottom',
            dy=-5,
            fontSize=18
        ).encode(
            text='Count:Q'
        )

        # Displaying the chart
        st.altair_chart((monthly_application_chart + monthly_application_text), use_container_width=True)


