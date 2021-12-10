def viewInventory():

    

def addNewBooks():


def removeBooks():

def viewReports():


def viewOrders():


def sendMoney():





def main():
    print("Welcome to the Owners dashboard, *Name*! \n")
    print("[1] View Current Inventory \n")
    print("[2] Add New Books \n")
    print("[3] Remove Books \n")
    print("[4] View Reports \n")
    print("[5] View Orders \n")
    print("[6] Send Money to Publishers \n")
    print("[0] Log Out \n")

    selection = input("Please select an option (0-6): \n")

    if(selection == "0"):
        logOut()

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
    


