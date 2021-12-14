from os import path
from numpy import intp
from numpy.core.getlimits import _discovered_machar
from numpy.lib.shape_base import dstack
import psycopg2
import pandas as pd

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
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('expand_frame_repr', False)

# cur.execute(open("DDL.sql", "r").read())
# cur.execute(open("DDLInserts.sql", "r").read())

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

def bookCatalogue(userID, cart):
    print("\n#####################################\n")
    print("Hello", userID, "Welcome to the bookstore!\n")
    print("[1] Search for book (by Title, ISBN, Author, Genre, Rating)")
    print("[2] View Cart")
    selection = input()
    if (selection == '1'):
        searchBook(userID, cart)
    if (selection == '2'):
        viewCart(userID, cart)

def viewCart(userID, cart):
    df_cart = pd.DataFrame()
    for book in cart:
        SQL = "select isbn, name, author_firstname, author_lastname, genre, num_pages, rating, price, stock, format from book where ISBN = '{isbn}';".format(isbn=book)
        cur.execute(SQL)
        print(cur.fetchall())
        df_cart = df_cart.append(cur.fetchall())
    # df_cart.columns=['ISBN', 'Title', 'Author FirstName', 'Author LastName', 'Genre', 'Pages', 'Rating', 'Price', 'Stock', 'Format']
    print(df_cart)

def searchBook(userID, cart):
    flag = True
    print("Would you like to search for a book by: ")
    print("[1] Title")
    print("[2] ISBN")
    print("[3] Author")
    print("[4] Genre")
    print("[5] Rating")
    print("[6] Rating (all inclsuive and above)")
    selection = input()
    if (selection == '1'):
        titleSearch = input("Please enter title (Case sensitive): ")
        SQL = "select isbn, name, author_firstname, author_lastname, genre, num_pages, rating, price, stock, format from book where name = '{name}';".format(name=titleSearch)
        cur.execute(SQL)
        df_search = pd.DataFrame(cur.fetchall())
        df_search.columns=[ x.name for x in cur.description ]
        print(df_search)

    elif (selection == '2'):
        isbnSearch = input("Please enter ISBN: ")
        SQL = "select isbn, name, author_firstname, author_lastname, genre, num_pages, rating, price, stock, format from book where ISBN = '{isbn}';".format(isbn=isbnSearch)
        cur.execute(SQL)
        df_search = pd.DataFrame(cur.fetchall())
        df_search.columns=[ x.name for x in cur.description ]
        print(df_search)

    elif (selection == '3'):
        authorFirstSearch = input("Please enter Author's Name (first and last)' ")
        first, last = authorFirstSearch.split(" ")
        SQL = "select isbn, name, author_firstname, author_lastname, genre, num_pages, rating, price, stock, format from book where author_firstname = '{firstname}' and author_lastname = '{lastname}' group by isbn, author_lastname;".format(firstname=first, lastname=last)
        cur.execute(SQL)
        df_search = pd.DataFrame(cur.fetchall())
        df_search.columns=[ x.name for x in cur.description ]
        print(df_search)

    elif (selection == '4'):
        genreSearch = input("Please enter Genre: ")
        SQL = "select isbn, name, author_firstname, author_lastname, genre, num_pages, rating, price, stock, format from book where genre = '{genre}' group by isbn, genre;".format(genre=genreSearch)
        cur.execute(SQL)
        df_search = pd.DataFrame(cur.fetchall())
        df_search.columns=[ x.name for x in cur.description ]
        print(df_search)

    elif (selection == '5'):
        ratingSearch = input("Please enter Rating (specific number from 1-5): ")
        SQL = "select isbn, name, author_firstname, author_lastname, genre, num_pages, rating, price, stock, format from book where rating = '{rating}' group by isbn, rating;".format(rating=ratingSearch)
        cur.execute(SQL)
        df_search = pd.DataFrame(cur.fetchall())
        df_search.columns=[ x.name for x in cur.description ]
        print(df_search)

    elif (selection=='6'):
        ratingSearch = input("Please enter Rating (Number from 1-5), ex. 4, results will be all books higher than (and equal to) 4: ")
        SQL = "select isbn, name, author_firstname, author_lastname, genre, num_pages, rating, price, stock, format from book where rating >= '{rating}' group by isbn, rating;".format(rating=ratingSearch)
        cur.execute(SQL)
        df_search = pd.DataFrame(cur.fetchall())
        df_search.columns=[ x.name for x in cur.description ]
        print(df_search)

    else:
        print("ERROR: Invalid choice! Please choose an option from the menu (1-6)")
        searchBook(userID, cart)
    
    while (flag):
            print("\nIf you would like to add a book to your cart, please enter the book number from your search result. \nIf you want to continue browsing press c. \n If you want to go back to the menu press b")
            selection = input()
            results = df_search.shape[0]
        
            if (selection == 'c' or selection == 'C'):
                flag = False
                searchBook(userID, cart)
            elif(selection == 'b' or selection == 'B'):
                flag = False
                bookCatalogue(userID, cart)
            elif (0 <= int(selection) <= results-1):
                if (df_search.at[int(selection), 'stock'] > 0):
                    flag = False
                    # Add book to cart
                    cart.append(df_search.at[int(selection), 'isbn'])
                    print("Book added to cart!", selection)
                    bookCatalogue(userID, cart)
                else:
                    print("Sorry! We are out of that book. Please choose another one")
                    searchBook(userID, cart)
            else:
                print("ERROR: Please enter a valid choice!!")

def main():
    cart = []
    landing_page()
    selection = input()
    print('selection is', selection)
    if(selection=='1'):
        loggedUser = user_login()

        # If there was an error with the login, they go here
        while(loggedUser == 0):
            print("Error with either username or password.")
            selection = input("Please press [1] to try again or press [0] to return to the main menu.")
            if selection=='1':
                loggedUser = user_login()
            else:
                landing_page()
                break
        bookCatalogue(loggedUser, cart)
    elif(selection=='2'):
        create_account()
    elif(selection=='3'):
        owner_login()
    else:
        print("ERROR: Invalid choice! Please choose an option from the menu (1-3)")
    

if __name__ == "__main__":
    main()
    # linkDatabase()
