def great_username(username):
    """Display a simple geeting"""
    print("Hello, " + username.title())

great_username('Michel')

print("-----------------------------------------")

def describe_pet(pet_name, animal_type = 'dog'):
    """ Display information about a pet """
    print("\nI have a " + animal_type + " .")
    print("My " + animal_type + "'s name is " + pet_name.title() + ". ")

describe_pet(pet_name='harry')

print("-----------------------------------------")

def get_formatted_name(first_name, last_name,  middle_name = ''):
    """ Return a full name, neatly formatted. """
    if middle_name:
        full_name = first_name + ' ' +  middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name

    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

print("-----------------------------------------")

def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

print("-----------------------------------------")

def get_formatted_name(first_name, last_name):
    """ Return a full name, neatly formatted. """
    full_name = first_name + " " + last_name
    return full_name.title()


    while True:
        print("\nPlease tell me your name:")
        print("(enter 'q' at any time to quit)")

        f_name = input("First name: ")
        if f_name == 'q':
            break

        l_name = input("Last name: ")
        if l_name == 'q':
            break

        formatted_name = get_formatted_name(f_name, l_name)
        print("\nHello, " + formatted_name + "!")

#170 170 170 170 170 17
