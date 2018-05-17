from django.http import HttpResponse
import MySQLdb
import pymongo
from classcast_test_submissions.v2.dbv import *

sql_user = MYSQL_USER
sql_pswd = MYSQL_PSWD
mysql_db = MYSQL_DB
mongo_db = MONGO_DB


def get_all_student_test_submission(user_id):
    
    try:
        db_mysql = MySQLdb.connect(user=sql_user, passwd=sql_pswd, db=mysql_db) # Establishing MySQL connection
    except:
        print "MySQL connection not established"
        return HttpResponse("MySQL connection not established") # MySQL could not be connected

    query = "select * from classcast_test_submissions where student_id=%s"

    mysql_cursor = db_mysql.cursor()
    mysql_cursor.execute(query, (str(user_id), ))
    all_submissions = mysql_cursor.fetchall()

    if len(all_submissions)==0:
        return None

    dict = {'user_id': str(user_id)}

    list = []

    for sub in all_submissions:
        block = {}
        block['user_id'] = sub[0]
        block['display_name'] = sub[1]        
        list.append(block)

    dict['submission'] = list

    return dict
