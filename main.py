contacts = {}

def hello():
    return "How i can help you?"

def add_contact(name, phone):
    contacts[name] = phone
    return f"Contact {name} with phone number {phone} has been added."

def change_contact(name, phone):
    if name in contacts:
        contacts[name] = phone
        return f"Contact {name}'s phone number has been update to {phone}. "
    else:
        return f"Contact {name}'s does not exist"

def get_number_contact(name):
    if name in contacts:
        return f"The phone number of {name} is {contacts[name]}. "
    else:
        return f"Contact {name} does not exist. "

def show_all_contact():
    contacts_all = ""
    for name, phone in contacts.items():
        contacts_all += f"| {name}: {phone} |\n"
    return contacts_all
        

def exit(): 
    return "Good bye!"

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            print("The contact is missing. ")
        except IndexError:
            print("Enter the name and number separated by a space. ")
        except ValueError:
            print("ValueError. Please try again. ")
    return wrapper

@input_error
def main():
    print("Welcome to the Assistant bot! ")
    while True:
        user_input = input("Enter a command: ")
        if user_input.lower() in ["good bye", "close", "exit"]:
            print(exit())
            break
        elif user_input.lower() == "hello":
            print(hello())
        elif user_input.lower() == "show all contacts":
             print(show_all_contact())
        elif user_input.lower() == "add contact":
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            print(add_contact(name, phone))
        elif user_input.lower() == "change contact":
            name = input("Enter a new name: ")
            phone = input("Enter the new phone number: ")
            print(change_contact(name, phone))
        elif user_input.lower() == "get number contact":
            name = input("Enter the name: ")
            print(get_number_contact(name))
        else:
            print("Invalid command. ")



if __name__ == "__main__":
    main()
