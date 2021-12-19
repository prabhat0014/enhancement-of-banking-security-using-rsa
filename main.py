import rsa
import stdiomask
from os import system
from time import sleep
import random


class Account:
    def __init__(self, name, id, ccn, address, password, balance, code):
        self.name = name
        self.id = id
        self.ccn = ccn
        self.address = address
        self.password = password
        self.balance = balance
        self.code = code


def enqueue():
    while True:
        system('cls')
        print("\t\t\t---ADD USER---\n")
        print("\n\nEnter the following details:\n")
        name = input("Enter User Name: ")
        id = input("Enter User ID: ")
        ccn = input("Enter CCN: ")
        address = input("Enter Address: ")
        while True:
            password1 = stdiomask.getpass('Create new password: ')
            password2 = stdiomask.getpass('Re-Enter new password: ')
            count = 0
            if len(password1) == len(password2):
                for i in range(len(password2)):
                    if password1[i] == password2[i]:
                        count = count + 1
                    else:
                        break
                if count == len(password2):
                    break
                else:
                    print("\nRe-Entered password does not match\n")
            else:
                print("\nRe-Entered password does not match\n")
        password = password2
        bal = int(input("Enter the initial balance: "))
        balance = str(bal)
        break
    r_code = random.randint(1000, 9999)
    code = str(r_code)
    e_name = rsa_module(name, 1)
    e_id = rsa_module(id, 1)
    e_ccn = rsa_module(ccn, 1)
    e_address = rsa_module(address, 1)
    e_password = rsa_module(password, 1)
    e_balance = rsa_module(balance, 1)
    e_code = rsa_module(code, 1)
    users.append(Account(e_name, e_id, e_ccn, e_address, e_password, e_balance, e_code))
    print("\nUSER HAS BEEN SUCCESSFULLY CREATED...\n")
    print("User code:", code)
    input("Press Enter to continue...")


def rsa_module(msg, val):
    if val == 1:
        enc_message = rsa.encrypt(msg.encode(), publicKey)
        return enc_message
    elif val == 2:
        dec_message = rsa.decrypt(msg, privateKey).decode()
        return dec_message
    else:
        print("")


def check_banker_id(id):
    count = 0
    system('cls')
    print("\t\t\t---LOGIN PAGE---")
    check_id = input("\n\nENTER BANKER ID: ")
    if len(id) == len(check_id):
        for i in range(len(id)):
            if id[i] == check_id[i]:
                count = count + 1
            else:
                break

        if count == len(id):
            return 1
        else:
            return 0


def check_banker_password(password):
    check_password = stdiomask.getpass('Enter password: ')
    count = 0
    if len(password) == len(check_password):
        for i in range(len(check_password)):
            if password[i] == check_password[i]:
                count = count + 1
            else:
                break
        if count == len(check_password):
            return 1
        else:
            return 0
    else:
        return 0


def display():
    system('cls')
    print("\t\t\t---RECORDS---")
    print("\n\n")
    if len(users) == 0:
        print("\n\t\t---NO RECORDS AVAILABLE---\n\n\n")
        input("Press Enter to continue...")
    else:
        print("\nSELECT YOUR CHOICE:\n\n1 View All Records \n2 View SpecificRecord\n")
        select = int(input("\nENTER YOUR CHOICE: "))
        if select == 1:
            system('cls')
            print("\t\t\t---RECORDS---")
            print("\n\n")
            num = 1
            for usr in users:
                print("User", num)
                print("User Name:", rsa_module(usr.name, 2))
                print("User ID:", rsa_module(usr.id, 2))
                print("User CCN:", rsa_module(usr.ccn, 2))
                print("User Address:", rsa_module(usr.address, 2))
                print("User Password:", rsa_module(usr.password, 2))
                print("User Balance:", rsa_module(usr.balance, 2))
                print("User Code:", rsa_module(usr.code, 2))
                print("\n\n")
                num = num + 1
            input("Press Enter to continue...")
        elif select == 2:
            system('cls')
            print("\t\t\t---RECORDS---")
            want_id = input("\nEnter ID you want to search: ")
            flag = 0
            for usr in users:
                if rsa_module(usr.id, 2) == want_id:
                    flag = 1
                    print("\nRECORD FOUND!!!")
                    print("User Name:", rsa_module(usr.name, 2))
                    print("User ID:", rsa_module(usr.id, 2))
                    print("User CCN:", rsa_module(usr.ccn, 2))
                    print("User Address:", rsa_module(usr.address, 2))
                    print("User Password:", rsa_module(usr.password, 2))
                    print("User Balance:", rsa_module(usr.balance, 2))
                    print("User Code:", rsa_module(usr.code, 2))
                    print("\n\n")
                    input("Press Enter to continue...")
            if flag == 0:
                print("\nRECORD NOT FOUND!!!\n")
                input("Press Enter to continue...")


def update():
    system('cls')
    print("\t\t\t---UPDATE USER---")
    print("\n\n")
    if len(users) == 0:
        print("NO USERS FOUND!!!\n")
        input("Press Enter to continue...")
    else:
        update_id = input("Enter ID you want to update: ")
        flag = 0
        for usr in users:
            if rsa_module(usr.id, 2) == update_id:
                flag = 1
                print("\n!!! USER FOUND !!!\n")
                print("User ID:", rsa_module(usr.id, 2))
                print("User Name:", rsa_module(usr.name, 2))
                print("User CCN:", rsa_module(usr.ccn, 2))
                print("User Address:", rsa_module(usr.address, 2))
                print("User Password:", rsa_module(usr.password, 2))
                print("User Balance:", rsa_module(usr.balance, 2))

                new_name = input("\nEnter Updated Name: ")
                new_ccn = input("Enter Updated CCN: ")
                new_address = input("Enter Updated Address: ")
                while True:
                    password1 = stdiomask.getpass('Enter Updated password: ')
                    password2 = stdiomask.getpass('Re-Enter Updated password: ')
                    count = 0
                    if len(password1) == len(password2):
                        for i in range(len(password2)):
                            if password1[i] == password2[i]:
                                count = count + 1
                            else:
                                break
                        if count == len(password2):
                            break
                        else:
                            print("\nRe-Entered password does not match\n")
                    else:
                        print("\nRe-Entered password does not match\n")
                new_password = password2
                new_balance = input("Enter Updated Balance: ")

                usr.name = rsa_module(new_name, 1)
                usr.ccn = rsa_module(new_ccn, 1)
                usr.address = rsa_module(new_address, 1)
                usr.password = rsa_module(new_password, 1)
                usr.balance = rsa_module(new_balance, 1)
                r_code = random.randint(1000, 9999)
                code = str(r_code)
                usr.code = rsa_module(code, 1)
                print("\nUser has been Updated Successfully...\n")
                print("Updated User Code:", code)
                input("Press Enter to continue...")
        if flag == 0:
            print("\n!!! USER NOT FOUND !!!\n")
            input("Press Enter to continue...")


def user():
    if len(users) == 0:
        system('cls')
        print("\t\t\t---LOGIN PAGE---")
        print("\nNO USERS FOUND\n")
        input("Press Enter to continue...")
    else:
        system('cls')
        print("\t\t\t---LOGIN PAGE---")
        usr_id = input("\n\nEnter USER ID: ")
        flag = 0
        for usr in users:
            if rsa_module(usr.id, 2) == usr_id:
                flag = 1
                password = stdiomask.getpass('Enter USER password: ')
                if rsa_module(usr.password, 2) == password:
                    while True:
                        system('cls')
                        print("\t\t\t---HOME PAGE---")
                        print("\n\nSELECT YOUR CHOICE:\n\n1 Payment Process\n2 Logout\n\n")
                        select = int(input("ENTER YOUR CHOICE: "))
                        if select == 1:
                            system('cls')
                            print("\t\t\t---PAYMENT---\n")
                            print("Remaining balance:", int(rsa_module(usr.balance, 2)))
                            rec_id = input("Enter Recipient's ID: ")
                            flag = 0
                            for rec in users:
                                if rsa_module(rec.id, 2) == rec_id:
                                    flag = 1
                                    print("\n!!! RECIPIENT ID FOUND !!!\n")
                                    print("User ID:", rsa_module(rec.id, 2))
                                    print("User Name:", rsa_module(rec.name, 2))
                                    amt = int(input("\nEnter the amount: "))
                                    if int(rsa_module(usr.balance, 2)) > amt:
                                        code = stdiomask.getpass('Enter you code: ')
                                        if rsa_module(usr.code, 2) == code:
                                            bal1 = int(rsa_module(usr.balance, 2))
                                            bal2 = int(rsa_module(rec.balance, 2))
                                            bal1 = bal1 - amt
                                            bal2 = bal2 + amt

                                            usr.balance = rsa_module(str(bal1), 1)
                                            rec.balance = rsa_module(str(bal2), 1)

                                            print("\n!!! PAYMENT SUCCESSFUL !!!")
                                            print("Remaining balance:", int(rsa_module(usr.balance, 2)))
                                            input("Press Enter to continue...")
                                        else:
                                            print("\nInvalid Code\n")
                                            print("!!! PAYMENT UNSUCCESSFUL !!!")
                                            input("Press Enter to continue...")
                                    else:
                                        print("\nInsufficient balance\n")
                                        print("!!! PAYMENT UNSUCCESSFUL !!!")
                                        input("Press Enter to continue...")
                            if flag == 0:
                                print("\n!!! RECIPIENT ID NOT FOUND !!!\n")
                                input("Press Enter to continue...")
                        elif select == 2:
                            print("\n\n\t\t\t---Logging Out---")
                            sleep(3)
                            start()
                        else:
                            print("\n\t\t\t---Invalid Input---")
                            sleep(3)
                else:
                    print("\t\t\t---INVALID PASSWORD---")
                    sleep(3)
        if flag == 0:
            print("\t\t\t---INVALID USER ID---")
            sleep(3)


def start():
    while True:
        system('cls')
        print("\t\t\t---WELCOME TO ONLINE PORTAL---")

        print("\n\nSELECT YOUR CHOICE:\n\n1 Banker\n2 User\n3 Exit \n\n")
        select = int(input("ENTER YOUR CHOICE: "))

        if select == 1:
            check = check_banker_id(banker_id)
            if check == 1:
                check = check_banker_password(psw)
                if check == 1:
                    system('cls')
                    print("\t\t\t---ADMINISTRATOR PAGE---\n")
                    while True:
                        system('cls')
                        print("\t\t\t---ADMINISTRATOR PAGE---")
                        print("\nSELECT YOUR CHOICE:\n\n1 Add User\n2 View User Details\n3 Update User\n4 Logout")
                        select = int(input("\nENTER YOUR CHOICE: "))
                        if select == 1:
                            enqueue()
                        elif select == 2:
                            display()
                        elif select == 3:
                            update()
                        elif select == 4:
                            start()
                        else:
                            print("\n\n\t\t\t---INVALID INPUT---")
                            sleep(3)
                else:
                    print("\n\n\t\t\t---WRONG PASSWORD---")
                    sleep(3)
            else:
                print("\n\n\t\t\t---INVALID BANKER ID---")
                sleep(3)

        elif select == 2:
            user()

        elif select == 3:
            print("\n\n\t\t\t---EXITING THE PORTAL---")
            sleep(3)
            exit(0)

        else:
            print("\n\t\t\t---Invalid Input---")
            sleep(3)
            start()


banker_id = "0000"
psw = "password"
publicKey, privateKey = rsa.newkeys(512)
users = []
start()