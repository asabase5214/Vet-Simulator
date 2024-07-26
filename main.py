import random, MaleNames, FemaleNames, Surnames, Calls, sys

animals = ['dog', 'cat', 'parrot', 'goldfish', 'snake', 'dog', 'cat', 'dog', 'cat']
unownedUpgrades = [['Bathrooms', 30_000], ['Waiting Area', 10_000], ['Doggy Playpen', 8_000], ['Cat Lounge', 5_000], ['Grooming Stations', 5_000], ['Isolation Room', 10_000], ['On-Site Pharmacy', 10_000], ['Digital Imaging Machine (Such as an X-Ray Machine)', 35_000]]
unownedToolUpgrades = [['Veterinary Surgical Equipment', 1_000], ['Veterinary Diagnostic Equipment', 8_000], ['Computers and Software', 800], ['Laboratory Equipment', 2_000], ['Animal Containment and Handling Equipment', 1_000], ['Pet Care Products and Supplies', 500]]
ownedUpgrades = []
ownedToolUpgrades = []

money = 1000
callOne, callTwo, callThree, callFour, callFive, callSix, callSeven, callEight, callNine, callTen, callEleven = False, False, False, False, False, False, False, False, False, False, False

def generateName(gender):
  if gender == 'male':
    first = random.choice(MaleNames.male_names)
    middle = random.choice(MaleNames.male_names)
  else:
    first = random.choice(FemaleNames.female_names)
    middle = random.choice(FemaleNames.female_names)
  last = random.choice(Surnames.surnames)
  return first + ' ' + middle + ' ' + last

ownedDoctors = []
ownedNurses = []
receptionist = 'None'
ownedjanitors = []
cost = random.randint(60_000, 150_000)
doctorCost = cost / 365
cost = random.randint(30_000, 60_000)
nurseCost = cost / 365
cost = random.randint(25_000, 35_000)
receptionistCost = cost / 365
cost = random.randint(20_000, 30_000)
janitorCost = cost / 365
cost = random.randint(1_000, 2_000)


print('Welcome to West Valley Clinic! Your uncle recently retired, and has handed this clinic down to YOU! Good luck!')
print('First things first, you need to hire some staff! To hire staff, enter \'1\' to acess the staff menu, and then choose which staff you want. You have $1,000 to spend on your staff. You can hire a doctor, nurse, receptionist, or a janitor.')
input('Press ENTER to start!')

while True:
  print()
  print('1. Hire staff.')
  print('2. View staff.')
  print('3. Train staff.')
  print('4. View clinic upgrades.')
  print('5. View tool upgrads.')
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
      print('Choose which janitor you would like to hire. Here are the available janitor(s):')
      numOfjanitors = random.randint(1, 3)
      janitors = []
      janitorsDict = {}
      for i in range(numOfjanitors):
        gender = random.choice(['male', 'female'])
        janitors.append(generateName(gender))
      for i in range(numOfjanitors):
        rating = random.randint(1, 5)
        print(i+1, end="")
        print('. '+janitors[i]+'.', end="")
        print(' Rating: '+str(rating)+' stars. $'+str(10*rating))
        janitorsDict[i+1] = [janitors[i], rating]
      print('Enter BACK to go back to the main menu.')
      answer = input('> ')
      if answer == '1':
        if money < janitorsDict[1][1]*10:
          print('You do not have enough money to hire this janitor.')
        else:
          print('You have hired '+janitorsDict[1][0]+' as a janitor.')
          money -= janitorsDict[1][1]*10
          ownedjanitors.append(janitorsDict[1])
      elif answer == '2' and numOfjanitors >= 2:
        if money < janitorsDict[2][1]*10:
          print('You do not have enough money to hire this janitor.')
        else:
          print('You have hired '+janitorsDict[2][0]+' as a janitor.')
          money -= janitorsDict[2][1]*10
          ownedjanitors.append(janitorsDict[2])
      elif answer == '3' and numOfjanitors >= 3:
        if money < janitorsDict[3][1]*10:
          print('You do not have enough money to hire this janitor.')
        else:
          print('You have hired '+janitorsDict[3][0]+' as a janitor.')
          money -= janitorsDict[3][1]*10
          ownedjanitors.append(janitorsDict[3])
      elif answer == '4' and numOfjanitors >= 4:
        if money < janitorsDict[4][1]*10:
          print('You do not have enough money to hire this janitor.')
        else:
          print('You have hired '+janitorsDict[4][0]+' as a janitor.')
          money -= janitorsDict[4][1]*10
          ownedjanitors.append(janitorsDict[4])
      elif answer == '5' and numOfjanitors == 5:
        if money < janitorsDict[5][1]*10:
          print('You do not have enough money to hire this janitor.')
        else:
          print('You have hired '+janitorsDict[5][0]+' as a janitors.')
          money -= janitorsDict[5][1]*10
          ownedjanitors.append(janitorsDict[5])
      else:
        continue
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
    print(receptionist[0])
    print('Janitor(s):')
    for i in range(len(ownedjanitors)):
      print(i+1, end="")
      print('. '+ownedjanitors[i][0]+'.', end="")
      print(' Rating: '+str(ownedjanitors[i][1])+' stars.')
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
    elif answer == '2':
      if len(ownedNurses) > 0:
        for i in range(len(ownedNurses)):
          print(i+1, end="")
          print('. '+ownedNurses[i][0]+'.', end="")
          print(' Rating: '+str(ownedNurses[i][1])+' stars.')
        answer = input('> ')
        if answer == '1':
          print(f'It will cost ${ownedNurses[0][1]*5} to train this nurse.')
          if money < ownedNurses[0][1]*5:
            print('You do not have enough money to train this nurse.')
          else:
            money -= ownedNurse[0][1]*5
            ownedNurses[0][1] += 1
            print('You have trained '+ownedNurses[0][0]+'!')
    elif answer == '3':
      if len(receptionist) > 0:
        print(i+1, end="")
        print('. '+receptionist[0]+'.', end="")
        print(' Rating: '+str(receptionist[1])+' stars.')
        answer = input('> ')
        if answer == '1':
          print(f'It will cost ${receptionist[1]*5} to train this receptionist.')
          if money < receptionist[1]*5:
            print('You do not have enough money to train this receptionist.')
          else:
            money -= receptionist[1]*5
            receptionist[1] += 1
            print('You have trained '+receptionist[0]+'!')
    elif answer == '4':
      if len(ownedjanitors) > 0:
        for i in range(len(ownedjanitors)):
          print(i+1, end="")
          print('. '+ownedjanitors[i][0]+'.', end="")
          print(' Rating: '+str(ownedjanitors[i][1])+' stars.')
        answer = input('> ')
        if answer == '1':
          print(f'It will cost ${ownedjanitors[0][1]*5} to train this janitor.')
          if money < ownedjanitors[0][1]*5:
            print('You do not have enough money to train this janitor.')
          else:
            money -= ownedjanitors[0][1]*5
            ownedjanitors[0][1] += 1
            print('You have trained '+ownedjanitors[0][0]+'!')
  elif answer == '4':
    for i in range(len(unownedUpgrades)):
      print(str(i+1) + '. ', end="")
      print(unownedUpgrades[i][0], end="")
      print(': $'+ str(unownedUpgrades[i][1]))
    print('Enter BACK to go back to the main menu.')
    answer = input('> ')
    if answer == '1' and len(unownedUpgrades) > 0:
      if money < unownedUpgrades[0][1]:
        print('You do not have enough money to buy this upgrade.')
      else:
        money -= unownedUpgrades[0][1]
        unownedUpgrades.pop(0)
        ownedUpgrades.append(unownedUpgrades[0])
        print('You have bought '+ownedUpgrades[0][0]+'!')
    elif answer == '2' and len(unownedUpgrades) > 1:
      if money < unownedUpgrades[1][1]:
        print('You do not have enough money to buy this upgrade.')
      else:
        money -= unownedUpgrades[1][1]
        unownedUpgrades.pop(1)
        ownedUpgrades.append(unownedUpgrades[1])
        print('You have bought '+ownedUpgrades[1][0]+'!')
    elif answer == '3' and len(unownedUpgrades) > 2:
      if money < unownedUpgrades[2][1]:
        print('You do not have enough money to buy this upgrade.')
      else:
        money -= unownedUpgrades[2][1]
        unownedUpgrades.pop(2)
        ownedUpgrades.append(unownedUpgrades[2])
        print('You have bought '+ownedUpgrades[2][0]+'!')
    elif answer == '4' and len(unownedUpgrades) > 3:
      if money < unownedUpgrades[3][1]:
        print('You do not have enough money to buy this upgrade.')
      else:
        money -= unownedUpgrades[3][1]
        unownedUpgrades.pop(3)
        ownedUpgrades.append(unownedUpgrades[3])
        print('You have bought '+ownedUpgrades[3][0]+'!')
    elif answer == '5' and len(unownedUpgrades) > 4:
      if money < unownedUpgrades[4][1]:
        print('You do not have enough money to buy this upgrade.')
      else:
        money -= unownedUpgrades[4][1]
        unownedUpgrades.pop(4)
        ownedUpgrades.append(unownedUpgrades[4])
        print('You have bought '+ownedUpgrades[4][0]+'!')
    elif answer == '6' and len(unownedUpgrades) > 5:
      if money < unownedUpgrades[5][1]:
        print('You do not have enough money to buy this upgrade.')
      else:
        money -= unownedUpgrades[5][1]
        unownedUpgrades.pop(5)
        ownedUpgrades.append(unownedUpgrades[5])
        print('You have bought '+ownedUpgrades[5][0]+'!')
    elif answer == '7' and len(unownedUpgrades) > 6:
      if money < unownedUpgrades[6][1]:
        print('You do not have enough money to buy this upgrade.')
      else:
        money -= unownedUpgrades[6][1]
        unownedUpgrades.pop(6)
        ownedUpgrades.append(unownedUpgrades[6])
        print('You have bought '+ownedUpgrades[6][0]+'!')
    elif answer == '8' and len(unownedUpgrades) > 7:
      if money < unownedUpgrades[7][1]:
        print('You do not have enough money to buy this upgrade.')
      else:
        money -= unownedUpgrades[7][1]
        unownedUpgrades.pop(7)
        ownedUpgrades.append(unownedUpgrades[7])
        print('You have bought '+ownedUpgrades[7][0]+'!')
  elif answer == '5':
    for i in range(len(unownedToolUpgrades)):
      print(str(i+1) + '. ', end="")
      print(unownedToolUpgrades[i][0], end="")
      print(': $'+ str(unownedToolUpgrades[i][1]))
    print('Enter BACK to go back to the main menu.')
    answer = input('> ')
    if answer == '1' and len(unownedToolUpgrades) > 0:
      if money < unownedToolUpgrades[0][1]:
        print('You do not have enough money to buy this upgrade.')
      else:
        money -= unownedToolUpgrades[0][1]
        unownedToolUpgrades.pop(0)
        ownedToolUpgrades.append(unownedToolUpgrades[0])
        print('You have bought '+ownedToolUpgrades[0][0]+'!')
    elif answer == '2' and len(unownedToolUpgrades) > 1:
      if money < unownedToolUpgrades[1][1]:
        print('You do not have enough money to buy this upgrade.')
      else:
        money -= unownedToolUpgrades[1][1]
        unownedToolUpgrades.pop(1)
        ownedToolUpgrades.append(unownedToolUpgrades[1])
        print('You have bought '+ownedToolUpgrades[1][0]+'!')
    elif answer == '3' and len(unownedToolUpgrades) > 2:
      if money < unownedToolUpgrades[2][1]:
        print('You do not have enough money to buy this upgrade.')
      else:
        money -= unownedToolUpgrades[2][1]
        unownedToolUpgrades.pop(2)
        ownedToolUpgrades.append(unownedToolUpgrades[2])
        print('You have bought '+ownedToolUpgrades[2][0]+'!')
    elif answer == '4' and len(unownedToolUpgrades) > 3:
      if money < unownedToolUpgrades[3][1]:
        print('You do not have enough money to buy this upgrade.')
      else:
        money -= unownedToolUpgrades[3][1]
        unownedToolUpgrades.pop(3)
        ownedToolUpgrades.append(unownedToolUpgrades[3])
        print('You have bought '+ownedToolUpgrades[3][0]+'!')
    elif answer == '5' and len(unownedToolUpgrades) > 4:
      if money < unownedToolUpgrades[4][1]:
        print('You do not have enough money to buy this upgrade.')
      else:
        money -= unownedToolUpgrades[4][1]
        unownedToolUpgrades.pop(4)
        ownedToolUpgrades.append(unownedToolUpgrades[4])
        print('You have bought '+ownedToolUpgrades[4][0]+'!')
    elif answer == '6' and len(unownedToolUpgrades) > 5:
      if money < unownedToolUpgrades[5][1]:
        print('You do not have enough money to buy this upgrade.')
      else:
        money -= unownedToolUpgrades[5][1]
        unownedToolUpgrades.pop(5)
        ownedToolUpgrades.append(unownedToolUpgrades[5])
        print('You have bought '+ownedToolUpgrades[5][0]+'!')
  dirtiness = 10-len(ownedjanitors)
  if dirtiness > 8:
    print('Your customers are very displeased by the lack of janitors. Your clinic is very dirty.')
  elif dirtiness > 5:
    print('A few customers were annoyed by the lack of janitors. Your clinic is somewhat dirty.')
  elif dirtiness > 3:
    print('Your janitors are doing well. Your clinic is nearly spotless.')
  else:
    print('Customers are impressed and very happy with the amount of janitors and cleanliness of your clinic. Your clinic is spotless.')
  if random.randint(1, 10) != 1:
    print()
    num = random.randint(1, 11)
    if num == 1 and not callOne:
      print('The phone begins to ring. you pick it up.')
      input('Press ENTER to continue.')
      print('\n'*5)
      money += Calls.call1()
      callOne = True
    elif num == 2 and not callTwo:
      print('The phone begins to ring. you pick it up.')
      input('Press ENTER to continue.')
      print('\n'*5)
      money += Calls.call2()
      callTwo = True
    elif num == 3 and not callThree:
      print('The phone begins to ring. you pick it up.')
      input('Press ENTER to continue.')
      print('\n'*5)
      money += Calls.call3()
      callThree = True
    elif num == 4 and not callFour:
      print('The phone begins to ring. you pick it up.')
      input('Press ENTER to continue.')
      print('\n'*5)
      money += Calls.call4(money)
      callFour = True
    elif num == 5 and not callFive:
      print('The phone begins to ring. you pick it up.')
      input('Press ENTER to continue.')
      print('\n'*5)
      money += Calls.call5()
      callFive = True
    elif num == 6 and not callSix:
      print('The phone begins to ring. you pick it up.')
      input('Press ENTER to continue.')
      print('\n'*5)
      money += Calls.call6()
      callSix = True
    elif num == 7 and not callSeven:
      print('The phone begins to ring. you pick it up.')
      input('Press ENTER to continue.')
      print('\n'*5)
      money += Calls.call7()
      callSeven = True
    elif num == 8 and not callEight:
      print('The phone begins to ring. you pick it up.')
      input('Press ENTER to continue.')
      print('\n'*5)
      money += Calls.call8()
      callEight = True
    elif num == 9 and not callNine:
      print('The phone begins to ring. you pick it up.')
      input('Press ENTER to continue.')
      print('\n'*5)
      money += Calls.call9()
      callNine = True
    elif num == 10 and not callTen:
      print('The phone begins to ring. you pick it up.')
      input('Press ENTER to continue.')
      print('\n'*5)
      money += Calls.call10()
      callTen = True
    elif num == 11 and not callEleven:
      print('The phone begins to ring. you pick it up.')
      input('Press ENTER to continue.')
      print('\n'*5)
      money += Calls.call11()
      callEleven = True
    elif num == 12:
      print('The phone begins to ring. you pick it up.')
      input('Press ENTER to continue.')
      print('\n'*5)
      Calls.call12(animals)
  income = random.randint(100000, 500000)*(len(ownedDoctors)+(len(ownedNurses)/2))
  for i in range(len(ownedDoctors)):
    income += ownedDoctors[i][1]*10000
  for i in range(len(ownedNurses)):
    income += ownedNurses[i][1]*10000
  income+=len(ownedUpgrades)*100_000
  income+=len(ownedToolUpgrades)*100_000
  income /= 365
  if receptionist == 'None':
    income = 0
  total = income-doctorCost*len(ownedDoctors)-nurseCost*len(ownedNurses)-janitorCost*len(ownedjanitors)
  if receptionist != 'None':
    total -= receptionistCost
  total = round(total, 2)
  money+=total
  print('You have made $'+str(total)+' today.')
  if money <= 0:
    print('You have no money left. The animal clinic closes. GAME OVER.')
    sys.exit()