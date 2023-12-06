import pymysql

def get_record(user_id):
    connection = pymysql.connect(host='localhost',
                            user='frosch',
                            password='frosch',
                            database='Users',
                            port=3306)
    
    cursor = connection.cursor()

    # Execute a query
    sql_query = "SELECT user_name FROM Users WHERE user_id = " + user_id
    cursor.execute(sql_query)

    # Fetch the results
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    print(results)
    return results[0][0]
    # Close the cursor and connection
    # cursor.close()
    # connection.close()
    # Process the results
    # for row in results:
    #     print(row)

def update_record(user_id):
    connection = pymysql.connect(host='localhost',
                            user='frosch',
                            password='frosch',
                            database='Users',
                            port=3306)
    
    cursor = connection.cursor()

    # Execute a query UPDATE MyGuests SET lastname='Doe' WHERE id=2
    sql_update = "UPDATE Users SET user_name='Tim' WHERE user_id = " + user_id + ";"
    cursor.execute(sql_update)
    connection.commit()
    sql_query = "SELECT user_name FROM Users WHERE user_id = " + user_id + ";"
    cursor.execute(sql_query)
    results = cursor.fetchall()
    print(results)
    # Fetch the results
    cursor.close()
    connection.close()
    return results

def create_record(user_creation_request):
    connection = pymysql.connect(host='localhost',
                            user='frosch',
                            password='frosch',
                            database='Users',
                            port=3306)
    
    cursor = connection.cursor()

    sql_create = "INSERT INTO Users(user_id,user_name) VALUES(8,'Jason');"
    cursor.execute(sql_create)
    connection.commit()
    sql_query = "SELECT user_name FROM Users WHERE user_id = 8"
    cursor.execute(sql_query)
    results = cursor.fetchall()
    print(results)
    cursor.close()
    connection.close()
    return results

def delete_record(user_id):
    connection = pymysql.connect(host='localhost',
                            user='frosch',
                            password='frosch',
                            database='Users',
                            port=3306)
    
    cursor = connection.cursor()

    sql_create = "DELETE FROM Users WHERE user_id = " + user_id + ";"
    cursor.execute(sql_create)
    connection.commit()
    sql_query = "SELECT user_name FROM Users WHERE user_id = " + user_id + ";"
    cursor.execute(sql_query)
    results = cursor.fetchall()
    print(results)
    cursor.close()
    connection.close()
    return results
