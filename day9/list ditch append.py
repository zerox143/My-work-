aliens = []
for alien_number in range (30):
    new_alien={
    'color':'green','point':5,'speed':'slow',
    }
    aliens.append(new_alien)
for alien in aliens [:5]:
    print(alien)


    print("...")
    print(f"Total Number of alien:{len(aliens)}")