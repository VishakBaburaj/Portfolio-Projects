# Importing libraries
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


# Reading linkedIn job application data
job_application_data = pd.read_csv("C:/Users/visha/Documents/Projects/linkedin_data_part_1/Jobs/Job Applications.csv")
job_application_data.head()

# Data processing steps

# Droping sensitive data
job_application_data = job_application_data[['Application Date',
                                            'Company Name', 
                                            'Job Title']]
        
# Droping duplicate rows
job_application_data.drop_duplicates(keep = 'first', inplace = True)

# Splitting the date and time column into separate columns
split_df = job_application_data['Application Date'].str.split(' ', expand = True)

# Assigning new column names
split_df.columns = ['Date', 'Time', 'AM/PM']

# Replacing missing or null values with NaN
split_df = split_df.replace('', pd.NA)

# Concatenating the split DataFrame with the original DataFrame
job_application_data = pd.concat([job_application_data, split_df], axis=1)

# Droping the 'Application Date', 'Time' and 'AM/PM' columns in place
job_application_data.drop(columns = ['Application Date', 'Time', 'AM/PM'], inplace = True)

# Converting the 'Date' column to a datetime data type
job_application_data['Date'] = pd.to_datetime(job_application_data['Date'])

# Droping the index column from the DataFrame
job_application_data = job_application_data.reset_index(drop=True)

# Data insights and visualization

# Grouping the DataFrame by the date column and counting the number of applications for each day
daily_applications = job_application_data.groupby('Date').size().reset_index(name='count')

# Ploting the data using a line chart
daily_applications_sent = px.line(daily_applications, x = 'Date', y = 'count')
daily_applications_sent.show()

# Exploring KPI's
#Total number of jobs applied
print(len(job_application_data), 'jobs applied')

# Grouping the data by job title and counting the number of occurrences
jobs_applied = job_application_data.groupby('Job Title').size().reset_index(name='count')
# Sorting the data by count in descending order and selecting the top 10 rows
top_jobs_applied = jobs_applied.sort_values("count", ascending=False).head(10)
# Sorting the top jobs by count in descending order
top_jobs_applied = top_jobs_applied.sort_values("count", ascending=True)

# Ploting the top jobs applied in a vertical bar chart
plt.barh(top_jobs_applied['Job Title'], top_jobs_applied['count'])
plt.title("Top 10 Job Titles Applied")
plt.xticks(rotation = 90)
plt.xlabel('Job Totle')
plt.ylabel('Number of jobs applied')
# Adding labels to the bars
for i, v in enumerate(top_jobs_applied["count"]):
    plt.text(v + 0, i, str(v), color="black", fontweight="bold", fontsize=16)

plt.show()





