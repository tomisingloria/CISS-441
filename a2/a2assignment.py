import csv
import sqlite3

db_file = 'swift_lyrics.db'
conn = sqlite3.connect(db_file)


def create_swift_table():
    """
    Here i am creating the table for my data.
    """
    c = conn.cursor()
    sql_str = """
        create table if not exists taylor_swift_lyrics (
        id integer primary key autoincrement,
        artist text,
        album text,
        track_title text,
        track_n int,
        lyric text,
        line int,
        year int
        );
        """
    c.execute(sql_str)
    conn.commit()


def process_csv_file():

    c = conn.cursor()

    with open('taylor_swift_lyrics.csv', 'r') as csvfile:

        # parse csv file pointer into hero_stream
        swift_stream = csv.DictReader(csvfile, delimiter=',', quotechar='"')

        # interate over hero_stream to process. 
        for r_ct, taylor_swift_lyrics_row in enumerate(swift_stream):

            t_artist = taylor_swift_lyrics_row['artist']
            t_album= taylor_swift_lyrics_row['album']
            t_track = taylor_swift_lyrics_row['track_title']
            t_number = taylor_swift_lyrics_row['track_n']
            t_lyric = taylor_swift_lyrics_row['lyric'].replace("'","''")
            t_line = taylor_swift_lyrics_row['line']
            t_year = taylor_swift_lyrics_row['year']


            # only show the first 20 rows. 
            if r_ct <= 50:
                strsql = """
                    insert into taylor_swift_lyrics ( artist,album,track_title,track_n,
                    lyric, line, year) values (
                    '{t_artist}',
                    '{t_album}',
                    '{t_track}',
                     {t_number},
                    '{t_lyric}',
                     {t_line},
                     {t_year}
                    );
                """.format(
                    t_artist=t_artist,
                    t_album=t_album,
                    t_track=t_track,
                    t_number=t_number,
                    t_lyric=t_lyric,
                    t_line=t_line,
                    t_year=t_year
                )
                #print(strsql)          ### troubleshooting
                c.execute(strsql)
                conn.commit()

            # only show the first 20 rows. 
            if r_ct <= 20:
                print(r_ct, t_album, t_track, t_lyric)


def main():
    print('Creating a Taylor Swift lyric database from a csv file.')
    create_swift_table()
    process_csv_file()

if __name__ == "__main__":
    main()
