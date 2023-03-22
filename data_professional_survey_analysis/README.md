# Exploring the Landscape of Data Analyst Roles in the United States:
# An Exploratory Analysis

## Project Overview
As an entry-level data analyst with F1 OPT work authorization in the United States. This project aims to understand the scope of data analyst roles in the United States. The project aims to identify the following key points:
* The satisfaction levels with work-life balance and upward mobility among data analysts in the United States.
* The preferred programming languages among data analysts in the United States.
* The difficulty of transitioning into a data analyst role from a different career path in the United States.

## Stakeholders
* Entry-level data analysts in the United States.
* General public in the United States.

## Google Sheet
https://docs.google.com/spreadsheets/d/1rau8clY4md4wYJyrEekmnjRKfGZL37iF/edit#gid=1128230716

## Dashboard
https://app.powerbi.com/view?r=eyJrIjoiMWIzOGI2NDgtZGE2YS00MTYzLWEzYzItZGM1MWQ4MTUxMDA3IiwidCI6ImI4ZTNmM2I3LWNkNGUtNDI0Ny1hOGIwLWEwZGIxOTYwODZmMiIsImMiOjF9

![](https://github.com/VishakBaburaj/Portfolio-Projects/blob/master/data_professional_survey_analysis/Figures/Dashboard.png)

## Description of the Data Source
* The open dataset used for this analysis is provided by Alex Freberg.
* For this analysis, the data has been collected from 10 June 2022 to 26 June 2022.
* The dataset contains 630 rows and 28 columns.

## Data Cleaning and Manipulation
The following steps were taken to clean and prepare the survey data for analysis:
Step 1: Duplicated the survey data in Google Sheets to ensure that the original data remained unaltered during the cleaning process.
Step 2: 1. Deleted irrelevant columns, assigned filters, and renamed remaining columns for clarity.
Step 3:
Cleaned the “Current Roles” column by creating a new “Other Roles” column by using the “Split Text to Columns” function.
Grouped other related roles into the “Current Roles” category and corrected spelling errors by using the find and replace tool.
Added a new column called “Current roles cleaned” which consists of all the “Current Roles” with the “Other Roles” that were grouped under the “Current Roles” category.
Step 4: Used a pivot table to determine the distribution of current roles in the sample size.
![](https://github.com/VishakBaburaj/Portfolio-Projects/blob/master/data_professional_survey_analysis/Figures/Fig%203.1.png)
Step 5:
Cleaned the “Country” column by creating a new “Other Country” column by using the “Split Text to Columns” function.
Grouped countries, and corrected spelling errors by using the find and replace tool.
Added a new column called “Country Cleaned” which consists of the “Country” column with the “Other Country” column that was grouped.
Step 6: Used a pivot table to determine the distribution of countries in the sample size.
![](https://github.com/VishakBaburaj/Portfolio-Projects/blob/master/data_professional_survey_analysis/Figures/Fig%203.2.png)
Step 7: Cleaned the “Favorite Programming Language” column by separating the “Other Favorite Programming Language” using the “Split Text to Columns” function.
Step 8: Filtered and copied all data analyst respondents to another sheet to narrow down data to the project objective for further analysis.
Step 9: Deleted columns that were added to clean certain columns and renamed the remaining columns for clarity.
Step 10:
Used conditional formatting to identify missing values in the data analyst dataset.
The missing values in the “Highest Level of Education” attribute were replaced with “Null.
Conditional formatting revealed that 4 observations had null values in both the “Work-Life Balance” and “Upward Mobility” columns. Additionally, there were 3 observations that had missing values only in the “Upward Mobility” column.
It was determined that since these 7 observations were not from the United States, the data from the United States was filtered and copied to a separate sheet for the data analysis process.

## Data Analysis
The total number of data analyst respondents from the United States was determined by creating a card visualization.
The average age of data analyst respondents from the United States was determined by creating a card visualization.
The start and end dates of the data collection were determined by creating card visualizations.
The average satisfaction levels with upward mobility and work-life balance among data analysts in the United States were determined by creating gauge visualizations.
The preferred programming languages among data analysts in the United States were determined by creating a bar graph visualization.
The difficulty of transitioning into a data analyst role from a different career path in the United States was determined by creating a 100% stacked bar chart visualization.

Note: In order to custom sort the 100% stacked bar chart the following source was referred.
https://devoworx.net/power-bi-custom-sort-order-bar-chart/

To further analyze the data, the following questions were answered:
1. What is the satisfaction level with work-life balance among data analysts in the United States?
![](https://github.com/VishakBaburaj/Portfolio-Projects/blob/master/data_professional_survey_analysis/Figures/Fig%203.3.png)
2. What is the satisfaction level with upward mobility among data analysts in the United States?
![](https://github.com/VishakBaburaj/Portfolio-Projects/blob/master/data_professional_survey_analysis/Figures/Fig%203.4.png)
3. What is the preferred programming language among data analysts in the United States?
![](https://github.com/VishakBaburaj/Portfolio-Projects/blob/master/data_professional_survey_analysis/Figures/Fig%203.5.png)
4. What is the difficulty level of transitioning into a data analyst role from a different career path in the United States?
![](https://github.com/VishakBaburaj/Portfolio-Projects/blob/master/data_professional_survey_analysis/Figures/Fig%203.6.png)
The visualizations created provide insights into the answers to these questions and reveal trends in the data analyst community in the United States.

## Key Findings
* The data indicates that on average, data analysts in the United States have a moderate level of satisfaction with their work-life balance, with a score of 6.62 out of 10. This suggests that while there may be room for improvement in balancing work and personal life for these respondents, they still have a relatively positive view of their current situation. Further analysis could be conducted to understand the specific factors contributing to this score and identify areas for improvement.
* The data indicates that on average, data analysts in the United States have a moderate level of dissatisfaction with their upward mobility, with a score of 5.14 out of 10. This suggests that many of these respondents may feel limited in their career advancement opportunities. Further analysis should be conducted to understand the reasons behind this low satisfaction score and identify potential solutions to improve it.
* The data indicates that the preferred programming language among data analysts in the United States is Python, with 92 out of 168 respondents (55%) choosing it as their preferred language. This highlights the widespread use and popularity of Python among data analysts.
* The data indicates that individuals who switched careers to become data analysts found the transition to be more challenging, with 28.97% reporting difficult and 6.54% reporting very difficult experiences. In comparison, those who did not switch careers reported facing less difficulty in their transition to a data analyst role, with 16.39% reporting difficult and 3.28% reporting very difficult experiences. This highlights the potential challenges for individuals looking to switch careers into data analysis and the importance of considering these difficulties in career transition planning.

## Recommendations
* Addressing work-life balance: Further analysis should be conducted to understand the specific factors contributing to the moderate satisfaction score for work-life balance and identify areas for improvement. Solutions could include flexible working arrangements, better time management tools, and resources, or improved support for personal time and activities outside of work.
* Improving upward mobility: To improve satisfaction with upward mobility, it is important to understand the reasons behind the low satisfaction score. Potential solutions could include offering more training and development opportunities, improving promotion processes, or increasing transparency in career advancement paths.
* Addressing challenges in career transition: Offering support for individuals who are facing challenges in transitioning to a data analyst career. This could include support for overcoming specific obstacles, such as obtaining relevant certifications or finding job opportunities, as well as guidance on how to navigate the challenges of a new career.

## Appendix
![](https://github.com/VishakBaburaj/Portfolio-Projects/blob/master/data_professional_survey_analysis/Figures/Fig%203.7.png)
![](https://github.com/VishakBaburaj/Portfolio-Projects/blob/master/data_professional_survey_analysis/Figures/Fig%203.8.png)
![](https://github.com/VishakBaburaj/Portfolio-Projects/blob/master/data_professional_survey_analysis/Figures/Fig%203.9.png)
![](https://github.com/VishakBaburaj/Portfolio-Projects/blob/master/data_professional_survey_analysis/Figures/Fig%203.10.png)
