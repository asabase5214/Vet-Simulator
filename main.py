import random, MaleNames, FemaleNames, Surnames

def generateName(gender):
  if gender == 'male':
    first = random.choice(MaleNames.male_names)
    middle = random.choice(MaleNames.male_names)
  else:
    first = random.choice(FemaleNames.female_names)
    middle = random.choice(FemaleNames.female_names)
  last = random.choice(Surnames.surnames)
  return first + ' ' + middle + ' ' + last

money = 100
ownedDoctors = []
ownedNurses = []
receptionist = 'nobody'


print('Welcome to West Valley Clinic! Your uncle recently retired, and has handed this clinic down to YOU! Good luck!')
print('First things first, you need to hire some staff! To hire staff, enter \'1\' to acess the staff menu, and then choose which staff you want. You have $100 to spend on your staff. You can hire a doctor, nurse, receptionist, or a janitor.')

while True:
  print('1. Hire staff.')
  print('2. View staff.')
  print('3. Train staff.')
  print(f'4. Upgrade equipment. You have ${money} to spend.')
  answer = input('> ')
  if answer == '1':
    print('Choose which kind of staff you would like to hire.')
    print('1. Doctor')
    print('2. Nurse')
    print('3. Receptionist')
    print('4. Janitor')
    answer = input('> ')
    if answer == '1':
      print('Choose which doctor you would like to hire. Here are the available doctor(s):')
      numOfDoctors = random.randint(1, 3)
      docs = []
      doctors = {}
      for i in range(numOfDoctors):
        gender = random.choice(['male', 'female'])
        docs.append(generateName(gender))
      for i in range(numOfDoctors):
        rating = random.randint(1, 5)
        print(i+1, end="")
        print('. '+docs[i]+'.', end="")
        print(' Rating: '+str(rating)+' stars. $'+str(10*rating))
        doctors[i+1] = [docs[i], rating]
      print('Enter BACK to go back to the main menu.')
      answer = input('> ')
      if answer == '1':
        if money < doctors[1][1]*10:
          print('You do not have enough money to hire this doctor.')
        else:
          print('You have hired '+doctors[1][0]+' as a doctor.')
          money -= doctors[1][1]*10
          ownedDoctors.append(doctors[1])
      elif answer == '2' and numOfDoctors >= 2:
        if money < doctors[2][1]*10:
          print('You do not have enough money to hire this doctor.')
        else:
          print('You have hired '+doctors[2][0]+' as a doctor.')
          money -= doctors[2][1]*10
          ownedDoctors.append(doctors[2])
      elif answer == '3' and numOfDoctors >= 3:
        if money < doctors[3][1]*10:
          print('You do not have enough money to hire this doctor.')
        else:
          print('You have hired '+doctors[3][0]+' as a doctor.')
          money -= doctors[3][1]*10
          ownedDoctors.append(doctors[3])
      elif answer == '4' and numOfDoctors >= 4:
        if money < doctors[4][1]*10:
          print('You do not have enough money to hire this doctor.')
        else:
          print('You have hired '+doctors[4][0]+' as a doctor.')
          money -= doctors[4][1]*10
          ownedDoctors.append(doctors[4])
      elif answer == '5' and numOfDoctors == 5:
        if money < doctors[5][1]*10:
          print('You do not have enough money to hire this doctor.')
        else:
          print('You have hired '+doctors[5][0]+' as a doctor.')
          money -= doctors[5][1]*10
          ownedDoctors.append(doctors[5])
      else:
        continue
    elif answer == '2':
      print('Choose which nurse you would like to hire. Here are the available nurse(s):')
      numOfNurses = random.randint(1, 3)
      nurses = []
      nursesDict = {}
      for i in range(numOfNurses):
        gender = random.choice(['male', 'female'])
        nurses.append(generateName(gender))
      for i in range(numOfNurses):
        rating = random.randint(1, 5)
        print(i+1, end="")
        print('. '+nurses[i]+'.', end="")
        print(' Rating: '+str(rating)+' stars. $'+str(10*rating))
        nursesDict[i+1] = [nurses[i], rating]
      print('Enter BACK to go back to the main menu.')
      answer = input('> ')
      if answer == '1':
        if money < nursesDict[1][1]*10:
          print('You do not have enough money to hire this nurse.')
        else:
          print('You have hired '+nursesDict[1][0]+' as a nurse.')
          money -= nursesDict[1][1]*10
          ownedNurses.append(nursesDict[1])
      elif answer == '2' and numOfNurses >= 2:
        if money < nursesDict[2][1]*10:
          print('You do not have enough money to hire this nurse.')
        else:
          print('You have hired '+nursesDict[2][0]+' as a nurse.')
          money -= nursesDict[2][1]*10
          ownedNurses.append(nursesDict[2])
      elif answer == '3' and numOfNurses >= 3:
        if money < nursesDict[3][1]*10:
          print('You do not have enough money to hire this nurse.')
        else:
          print('You have hired '+nursesDict[3][0]+' as a nurse.')
          money -= nursesDict[3][1]*10
          ownedNurses.append(nursesDict[3])
      elif answer == '4' and numOfnurses >= 4:
        if money < nursesDict[4][1]*10:
          print('You do not have enough money to hire this nurse.')
        else:
          print('You have hired '+nursesDict[4][0]+' as a nurse.')
          money -= nursesDict[4][1]*10
          ownedNurses.append(nursesDict[4])
      elif answer == '5' and numOfNurses == 5:
        if money < nursesDict[5][1]*10:
          print('You do not have enough money to hire this nurse.')
        else:
          print('You have hired '+nursesDict[5][0]+' as a nurses.')
          money -= nursesDict[5][1]*10
          ownedNurses.append(nursesDict[5])
      else:
        continue
    elif answer == '3':
      print('Choose which receptionist you would like to hire. Here are the available receptionist(s):')
      numOfRecepts = random.randint(1, 3)
      receptionists = []
      recepts = {}
      for i in range(numOfRecepts):
        gender = random.choice(['male', 'female'])
        receptionists.append(generateName(gender))
      for i in range(numOfRecepts):
        rating = random.randint(1, 5)
        print(i+1, end="")
        print('. '+receptionists[i]+'.', end="")
        print(' Rating: '+str(rating)+' stars. $'+str(10*rating))
        recepts[i+1] = [receptionists[i], rating]
      print('Enter BACK to go back to the main menu.')
      answer = input('> ')
      if answer == '1':
        if money < recepts[1][1]*10:
          print('You do not have enough money to hire this receptionist.')
        else:
          print('You have hired '+recepts[1][0]+' as a receptionist.')
          money -= recepts[1][1]*10
          receptionist = recepts[1]
      elif answer == '2' and numOfRecepts >= 2:
        if money < recepts[2][1]*10:
          print('You do not have enough money to hire this receptionist.')
        else:
          print('You have hired '+recepts[2][0]+' as a receptionist.')
          money -= recepts[2][1]*10
          receptionist = recepts[2]
      elif answer == '3' and numOfNurses == 3:
        if money < recepts[3][1]*10:
          print('You do not have enough money to hire this receptionist.')
        else:
          print('You have hired '+recepts[3][0]+' as a receptionist.')
          money -= recpets[3][1]*10
          receptionist = recepts[3]
      else:
        continue
    elif answer == '4':
      print('You cannot hire any janitors right now.')
  elif answer == '2':
    print('Here are your staff:')
    print('Doctor(s):')
    for i in range(len(ownedDoctors)):
      print(i+1, end="")
      print('. '+ownedDoctors[i][0]+'.', end="")
      print(' Rating: '+str(ownedDoctors[i][1])+' stars.')
    print('Nurse(s):')
    for i in range(len(ownedNurses)):
      print(i+1, end="")
      print('. '+ownedNurses[i][0]+'.', end="")
      print(' Rating: '+str(ownedNurses[i][1])+' stars.')
    print('Receptionist:')
    print(receptionist)
    print('Janitor(s):')
    print('None')
  elif answer == '3':
    print('Choose if you would like to train you doctor(s), nurse(s), receptionist, or janitor(s).')
    print('1. Doctor(s)')
    print('2. Nurse(s)')
    print('3. Receptionist')
    print('4. Janitor(s)')
    answer = input('> ')
    if answer == '1':
      if len(ownedDoctors) > 0:
        for i in range(len(ownedDoctors)):
          print(i+1, end="")
          print('. '+ownedDoctors[i][0]+'.', end="")
          print(' Rating: '+str(ownedDoctors[i][1])+' stars.')
        answer = input('> ')
        if answer == '1':
          print(f'It will cost ${ownedDoctors[0][1]*5} to train this doctor.')
          if money < ownedDoctors[0][1]*5:
            print('You do not have enough money to train this doctor.')
          else:
            money -= ownedDoctors[0][1]*5
            ownedDoctors[0][1] += 1
            print('You have trained '+ownedDoctors[0][0]+'!')