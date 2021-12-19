from os import path, spawnl
from numpy import add, intp
from numpy.core.getlimits import _discovered_machar
from numpy.lib.function_base import select
from numpy.lib.shape_base import dstack
import psycopg2
import pandas as pd
import time
import sys

###################################################################################

# Enter DB login info after inserting DDL

# conn = psycopg2.connect(host="localhost", port = 8080, database="bookstore", user="postgres", password=90210)
conn = psycopg2.connect("dbname=bookstore user=postgres password=abcd123")

cur = conn.cursor()
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('expand_frame_repr', False)

###################################################################################

def viewInventory():

    ## view inventory page

    print("\n#####################################\n")
    print("\nView Inventory Page  \n")

    # Add login creds here
    # conn = psycopg2.connect(host="localhost", port = 8080, database="bookstore", user="postgres", password=90210)
    # conn = psycopg2.connect("dbname=bookstore user=postgres password=abcd123")
    # cur = conn.cursor()

    print("[1] Number of different types of books \n")
    print("[2] Total stock in warehouse \n")
    print("[3] Number of distinct authors \n")
    print("[0] Go back to Owner's dashboard \n")

    ## Try catch block to error check input values
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
        

        viewInventory()


    if(selection == 2):
        cur.execute("""select sum(stock) as total from book""")
        query = cur.fetchone()[0]
        print(f"Total stock in warehouse: {query}")
       

        viewInventory()
        
    
    if(selection == 3):
        cur.execute("""select count(DISTINCT auth_name) from (SELECT CONCAT(author_firstname, ' ', author_lastname) AS auth_name FROM book) as authorCount""")
        query = cur.fetchone()[0]
        print(f"Number of distinct authors: {query}")
        

        viewInventory()

    if(selection == 0):
        owner_screen()

def addNewBooks():

    ## add new books page
    print("\n#####################################\n")
    print("\n Adding a New Book Page  \n")

    # conn = psycopg2.connect(host="localhost", port = 8080, database="bookstore", user="postgres", password=90210)
    # conn = psycopg2.connect("dbname=bookstore user=postgres password=abcd123")
    # cur = conn.cursor()

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

        ## error checks if publisher is in publisher table since it is a foreign key of book
        pubPercent = input("Please enter the percentage of profit the publisher will recieve (in decimel form): ")
        format = input("Please enter the Format of the book: ")

        ## try catch block to error check if book was correctly inserted IF NOT the error is with one of the input values
        try:
            cur.execute(f"""insert into book values ('{isbn}', '{name}', '{firstname}', '{lastname}', '{genre}', '{numPages}', '{rating}', '{price}', '{stock}', '{publisherId}', '{pubPercent}', '{format}')""")

            conn.commit()

            print("\n Successfully added the book to catalogue! \n Returning back to Owner's dashboard \n")
            owner_screen()

        ## Since there is an erro ask user to properly check input values    
        except:
            print("Failed to add new book, please check your input values \n")
            selection = input("Select 0 to try again and 1 to go back to Owner's dashboard:  ")

            if(selection == "0"):
                removeBooks()
            else:
                owner_screen()

    else:
        print("\nThis publisher is not authorised to sell \nCannot add book, returning back to Owner's dashboard!\n")
        owner_screen()


def removeBooks():
    ## remove books page
    print("\n#####################################\n")
    print("\n ** Removing a Book Page **  \n")

    isbn = input("\n Please enter the ISBN of the book to be cleared from the warehouse or 0 to exit to Owner's dashboard: ")

    if(isbn == "0"):
        return owner_screen()

    ## Checking if book exists 
    query = pd.read_sql('SELECT ISBN FROM book', conn)


    #if book exists
    if(isbn in query['isbn'].values):
        #error check if we removed the book from the table properly
        try:
            cur.execute(f"""DELETE FROM book WHERE ISBN ='{isbn}'""")
            conn.commit()

            print("\n Successfully removed the book from warehouse! \n Returning back to Owner's dashboard \n")
            owner_screen()

        ## IF failed to remove book let user know  
        except:
            print("\n Failed to delete book \n")

            selection = input("\n Select 0 to try again and 1 to go back to Owner's dashboard:  ")

            if(selection == 0):
                removeBooks()
            else:
                owner_screen()
    
    #if book does not exist let user know 
    else:
        print("\n This book does not exist in current inventory \n Please try again!\n")
        removeBooks()

def viewReports():
    ## view reports page
    print("\n#####################################\n")
    print("\n View Reports Page  \n")

    print("[1] View Sales Vs Expenditure Report \n")
    print("[2] View Sales per Author Report \n")
    print("[3] View Sales per Genre Report \n")
    print("[4] View Sales per Publisher \n")
    print("[0] Go back to landing page \n")
    print("(Bare in mind list needs to be updated manually)\n") #wanted to refresh materlialized view under the hood but it took too long to do so - Samar


    #Error handling for wrong input
    try:
        selection = int(input("Please select an option (0-4): "))
        while selection < 0 or selection > 4 :
            print("\nWrong input please try again!\n")
            selection = int(input("Please select an option (0-4): "))

        if(selection != 0 ):
            date = int(input("Please enter the time period (in months) of the report you wish to view (past month: 1, past two months: 2, past year: 12): "))
            #Error checking for correct month value
            if(date < 0):
                raise Exception
            if(date % 12 == 0):
                date -= 1

        print("\n#####################################\n")

        if(selection == 1):
            
            # cur.execute("""REFRESH MATERIALIZED VIEW  salesVsExpen""")
            # conn.commit()
            query = pd.read_sql("SELECT * FROM salesVsExpen where salesVsExpen.month >  EXTRACT(month  FROM current_date - INTERVAL" + f"'{date} months')", conn)
            query = query.astype({"year": int, "month": int})
            
            print(query)


            viewReports()


        if(selection == 2):
            # cur.execute("""REFRESH MATERIALIZED VIEW  salesPerAuthor""")
            # conn.commit()
            query = pd.read_sql("SELECT * FROM salesPerAuthor where salesPerAuthor.month >  EXTRACT(month  FROM current_date - INTERVAL" + f"'{date} months')", conn)

            query = query.astype({"year": int, "month": int})
            print(query)
  

            viewReports()
        
    
        if(selection == 3):
            # cur.execute("""REFRESH MATERIALIZED VIEW  salesPerGenre""")
            # conn.commit()
            query = pd.read_sql("SELECT * FROM salesPerGenre where salesPerGenre.month >  EXTRACT(month  FROM current_date - INTERVAL" + f"'{date} months')", conn)

            query = query.astype({"year": int, "month": int})
            print(query)
 

            viewReports()
        

        if(selection == 4):
            # cur.execute("""REFRESH MATERIALIZED VIEW  salesPerPublisher""")
            # conn.commit()
            query = pd.read_sql("SELECT * FROM salesPerPublisher where salesPerPublisher.month >  EXTRACT(month  FROM current_date - INTERVAL" + f"'{date} months')", conn)

            query = query.astype({"year": int, "month": int})
            print(query)
         

            viewReports()

        if(selection == 0):
            owner_screen()
     
    #User failed to enter correct input format let user know 
    except:
        print("\nWrong input type please try again with an integer!\n")
        viewReports()


def viewOrders():

    print("\n#####################################\n")

    print("\n View Orders Page  \n")

    SQL = "SELECT * FROM orders"
    cur.execute(SQL)
    query = pd.DataFrame(cur.fetchall())
    query.columns=[ x.name for x in cur.description ]
    print(query)

    flag = True

    while(flag):
        orderID = input("\nTo update the shipping status please enter the orderID or press 0 to go back to menu: ")

        if(orderID.isnumeric()):
            if(orderID == '0'):
                owner_screen()
                flag = False
                break
            
            if(query.isin([int(orderID)]).any().any()):

                status = input("Enter the updated shipping status (Pending, Delayed, Shipped): ")

                SQL = "UPDATE orders SET status_order = '{stat}' WHERE order_id = {id};".format(stat=status, id=orderID)
                cur.execute(SQL)
                conn.commit()
                continue
                    
            else:
                print("\nERROR: Please enter a valid orderID!!")

        if(not orderID.isnumeric()):
                print("\nERROR: Please enter a valid orderID ee!!")
            
def sendMoney():

    print("\n#####################################\n")

    print("\n Send Money to Publishers Page  \n")
    print("Current Publisher list")
    print("\n#####################################\n")

    pubList = pd.read_sql('SELECT publisher_name FROM Publisher', conn)
    print(pubList)
    print("\n#####################################\n")

    selection = input("Using the index on left hand side, please enter the index of the publisher you wish to send money to (Bare in mind list needs to be updated manually): ")
    #Error check for input values
    while selection not in ('0', '1', '2', '3') :
        print("\nWrong input please try again!\n")
        selection = input("Using the index on left hand side, please enter the index of the publisher you wish to send money to: ")

    print("\n#####################################\n")



    query = pd.read_sql("SELECT year, month, publisher_id, salesPerPublisher.publisher_name, total_profits FROM salesPerPublisher join Publisher on publisher.publisher_name = salesPerPublisher.publisher_name where salesPerPublisher.publisher_name = " + f"'{pubList.iloc[int(selection)]['publisher_name']}' ", conn)
    print(query.astype({"year": int, "month": int}))
    print("\n#####################################\n")
    
    try:

        year, month = input("Which year and month's profits do you wish to send? (year,month) ").split(',')

        ##### THIS BLOCK OF CODE FOR THE LOADING SCREEN IS FROM STOCK OVERFLOW I HAVE CITED IT IN THE REPORT #####
        print("Loading:")
        #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
        animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

        for i in range(len(animation)):
            time.sleep(0.2)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()

        print("\n")

        ##########################################################################################################

        transfer = pd.read_sql("SELECT year, month, publisher_id, salesPerPublisher.publisher_name, total_profits, publisher_bankAccount FROM salesPerPublisher join Publisher on publisher.publisher_name = salesPerPublisher.publisher_name where salesPerPublisher.publisher_name = " + f"'{pubList.iloc[int(selection)]['publisher_name']}' and year = " +  f"'{year}' " + " and month = " + f"'{month}' ", conn)

        #If dataframe is empty users input values are probably wrong raise exception
        if (transfer.empty):
            raise Exception
        transfer = transfer.astype({"year": int, "month": int, "publisher_bankaccount": int})
        print(transfer)
        print(f"\n SUCCESSFUL TRANSFER\n Sent ${round(transfer.iloc[0]['total_profits'], 2)} to  {pubList.iloc[int(selection)]['publisher_name']}'s bank account no: {transfer.iloc[0]['publisher_bankaccount']}")
        print("\n Returning back to Owner's dashboard!")
        print("\n#####################################\n")

        return owner_screen()
           

    ## Checking if input for month and year is correct   
    except:
        print("\n Failed to enter correct values \n")

        selection = input("\n Select 0 to try again from the beginning and 1 to go back to Owner's dashboard: ")

        if(selection == '0'):
            sendMoney()
        else:
            owner_screen()



def owner_screen():

    # Owner dashboard page
    print("\n#####################################\n")
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
        print("\n Thank you LookInnaAdmin, Hope you had a nice visit \n")

    elif(selection == "1"):
        viewInventory()
        
    elif(selection == "2"):
        addNewBooks()

    elif(selection == "3"):
        removeBooks()


    elif(selection == "4"):
        viewReports()


    elif(selection == "5"):
        viewOrders()


    elif(selection == "6"):
        sendMoney()

    else:
        print("\nWrong input please try again!\n")
        owner_screen()

def landing_page():
    print("\n#####################################\n")
    print("Welcome to the Look Inna Bookstore!\n")
    print("[1] Login")
    print("[2] Create a new account")
    print("[3] Admin\n")
    print("#####################################\n")

def user_login():
    print("\n\nUser Login Page")
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

    ## ADD ERROR CHECK FOR UNIQUE EMAIL ID 
    try:
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

    except:
        print("Oh no! That email already has an account, maybe reset your password (when that functionality is allowed) or use another email :/ \n")
        selection = input("Please enter 0 to try again or any other key to go back!: ")

        if(selection == "0"):
            create_account()
        else:
            main()



def bookCatalogue(userID, cart):
    print("\n#####################################\n")
    print("Hello and Welcome to the bookstore!\n")
    print("[1] Search for book (by Title, ISBN, Author, Genre, Rating)")
    print("[2] View Cart")
    print('[Q] to quit and log out')
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
            print("\nERROR! Please enter a valid choice (value between 1-2)")
            bookCatalogue(userID, cart)
    if (selection == 'q' or selection == 'Q'):
        print("***** Thank you for choosing Look Inna Bookstore. Have a great day! *****")
        cur.close()
        conn.close()
        exit(-1)
       

    else:
            print("\nERROR! Please enter a valid choice (value between 1-3)")
            bookCatalogue(userID, cart)

def viewCart(userID, cart):
    
    cartList = []
    df_cart = pd.DataFrame(cartList)
    if not cart:
        print("\n*** Cart is empty!! ***")
        bookCatalogue(userID, cart)
    for book in cart:
        SQL = "select isbn, name, author_firstname, author_lastname, genre, num_pages, rating, price, stock, format from book where ISBN = '{isbn}';".format(isbn=book)
        cur.execute(SQL)
        df_cart = df_cart.append(cur.fetchall())
    df_cart.columns=['ISBN', 'Title', 'Author FirstName', 'Author LastName', 'Genre', 'Pages', 'Rating', 'Price', 'Stock', 'Format']
    print(df_cart)

    return df_cart
    

def checkout(userID, cart, df_cart):
    print("\n#####################################\n")
    print("Checkout")
    viewCart(userID, cart)
    print("\n#####################################\n")
    SQL = "select street_number, street_name, city, prov, postal_code, country from users where user_id = {userID};".format(userID=userID)
    
    cur.execute(SQL)
    adrs = cur.fetchone()
    address = adrs[0] + " " + adrs[1] + " " + adrs[2] + " " + adrs[3] + " " + adrs[4] + " " + adrs[5]
    print("\n[1] Ship order to address on file: ", address)
    print("[2] Ship to new address")
    selection = input()
    if(selection == '1'):
        orderID = createOrder(userID, df_cart, selection, True)
    if(selection == '2'):
        orderID = createOrder(userID, df_cart, selection, False)
        shipping(userID, orderID)

def shipping(userID, orderID):
    street_number = input("Street Number: ")
    street_name = input("Street Name (Ex. Main St): ")
    city = input("City: ")
    prov = input("Province: ")
    postal_code = input("Postal Code: ") 
    country = input("Country: ")  
    SQL = "insert into addresses (order_id, street_number, street_name, city, prov, postal_code, country) values ('{orderID}','{strNum}','{strName}','{city}','{prov}','{postal}','{country}');".format(orderID=orderID, strNum=street_number, strName=street_name, city=city, prov=prov, postal=postal_code, country=country)
    cur.execute(SQL)
    conn.commit()

    print("\nOrder Successfully Placed!")
    print("******", orderID, "is your Tracking Number ******")

    print("\nPress any key to quit and log out")
    selection = input()
    cur.close()
    conn.close()
    exit(-1)


def createOrder(userID, df_cart, selection, flag):
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
        
    if(flag):
        print("\nOrder Successfully Placed!")
        print("******", orderID, "is your Tracking Number ******")

        print("\n\n[1] Main Menu")
        print("Press any key to quit and log out")

        selection = input()
        if (selection=="1"):
            landing_page()
        else:
            cur.close()
            conn.close()
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
    print("\n[0] Go back to main menu")    
    selection = input()
    if (selection == '1'):
        titleSearch = input("Please enter title (Case sensitive): ")

        SQL = "SELECT name FROM book;"
        cur.execute(SQL)
        df_title = pd.DataFrame(cur.fetchall())
        df_title.columns=["title"]

        # if(df_title.isin([titleSearch]).any().any()):
        if(df_title['title'].str.contains(titleSearch).any()):
            SQL = "select isbn, name, author_firstname, author_lastname, genre, num_pages, rating, price, stock, format from book where name LIKE '%{name}%';".format(name=titleSearch)
            cur.execute(SQL)
            df_search = pd.DataFrame(cur.fetchall())
            df_search.columns=[ x.name for x in cur.description ]
            print("\n####################################")
            print(df_search)
            print("\n####################################")
        else:
            print("\n########## ERROR ##########")
            print("Your Title is not in our bookstore database (yet)! Please try another search.\n")
            searchBook(userID, cart)

    elif (selection == '2'):
        isbnSearch = input("Please enter ISBN (ex. 989-28-3705-987-7): ")

        SQL = "SELECT ISBN FROM book;"
        cur.execute(SQL)
        df_isbn = pd.DataFrame(cur.fetchall())
        df_isbn.columns=["isbn"]

        if(df_isbn.isin([isbnSearch]).any().any()):
                SQL = "select isbn, name, author_firstname, author_lastname, genre, num_pages, rating, price, stock, format from book where ISBN = '{isbn}';".format(isbn=isbnSearch)
                cur.execute(SQL)
                df_search = pd.DataFrame(cur.fetchall())
                df_search.columns=[ x.name for x in cur.description ]
                print("\n####################################")
                print(df_search)
                print("\n####################################")

        else:
            print("\n########## ERROR ##########")
            print("Your ISBN is not in our bookstore database (yet)! Please try another search.\n")
            searchBook(userID, cart)

    elif (selection == '3'):
        authorFirstSearch = input("Please enter Author's Name: ")
        if(" " not in authorFirstSearch):
            # Case where user wants to search by authors first OR last name only
            SQL = "SELECT author_firstname, author_lastname FROM book"
            cur.execute(SQL)
            df_auth = pd.DataFrame(cur.fetchall())
            df_auth.columns=["firstname", "lastname"]

            if(df_auth.isin([authorFirstSearch]).any().any()):
                    SQL = "select isbn, name, author_firstname, author_lastname, genre, num_pages, rating, price, stock, format from book where author_firstname like '%{firstname}%' or author_lastname like '%{lastname}%' group by isbn, author_lastname;".format(firstname=authorFirstSearch, lastname=authorFirstSearch)
                    cur.execute(SQL)
                    df_search = pd.DataFrame(cur.fetchall())
                    df_search.columns=[ x.name for x in cur.description ]
                    print("\n####################################")
                    print(df_search)
                    print("\n####################################")

            else:
                print("\n########## ERROR ##########")
                print("Your Author is not in our bookstore database (yet)! Please try another search.\n")
                searchBook(userID, cart)
        else:
            # Case where user enters BOTH first and last name
            first, last = authorFirstSearch.split(" ")
            
            SQL = "SELECT author_firstname, author_lastname FROM book"
            cur.execute(SQL)
            df_auth = pd.DataFrame(cur.fetchall())
            df_auth.columns=["firstname", "lastname"]

            if(((df_auth['firstname'] == first) & (df_auth['lastname'] == last)).any()):
                    SQL = "select isbn, name, author_firstname, author_lastname, genre, num_pages, rating, price, stock, format from book where author_firstname = '{firstname}' and author_lastname = '{lastname}' group by isbn, author_lastname;".format(firstname=first, lastname=last)
                    cur.execute(SQL)
                    df_search = pd.DataFrame(cur.fetchall())
                    df_search.columns=[ x.name for x in cur.description ]
                    print("\n####################################")
                    print(df_search)
                    print("\n####################################")

            else:
                print("\n########## ERROR ##########")
                print("Your Author is not in our bookstore database (yet)! Please try another search.\n")
                searchBook(userID, cart)

    elif (selection == '4'):
        genreSearch = input("Please enter Genre: ")
     
        SQL = "SELECT genre FROM book"
        cur.execute(SQL)
        df_genre = pd.DataFrame(cur.fetchall())
        df_genre.columns=["genre"]

        if(df_genre.isin([genreSearch]).any().any()):
                SQL = "select isbn, name, author_firstname, author_lastname, genre, num_pages, rating, price, stock, format from book where genre = '{genre}' group by isbn, genre;".format(genre=genreSearch)
                cur.execute(SQL)
                df_search = pd.DataFrame(cur.fetchall())
                df_search.columns=[ x.name for x in cur.description ]
                print("\n####################################")
                print(df_search)
                print("\n####################################")

        else:
            print("\n########## ERROR ##########")
            print("Your Genre is not in our bookstore database (yet)! Please try another search.\n")
            searchBook(userID, cart)

    elif (selection == '5'):
        ratingSearch = input("Please enter Rating (specific number from 1-5): ")
        if(ratingSearch not in ["1",'2','3','4','5']):
            print("\nERROR: Please enter a rating that is between 1-5! Returning to menu.")
            searchBook(userID, cart)
        SQL = "select isbn, name, author_firstname, author_lastname, genre, num_pages, rating, price, stock, format from book where rating = '{rating}' group by isbn, rating;".format(rating=ratingSearch)
        cur.execute(SQL)
        df_search = pd.DataFrame(cur.fetchall())
        df_search.columns=[ x.name for x in cur.description ]
        print("\n####################################")
        print(df_search)
        print("\n####################################")

    elif (selection=='6'):
        ratingSearch = input("Please enter Rating (Number from 1-5), ex. 4, results will be all books higher than (and equal to) 4: ")
        if(ratingSearch not in ["1",'2','3','4','5']):
            print("\nERROR: Please enter a rating that is between 1-5! Returning to menu.")
            searchBook(userID, cart)
        SQL = "select isbn, name, author_firstname, author_lastname, genre, num_pages, rating, price, stock, format from book where rating >= '{rating}' group by isbn, rating;".format(rating=ratingSearch)
        cur.execute(SQL)
        df_search = pd.DataFrame(cur.fetchall())
        df_search.columns=[ x.name for x in cur.description ]
        print("\n####################################")
        print(df_search)
        print("\n####################################")
    
    elif (selection=='0'):
        bookCatalogue(userID, cart)

    else:
        print("ERROR: Invalid choice! Please choose an option from the menu (1-6)")
        searchBook(userID, cart)
    
    while (flag):
            print("\nIf you would like to add a book to your cart, please enter the book number from your search result. \nIf you want to continue browsing press c. \nIf you want to go back to the menu press b")

            selection = input()
            results = df_search.shape[0]
        
            if (selection == 'c' or selection == 'C'):
                flag = False
                searchBook(userID, cart)
            elif(selection == 'b' or selection == 'B'):
                flag = False
                bookCatalogue(userID, cart)
            elif (selection.isnumeric()):
                if(0 <= int(selection) <= results-1):
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
                    flag = True
            else:
                print("ERROR: Please enter a valid choice!!")
                flag = True

def main():
    cart = []

    landing_page()
    selection = input("Select an option: ")
    if(selection=='1'):
        loggedUser = user_login()

        # If there was an error with the login, they go here
        while(loggedUser == 0):
            print("\nError with either username or password.")
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
        main()
    

if __name__ == "__main__":
    main()

