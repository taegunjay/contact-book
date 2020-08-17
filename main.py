from peewee import *
from datetime import date
import re
db = PostgresqlDatabase('contacts', user='postgres', password='',
                        host='localhost', port=5432)

db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Contact(BaseModel):
    first_name = CharField()
    last_name = CharField()
    phone_number = CharField()


db.create_tables([Contact])

# jay = Contact(first_name='Jay', last_name='Choe', phone_number='123-456-7890')
# jay.save()
# jay.delete_instance()


def search_Contacts():
    start = input(" ========== Contact Menu ==========\n   What do you like to do?\n \n   press 1 to ADD\n   press 2 to UPDATE\n   press 3 to DELETE\n   press 4 to SEARCH\n   press 5 to SHOWALL\n   \n ================================== \n\n   please choose from menu above: ")

    if start == "4":

        search_name = input(
            "To search, enter the person's first name: ")
        single_search = Contact.get(Contact.first_name == search_name)
        print(
            f"{single_search.first_name} {single_search.last_name} {single_search.phone_number}")
        next = input(
            'Would you like to continue? (y/n) If not, the app will exit: ')
        if next == "y":
            search_Contacts()

    elif start == "1":

        create_first_name = input(
            "Follow to create a new contact.\n First name: ")
        create_last_name = input(
            "Last name: "
        )

        create_phone_number = input("Phone Number (000-000-0000): ")

        while(not re.match("[0-9]{3}-[0-9]{3}-[0-9]{4}$", create_phone_number)):
            print("please write in format has been provided. Including '-'")
            create_phone_number = input("Phone Number (000-000-0000): ")
        new = Contact(first_name=create_first_name, last_name=create_last_name,
                      phone_number=create_phone_number)
        new.save()
        print(
            f'{new.first_name} {new.last_name} {new.phone_number} ')

        next = input(
            'Would you like to continue ? (y/n) If not, the app will exit: ')
        if next == "y":
            search_Contacts()
    elif start == "5":
        for contact in Contact.select():
            print(
                f"{contact.first_name} {contact.last_name} {contact.phone_number}")
        next = input(
            'Would you like to continue? (y/n) If not, the app will exit: ')
        if next == "y":
            search_Contacts()
    elif start == "2":
        for contact in Contact.select():
            print(
                f" {contact.id} : {contact.first_name} {contact.last_name}, {contact.phone_number}")
        single_entry = input(
            "Type id number provided above for the person you like to update : ")
        contact = Contact.get(Contact.id == single_entry)
        print(
            f"{contact.first_name} {contact.last_name} {contact.phone_number}")

        question_update = input(
            'What would you like to update?\n  First Name = 1\n  Last Name = 2\n  Phone Number = 3\n :')
        if question_update == "1":
            new_first_name = input('Enter the new first name: ')
            contact.first_name = new_first_name
            contact.save()
            print(
                f"{contact.first_name} {contact.last_name} {contact.phone_number}")
        elif question_update == "2":
            new_last_name = input('Enter the new last name: ')
            contact.last_name = new_last_name
            contact.save()
            print(
                f"{contact.first_name} {contact.last_name} {contact.phone_number}")

        elif question_update == "3":
            new_phone_number = input(
                "Enter the new phone number (000-000-0000)")
            while(not re.match("[0-9]{3}-[0-9]{3}-[0-9]{4}$", new_phone_number)):
                print("please write in format has been provided. Including '-'")
                new_phone_number = input("Phone Number (000-000-0000): ")
            contact.phone_number = new_phone_number
            contact.save()
            print(
                f"{contact.first_name} {contact.last_name}, {contact.phone_number}")
        next = input(
            'Would you like to continue? (y/n) If not, the app will exit: ')
        if next == "y":
            search_Contacts()
    elif start == "3":
        for contact in Contact.select():
            print(
                f" {contact.id} :{contact.first_name} {contact.last_name}, {contact.phone_number}")
        single_entry = input(
            "Type ID number which you like to delete ")
        contact = Contact.get(Contact.id == single_entry)

        contact.delete_instance()
        print(
            f" {contact.id} :{contact.first_name} {contact.last_name}, {contact.phone_number}   has been deleted")

        next = input(
            'Would you like to continue? (y/n) If not, the app will exit: ')
        if next == "y":
            search_Contacts()


search_Contacts()
db.close()
