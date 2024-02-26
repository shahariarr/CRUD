import mysql.connector

# Function to establish database connection
def get_database_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="user_info_python"
    )

# CREATE operation
def create_record(name, email):
    try:
        mydb = get_database_connection()
        my_cursor = mydb.cursor()
        sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
        val = (name, email)
        my_cursor.execute(sql, val)
        mydb.commit()
        print("Record inserted successfully.")
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        if mydb.is_connected():
            my_cursor.close()
            mydb.close()

# READ operation
def read_records():
    try:
        mydb = get_database_connection()
        my_cursor = mydb.cursor()
        my_cursor.execute("SELECT * FROM users")
        result = my_cursor.fetchall()
        for row in result:
            print(row)
            # id=row[0]
            # name=row[1],
            # email=row[2]
            # print(id,name,email)

            # print(f"| ID=>{'row[0]'} | Name=> {'row[1]'} | Email=> {'row[2]'} |")


    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        if mydb.is_connected():
            my_cursor.close()
            mydb.close()

# UPDATE operation
def update_record(user_id, new_email):
    try:
        mydb = get_database_connection()
        my_cursor = mydb.cursor()
        sql = "UPDATE users SET email = %s WHERE id = %s"
        val = (new_email, user_id)
        my_cursor.execute(sql, val)
        mydb.commit()
        print("Record updated successfully.")
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        if mydb.is_connected():
            my_cursor.close()
            mydb.close()

# DELETE operation
def delete_record(user_id):
    try:
        mydb = get_database_connection()
        my_cursor = mydb.cursor()
        sql = "DELETE FROM users WHERE id = %s"
        val = (user_id,)
        my_cursor.execute(sql, val)
        mydb.commit()
        print("Record deleted successfully.")
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        if mydb.is_connected():
            my_cursor.close()
            mydb.close()

# Main function
def main():
    while True:
        print("\nChoose CRUD operation:")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            create_record(name, email)
        elif choice == "2":
            read_records()
        elif choice == "3":
            user_id = input("Enter user ID: ")
            new_email = input("Enter new email: ")
            update_record(user_id, new_email)
        elif choice == "4":
            user_id = input("Enter user ID: ")
            delete_record(user_id)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
