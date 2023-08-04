
USERS_DICT = {}

def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            print ('Please,  enter all required information!')
    
    return inner
        
def hello_handler (*args):
    return 'How can I help you?'
    
def add_contact(data):
    name = data[0].title()
    number = data[1]
    if number.isdigit():
        USERS_DICT[name] = number
        return f'Contact {name} has been added'
    return f'{number} is not a number!' 

def change_contact(data):
    name = data[0].title()
    number = data[1]
    if not number.isdigit():
        return f'{number} is not a number!'
    for key in USERS_DICT.keys():
        if key == name:
            USERS_DICT[name] = number
            return "The contact's phone number has been updated"
    return f'Contact {name} has not been added before'

def show_all(*args):
    return USERS_DICT
 
COMMANDS = {hello_handler: 'hello',
            add_contact: 'add',
            change_contact: 'change',
            show_all: 'show all',
            }

@input_error
def command_parser(user_input: str):
    user_info = user_input.split()
    command = user_info[0]
    
    for key, value in COMMANDS.items():
        if command.lower() == value:
            return key(user_info[1:])
        
    if command.lower() == 'show' and user_info[1].lower() == 'all':
        return show_all(user_info[1:])

    return 'Unknown command. Try one more time!'


def main():
    while True:
        user_input = input('>>> ')
        if user_input.lower() in ['good bye', 'exit', 'close']:
            print ('Good bye!')
            break
        result = command_parser(user_input)
      
        print (result)
        

if __name__ == '__main__':
    main()