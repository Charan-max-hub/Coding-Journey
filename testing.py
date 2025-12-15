import os

f_name = "contact_book.txt"

def ensure_file():
    if not os.path.exists(f_name):
        with open(f_name,"w") as f:
            pass

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()

    if not (name,phone,email):
        print("Invalid input.Fields can not be empty\n")
        return

    try:
        with open(f_name,"a") as f:   
            f.write(f"{name}|{phone}|{email}\n")
        print("Contact added succesfully.\n")

    except Exception as e:
        print("error in adding contact: ",e)

def view_contact():

    try:
        with open(f_name,"r") as f:
            lines = f.readlines()

            if not lines:
                print("contact not found.\n")
                return
            
            for line in lines:
                parts = line.strip().split("|")

                if len(parts) == 3:
                    name,phone,email = parts
                    print(f"Name: {name}, Phone: {phone}, Email: {email}")

    except Exception as e:
        print("error in view contact: ",e)

def search_contact():

    key = input("Enter name or phone number to search contact: ").strip()
    if not key:
        print("Your key is invalid")
        search_contact()
    try:
        flag = 0
        with open(f_name,"r") as f:
            lines = f.readlines()

            for line in lines:
                parts = line.strip().split("|")
                name,phone,email = parts

                if key.lower() in name.lower() or phone == key:
                    flag = 1
                    print(f"Found: Name: {name}, Phone: {phone}, Email: {email}\n")

            if flag == 0:
                print("Contact not found")
                return
    except Exception as e:
        print("error in search contact: ",e)

def update_contact():
    key = input("Enter name or phone number to update contact: ").strip()
    contact_list = []
    updated = False

    try:
        
        with open(f_name,"r") as f:
            lines = f.readlines()

            for line in lines:
                
                parts = line.strip().split("|")
                if len(parts) == 3:
                    name,phone,email = parts

                    if key.lower() in name.lower() or phone == key:
                        print("Contact updating...")
                        new_name = input("Enter name: ").strip()
                        new_phone = input("Enter phone: ").strip()
                        new_email = input("Enter email: ").strip()
                        contact_list.append(f"{new_name}|{new_phone}|{new_email}\n")
                        print("Succesfully contact updated")
                        updated = True
                    else:
                        contact_list.append(line)
            
            if not updated:
                print("Contact not found.")
                return
       
        with open(f_name,"w") as f:
            f.writelines(contact_list)

    except Exception as e:
        print("error in updating contact: ",e)

def delete_contact():

    key = input("Enter name or phone number to delete contact: ").strip()
    contact_list = []
    deleted = False

    try:
        with open(f_name,"r") as f:
            lines = f.readlines()

            for line in lines:
                parts = line.strip().split("|")

                if len(parts) == 3:

                    name,email,phone = parts

                    if key.lower() in name.lower() or phone == key:
                        deleted = True
                        print("Contact deleted succesfully")
                        continue
                    else:
                        contact_list.append(line)
        if not deleted:
            print('Contact not found.')
            
        with open(f_name,"w") as f:
            f.writelines(contact_list)

    except Exception as e:
        print("error in deleting contact: ",e)

def main():
    ensure_file()

    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Enter 1–6 only.")


main()


        