from os import path
import psycopg2
from pandas import DataFrame


# def viewInventory():

# def addNewBooks():

# def removeBooks():

# def viewReports():

# def viewOrders():

# def sendMoney():

# def owner_screen():
#     print("Welcome to the Owners dashboard, *Name*! \n")
#     print("[1] View Current Inventory \n")
#     print("[2] Add New Books \n")
#     print("[3] Remove Books \n")
#     print("[4] View Reports \n")
#     print("[5] View Orders \n")
#     print("[6] Send Money to Publishers \n")
#     print("[0] Log Out \n")

#     selection = input("Please select an option (0-6): \n")

#     if(selection == "0"):
#         logOut()

#     if(selection == "1"):
#         viewInventory()
    
#     if(selection == "2"):
#         addNewBooks()

#     if(selection == "3"):
#         removeBooks()


#     if(selection == "4"):
#         viewReports()


#     if(selection == "5"):
#         viewOrders()


#     if(selection == "6"):
#         sendMoney()    
    
conn = psycopg2.connect("dbname=bookstore user=postgres password=abcd123")
cur = conn.cursor()

cur.execute(open("DDL.sql", "r").read())
cur.execute(open("DDLInserts.sql", "r").read())

def landing_page():
    print("\n#####################################\n")
    print("Welcome to the Look Inna Bookstore!\n")
    print("[1] Login")
    print("[2] Create a new account")
    print("[3] Admin\n")
    print("#####################################\n")

def user_login():
    print("\n#####################################\n")
    print("User Login Page")
    username = input("Please enter your username (email): ")
    password = input("Please enter your password: ")
    # cur.execute("Select * from users")
    SQL = "SELECT user_ID FROM users WHERE user_email = '{uname}' AND user_password = '{psswrd}';".format(uname=username, psswrd=password)
    # SQL = (SQL,username)
    print(SQL)
    cur.execute(SQL)
    userID = cur.fetchone()
    # df_pass = DataFrame(cur.fetchall())
    # df_pass.columns=[ x.name for x in cur.description ]
    if(userID == None):
        return 0
        
    else:
        print("Success! Logged in as", username, 'with ID', userID)
        return userID

def owner_login():
    print("\n#####################################\n")
    print("Owner Login Page")
    username = input("Please enter your username (email): ")
    password = input("Please enter your password: ")
    # cur.execute("Select * from users")
    SQL = "SELECT user_ID FROM owners WHERE owner_email = '{uname}' AND owner_password = '{psswrd}';".format(uname=username, psswrd=password)
    # SQL = (SQL,username)
    print(SQL)
    cur.execute(SQL)
    ownerID = cur.fetchone()
    # df_pass = DataFrame(cur.fetchall())
    # df_pass.columns=[ x.name for x in cur.description ]
    if(ownerID == None):
        return 0
        
    else:
        print("Success! Logged in as", username, 'with ID', ownerID)
        return ownerID


def create_account():
    print("\n#####################################\n")
    print("Create an Account page.\n Please enter the following information")

    name = input("Name: ")
    user_email = input("Email: ")
    user_phonenumber = input("Phone Number (ex. 111-111-1111: ")
    user_password = input("Password: ")
    street_number = input("Street Number: ")
    street_name = input("Street Name: ")
    city = input("City: ")
    prov = input("Province (Ex. ON): ")
    postal_code = input("Postal Code: ")
    country = input("Country: ")

    SQL = "insert into users (user_name, user_email, user_phonenumber, user_password, street_number, street_name, city, prov, postal_code, country, member_years) values ('{name}', '{user_email}', '{user_phonenumber}', '{user_password}', '{street_number}', '{street_name}', '{city}', '{prov}', '{postal_code}', '{country}', 0);".format(name=name, user_email=user_email, user_phonenumber=user_phonenumber, user_password=user_password, street_number=street_number, street_name=street_name, city=city, prov=prov, postal_code=postal_code, country=country)
    cur.execute(SQL)
    conn.commit()

    SQL = "SELECT user_ID FROM users WHERE user_email = '{uname}' AND user_password = '{psswrd}';".format(uname=user_email, psswrd=user_password)
    cur.execute(SQL)
    userID = cur.fetchone()

    if(userID == None):
        print("Error with either username or password.")
    else:
        print("Successfully created an account! Logged in as", user_email, 'with ID', userID)
        return userID
    

def main():
    landing_page()
    selection = input()
    print('selection is', selection)
    if(selection=='1'):
        loggedUser = user_login()

        # If there was an error with the login, they go here
        if(loggedUser == 0):
            print("Error with either username or password.")
            selection = input("Please press [1] to try again or press [0] to return to the main menu.")
            if selection=='1':
                user_login()
            else:
                landing_page()
    elif(selection=='2'):
        create_account()
    elif(selection=='3'):
        owner_login()
    else:
        print("ERROR: Invalid choice! Please choose an option from the menu (1-3)")
    

if __name__ == "__main__":
    main()
    # linkDatabase()
