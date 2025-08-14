# Task 1
## Gather Data Using APIs
The assignment is to obtain the number of job openings using the GitHub Jobs API for technologies such as:
- Java
- Python
- MySQL
- C++
- C#
  
Since GitHub Jobs has been deprecated, a custom JOBS_API backend will be hosted on Flask to mimic the service. The data will be populated from the following source: https://www.kaggle.com/promptcloud/jobs-on-naukricom under a Public Domain license.
> Note: A modified subset of the dataset is being used rather than the dataset from the original source. The original dataset is in CSV format and has been converted to JSON to meet the requirements of this project.

### Github Jobs Information
GitHub Jobs API allows anyone to query for the jobs based upon:
- Technology like Python, MySQL
- City like New York, Bangalore

Here are the technical details to access the API.

The GitHub Jobs API allows you to search, and view jobs with JSON over HTTP.

To obtain the JSON representation of any search result or job listing, .json should be appended to the URL used on the HTML GitHub Jobs site.

For example, the below URL will search for Python jobs near New York:
https://jobs.github.com/positions?description=python&location=new+york

To get the JSON representation of those jobs, just use positions.json:
https://jobs.github.com/positions.json?description=python&location=new+york

Pagination is also supported by the API. For example, /positions.json will return only 50 positions at a time. Results can be paginated by adding a page parameter to the queries.

Pagination starts by default at 0.

Examples:</br>
https://jobs.github.com/positions.json?description=ruby&page=1</br>
https://jobs.github.com/positions.json?page=1&search=code</br>

GET /positions.json Search for jobs by term, location, full-time vs part-time, or any combination of the three. All parameters are optional.

Parameters description — A search term, such as “ruby” or “java”. This parameter is aliased to search. location — A city name, zip code, or other location search term. lat — A specific latitude. If used, you must also send long and must not send location. long — A specific longitude. If used, you must also send lat and must not send location. full_time — If you want to limit results to full-time positions set this parameter to ‘true’.</br>
Examples:</br>
https://jobs.github.com/positions.json?description=python&full_time=true&location=sf</br>
https://jobs.github.com/positions.json?search=node</br>
https://jobs.github.com/positions.json?lat=37.3229978&long=-122.0321823</br>

GET /positions/ID.json Retrieve the JSON representation of a single job posting.

Parameters markdown — Set to ‘true’ to get the description and how_to_apply fields as Markdown.</br>
Examples:</br>
https://jobs.github.com/positions/21516.json</br>
https://jobs.github.com/positions/21516.json?markdown=true

## Gather Data Using Web Scraping
Gather Average Salary Information from this website: https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html

The data required to be scraped includes the name of the programming language and the average annual salary.
- Extract information from a given web site
- Write the scraped data into a csv file.

## Exploring Data
Goals:
- Load the dataset that will be used throughout the capstone project.
- Explore the dataset.
- Get familier with the data types.
