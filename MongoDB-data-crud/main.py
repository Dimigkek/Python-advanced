from bson import ObjectId
from pymongo import MongoClient
from random import *
import datetime
import random
import string
import names

cluster = MongoClient("mongodb://localhost:27017/employees")
db = cluster["employees"]
collection = db["employees"]


def create_employees():
    ask1 = input("Insert a name:\t").title()
    ask2 = int(input("Insert an age:\t"))
    ask3 = input("Insert ID Number:\t").upper()
    ask4 = int(input("Insert Salary:\t"))
    ask_date = input("Insert year hired")
    post = {"name": ask1, "age": ask2, "ID Number": ask3, "Salary": ask4, "Year Hired": ask_date}
    collection.insert_one(post)
    print("\nRegistration Success!\n")


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



def random_dater():
    year = random.randrange(2008, 2022)
    dater = str(year)
    return dater


def auto_create_employees():
    ask1 = names.get_full_name()
    ask2 = randrange(20, 65)
    ask3 = id_generator()
    ask4 = randrange(400, 2000)
    ask_dater = random_dater()
    post = {"name": ask1, "age": ask2, "ID Number": ask3, "Salary": ask4, "Year Hired": ask_dater}
    collection.insert_one(post)


def search_employee():
    ask5 = input("Do you like to search base on name,age,ID,income or the whole company?\t").lower()
    if ask5 == "name":
        ask6 = input("Insert a name:\t")
        ask6_1 = ask6.title()
        for x in collection.find({"name": ask6_1}):
            print(x)
    elif ask5 == "age":
        ask6 = int(input("Insert age:\t"))
        for x in collection.find({"age": ask6}):
            print(x)

    elif ask5 == "income":
        ask6 = int(input("Insert income:\t"))
        for x in collection.find({"Salary": ask6}):
            print(x)

    elif ask5 == "id":
        ask6 = input("Insert id:\t")
        ask6_1 = ask6.upper()
        for x in collection.find({"ID Number": ask6_1}):
            print(x)

    elif ask5 == "whole company":
        for x in collection.find():
            print(x)

    else:
        pass


def delete_employee():
    ask8 = input("Insert the id you want to be deleted:\t").title()
    collection.delete_one({"_id": ObjectId(ask8)})
    print("Deleted!")


def edit_employee():
    ask7 = input("Insert the object_id of the person you want to edit:\t").lower()
    ask7_2 = input("What you want to change?\t")
    ask7_3 = input("To what?\t")
    doc = collection.find_one_and_update(
        {"_id": ObjectId(ask7)}, {"$set": {ask7_2: ask7_3}}, upsert=True)
    print("Edit Done!")


def main():
    print("Welcome to MongoDB Test:\n")
    menu_active = True
    while menu_active:
        print("1: Create\n"
              "2: Search\n"
              "3: Edit\n"
              "4: Delete\n"
              "5: Auto-fill db\n"
              "6: Exit")
        option = int(input("Choose an option:\t "))
        if option == 1:
            ask = input("You want to create one or more element?\t").lower()
            if ask == "one":
                create_employees()
            elif ask == "more":
                ask4 = int(input("How many?\t"))
                for somany in range(0, ask4):
                    create_employees()
            else:
                pass
        elif option == 2:
            search_employee()
        elif option == 3:
            edit_employee()
        elif option == 4:
            delete_employee()
        elif option == 6:
            ask11 = input("Do you want to clear the data already exist?\t").lower()
            if ask11 == "yes" or ask11 == "Yes":
                collection.delete_many({})
                print("GoodBye!")
                break
            else:
                print("GoodBye!")
                break
        elif option == 5:
            ask10 = int(input("How many employees should I insert?\t"))
            for employ in range(0, ask10):
                auto_create_employees()


main()
