# Обробник помилок 
def input_error(func):
    def inner(*args, **kwargs):
        
        try:
            return func(*args, **kwargs)
        
        except ValueError as e:
            return f"The worng numbers of arguments: {e}"
        
        except KeyError as e:
            return f"User - {e} not found."
        
        except IndexError as e:
            return f"Please enter the correct number of arguments. Error: {e}"
        # Для інших
        except Exception as e:
            return f"An unexpected error occured: Error: {e}"
        
    return inner

# Input handler
@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_number(args, contacts):
    name, new_number = args
    if name in contacts:
        contacts[name] = new_number
        return "Contact updated."
    else:
        return "Name not found."

@input_error
def show_phone(user, contacts):
    return f"Phone {user[0]} - {contacts[user[0]]}"

@input_error
def show_base(contacts):
    result = ""
    
    if len(contacts) == 0:
        return "Base is empty."
    
    else:
        for name, number in contacts.items():
            result += f"name: {name}, number: {number}\n"
            
    return result

commands = "Commands:\n\tall;\n\tcommands\n\tadd user number;\n\tphone user;\n\tchange user number;\n\texit/quit/close"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    print(commands)
    
    while True:
        user_input = input("Enter a commands: ")
        command, *args = parse_input(user_input)

        if command in ['close', 'quit', 'exit']:
            print("Good bye!")
            break
        
        match command:
            
            case 'commands':
                print(commands)
                            
            case 'hello':
                print("Hello im Jarvis! Im here for help you!")
                
            case 'all':
                print(show_base(contacts))
                
            case 'add':
                print(add_contact(args, contacts))
                
            case 'phone':
                print(show_phone(args, contacts))
                
            case 'change':
                print(change_number(args, contacts))

if __name__ == '__main__':
    main()
