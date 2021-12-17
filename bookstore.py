from os import path, spawnl
from numpy import add, intp
from numpy.core.getlimits import _discovered_machar
from numpy.lib.function_base import select
from numpy.lib.shape_base import dstack
import psycopg2
import pandas as pd
import time
import sys

def viewInventory():

    print("\n#####################################\n")
    print("\n View Inventory Page  \n")

    conn = psycopg2.connect(host="localhost", port = 8080, database="bookstore", user="postgres", password=90210)
    cur = conn.cursor()

    print("[1] Number of different types of books \n")
    print("[2] Total stock in warehouse \n")
    print("[3] Number of distinct authors \n")
    print("[0] Go back to landing page \n")

    try:
        selection = int(input("Please select an option (0-3): "))
        while selection < 0 or selection > 3 :
            print("\nWrong input please try again!\n")
            selection = int(input("Please select an option (0-3): "))

    except:
        print("\nWrong input type please try again with an integer!\n")
        viewInventory()

    

    print("\n#####################################\n")


    if(selection == 1):
        cur.execute("""select count(DISTINCT genre) as genre from book""")
        query = cur.fetchone()[0]
        print(f" Number of different types of books: {query}")
        print("\n#####################################\n")

        viewInventory()


    if(selection == 2):
        cur.execute("""select sum(stock) as total from book""")
        query = cur.fetchone()[0]
        print(f"Total stock in warehouse: {query}")
        print("\n#####################################\n")

        viewInventory()
        
    
    if(selection == 3):
        cur.execute("""select count(DISTINCT auth_name) from (SELECT CONCAT(author_firstname, ' ', author_lastname) AS auth_name FROM book) as authorCount""")
        query = cur.fetchone()[0]
        print(f"Number of distinct authors: {query}")
        print("\n#####################################\n")

        viewInventory()

    if(selection == 0):
        owner_screen()



def addNewBooks():
    print("\n#####################################\n")
    print("\n Adding a New Book Page  \n")

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

        try:
            cur.execute(f"""insert into book values ('{isbn}', '{name}', '{firstname}', '{lastname}', '{genre}', '{numPages}', '{rating}', '{price}', '{stock}', '{publisherId}', '{pubPercent}', '{format}')""")

            conn.commit()

            print("\n Successfully added the book to catalogue! \n Returning back to landing page \n")
            owner_screen()

        ## Checking if book is inserted properly    
        except:
            print("Failed to add new book \n")
            selection = input("Select 0 to try again and 1 to go back to landing page:  ")

            if(selection == "0"):
                removeBooks()
            else:
                owner_screen()



    else:
        print("\nThis publisher is not authorised to sell \nCannot add book, returning back to landing page!\n")
        owner_screen()

    


    

    cur.close()
    conn.close()



    


def removeBooks():
    print("\n#####################################\n")
    print("\n ** Removing a Book Page **  \n")

    conn = psycopg2.connect(host="localhost", port = 8080, database="bookstore", user="postgres", password=90210)
    cur = conn.cursor()

    isbn = input("\n Please enter the ISBN of the book to be cleared from the warehouse or 0 to exit to landing page: ")

    if(isbn == "0"):
        return owner_screen()

    ## Checking if book exists 
    query = pd.read_sql('SELECT ISBN FROM book', conn)


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
    print("\n#####################################\n")
    conn = psycopg2.connect(host="localhost", port = 8080, database="bookstore", user="postgres", password=90210)
    cur = conn.cursor()

    print("\n View Reports Page  \n")

    print("[1] View Sales Vs Expenditure Report \n")
    print("[2] View Sales per Author Report \n")
    print("[3] View Sales per Genre Report \n")
    print("[4] View Sales per Publisher \n")
    print("[0] Go back to landing page \n")


    #Error handling for wrong input
    try:
        selection = int(input("Please select an option (0-4): "))
        while selection < 0 or selection > 4 :
            print("\nWrong input please try again!\n")
            selection = int(input("Please select an option (0-4): "))

        if(selection != 0 ):
            date = input("Please enter the time period of the report you wish to view (past month: 1, past two months: 2, past year: 12): ")
            if(date == "12"):
                date = "11"


        #Error checking for correct month value
        if(int(date) < 0):
            raise Exception


        print("\n#####################################\n")

        if(selection == 1):
            query = pd.read_sql("SELECT * FROM salesVsExpen where salesVsExpen.month >  EXTRACT(month  FROM current_date - INTERVAL" + f"'{date} months')", conn)
            query = query.astype({"year": int, "month": int})
            
            print(query)
            print("\n#####################################\n")

            viewReports()


        if(selection == 2):
            query = pd.read_sql("SELECT * FROM salesPerAuthor where salesPerAuthor.month >  EXTRACT(month  FROM current_date - INTERVAL" + f"'{date} months')", conn)

            query = query.astype({"year": int, "month": int})
            print(query)
            print("\n#####################################\n")

            viewReports()
        
    
        if(selection == 3):
            query = pd.read_sql("SELECT * FROM salesPerGenre where salesPerGenre.month >  EXTRACT(month  FROM current_date - INTERVAL" + f"'{date} months')", conn)

            query = query.astype({"year": int, "month": int})
            print(query)
            print("\n#####################################\n")

            viewReports()
        

        if(selection == 4):
            query = pd.read_sql("SELECT * FROM salesPerPublisher where salesPerPublisher.month >  EXTRACT(month  FROM current_date - INTERVAL" + f"'{date} months')", conn)

            query = query.astype({"year": int, "month": int})
            print(query)
            print("\n#####################################\n")

            viewReports()

        if(selection == 0):
            owner_screen()
            

        


        cur.close()
        conn.close()


    except:
        print("\nWrong input type please try again with an integer!\n")
        viewReports()





    


def viewOrders():
    print("\n#####################################\n")

    print("\n View Orders Page  \n")
    conn = psycopg2.connect(host="localhost", port = 8080, database="bookstore", user="postgres", password=90210)
    cur = conn.cursor()

    query = pd.read_sql('SELECT * FROM orders', conn)
    print(query)

    print("\n Returning back to landing page!\n")
    owner_screen()

    cur.close()
    conn.close()


def sendMoney():

    print("\n#####################################\n")

    print("\n Send Money to Publishers Page  \n")

    conn = psycopg2.connect(host="localhost", port = 8080, database="bookstore", user="postgres", password=90210)
    cur = conn.cursor()

    print("Current Publisher list")
    print("\n#####################################\n")

    pubList = pd.read_sql('SELECT publisher_name FROM Publisher', conn)
    print(pubList)
    print("\n#####################################\n")

    selection = input("Using the index on left hand side, please enter the index of the publisher you wish to send money to: ")
    while selection not in ('0', '1', '2', '3') :
        print("\nWrong input please try again!\n")
        selection = input("Using the index on left hand side, please enter the index of the publisher you wish to send money to: ")

    print("\n#####################################\n")


    query = pd.read_sql("SELECT year, month, publisher_id, salesPerPublisher.publisher_name, total_profits FROM salesPerPublisher join Publisher on publisher.publisher_name = salesPerPublisher.publisher_name where salesPerPublisher.publisher_name = " + f"'{pubList.iloc[int(selection)]['publisher_name']}' ", conn)
    print(query.astype({"year": int, "month": int}))
    print("\n#####################################\n")

    

    try:

        year, month = input("Which year and month's profits do you wish to send? (year,month) ").split(',')

        print("Loading:")

        #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
        animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

        for i in range(len(animation)):
            time.sleep(0.2)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()

        print("\n")

        transfer = pd.read_sql("SELECT year, month, publisher_id, salesPerPublisher.publisher_name, total_profits, publisher_bankAccount FROM salesPerPublisher join Publisher on publisher.publisher_name = salesPerPublisher.publisher_name where salesPerPublisher.publisher_name = " + f"'{pubList.iloc[int(selection)]['publisher_name']}' and year = " +  f"'{year}' " + " and month = " + f"'{month}' ", conn)

        if (transfer.empty):
            raise Exception
        transfer = transfer.astype({"year": int, "month": int, "publisher_bankaccount": int})
        print(transfer)
        print(f"\n Sent ${round(transfer.iloc[0]['total_profits'], 2)} to  {pubList.iloc[int(selection)]['publisher_name']}'s bank account no: {transfer.iloc[0]['publisher_bankaccount']}")
        print("\n Returning back to landing page!")
        print("\n#####################################\n")

        return owner_screen()
           

    ## Checking if input for month and year is correct   
    except:
        print("\n Failed to enter correct values \n")

        selection = input("\n Select 0 to try again from the beginning and 1 to go back to landing page: ")

        if(selection == '0'):
            sendMoney()
        else:
            owner_screen()


    










def owner_screen():
    print("\n#####################################\n")

    cur.close()
    conn.close()

    print("Welcome to the Owners dashboard, LookInnaAdmin! \n")
    print("[1] View Current Inventory \n")
    print("[2] Add New Books \n")
    print("[3] Remove Books \n")
    print("[4] View Reports \n")
    print("[5] View Orders \n")
    print("[6] Send Money to Publishers \n")
    print("[0] Log Out \n")

    selection = input("Please select an option (0-6): ")

    if(selection == "0"):
        main()

    if(selection == "1"):
        viewInventory()
    
    if(selection == "2"):
        addNewBooks()

    if(selection == "3"):
        removeBooks()


    if(selection == "4"):
        viewReports()


    if(selection == "5"):
        viewOrders()


    if(selection == "6"):
        sendMoney()    

# conn = psycopg2.connect("dbname=bookstore user=postgres password=abcd123")
conn = psycopg2.connect(host="localhost", port = 8080, database="bookstore", user="postgres", password=90210)

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
    selection = input("Select an option:")
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
