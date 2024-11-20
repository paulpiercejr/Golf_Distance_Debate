# Golf Distance Debate

This project was developed to analyze the data of the PGA TOUR, all 4 men's Major Championship golf tournaments, and the attributes of the courses that the tournaments from 1980-2022 were played on. It was done to rebut the claims made by the USGA and R&A that distance is a major problem in elite golf. Data from the PGA TOUR and Major Championships was chosen because it is the most robust dataset over the past 40+ years.

To complete this project I webscraped of all stats from PGATOUR.com using Python with the Pandas, BeautifulSoup, and Selenium libraries. I also webscraped data from all four major championships. I collected statistics in PDF form and using simple data entry methods from various sources to complete data validation where entries were incomplete. Those stats were then cleaned and transformed using both manual techniques in Excel and automated techniques in Python. Once the validity of the data was confirmed, it was loaded into a MySQL database using both the LOAD DATA INFILE method within SQL and by using the Table Data Import Wizard in MySQLWorkbench. From there, the data was analyzed based on conclusion made by the USGA and R&A in their final Distance Insights Report in 2020. https://www.usga.org/content/dam/usga/pdf/2020/distance-insights/DIPR-FINAL-2020-usga.pdf 

## Scrape Scripts by Category

This folder includes the Python scripts to pull data from PGATOUR.com on each statistical category that was used for analysis. These scripts most likely need to be edited to scrape the site as there have been many updates to PGATOUR.com since this project was completed. Many of these scripts had to be re-written during the project as they made a major change to their website while I was in the middle of pulling data, thus killing all of the scripts. These scripts pull data for every available year from 1980-2022. These categories will list all players that qualified for these statistics based on number of rounds played and status as members of the tour. Golfers that do not qualify will not be included.

Categories:
1. Birdie average
2. Birdie or better conversion
3. Bogey average
4. Bonus putting
5. Driving accuracy
6. Driving distance
7. Green or fringe in regulation
8. Greens in regulation from fairway
9. Greens in regulation
10. Missed fairway from other
11. One-putt percentage
12. Par 3 birdie or better
13. Par 3 performance
14. Par 4 birdie or better
15. Par 4 performance
16. Par 5 birdie or better
17. Par 5 performance
18. Percent of potential money won
19. Proximity to the hole
20. Putting average
21. Putts per round
22. Scrambling
23. Strokes Gained (SG) total
24. SG approach green
25. SG putting
26. SG off the tee
27. SG tee to green
28. Stroke differential vs field average
29. Three plus putts per round
30. Three putt avoidance
31. Three putts per round
32. Total birdies
33. Total eagles
34. Total putting

## Scrape Scripts by Player or Tournament

This folder includes scripts to pull data from each players' profile including demographic data and all statistics. This will pull many statistics that were already pulled in the Category scripts, but will also provide more data that is not included in those scripts, plus it pulls data on players that may not have qualified to be part of those categories and therefore may not be included in them.

1. Pull-PGA-Tour-Player-Info.py - pulls data on all players listed in the PGA players list on PGATOUR.com
2. pga-tour-schedule.py - pulls the schedule information from PGATOUR.com
3. wiki-tour-schedule-winners.py - pulls the data about each tournament from Wikipedia. This data was validated as accurate through manual means, but pulled as it was faster to get information about winners of each tournament. 

## PGA Tour Data Schedule

This folder includes PGA Tour media guides from most years between 1980 and 2022. Many of these are in PDF format and the extract PDF feature of Tableau was used to convert this information to CSV files. This data was then manually evaluated and validated to ensure accuracy.

## Database Files

This folder contains the CSV files that are loaded into the MySQL database. The file named pga-data-schema.sql that is listed in the database section below uses LOAD DATA INFILE function to load each of these CSV files to the database. Read notes for that file to find out more.

## Database

This folder contains all the SQL scripts that create the schema, load the data, query the database, and create CSV files from queries for use in Tableau for analysis and visualization.

1. pga-data-schema.sql - Creates the schema and loads all data from database files folder via LOAD DATA INFILE. If that function fails to load, the SQL script may need to be modified to eliminate the loading of the data. It may also require some or all constraints to be disabled to load the data, though I would advise against that in case some data is not formatted correctly. In that case, create each table in order and load the data via another means such as MySQLWorkbench Table Data Import Wizard. Don't forget to re-enable all constraints.
2. pga-tour-queries.sql - has a list of the queries run to perform data anlysis
3. create_spreadsheets_pga.sql - has queries which are exported to CSV files for analysis and visualization

## Data Points CSVs

Folder contains all the CSV files that were created when the webscrape pulled the data. It also contains folders that have aggregates of the data where they were combined to make files that are more useful for analysis.

The Distance Analysis folder within contains a script to be able to analyze distance.

## Tools used on project

- Python [Pandas, BeautifulSoup, Selenium] (Webscrape, data cleaning and transformation)
- Excel (Data cleaning and transformation, data validation, exploratory data analysis)
- MySQL (Database creation, data type validation, querying, exploratory data analysis, data export for visualization)
- MySQLWorkbench (Run SQL code and manage database)
- Tableau (Conversion of PDF tables, In-depth data analysis, data visualization, data reporting and sharing)


### NOTE: Many of the file paths within the script files may need to be evaluated to make sure they are still accurate as sites and paths have likely changed.
