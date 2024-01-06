def build_person(first_name, last_name,age=None):
    '''return a dictionary of info about the person'''
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi','zeus')
print(musician)
