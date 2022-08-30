#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 23:42:43 2021

@author: garycoxhead
"""

# Import the date time module and define a function formatDate.

import datetime
import json
import csv

# Define a new function formatDate
def formatDate(refValue, dateValue):
    """A function to set the format of date"""
    formatRef = datetime.datetime.strptime(refValue, "%Y-%m-%d")
    newDate = (formatRef + datetime.timedelta(days=int(dateValue))).strftime("%Y-%m-%d")
    return newDate


# Create an object that can be used to calculate todays date.
dateToday = datetime.datetime.now().strftime("%Y-%m-%d")

# print(dateToday)

# Define a function to format and re-arrange the names

def formatName(name):
    """A function to format and re-arrange the input characters
    Pre-conditions:
    Post-Conditions:
    """

    # split where the name has a comma
    if ("," in name) and ("-" not in name):
        splitId = name.split(", ")
        first = splitId[0]
        second = splitId[1]
        return second + " " + first

    # split where the name has a comma and hyphen
    elif (", " in name) and (" - " in name):
        splitHyphen = name.split("-")
        first0 = splitHyphen[0]
        part_3 = splitHyphen[1]
        splitComma = first0.split(", ")
        part_2 = splitComma[0]
        part_1 = splitComma[1]
        return part_1 + part_2 + part_3

    elif len(name) == 0:
        name = "Unknown"
        return name

    elif len(name) > 0:
        return name


except_message = "Oops... Something went wrong"


try:
    with open("books.csv", mode="r", encoding="utf-8-sig") as file:
        csvFile = csv.reader(file)
        rowCount = 0
        booksDict = {}
        booksList = []
        for row in csvFile:
            if rowCount == 0:
                # Capture row names for use in the dictionary
                rowCount += 1
                name0 = row[0]
                name1 = row[1]
                name2 = row[2]
                name3 = row[3]
                name4 = row[4]
                name5 = row[5]
            else:
                booksList += [row[0]]
                booksDict[row[0]] = {
                    name1: formatName(row[1]),
                    name2: formatName(row[2]),
                    name3: formatName(row[3]),
                    name4: formatName(row[4]),
                    name5: row[5],
                    "Available": "Yes",
                    "Reserved": "No",
                    "ReservedID": [],
                }

                rowCount += 1

            # print("CSV imported successfully...")
except Exception:
    print(except_message + " when importing the books")

finally:
    file.close()

# print(booksDict)
# print(booksList)

try:
    with open("bookloans.csv", mode="r", encoding="utf-8-sig") as file:
        csvFile = csv.reader(file)
        rowCount = 0
        loanDict = {}
        for row in csvFile:
            if row[0] in booksList:
                rowCount += 1
                if row[3] != "0":
                    dateOfReturn = formatDate("1900-01-01", row[3])
                    lengthOfBorrow = int(row[3]) - int(row[2])
                else:
                    dateOfReturn = "NaN"
                    lengthOfBorrow = "NaN"
                    booksDict[row[0]]["Available"] = "No"

                loanDict[rowCount] = {
                    "BookID": row[0],
                    "MemberID": row[1],
                    "Date of loan": formatDate("1900-01-01", row[2]),
                    "Data of return": dateOfReturn,
                    "Length of Borrow": lengthOfBorrow,
                }
                # print("CSV imported successfully...")
except Exception:
    print(except_message + " when importing CSV file!")

finally:
    file.close()
# print(loanDict)

# Import the members.csv file and read into a members dictionary.

try:
    with open("members.csv", mode="r", encoding="utf-8-sig") as file:
        csvFile = csv.reader(file)
        rowCount = 0
        memberDict = {}
        for row in csvFile:
            if rowCount == 0:
                rowCount += 1
                name0 = row[0]
                name1 = row[1]
                name2 = row[2]
                name3 = row[3]
                name4 = row[4]
                name5 = row[5]
            else:
                memberDict[row[0]] = {
                    name1: row[1],
                    name2: row[2],
                    "Name": (row[1] + " " + row[2]),
                    name3: row[3],
                    name4: row[4],
                    name5: row[5],
                }
                rowCount += 1
except Exception:
    print(except_message, "whilst importing members.csv")

finally:
    file.close()

# print(memberDict)

# Write the book, loan and member dictionaries to json files.
# import json

try:
    with open("books.json", "w") as write_file:
        json.dump(booksDict, write_file)
        json_str = json.dumps(booksDict)
        print("booksDict data has been saved to books.json.")

    with open("loans.json", "w") as write_file:
        json.dump(loanDict, write_file)
        json_str = json.dumps(loanDict)
        print("loanDict data has been saved to loans.json")

    with open("members.json", "w") as write_file:
        json.dump(memberDict, write_file)
        json_str = json.dumps(memberDict)
        print("memberDict data has been saved to members.json")

except Exception:
    print(except_message + "when writing the dictionaries to the json file.")

finally:
    file.close()

# Define a function loadJSON that can be called


def loadJSON(file):
    f = open(file)
    file = json.load(f)
    f.close()
    return file


# Load all three dictionaries
try:
    books = loadJSON("books.json")
    print("books.json has been loaded")
    loans = loadJSON("loans.json")
    print("loans.json has been loaded")
    members = loadJSON("members.json")
    print("members.json has been loaded")

except Exception:
    print("ERROR: There was an error while loading the json files")


# print(len(members))

# Create a book object class


class Book(object):
    """The Book class can contain methods that are related
    to the Book class.Other classes may inherit methods
    from the book class.

    pre-Conditions:  The book class assumes there is a
    dictionary available called books that has been
    loaded into memory from books.json

    The exact book title needs to be entered for the scan
    method to function correctly. The title should be
    entered as an argument in the scan method.

    Post- Conditions:lookedUpBook can be used to test the functionality of the scan method. The book ID is
                     returned if the scan is successful.
                     If the scan has been unsuccessful a message is returned to warn the operator.
    """

    @classmethod
    def scan(cls, title):

        ID = [key for key in books if books[key]["Title"] == title]
        if len(ID) >= 1:
            return ID
        elif len(ID) == 0:
            return print(title, "was not found in the library.")


# Check class functionality
# lookedUpBook = Book.scan("God Created the Integers")
# print(lookedUpBook)

# Create a members object class
class Member(object):
    """The Method scan searches the members dictionary and returns a member ID. The Method apply accepts input data from
     a user and writes the data to members.json and new_member_details.txt. lookedUpMember can be used to check the scan method.
     apply=Member.apply() can be used to check the apply methid functionality.
    Pre-Conditions: Assumes that the members.json file has been loaded into memory.
                    The name must be entered exactly as in the members dictionary for the scan method to function
                    The user must correctly enter each piece of data when the apply method is called.
    Post-Conditions: The scan method returns the member ID or a warning message if the name is not in the dictionary.
                     The new member details will appear exactly as stated when the user inputs the data.
                     The new member is advised the membership card may take 3 days to apply.
                     The new member is issued with a member number that can be used straight away.
    """

    @classmethod
    def scan(cls, name):

        ID = [key for key in members if members[key]["Name"] == name]
        if len(ID) >= 1:
            return ID
        elif len(ID) == 0:
            return print(
                name,
                "does not have an account. Please apply for membership or check member details",
            )

    @classmethod
    def apply(cls):

        first_name = input("Please enter your first name:")
        last_name = input("Please enter your last name:")
        gender = input("please enter your gender:")
        email = input("please enter your email:")
        member_no = len(members)
        member_no = int(member_no)
        member_no = member_no + 1
        member_no_s = str(member_no)
        print("/n")
        print("Your membership number is" + member_no_s)

        members[member_no] = {
            "Firstname": first_name,
            "Last Name": last_name,
            "Gender": gender,
            "Email": email,
            "CardNumber": str(member_no) + "1",
        }

        with open("members.json", "w") as write_file:
            json.dump(members, write_file)
            json_str = json.dumps(members)
            print("The application data has been saved. \n")

        new_member = str(members[member_no])

        f = open("new_member_details.txt", "a")
        f.write("NEW MEMBER APPLICATION ON:" + str(dateToday) + "\n" "\n")
        f.write("")
        f.write(new_member)
        f.close()


# check the class functionality
# lookedUpMember = Member.scan("Charlie Roberts")

# apply=Member.apply()


class Loan(Book, Member):
    """This class allows members to borrow, reserve and return a book.
    This class inherits attibutes from the parent classes Book and Member.
    Pre-conditions: The Book and Member classes should be defined before this class can inherit attributes.
                    The classmethods in this class are encapsulated within the Loan class and accept name and titles as arguments.
    Post-conditions: json data files are loaded and updated after each classmethod has been implemented effectively.
    """

    @classmethod
    def Borrow(cls, name, title):
        """Allows existing members of the library to borrow a book from the library"""

        # Find the ID of a book and member
        BookID = Book.scan(title)[0]
        MemberID = Member.scan(name)[0]
        LoanID = [len(loans) + 1]

        # Check if the book is available
        Status = books[BookID]["Available"]
        if Status == "Yes":
            # If the book isn't reserved then issue the book and add new loan to the json file.
            if books[BookID]["Reserved"] == "No":
                dateToday = datetime.datetime.now().strftime("%Y-%m-%d")
                loans[len(loans) + 1] = {
                    "BookID": BookID,
                    "MemberID": MemberID,
                    "Date of loan": dateToday,
                    "Date of return": "NaN",
                    "Length of borrow": "NaN",
                }
                books[BookID]["Available"] = "No"
                print("You have now borrowed", title)
                print("")
                print(
                    "The loan ID for this book loan is",
                    LoanID,
                    "Please return the book using this ID.",
                )

                with open("books.json", "w") as write_file:
                    json.dump(books, write_file)
                    json_str = json.dumps(books)
                    print("The book loan has been set to unavailable in books.json")

                with open("loans.json", "w") as write_file:
                    json.dump(loans, write_file)
                    json_str = json.dumps(loans)
                    print("The book loan has been added to loans.json")

            elif books[BookID]["Reserved"] == "Yes" and books[BookID]["ReservedID"]:
                dateToday = datetime.datetime.now().strftime("%Y-%m-%d")
                loans[len(loans) + 1] = {
                    "BookID": BookID,
                    "MemberID": MemberID,
                    "Date of loan": dateToday,
                    "Date of return": "NaN",
                    "Length of borrow": "NaN",
                }
                books[BookID]["Available"] = "No"

                if len(books[BookID]["ReservedID"]) == 0:
                    books[BookID]["Reserved"] = "No"
                print("you have now borrowed", title)

            elif (
                books[BookID]["Reserved"] == "Yes"
                and MemberID in books[BookID]["ReservedID"] == MemberID
            ):
                print(
                    "Unfortunately",
                    title,
                    "is not available at the moment. You have been put on the reserved list for this book.",
                )

            else:
                print(
                    title,
                    "is not available at the moment, you can reserve this book if you like?",
                )

        elif Status == "No":
            if MemberID in books[BookID]["ReservedID"]:
                print(title, "is not available at the moment")
            else:
                print(title, "is not available at the moment")
        with open("loans.json", "w") as write_file:
            json.dump(loans, write_file)
            json_str = json.dumps(loans)
            print("The book loan has been added to loans.json")

    @classmethod
    def Return(cls, name, title):
        """Allows existing members of the library to return a book that was previously borrowed from the library
        Pre-conditions: The correct member name and book title should be used. The member should remember and use the
                        loanID that was issued when the book was loaned. The latest versions of books and loans must be
                        loaded in order to amend details.
        post-conditions: The books and loans data is updated and saved back into the permanent storage json files.
                         The borrowed book then becomes available for loan once more.
        """

        books = loadJSON("books.json")
        print("books.json has been loaded")

        loans = loadJSON("loans.json")
        print("loans.json has been loaded")

        # Find the ID of the book and member from the book and member files.
        dateToday = datetime.datetime.now().strftime("%Y-%m-%d")
        BookID = Book.scan(title)[0]
        MemberID = Member.scan(name)[0]
        LoanID = input("Please enter the loan ID of the book you are returning:")

        # Check if the book is available
        Status = books[BookID]["Available"]

        if Status == "Yes":
            print(
                "Error... The requested book return has failed. This book appears to already be available in the database???"
            )

        elif Status == "No":
            books[BookID]["Available"] = "Yes"
            loans[LoanID]["Date of return"] = dateToday

            print(
                title,
                "has been successfully returned. Thank you for using the library",
                name,
                ".",
            )

            with open("books.json", "w") as write_file:
                json.dump(books, write_file)
                json_str = json.dumps(books)
                print("The returned book data has been added to loans.json")

            with open("loans.json", "w") as write_file:
                json.dump(loans, write_file)
                json_str = json.dumps(loans)
                print("The returned book data has been added to loans.json")

    @classmethod
    def Reserve(cls, name, title):
        """The Reserve class method allows a member to reserve a book from the book library.
        Pre-conditions: The membership name and title of the book must be entered exactly as they appear in the respective
                        dictionaries.
                        Both members names and book titles must already be present in the dictionaries.
        Post-conditions: books.json file is updated with the new reservation details.


        """
        books = loadJSON("books.json")
        BookID = Book.scan(title)[0]
        books[BookID]["Reserved"] = "Yes"
        MemberID = Member.scan(name)[0]
        books[BookID]["ReservedID"] = MemberID

        with open("books.json", "w") as write_file:
            json.dump(books, write_file)
            json_str = json.dumps(books)
            print("You have sucessfully reserved", title)


# User Interface:
"""This is the user interface that would be present at the console of the library.
       Pre-conditions:  The user must correctly select the options from each menu.
                        There is currently no security or password system used.
                        Users must know and enter the exact details of their membership and book titles
                        The user interface calls classmethods from Book, Member and Loan classes.
       Post-conditions: Relevent data is written to external permanent storage in the form of json files.
                        The interface is expandable by creating new options in the menus.
"""

print("Welcome to the Library Console!\n")
print("\t Please select an option between 1-3 for the following options:")
print("\t \t 1: Existing member login")
print("\t \t 2: Apply for membership")
print("\t \t 3: Staff Login")

option = input("Please enter a number between 1 and 3:")
print("\n")
option = int(option)

# If a member wants to access the library system
if option == 1:
    ID = input("Please enter your member ID:")
    ID = str(ID)
    if ID in members:
        print("ID found")
        print(members[ID])

    else:
        print("Error, member ID not found in the database. Please check your details")

    print("Welcome to the library", ".")
    print("\n")
    print("Please select an option between 1 and 3:")
    print("\t \t 1: Borrow a Book")
    print("\t \t 2: Return a Book")
    print("\t \t 3: Reserve a Book")
    member_option = input("Please select an option")
    member_option = int(member_option)

    # If member wants to borrow a book
    if member_option == 1:
        name = input("Please enter your full name:")
        title = input("Please enter the full title of the book you'd like to borrow:")
        Loan.Borrow(name, title)

    # If member wants to return a book
    if member_option == 2:
        name = input("Please enter your full name:")
        title = input("Please enter the full title of the book you'd like to return:")
        Loan.Return(name, title)

    # If member wants to reserve a book
    if member_option == 3:
        name = input("Please enter your full name:")
        title = input("Please enter the full title of the book you'd like to return:")
        Loan.Reserve(name, title)

# If a non member wants to apply for a library membership
if option == 2:
    Member.apply()
    print(
        "Your membership application is complete. \nPlease note it may take up to 3 days for your application to be processed"
    )

# If a member of staff wants to access the
if option == 3:
    print("Welcome, please select an option")
    print("\t \t 1: Email new membership details to printers" "\n")
    staff_option = input("please enter a number")
    staff_option = int(staff_option)

    # If staff member selects option 1, remind them to email new membership details.
    if staff_option == 1:
        print(
            "At the end of the working day please email the new_member_details.txt files to the printers."
        )
        print("Still under construction...")
    else:
        print("ERROR, Please select a valid option!")
