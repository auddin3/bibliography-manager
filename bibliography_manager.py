import json

def load_bibliography():
    try:
        with open("bibliography.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def add_entry(bibliography):
    citation_key = input("Enter citation key: ")
    title = input("Enter title: ")
    author = input("Enter author: ")
    year = input("Enter publication year: ")

    entry = {
        "title": title,
        "author": author,
        "year": year,
    }

    bibliography[citation_key] = entry
    print("Entry added successfully!")

def view_entry(bibliography):
    citation_key = input("Enter citation key: ")

    if citation_key in bibliography:
        entry = bibliography[citation_key]
        print(f"Citation Key: {citation_key}")
        print(f"Title: {entry['title']}")
        print(f"Author: {entry['author']}")
        print(f"Year: {entry['year']}")
    else:
        print("Entry not found!")

def list_entries(bibliography):
    if bibliography:
        print("Bibliography Entries:")
        for citation_key, entry in bibliography.items():
            print(f"{citation_key}: {entry['title']}")
    else:
        print("Bibliography is empty!")

def delete_entry(bibliography):
    citation_key = input("Enter citation key or ALL: ")
 
    if citation_key in bibliography:
        bibliography.pop(citation_key)
        print('Successfully deleted!')
        list_entries(bibliography)
    elif citation_key == "ALL":
        bibliography.clear()
    else:
        print("Entry not found!")
        
def save_bibliography(bibliography):
    with open("bibliography.json", "w") as file:
        json.dump(bibliography, file, indent=4)


bibliography = load_bibliography()

while True:
    print("\nBibliography Manager Menu:")
    print("1. Add Entry")
    print("2. View Entry")
    print("3. List Entries")
    print("4. Delete Entry")
    print("5. Save and Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_entry(bibliography)
    elif choice == "2":
        view_entry(bibliography)
    elif choice == "3":
        list_entries(bibliography)
    elif choice == "4":
        delete_entry(bibliography)
    elif choice == "5":
        save_bibliography(bibliography)
        print("Bibliography saved. Exiting.")
        break
    else:
        print("Invalid choice. Please try again.")


