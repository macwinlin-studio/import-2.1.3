# coding=utf-8
import sqlite3
def read(bh):
    con = sqlite3.connect('path.db')
    cur = con.cursor()
    cur.execute('select * from all_path')
    yz = cur.fetchall()
    if bh == 0:
        a = yz[1][1]
    elif bh == 1:
        a = yz[2][1]
    elif bh == 2:
        a = yz[3][1]
    elif bh == 3:
        a = yz[4][1]
    elif bh == 4:
        a = yz[5][1]
    elif bh == 5:
        a = yz[0][1]
    else:
        a = 'error'
    cur.close()
    con.close()
    return a
def pd(bh):
    if read(bh)[-1] != '\\':
        return True
    else:
        return False
def jd(a):
    if a == 'Python':
        return 0
    elif a == 'JavaScript':
        return 1
    elif a == 'HTML5':
        return 2
    elif a == 'JAVA':
        return 3
    elif a == 'C':
        return 4
    else:
        return 5
