<h1>Project: Data Modeling with Postgres</h1>

<br>
<br>
<br>

<h2>Introduction</h2>
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.
<br>
In this project, Sparkify database was created and ETL processes were developed to meet the above-mentioned needs.

<br>
<br>
<br>

<h2>Schema Design</h2>
Considering the needs, scheme structure preferred as star schema design. 
<br>
In this context, songplays, which is a table where song movements are kept, was created as a fact table. To provide detailed information to support this fact table, a user table, song table, artist table and time table were created as a dimension table.
<br>
The scheme design is as follows:
<br>
![deneme](https://github.com/onurozdem/udacity_data_engineer_project1/blob/dev/Schema.PNG)
<br>
<br>
<br>

<h2>ETL Pipeline</h2>
Scripts were created and added to the sql_queries.py file to provide the above schema structure, to create table, insert data and delete table.
By using the queries in this file in the crate_table.py file, it is possible to create a database and tables. For this, create_table.py file must be run before ETL processes. 
After the tables are created, the database will be ready for data entry. 
<br>
In this project, the data is located in the data folder in the main directory. There are song and user movement logs.
<br>
As seen in the sample song data below; song data provides information for songs and artists tables. The flow process_song_file has been developed for this in the etl.py file.

> {"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}

<br>

As seen in the sample user log data below; log data provides information for time, user and songplays tables. The flow process_log_file has been developed for this in the etl.py file. In addition, only NextPage log data are transferred to tables.
>{"artist":null,"auth":"Logged In","firstName":"Walter","gender":"M","itemInSession":0,"lastName":"Frye","length":null,"level":"free","location":"San Francisco-Oakland-Hayward, CA","method":"GET","page":"Home","registration":1540919166796.0,"sessionId":38,"song":null,"status":200,"ts":1541105830796,"userAgent":"\"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/36.0.1985.143 Safari\/537.36\"","userId":"39"}

<br>
In these ETL processes, necessary column mappings and filtering are made and transfers to the table are provided. 

<br>
<br>
<br>

<h2>Requirements</h2>
In order for the project to run smoothly, the libraries in requirements.txt must be installed with the following command.
<br>
>`pip install -r requirements.txt`
