import pymysql
from werkzeug.security import generate_password_hash, check_password_hash

__cnx = None


def get_sql_connection():
    print("Opening mysql connection")
    global __cnx

    if __cnx is None:
        __cnx = pymysql.connect(user='venkat', password='', database='credir_card')

    return __cnx


def reg_admin():
    newpassword = generate_password_hash("password")
    con = get_sql_connection()
    cursor = con.cursor()
    cursor.execute('insert into admin values(%s,%s,%s,%s,%s)',
                   (" ", "admin", "admin@test.com", newpassword, "123546789"))
    con.commit()


def admin_login(username, password=0):
    con = get_sql_connection()
    cursor = con.cursor()
    if password != 0:
        cursor.execute('select * from admin where email=%s', username)
        row = cursor.fetchone()
        if row:
            if check_password_hash(row[3], password):
                return row
            else:
                return False
        else:
            return False
    else:
        cursor.execute('select * from admin where email=%s', username)
        row = cursor.fetchone()
        if row:
            return row
        else:
            return False


def admin_profile_update_block(user_id, adminname, inputEmail, Phonenumber):
    con = get_sql_connection()
    cursor = con.cursor()
    cursor.execute('UPDATE admin SET email= %s,name=%s,number=%s WHERE id = %s;',
                   (inputEmail, adminname, Phonenumber, user_id))
    con.commit()


def password_update(password, id):
    newpassword = generate_password_hash(password)
    con = get_sql_connection()
    cursor = con.cursor()
    cursor.execute('UPDATE admin SET password = %s WHERE id = %s;', (newpassword, id))
    con.commit()


def new_cc_request(details):
    req_id = "REQ2020CC"
    import time
    req_id += str(round(time.time()))
    req = []

    for i in details:
        req.append(details[i])

    con = get_sql_connection()
    cursor = con.cursor()

    cursor.execute('Select * from user_request where number=%s and status = %s',(req[3],"approved"))
    row = cursor.fetchone()
    if row:
        return False
    else:
        cursor.execute('insert into user_request values(%s,%s,%s,%s,%s,%s,%s,%s)',
                       (" ", req_id, req[0], req[1], req[3], req[2], "Credit Card", "pending"))
        con.commit()

        return req_id


def cards_status_details():
    con = get_sql_connection()
    cursor = con.cursor()
    cursor.execute('select count(*) from user_request where status = "approved"')
    completed = cursor.fetchone()
    cursor.execute('select count(*) from user_request where status = "pending"')
    pending = cursor.fetchone()
    return completed, pending


def pending_details():
    con = get_sql_connection()
    cursor = con.cursor()
    cursor.execute('select * from user_request where status = "pending"')
    pending = cursor.fetchall()
    return pending


def card_number_generator():
    import random

    card = random.randrange(9999_9999_9999_9999)
    cvv = random.randrange(999)
    exp_month = random.randrange(12)
    exp_year = random.randrange(20, 30)
    pin = random.randrange(0000,9999)
    return card, cvv, exp_month, exp_year, pin


def generate_card(status):
    for i in status:
        state = i
        id = status[i]
    if state == "approve":
        details = card_number_generator()
        con = get_sql_connection()
        cursor = con.cursor()
        cursor.execute('select request_id,name ,number from user_request where id=%s', (str(id)))
        row = cursor.fetchone()
        print(row)

        cursor.execute('insert into card_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                       (" ",row[0], details[0], details[1], row[1], row[2], details[2], details[3],
                        details[4], "20000", "card approved"))
        cursor.execute('update user_request set  status = "approved" where id=%s', (str(id)))
        con.commit()
    if state == "reject":
        con = get_sql_connection()
        cursor = con.cursor()
        cursor.execute('update user_request set  status = "Rejected" where id=%s', (str(id)))
        con.commit()

def display_card(number):
    con = get_sql_connection()
    cursor = con.cursor()
    cursor.execute('select * from card_details where request_id=%s', (number))
    row =cursor.fetchone()
    if row:
        return row
    else:
        return False