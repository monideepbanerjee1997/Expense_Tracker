""" A Budget Tracker - Titled "Moni_Budget_Tracker"
It Helps Us To Track Our Daily Expenses, Provided which Details Are Entered On a Regular Basis, which Provides
Easy Calculation OF the Budget.
#It Has Validation OF All Stuffs, and A Thorough Check SO that Errors can Be avoided At All Cost.
#It is just The BASE Layout OF THE PROJECT and many More Advances Can BE Made upon it which i will be working on
HereAfter, I hope I will be able To Add The GUI into it too in the coming future.
#Connection to Database is Must for the Execution Of the program. Else It will show Error Message.
# localhost name should be "root" and password should be "" ,
Although the program, will ask for the username and password if it doesn't find the above.
Also Capable OF Creating the Data Base And Adding Tables To it.(IF Not found).
Modules In the Program are mysql.connector , sys, time, re, datetime, and math. """



import mysql.connector
import sys
import time
import re
import datetime
import math


class budget_track:
    #default Constructor
    def __init__(self):
        self.local_host_connect()
        self.program_menu()

    #Local_Host_Connection Validation.
    def local_host_connect(self):
        # If user= root and password="".
        try:
            self.conn = mysql.connector.connect(user="root", password="", host="localhost")
            self.mycursor = self.conn.cursor()
            self.database_connect(1, 'root' , '')

        # To Tackle Someother Kind OF Error like Connection Not Established..
        except mysql.connector.Error as e:
            print("""Some Other Kind OF Error HAS OCCURED.\nCHECK IF Xampp/Vampp is Connected/Started.\nALSO CHECK if user='root', password='',host='localhost' and Try Running The Source Code Again.""")
            exit()

        # Accept username and password from the user.
        except:
            while True:
                user_name = input("Enter UserName For DataBase Connection: ")
                user_name = user_name.lower()
                password_for = input("Enter The Password For The DataBase Connection: ")
                try:
                    self.conn = mysql.connector.connect(user=user_name, password=password_for, host="localhost")
                    self.mycursor = self.conn.cursor()
                    self.database_connect(2,user_name,password_for)
                    break
                except:
                    print("Wrong UserName and Password Given For Database Connection LocalHost... Please Try Again in 2 seconds...")
                    time.sleep(2)

    #DataBase_Connection_Validation.
    def database_connect(self,check,user_name,password_for):
        # If user= root and password="" and Proceeding to Connect to DataBase.
        if check == 1:
            # Check if Database Exists Then Connect TO IT.
            try:
                self.conn = mysql.connector.connect(user=user_name, password="", host="localhost",
                 database="Moni_Budget_Tracker")
                self.mycursor = self.conn.cursor()
                print("Connecting to DataBase.. Wait A While...  ")
            # If Database Doesn't Exists. Create The DataBase and Then Connect TO IT.
            except:
                self.conn = mysql.connector.connect(user=user_name, password="", host="localhost")
                self.mycursor = self.conn.cursor()
                self.mycursor.execute('CREATE DATABASE Moni_Budget_Tracker')
                self.conn.commit()
                print("Connecting to DataBase.. Wait A While...  ")
                time.sleep(2)
                self.conn = mysql.connector.connect(user="root", password="", host="localhost",
                                                    database="Moni_Budget_Tracker")
                self.mycursor = self.conn.cursor()

        # Accept username and password from the user and Proceeding to Connect to DataBase.
        elif check==2:
            # Check if Database Exists Then Connect TO IT.
            try:
                self.conn = mysql.connector.connect(user=user_name, password=password_for, host="localhost",
                 database="Moni_Budget_Tracker")
                self.mycursor = self.conn.cursor()

            # If Database Doesn't Exists. Create The DataBase and Then Connect TO IT.
            except:
                self.conn = mysql.connector.connect(user=user_name, password=password_for, host="localhost")
                self.mycursor = self.conn.cursor()
                self.mycursor.execute('CREATE DATABASE Moni_Budget_Tracker')
                self.conn.commit()
                print("Connecting to DataBase.. Wait A While... ")
                time.sleep(2)
                self.conn = mysql.connector.connect(user="root", password="", host="localhost",
                                                    database="Moni_Budget_Tracker")
                self.mycursor = self.conn.cursor()

        # To Tackle Someother Kind OF Error.
        else:
            print("""Some Other Kind OF Error OCCURED.CHECK IF Xampp/Vampp is Connected/Started. CHECK if user='root', password='',host='localhost'""" )

    #Program_Menu 1. Register. 2. Login 3. Exit
    def program_menu(self):
        user_response1=input("""***************************************************************Welcome to Moni_BUDGET_TRACKER***************************************************************\n1. Enter 1 TO REGISTER\n2. Enter 2 TO LOGIN \n3. Enter 3 TO EXIT\nENTER YOUR CHOICE : """)
        if user_response1 == "1":
            self.register()
        elif user_response1 == "2":
            self.login()
        elif user_response1 =="3":
            self.goodbye()
        else:
            print("WRONG CHOICE.!. Look At The Menu and Try Again Accordingly. ")
            self.program_menu()


    #User_Menu. Menu To BE Shown To User After Login. 1.Enter 1 to ADD SAVINGS
    # 2.Enter 2 TO ADD EXPENSES  3.Enter 3 To GENERATE BALANCE SHEET 4.Enter 4 To Logout
    def user_menu(self,current_user_id):
        user_response2=input("""1. Enter 1 TO ADD TO SAVINGS\n2. Enter 2 TO ADD TO EXPENSES \n3. Enter 3 TO GENERATE BALANCE SHEET\n4. Enter 4 TO LOGOUT \nENTER YOUR CHOICE : """)
        if user_response2 == "1":
            self.add_savings(current_user_id)
        elif user_response2 == "2":
            self.add_expenses(current_user_id)
        elif user_response2 == "3":
            self.generate_balance_sheet(current_user_id)
        elif user_response2 == "4":
            self.logout()
        else:
            print("WRONG CHOICE.!. Look At The Menu and Try Again Accordingly. ")
            self.user_menu()

    #Register To BE Done Here. With Proper Validation.
    def register(self):

        #Creating table `users_moni_budget_tracker` IF It Doesn't Exists into `moni_budget_tracker` .
        self.mycursor.execute("""CREATE TABLE if not Exists `Moni_Budget_Tracker`.`users_moni_budget_tracker`(`user_id` INT NOT NULL AUTO_INCREMENT, 
        `Full_Name` VARCHAR(255) NOT NULL, `Email_ID` VARCHAR(255) NOT NULL,
         `Password` VARCHAR(255) NOT NULL, `Gender` VARCHAR(255) NOT NULL,
         `City` VARCHAR(255) NOT NULL, PRIMARY
          KEY(`user_id`), UNIQUE(`Email_ID`)) ENGINE = InnoDB;""")
        self.conn.commit()

        print("Enter The Following Credentials To Register :- ")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")

        #Validation OF First Name. Name Strictly Cannot Have Digits.
        while True:
            first_name = input("ENTER YOUR FIRST NAME: ")
            if first_name and first_name.isalpha():
                break
            elif first_name and first_name.isdigit():
                print("FIRST NAME MUST BE ALPHABET CHARACTERS ONLY!")
            else:
                print("YOUR FIRST NAME CANNOT CONTAIN DIGITS..!!")

        # Validation OF Last Name. Name Strictly Cannot Have Digits.
        while True:
            last_name = input("ENTER YOUR LAST NAME : ")
            if last_name and last_name.isalpha():
                break
            elif last_name and last_name.isdigit():
                print("LAST NAME MUST BE ALPHABET CHARACTERS ONLY!")
            else:
                print("YOUR LAST NAME CANNOT CONTAIN DIGITS..!!")
        name = first_name + ' '+ last_name

        # Validation OF Email-ID. Email ID STRICTLY NEEDS TO BE UNIQUE. 
        # Same Email Cannot Have Already existed. IF Same Email Entered Which Already Exists.
        # Program REDIRECTS TO THE MAIN MENU.
        # Strictly Needs to have the format abc@cde.com
        # or abc@123.in is correct. but abc@123.123 is wrong and unacceptable.
        # Needs to have '@' and '.' and after domain Extension  name that is after '.' Strictly cannot contain DIGITS.
        while True:
            # Validation OF Email-ID. Email ID Strictly Needs to have the format abc@cde.com or abc@abc.in is correct etc.
            # or abc@123.in is INCORRECT, Domain Name CanNot Contain Digits and also abc@123.123 is wrong and STRICTLY UNACCEPTABLE.
            # Needs to have '@' and '.' and the Domain Name and Extension that is after '@' Strictly CANNOT CONTAIN DIGITS.
            # UNLESS EMAIL IS Entered Properly in the Correct format. Program will Keep Asking For A Valid Email-ID To be Entered.
            while True:
                email = input("ENTER YOUR EMAIL : ")
                # match = re.search(r'[\w.-]+@[\w.-]+.\w+', email)
                if re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z-]+\.[a-zA-Z-.]+$)", email):
                    break
                else:
                    print("ENTER A VALID EMAIL-ID THAT CONTAINS '@'  and '.' like:  abc@abc.com  BUT abc@123 and also abc@123.123 in is INCORRECT.\nUsername Can/May Contain digits But after '@' i.e. DOMAIN NAME AND EXTENSION (After '.') Cannot Strictly Contain Digits ")
            self.mycursor.execute("SELECT * FROM `users_moni_budget_tracker` WHERE `Email_ID` LIKE '%s' " % (email))
            user_list = self.mycursor.fetchall()
            counter = 0
            for i in user_list:
                counter = counter + 1
            if counter == 0:
                break
            else:
                print("SORRY!.THE SAME EMAIL-ID EXISTS IN THE ACCOUNT\nPLEASE TRY REGISTERING WITH A DIFFERENT EMAIL-ID OR LOGIN IF YOU ALREADY HAVE AN ACCOUNT.")
                print("Your Being Redirected To The Main Menu.. ")
                time.sleep(1.5)
                self.program_menu()

        # Validation OF PASSWORD. Strong PassWord Only Accepted. MUST CONTAIN
        # An UPPERCASE CHARACTER (A-Z), A LOWERCASE CHARACTER (a-z)
        # A NUMBER(0-9), and Any of these SPECIAL CHARACTERS (@#$%^&+=)
        while True:
            password = input("""ENTER YOUR PASSWORD, PASSWORD MUST BE STRONG. (MUST CONTAIN ATLEAST 8 CHARACTERS,\nAn UPPERCASE CHARACTER (A-Z), A LOWERCASE CHARACTER (a-z), A NUMBER (0-9), and Any of these SPECIAL CHARACTERS (@#$%^&+=) : """)
            pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=*]).*$"
            result = re.findall(pattern, password)
            if (result):
                break
            else:
                print("PASSWORD NOT VALID!. PASSWORD MUST BE STRONG.(MUST CONTAIN ATLEAST 8 CHARACTERS For Securty Reasons.)\n ")
        # Validation For Proper Gender.
        # M/m FOR MALE, F/f FOR FEMALE, O/o FOR OTHERS. ONLY THESE 6 CHARACTERS WILL BE ACCEPTED.
        while True:
            gender=input("ENTER YOUR GENDER (M for Male /F for Female /O for Others) : ")
            gender=gender.upper()
            if gender == 'M' or gender == 'F' or gender == 'O':
                break
            else:
                print("Enter Gender in Either M for Male or F for Female or O for Others")

        # Validation for City. Cannot Contain Digits.
        while True:
            city=input("ENTER YOUR CITY: ")
            if city and city.isalpha():
                break
            else:
                print("SORRY! CITY NAME CANNOT CONTAIN DIGITS, PLEASE TRY ENTERING CITY NAME AGAIN.. ")

        self.mycursor.execute("""INSERT INTO `users_moni_budget_tracker`
            (`user_id`, `Full_Name`, `Email_ID`, `Password`, `Gender`, `City`)
            VALUES (NULL, '%s', '%s', '%s', '%s', '%s')""" % (name, email, password, gender, city))
        self.conn.commit()
        print("REGISTERING..  THIS MAY TAKE A WHILE.. HAVE PATIENCE..")
        time.sleep(2)
        print("REGISTRATION SUCCESSFUL at ... " + time.asctime() + "\nPLEASE LOG IN TO CONTINUE.. ")
        self.program_menu()


    # Login To BE Done Here. Email-Id entered Needs To already exist for Login To be Successfull.
    # Along with Correct Password. If Incorrect Email/Password Entered, Program is Redirected To The Program Menu.
    def login(self):
        self.mycursor.execute("""CREATE  TABLE if not Exists `Moni_Budget_Tracker`.`users_moni_budget_tracker`(`user_id` INT NOT NULL AUTO_INCREMENT, 
        `Full_Name` VARCHAR(255) NOT NULL, `Email_ID` VARCHAR(255) NOT NULL,
        `Password` VARCHAR(255) NOT NULL, `Gender` VARCHAR(255) NOT NULL,
         `City` VARCHAR(255) NOT NULL, PRIMARY KEY(`user_id`), UNIQUE(`Email_ID`)) ENGINE = InnoDB;""")
        self.conn.commit()
        print("ENTER THE FOLLOWING CREDENTIALS TO LOGIN : ")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")

        # Validation OF Email-ID. Email ID Strictly Needs to have the format abc@cde.com or abc@abc.in is correct etc.
        # or abc@123.in is INCORRECT, Domain Name CanNot Contain Digits and also abc@123.123 is wrong and STRICTLY UNACCEPTABLE..
        # Needs to have '@' and '.' and the Domain Name and Extension that is after '@' Strictly CANNOT CONTAIN DIGITS.
        # UNLESS EMAIL IS Entered Properly in the Correct format. Program will Keep Asking For A Valid Email-ID To be Entered.
        while True:
            email_for_login = input("ENTER YOUR EMAIL TO LOGIN : ")
            # match = re.search(r'[\w.-]+@[\w.-]+.\w+', email)
            if re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z-]+\.[a-zA-Z-.]+$)", email_for_login):
                break
            else:
                print("HAVE PATIENCE... ENTER A VALID EMAIL-ID THAT CONTAINS '@' and '.' like:  abc@abc.com BUT abc@123 and also abc@123.123 in is INCORRECT.\nUsername Can/May Contain digits But after '@' i.e. DOMAIN NAME AND EXTENSION (After '.') Cannot Strictly Contain Digits")
                print("Your Being Redirected.. ")
                time.sleep(1.5)
                self.check_what()

        password_for_login = input("ENTER YOUR PASSWORD TO LOGIN : " )

        # Checking From Table 'users_moni_budget_tracker' that if any user with the same email and password exists.
        # IF exists login  and proceed to the User Menu ,else Redirect to the Program Menu.
        self.mycursor.execute("SELECT * FROM `users_moni_budget_tracker` WHERE `Email_ID` LIKE '%s' AND `Password` LIKE '%s'" %(email_for_login,password_for_login))
        user_list = self.mycursor.fetchall()
        counter = 0
        for i in user_list:
            counter=counter+1
            current_user = i

        if counter == 1:
            self.is_logged_in = 1
            current_user_id = current_user[0]
            print("LOGGING INTO YOUR ACCOUNT...")
            time.sleep(1.5)
            print("YOU HAVE LOGGED IN SUCCESSFULLY ... ")
            self.user_menu(current_user_id)
        else:
            print("Incorrect Email/Password!!...ENTER CORRECT EMAIL-ID TO LOGIN OR PLEASE REGISTER TO CONTINUE AND THEN LOGIN")
            self.program_menu()

    # Check so That User Doesn't Gets Stuck to an Infinite Loop During Login(While Not Entering a Valid Email).
    def check_what(self):
        check= input("1. ENTER 1 TO GO BACK TO MAIN MENU. \n2. ENTER 2 TO CONTINUE IN LOGIN MENU. \n3. ENTER 3 TO EXIT \nENTER YOUR CHOICE :  ")
        if check == "1":
            self.program_menu()
        elif check == "2":
            self.login()
        elif check == "3":
            self.goodbye()
        else:
            print("WRONG CHOICE.!. Look At The Menu and Try Again Accordingly. ")
            self.check_what()
    
    # Calculates Current Balance To Store into the DataBase. For The Specified Logged In User.
    def get_current_balance(self,current_user_id):
        self.mycursor.execute("SELECT * FROM `Budget_Transaction` WHERE `user_id` LIKE '%s'" % (current_user_id))
        all_list = self.mycursor.fetchall()
        if len(all_list) == 0:
            self.current_balance = 0
        else:
             self.current_balance = all_list[-1][6]

    
    # Calculates and Adds To Credit/Savings and also Calculates The Current_Balance.
    # For The Specified Logged In User.
    def add_savings(self,current_user_id):
        # Creating table `Budget_Transaction` IF It Doesn't Exists into `moni_budget_tracker` .
        self.mycursor.execute("""CREATE TABLE if NOT Exists `Moni_Budget_Tracker`.`Budget_Transaction`(`Transaction_ID` INT NOT NULL AUTO_INCREMENT,
        `user_id` INT NOT NULL, `Date` DATE NOT NULL, `Description` VARCHAR(255) NOT NULL,
        `Credit` DOUBLE DEFAULT NULL, `Debit` DOUBLE DEFAULT NULL, `Current_Amount` DOUBLE NOT NULL,
        PRIMARY KEY(`Transaction_ID`)) ENGINE = InnoDB;""")
        self.conn.commit()

        # Validation For Date Format. Strictly to YYYY-MM-DD AND DATE SHOULD BE A VALID ONE.
        while True:
            date = input("ENTER THE DATE STRICTLY IN YYYY-MM-DD FORMAT And MAKE SURE That the DATE ENTERED IS VALID ONE : ")
            try :
                datetime.datetime.strptime(date, '%Y-%m-%d')
                break
            except:
                print("MAKE SURE THAT THE DATE IS VALID/IMPROPER DATE FORMAT! (like 2017-02-20, i.e.YYYY: 2017, MM:02, DD:20)!\nTHE DATE SHOULD BE STRICTLY IN YYYY-MM-DD Format!!")

        # Validation For Descrition OF Savings. Description Cannot Contain Digits. Only Alphabets/String Alllowed.
        # Validation For Descrition OF Expense. Description Cannot Contain Digits. Only Alphabets/String Alllowed.
        while True:
            info_of_expense = input("ENTER THE DESCRIPTION OF THE EXPENSE : ")
            if info_of_expense and info_of_expense.isalpha():
                break
            else:
                print("DON'T ENTER DIGITS FOR DESCRIPTION,ENTER DETAILS TOO.. ELSE YOU WILL HAVE PROBLEM CHECKING OUT LATER ON.. ")

        # Validation for Amount Entered. AMOUNT NEEDS TO BE STRICTLY IN DIGITS. NO ALPHABETS OR OTHER CHARACTERS ALLOWED.
        while True:
            savings_amount = input("ENTER THE AMOUNT TO BE CREDITED : ")
            if re.search(r"^[+-]?([0-9]*[.])?[0-9]+$", savings_amount):
                break
            else:
                print("HOW CAN AMOUNT BE OF CHARACTERS? PLEASE ENTER THE AMOUNT PROPERLY AGAIN.. ")
        self.get_current_balance(current_user_id)
        self.current_balance = self.current_balance + float(savings_amount)
        self.mycursor.execute("""INSERT INTO `Budget_Transaction` (`Transaction_ID`, `user_id`, 
        `Date`, `Description`, `Credit`, `Debit`, `Current_Amount`)
         VALUES (NULL, '%s', '%s' , '%s', '%s', '%s' , '%s')""" %
         (current_user_id, date, info_of_expense, savings_amount, ' ' , self.current_balance))
        self.conn.commit()
        time.sleep(1)
        print("Amount Credited Successfully... ")
        self.user_menu(current_user_id)

    # Calculates and Adds To Debit/Expenses and also Calculates The Current_Balance.
    # For The Specified Logged In User.
    def add_expenses(self,current_user_id):
        # Creating table `Budget_Transaction` IF It Doesn't Exists into `moni_budget_tracker` .
        self.mycursor.execute("""CREATE TABLE if NOT Exists `Moni_Budget_Tracker`.`Budget_Transaction`(`Transaction_ID` INT NOT NULL AUTO_INCREMENT,
         `user_id` INT NOT NULL, `Date` DATE NOT NULL, `Description` VARCHAR(255) NOT NULL,
          `Credit` DOUBLE DEFAULT NULL, `Debit` DOUBLE DEFAULT NULL, `Current_Amount` DOUBLE NOT NULL,
          PRIMARY KEY(`Transaction_ID`)) ENGINE = InnoDB;""")
        self.conn.commit()
        
        # Validation For Date Format. Strictly to YYYY-MM-DD AND DATE SHOULD BE A VALID ONE.
        while True:
            date = input("ENTER THE DATE STRICTLY IN YYYY-MM-DD FORMAT And And MAKE SURE That the DATE ENTERED IS VALID ONE : ")
            try :
                datetime.datetime.strptime(date, '%Y-%m-%d')
                break
            except:
                print("MAKE SURE THAT THE DATE IS VALID/IMPROPER DATE FORMAT! (like 2017-02-20, i.e.YYYY: 2017, MM:02, DD:20)!\nTHE DATE SHOULD BE STRICTLY IN YYYY-MM-DD Format!!")

        # Validation For Descrition OF Expense. Description Cannot Contain Digits.
        # Only Alphabets/String Alllowed.
        while True:
            info_of_expense = input("ENTER THE DESCRIPTION OF THE EXPENSE : ")
            if info_of_expense and info_of_expense.isalpha():
                break
            else:
                print("DON'T ENTER DIGITS FOR DESCRIPTION,ENTER DETAILS TOO.. ELSE YOU WILL HAVE PROBLEM CHECKING OUT LATER ON.. ")

        # Validation for Amount Entered. AMOUNT NEEDS TO BE STRICTLY IN DIGITS.
        # NO ALPHABETS OR OTHER CHARACTERS ALLOWED.
        while True:
            expense_amount = input("ENTER THE AMOUNT TO BE DEBITED : ")
            if re.search(r"^[+-]?([0-9]*[.])?[0-9]+$", expense_amount):
                break
            else:
                print("HOW CAN AMOUNT BE OF CHARACTERS? PLEASE ENTER THE AMOUNT PROPERLY AGAIN.. ")

        self.get_current_balance(current_user_id)
        self.current_balance = self.current_balance - float(expense_amount)
        self.mycursor.execute("""INSERT INTO `Budget_Transaction` (`Transaction_ID`, `user_id`, 
        `Date`, `Description`, `Credit`, `Debit`, `Current_Amount`)
         VALUES (NULL, '%s', '%s', '%s', '%s' , '%s', '%s')""" %
         (current_user_id, date, info_of_expense,' ', expense_amount, self.current_balance))
        self.conn.commit()
        time.sleep(1)
        print("Expense Added Successfully...")
        self.user_menu(current_user_id)

    # Generates The Balance Sheet For The Specific User. According to the Transaction ID He Has Made Those Transactions.
    def generate_balance_sheet(self,current_user_id):
        # Creating table `Budget_Transaction` IF It Doesn't Exists into `moni_budget_tracker` .
        self.mycursor.execute("""CREATE TABLE if NOT Exists `Moni_Budget_Tracker`.`Budget_Transaction`(`Transaction_ID` INT NOT NULL AUTO_INCREMENT,
         `user_id` INT NOT NULL, `Date` DATE NOT NULL, `Description` VARCHAR(255) NOT NULL,
          `Credit` DOUBLE DEFAULT NULL, `Debit` DOUBLE DEFAULT NULL, `Current_Amount` DOUBLE NOT NULL,
           PRIMARY KEY(`Transaction_ID`)) ENGINE = InnoDB;""")
        self.conn.commit()

        # Selecting From DataBase where in tableeBudget_Transaction where user_id = current_user_id
        # And fetching the list to Generate the Balance Sheet.
        self.mycursor.execute("SELECT * FROM `Budget_Transaction` WHERE `user_id` LIKE '%s'" %(current_user_id))
        all_transactions_list= self.mycursor.fetchall()

        if len(all_transactions_list) == 0:
          print("SORRY.. YOU HAVE MADE NO INPUT THAT CAN BE VIEWED .. PLEASE PROVIDE SOME TRANSACTIONS MADE AND THEN CHECK THE BALANCE SHEET AGAIN.. ")
        else:
            print('{:^10}      {:^20}   {:^20}  {:^20}   {:^20}   {:^20} '.format("Date", "Transaction-ID", "Description", "Credit", "Debit" , "Current_Amount"))
            print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
            count=1
            for i in all_transactions_list:
                print(i[2],end="     ")
                print('||{:^16} || {:^22} || {:^16} || {:^22} || {:^17}' . format(count, i[3], i[4], i[5], round(i[6],2)))
                count=count+1
            print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
        self.user_menu(current_user_id)

    # Function That Logs an User Out When HE IS LOGGED IN. Redirects to The Main Menu.
    def logout(self):
        print("Logging Out... ")
        time.sleep(1.5)
        self.is_logged_in=0
        self.current_balance = 0
        print("You Have Successfully Logged Out at..." + time.asctime() +"\n Hope You Liked It Around.. Visit Us Again Soon... ")
        print("Redirecting To The Main Menu.. ")
        time.sleep(1)
        self.program_menu()
    
    # Function to Exit The Program/Source Code.
    def goodbye(self):
        print("Thanks For Using Moni_BUDGET_TRACKER.. Visit Us Again.. ")
        print("Closing APP... at " + time.asctime())
        time.sleep(1)
        print("Closed")
        exit()


#Object Call
obj1 = budget_track()