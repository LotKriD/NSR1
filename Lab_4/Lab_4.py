import os
import pandas as pd
import sqlite3 as sql
from datetime import datetime

create_table_orders = """CREATE TABLE IF NOT EXISTS orders(user_id text, order_id text, 
    order_time integer, order_cost real, success_order_flg text)"""
value_orders = "INSERT INTO orders VALUES (?,?,?,?,?)"
get_users = """SELECT user_id, order_time FROM orders"""
create_table_users = """CREATE TABLE IF NOT EXISTS users(date integer, gmv360d_new real, 
    gmv360d_reactivated real, users_count_new integer, users_count_reacivated integer)"""
get_time = """SELECT user_id, order_time FROM orders ORDER BY order_time"""
get_user = """SELECT user_id, order_cost FROM orders WHERE user_id = '{}'"""
value_users = "INSERT INTO users VALUES (?,?,?,?,?)"

dirname = os.path.dirname(__file__)
path = os.path.join(dirname, 'test_shop_dataset_1.csv')
path_db = os.path.join(dirname, 'orders.db')
data = pd.read_csv(path)

def create_table():
    cur.execute(create_table_orders)
    conn.commit()

    rows = []
    for i in range(1, data.shape[0]):
        rows.append([str(data['user_id'][i]), str(data['order_id'][i]), int(data['order_time'][i]),
        data['order_cost'][i], str(data['success_order_flg'][i])])

    cur.executemany(value_orders, rows)
    conn.commit()

def users():
    cur.execute(get_users)
    conn.commit()
    rows = cur.fetchall()

    cur.execute(create_table_users)
    conn.commit()

    for row in rows:
        if row[0] not in new_users:
            new_users[row[0]] = row[1]
        elif row[0] not in react_users:
            u_date = get_time_from_unix(new_users[row[0]])
            c_date = get_time_from_unix(row[1])
            if c_date.month > u_date.month + 3 or (c_date.month == u_date.month + 3 and c_date.day >= u_date.day):
                l = []
                l.append(row[1])
                react_users[row[0]] = l
        else:
            u_date = get_time_from_unix(react_users[row[0]][len(react_users[row[0]]) - 1])
            c_date = get_time_from_unix(row[1])
            if c_date.month > u_date.month + 3 or (c_date.month == u_date.month + 3 and c_date.day >= u_date.day):
                l = []
                for i in react_users[row[0]]:
                    l.append(i)
                l.append(row[1])
                react_users[row[0]] = l

    cur.execute(get_time)
    conn.commit()
    dates = cur.fetchall()

    l = []
    date_t = 0
    new_cost = 0
    react_cost = 0
    new_users_c = 0
    react_users_c = 0

    date = get_time_from_unix(dates[0][1]).day - 1
    for d in dates:
        new_cost = 0
        react_cost = 0
        new_users_c = 0
        react_users_c = 0
        if get_time_from_unix(d[1]).day == date + 1:
            date_t = d[1]
            for u in new_users.keys():
                if new_users[u] == d[1]:
                    new_users_c += 1
                    cur.execute(get_user, u)
                    conn.commit()
                    cost = cur.fetchall()
                    for c in cost:
                        try:
                            new_cost += float(c[1])
                        except:
                            print("Error: {}".format(c[1]))

            for u in react_users.keys():
                for d1 in react_users[u]:
                    if d1 == d[1]:
                        react_users_c += 1
                        cur.execute(get_user, u)
                        conn.commit()
                        cost = cur.fetchall()
                        for c in cost:
                            try:
                                react_cost += float(c[1])
                            except:
                                print("Error: {}".format(c[1]))
            
            if new_users_c != 0 or react_users_c != 0:
                l.append([date_t, new_cost, react_cost, new_users_c, react_users_c])
    
    cur.executemany(value_users, l)
    conn.commit()

def get_time_from_unix(time):
    return datetime.utcfromtimestamp(time)   

new_users = {}
react_users = {}

if __name__ == '__main__':
    print("<Connection to db>")
    conn = sql.connect(path_db)
    cur = conn.cursor()

    print("<Working>")
    create_table()
    users()

    conn.close()
    print("<End>")