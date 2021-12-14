from os import path, spawnl
from numpy import add, intp
from numpy.core.getlimits import _discovered_machar
from numpy.lib.function_base import select
from numpy.lib.shape_base import dstack
import psycopg2
import pandas as pd

# def viewInventory():

def addNewBooks():

    print("Adding a new book page  \n")

    conn = psycopg2.connect(host="localhost", port = 8080, database="bookstore", user="postgres", password=90210)
    cur = conn.cursor()

    isbn = input("Please enter the ISBN of the book: ")
    name = input("Please enter the Title of the book: ")
    firstname = input("Please enter the Author's First Name: ")
    lastname = input("Please enter the Author's Last Name: ")
    genre = input("Please enter the Genre of the book (Please choose from: Childrens, Fiction, Memoir, Mystery, Nonfiction, Romance, SciFi/Fantasy, Young Adult): ")
    numPages = input("Please enter the number of pages in the book: ")
    rating = 0.00
    price = input("Please enter the Price of the book: ")
    stock = input("Please enter the current number of books in stock: ")
    publisherId = input("Please enter the Publisher id for the book: ")

    ## Checking if Publisher Id exists 
    query = pd.read_sql('SELECT publisher_id FROM publisher', conn)

    if(publisherId in query['publisher_id'].values):

        pubPercent = input("Please enter the percentage of profit the publisher will recieve (in decimel form): ")
        format = input("Please enter the Format of the book: ")

        # try:
        cur.execute(f"""insert into book values ('{isbn}', '{name}', '{firstname}', '{lastname}', '{genre}', '{numPages}', '{rating}', '{price}', '{stock}', '{publisherId}', '{pubPercent}', '{format}')""")

        conn.commit()

        print("\n Successfully added the book to catalogue! \n Returning back to landing page \n")
        owner_screen()

        ## Checking if book is inserted properly    
        # except:
        print("Failed to add new book \n")
        selection = input("Select 0 to try again and 1 to go back to landing page:  ")

        if(selection == 0):
            removeBooks()
        else:
            owner_screen()



    else:
        print("\nThis publisher is not authorised to sell \nCannot add book, returning back to landing page!\n")
        owner_screen()

    


    

    cur.close()
    conn.close()



    


def removeBooks():

    print("\n ** Removing a book page **  \n")

    conn = psycopg2.connect(host="localhost", port = 8080, database="bookstore", user="postgres", password=90210)
    cur = conn.cursor()

    isbn = input("\n Please enter the ISBN of the book to be cleared from the warehouse: ")

    ## Checking if book exists 
    query = pd.read_sql('SELECT ISBN FROM book', conn)
    print(isbn in query['isbn'].values)

    if(isbn in query['isbn'].values):
        try:
            cur.execute(f"""DELETE FROM book WHERE ISBN ='{isbn}'""")
            conn.commit()

            print("\n Successfully removed the book from warehouse! \n Returning back to landing page \n")
            owner_screen()

        ## Checking if book is deleted properly    
        except:
            print("\n Failed to delete book \n")

            selection = input("\n Select 0 to try again and 1 to go back to landing page:  ")

            if(selection == 0):
                removeBooks()
            else:
                owner_screen()
        
    
    else:
        print("\n This book does not exist in current inventory \n Please try again!\n")
        removeBooks()

        
                

    cur.close()
    conn.close()

        






def viewReports():

    conn = psycopg2.connect(host="localhost", port = 8080, database="bookstore", user="postgres", password=90210)
    cur = conn.cursor()

    print("[1] View Sales Vs Expenditure Report \n")
    print("[2] View Sales per Author Report \n")
    print("[3] View Sales per Genre Report \n")
    print("[4] View Sales per Publisher \n")
    print("[0] Go back to landing page \n")

    selection = input("Please select an option (0-4): ")

    print("\n#####################################\n")

    if(selection == "1"):
        query = pd.read_sql('SELECT * FROM salesVsExpen', conn)
        print(query)
        print("\n#####################################\n")

        viewReports()


    if(selection == "2"):
        query = pd.read_sql('SELECT * FROM salesPerAuthor', conn)
        print(query)
        print("\n#####################################\n")

        viewReports()
        
    
    if(selection == "3"):
        query = pd.read_sql('SELECT * FROM salesPerGenre', conn)
        print(query)
        print("\n#####################################\n")

        viewReports()
        

    if(selection == "4"):
        query = pd.read_sql('SELECT * FROM salesPerPublisher', conn)
        print(query)
        print("\n#####################################\n")

        viewReports()

    if(selection == "0"):
        owner_screen()
        

    


    cur.close()
    conn.close()

def viewOrders():

    conn = psycopg2.connect(host="localhost", port = 8080, database="bookstore", user="postgres", password=90210)
    cur = conn.cursor()

    query = pd.read_sql('SELECT * FROM orders', conn)
    print(query)

    owner_screen()

    cur.close()
    conn.close()


# def sendMoney():

def owner_screen():

    cur.close()
    conn.close()

    print("Welcome to the Owners dashboard, *Name*! \n")
    print("[1] View Current Inventory \n")
    print("[2] Add New Books \n")
    print("[3] Remove Books \n")
    print("[4] View Reports \n")
    print("[5] View Orders \n")
    print("[6] Send Money to Publishers \n")
    print("[0] Log Out \n")

    selection = input("Please select an option (0-6): ")

#     if(selection == "0"):
#         logOut()

#     if(selection == "1"):
#         viewInventory()
    
    if(selection == "2"):
        addNewBooks()

    if(selection == "3"):
        removeBooks()


    if(selection == "4"):
        viewReports()


    if(selection == "5"):
        viewOrders()


#     if(selection == "6"):
#         sendMoney()    

conn = psycopg2.connect("dbname=bookstore user=postgres password=abcd123")

cur = conn.cursor()
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('expand_frame_repr', False)

# cur.execute(open("DDL.sql", "r").read())
# cur.execute(open("DDLInserts.sql", "r").read())
# cur.execute("SELECT * FROM test;")
# cur.fetchone()
# conn.commit() # Make the changes to the database persistent
# cur.execute("SELECT * FROM users;")
# df = pd.DataFrame(cur.fetchall())
# df.columns=[ x.name for x in cur.description ]
# print(df)
# Close communication with the database
# cur.close()
# conn.close()

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
    # print(SQL)
    cur.execute(SQL)
    userID = cur.fetchone()
    # df_pass = DataFrame(cur.fetchall())
    # df_pass.columns=[ x.name for x in cur.description ]
    if(userID == None):
        return 0
        
    else:
        print("Success! Logged in as", username, 'with ID', userID[0])
        userID = str(userID[0])
        return userID

def owner_login():
    print("\n#####################################\n")
    print("Owner Login Page")
    username = input("Please enter your username (email): ")
    password = input("Please enter your password: ")
    # cur.execute("Select * from users")
    SQL = "SELECT owner_ID FROM owners WHERE owner_email = '{uname}' AND owner_password = '{psswrd}';".format(uname=username, psswrd=password)
    # SQL = (SQL,username)
    # print(SQL)
    cur.execute(SQL)
    ownerID = cur.fetchone()
    # df_pass = DataFrame(cur.fetchall())
    # df_pass.columns=[ x.name for x in cur.description ]
    if(ownerID == None):
        return 0
        
    else:
        print("Success! Logged in as", username, 'with ID', ownerID)
        ownerID = str(ownerID[0])
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
        userID = str(userID[0])
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
        df_cart = viewCart(userID, cart)
        print("\n[1] Checkout")
        print("[2] Continue Shopping")
        selection = input()
        if(selection == '1'):
            checkout(userID, cart, df_cart)
        elif(selection == '2'):
            bookCatalogue(userID, cart)
        else:
            print("Error! (FIX THIS)")

def viewCart(userID, cart):
    
    cartList = []
    df_cart = pd.DataFrame(cartList)
    if not cart:
        print("Cart is empty")
        bookCatalogue(userID, cart)
    for book in cart:
        SQL = "select isbn, name, author_firstname, author_lastname, genre, num_pages, rating, price, stock, format from book where ISBN = '{isbn}';".format(isbn=book)
        cur.execute(SQL)
        # print(cur.fetchall())
        # cartList.append(cur.fetchall())
        df_cart = df_cart.append(cur.fetchall())
    # df_cart = pd.DataFrame(cartList)
    df_cart.columns=['ISBN', 'Title', 'Author FirstName', 'Author LastName', 'Genre', 'Pages', 'Rating', 'Price', 'Stock', 'Format']
    print(df_cart)

    return df_cart
    

def checkout(userID, cart, df_cart):
    print("\n#####################################\n")
    print("Checkout")
    viewCart(userID, cart)
    print("\n#####################################\n")
    print("userid is: " + userID)
    SQL = "select street_number, street_name, city, prov, postal_code, country from users where user_id = {userID};".format(userID=userID)
    print(SQL)
    cur.execute(SQL)
    adrs = cur.fetchone()
    address = adrs[0] + " " + adrs[1] + " " + adrs[2] + " " + adrs[3] + " " + adrs[4] + " " + adrs[5]
    print("[1] Ship order to address on file: ", address)
    print("[2] Ship to new address")
    selection = input()
    
    orderID = createOrder(userID, df_cart, selection)
    if(selection == '2'):
        shipping(userID)

def shipping(userID):
    SQL = "select order_id from orders where user_id = {userID}".format(userID=userID)
    cur.execute(SQL)
    orderID = cur.fetchone()
    orderID = str(orderID[0])

    street_number = input("Street Number: ")
    street_name = input("Street Name (Ex. Main St): ")
    city = input("City: ")
    prov = input("Province: ")
    postal_code = input("Postal Code: ") 
    country = input("Country: ")  
    SQL = "insert into addresses (order_id, street_number, street_name, city, prov, postal_code, country) values ('{orderID}','{strNum}','{strName}','{city}','{prov}','{postal}','{country}');".format(orderID=orderID, strNum=strNum, strName=strName, city=cityy, prov=provv, postal=pc, country=cntry)
    cur.execute(SQL)

def createOrder(userID, df_cart, selection):
    dateSQL = "SELECT CURRENT_DATE;"
    cur.execute(dateSQL)
    date = cur.fetchone()
    total = df_cart.Price.sum()
    SQL = "insert into orders (user_id, order_date, total_price, no_of_items, status_order) values ({userID},'{date}','{total}','1','Pending Shipment');".format(userID=userID, date=date[0], total=total)
    cur.execute(SQL)
    conn.commit()
    SQL = "select MAX(order_id) from orders where user_id = {userID}".format(userID=userID)
    cur.execute(SQL)
    orderID = cur.fetchone()
    orderID = str(orderID[0])
    for book in df_cart.ISBN:
        SQL = "insert into inOrder values('{orderID}','{book}');".format(orderID=orderID, book=book)
        cur.execute(SQL)
        conn.commit()

    if(selection=='1'):
    # Add current address to ADDRESSES
        SQL = "select * from users where user_id = {userID}".format(userID=userID)
        cur.execute(SQL)
        userInfo = cur.fetchone()
        strNum = str(userInfo[5])
        strName = str(userInfo[6])
        cityy = str(userInfo[7])
        provv = str(userInfo[8])
        pc = str(userInfo[9])
        cntry = str(userInfo[10])
        SQL = "insert into addresses (order_id, street_number, street_name, city, prov, postal_code, country) values ('{orderID}','{strNum}','{strName}','{city}','{prov}','{postal}','{country}');".format(orderID=orderID, strNum=strNum, strName=strName, city=cityy, prov=provv, postal=pc, country=cntry)
        cur.execute(SQL)
        conn.commit()

    print("Order Successfully Placed!")
    print(orderID, "is your Tracking Number")

    print("\n\n[1] Main Menu")
    print("Press any key to quit and log out")

    selection = input()
    if (selection=="1"):
        landing_page()
    else:
        exit(-1)
    return orderID

def searchBook(userID, cart):
    flag = True
    print("Would you like to search for a book by: ")
    print("[1] Title")
    print("[2] ISBN")
    print("[3] Author")
    print("[4] Genre")
    print("[5] Rating (Show ONLY one rating)")
    print("[6] Rating (Show ratings >= input)")
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
            selection = input("Please press [1] to try again or press [0] to return to the main menu: ")
            if selection=='1':
                loggedUser = user_login()
            else:
                main()
                # break
        bookCatalogue(loggedUser, cart)

    elif(selection=='2'):
        create_account()

    elif(selection=='3'):
        loggedOwner = owner_login()
        while(loggedOwner == 0):
            print("Error with either username or password.")
            selection = input("Please press [1] to try again or press [0] to return to the main menu. ")
            if selection=='1':
                loggedOwner = owner_login()
                print(loggedOwner)
            else:
                landing_page()
                break
        owner_screen()
    else:
        print("ERROR: Invalid choice! Please choose an option from the menu (1-3)")

    

if __name__ == "__main__":
    main()
    # linkDatabase()
