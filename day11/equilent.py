def describe_pet(animal_type,pet_name):
    """Display information about apet"""
    print(f"\nIhave a {animal_type}.")
    print(f"\{animal_type}'s name is  {pet_name.title()}")
 #a dog named whillie
describe_pet('whillie')
describe_pet(pet_name='whillie')

#a dog named hamster
describe_pet('harry','hamster')
describe_pet(pet_name='harry',animal_type='hamster')
describe_pet(animal_type='hamster',pet_name='harry')