# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id INT NOT NULL, 
                        start_time INT NOT NULL, 
                        user_id INT NOT NULL, 
                        level VARCHAR, 
                        song_id INT NOT NULL, 
                        artist_id INT NOT NULL, 
                        session_id INT, 
                        location VARCHAR, 
                        user_agent VARCHAR, 
                        PRIMARY KEY(songplay_id),
                        FOREIGN KEY (song_id) REFERENCES songs (song_id) ON DELETE CASCADE,
                        FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE,
                        FOREIGN KEY (artist_id) REFERENCES artists (artist_id) ON DELETE CASCADE,
                        FOREIGN KEY (start_time) REFERENCES time (start_time) ON DELETE CASCADE);
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id INT NOT NULL, 
                    first_name VARCHAR NOT NULL, 
                    last_name VARCHAR NOT NULL, 
                    gender VARCHAR, 
                    level VARCHAR,
                    PRIMARY KEY(user_id));
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id INT NOT NULL, 
                    title VARCHAR, 
                    artist_id INT NOT NULL, 
                    year INT, 
                    duration FLOAT,
                    PRIMARY KEY(song_id));
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id INT NOT NULL, 
                      name VARCHAR NOT NULL, 
                      location VARCHAR, 
                      latitude FLOAT, 
                      longitude FLOAT,
                      PRIMARY KEY(artist_id));
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time INT NOT NULL, 
                   hour INT, 
                   day INT, 
                   week VARCHAR, 
                   month INT, 
                   year INT, 
                   weekday INT,
                   PRIMARY KEY(start_time));
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (songplay_id, 
                       start_time, 
                       user_id, 
                       level, 
                       song_id, 
                       artist_id, 
                       session_id, 
                       location, 
                       user_agent)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (songplay_id) 
        DO NOTHING;
""")

user_table_insert = ("""INSERT INTO users (user_id, 
                   first_name, 
                   last_name, 
                   gender, 
                   level)
        VALUES(%s, %s, %s, %s, %s)
        ON CONFLICT (user_id) 
        DO NOTHING;
""")

song_table_insert = ("""INSERT INTO songs (song_id, 
                   title, 
                   artist_id, 
                   year, 
                   duration)
        VALUES(%s, %s, %s, %s, %s)
        ON CONFLICT (song_id) 
        DO NOTHING;
""")

artist_table_insert = ("""INSERT INTO artists (artist_id, 
                     name, 
                     location, 
                     latitude, 
                     longitude)
        VALUES(%s, %s, %s, %s, %s)
        ON CONFLICT (artist_id) 
        DO NOTHING;
""")


time_table_insert = ("""INSERT INTO time (start_time, 
                  hour, 
                  day, 
                  week, 
                  month, 
                  year, 
                  weekday)
        VALUES(%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (start_time) 
        DO NOTHING;
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]