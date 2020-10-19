import os
import glob
import psycopg2
import pandas as pd
import numpy as np
from sql_queries import *


def process_song_file(cur, filepath):
    """
        Reads song file and inserts to raleted table(songs and artists) with given cursor. 
    """
    # open song file
    df = pd.read_json(filepath, lines=True)

    try:
        # insert song record
        song_data = df[["song_id", "title", "artist_id", "year", "duration"]].values[0]
        cur.execute(song_table_insert, song_data)
    except psycopg2.Error as e:
        print("Song Record Insert Error for {}!".format(filepath))
        raise e
    
    try:
        # insert artist record
        artist_data = df[["artist_id", "artist_name", "artist_location", "artist_latitude", "artist_longitude"]].values[0]
        cur.execute(artist_table_insert, artist_data)
    except psycopg2.Error as e:
        print("Artist Record Insert Error for {}!".format(filepath))
        raise e

def process_log_file(cur, filepath):
    """
        Reads log file and inserts to raleted table(time, user and songplays) with given cursor. 
    """
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[(df.page == "NextSong")]

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], unit='ms')
    
    # insert time data records
    time_data = (df['ts'], t.dt.hour, t.dt.day, t.dt.week, t.dt.month, t.dt.year, t.dt.weekday)
    column_labels = ("start_time", "hour", "day", "week", "month", "year", "weekday")
    time_df = pd.DataFrame(data={column_labels[0]:time_data[0], column_labels[1]:time_data[1], column_labels[2]:time_data[2], column_labels[3]:time_data[3], column_labels[4]:time_data[4], column_labels[5]:time_data[5], column_labels[6]:time_data[6]})

    for i, row in time_df.iterrows():
        try:
            cur.execute(time_table_insert, list(row))
        except psycopg2.Error as e:
            print("Time Record Insert Error for {} - line_no:{}!".format(filepath, i+1))
            print(e)

    # load user table
    user_df = pd.DataFrame({"user_id": df["userId"], "first_name": df["firstName"], "last_name": df["lastName"], "gender": df["gender"], "level": df["level"]})

    # insert user records
    for i, row in user_df.iterrows():
        try:
            cur.execute(user_table_insert, row)
        except psycopg2.Error as e:
            print("User Record Insert Error for {} - line_no:{}!".format(filepath, i+1))
            print(e)

    # insert songplay records
    for index, row in df.iterrows():
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = songplay_data = (row.ts, 
                     row.userId, 
                     row.level, 
                     songid, 
                     artistid, 
                     row.sessionId, 
                     row.location, 
                     row.userAgent)
        try:
            cur.execute(songplay_table_insert, songplay_data)
        except psycopg2.Error as e:
            print("Songplay Record Insert Error for {} - line_no:{}!".format(filepath, index+1))
            print(e)

def process_data(cur, conn, filepath, func):
    """
        Finds all json files paths by given filepath and call function with given func for start insert flow.  
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        try:
            func(cur, datafile)
            conn.commit()
            print('{}/{} files processed.'.format(i, num_files))
        except Exception as e:
            print(e)

def main():
    """
        - Establishes connection with the sparkify database and gets
    cursor to it.  
        - Trigger sequentially data insert proccesses 
        - Finally close connection
    """
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
        
    try:
        cur = conn.cursor()

        process_data(cur, conn, filepath='data/song_data', func=process_song_file)
        process_data(cur, conn, filepath='data/log_data', func=process_log_file)
    except Exception as e:
        print(e)
    finally:
        conn.close()


if __name__ == "__main__":
    main()