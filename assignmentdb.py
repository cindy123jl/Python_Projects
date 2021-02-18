
import sqlite3

conn = sqlite3.connect('assigndb.db') #maintains connection with db

with conn: #execute command
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filelist TEXT \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('assigndb.db')

with conn:
    cur = conn.cursor() #inserting into table into column filename
    cur.execute("INSERT INTO tbl_files(col_filelist) VALUES \
                ('information.docx'))
    cur.execute("INSERT INTO tbl_files(col_filelist) VALUES (?)", \
                ('Hello.txt'))
    cur.execute("INSERT INTO tbl_files(col_filelist) VALUES (?)", \
                ('myImage.png'))
    cur.execute("INSERT INTO tbl_files(col_filelist) VALUES (?)", \
                ('myMovie.mpg'))
    cur.execute("INSERT INTO tbl_files(col_filelist) VALUES (?)", \
                ('World.txt'))
    cur.execute("INSERT INTO tbl_files(col_filelist) VALUES (?)", \
                ('data.pdf'))
    cur.execute("INSERT INTO tbl_files(col_filelist) VALUES (?)", \
                ('myPhoto.jpg'))
    conn.commit()
conn.close()




