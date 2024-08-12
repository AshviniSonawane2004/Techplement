import os
import json

# File to store contacts
CONTACTS_FILE = 'contacts.json'


# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}


# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)


# Add a new contact
def add_contact(contacts):
    name = input("Enter the contact's name: ").strip()
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("Enter the phone number: ").strip()
    email = input("Enter the email address: ").strip()
    if not phone or not email:
        print("Phone number and email address cannot be empty.")
        return
    contacts[name] = {'phone': phone, 'email': email}
    print(f"Contact '{name}' added successfully!")


# Search for a contact by name
def search_contact(contacts):
    name = input("Enter the contact's name to search: ").strip()
    contact = contacts.get(name)
    if contact:
        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
    else:
        print("Contact not found.")


# Update contact information
def update_contact(contacts):
    name = input("Enter the contact's name to update: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    phone = input("Enter the new phone number (leave empty to keep current): ").strip()
    email = input("Enter the new email address (leave empty to keep current): ").strip()
    contact = contacts[name]
    if phone:
        contact['phone'] = phone
    if email:
        contact['email'] = email
    contacts[name] = contact
    print(f"Contact '{name}' updated successfully!")


# Display all contacts
def display_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    for name, info in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print('-' * 20)


# Main function to run the contact management system
def main():
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Display All Contacts")
        print("5. Exit")1

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            display_contacts(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
