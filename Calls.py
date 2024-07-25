import random

def randomDog():
  return random.choice(['pitbull', 'great dane', 'dalmation', 'husky', 'french bulldog', 'german shepherd', 'pomeranian', 'rottweiler', 'bulldog', 'beagle', 'poodle', 'boxer', 'shiba inu', 'black lab', 'basset hound', 'dachshund', 'golden retriever', 'german short-haired pointer', 'chihuahua', 'shih tzu', 'terrier', 'chow chow', 'german spitz', 'doberman', 'bullmastiff', 'bloodhound', 'great pyrenees', 'komondor'])

def call1():
  print(f"YOU: Hello, West Valley Clinic, how may I help you? CALLER: Hello, I have a {randomDog()} and {random.choice(['he', 'she'])} just ate a s\'more that I dropped off of the ground. I know that dogs aren't supposed to have chocolate. What should I do?")
  
  print()
  print('1. Okay, you need to get to the clinic as soon as possible.')
  print('2. I\'m sorry, I\'m not sure what I\'m doing.')
  print('3. Uh, maybe just, like, massage the dog\'s tummy a bit, and maybe it will come out?')
  answer = input('> ')
  if answer == '1':
    print('YOU: Okay, you need to get to the clinic as soon as possible. CALLER: Okay, I\'ll be there in a few minutes. Thank you.')
    clinic = True
  elif answer == '2':
    print('YOU: I\'m sorry, I\'m not sure what I\'m doing. CALLER: Uhhh... okay... goodbye.')
  elif answer == '3':
    print('YOU: Uh, maybe just, like, massage the dog\'s tummy a bit, and maybe it will come out? CALLER: Okay... hmm.... It doesn\'t seem to be working. What should I do?')
    print()
    print('1. Okay, you need to get to the clinic as soon as possible.')
    print('2. Oh. Whoops. Sorry, goodbye. (HANG UP)')
    if answer == '1':
      print('YOU: Okay, you need to get to the clinic as soon as possible. CALLER: Okay, I\'ll be there in a few minutes. Thank you.')
      clinic = True
    elif answer == '2':
      print('YOU: Oh. Whoops. Sorry, goodbye.')
  
  if clinic:
    earned = random.randint(40, 100)
    print(f'The caller arrives, and their dog is taken care of. You earn {earned} dollars.')
    return earned
  else:
    return 0

def call2():
  print(f'YOU: Hello, West Valley Clinic, how may I help you? CALLER: Hello, I have a {randomDog()} and I think he just got bit by a snake! I don\'t know what to do. What should I do?')
  print()
  print('1. Okay, what kind of snake is it?')
  print('2. Kill the snake!')
  print('3. Where is the bite?')
  answer = input('> ')
  if answer == '1':
    print(f'YOU: Okay, what kind of snake is it? CALLER: I-I\'m not sure. It\'s, uh, black, completely black. Is it poisonous?')
    print()
    print('1. Yes, it is venemous. Don\'t go near it. You need to get to the clinic ASAP.')
    print('2. No, that\'s not poisonous. I\'m sure your dog will be fine. Goodbye. (HANG UP)')
    print('3. No, it\'s not venemous, but it can still be dangerous. Where is the bite?')
    answer = input('> ')
    if answer == '1':
      print('YOU: Yes, it is venemous. Don\'t go near it. You need to get to the clinic ASAP. CALLER: Okay, I\'ll be there in a 10 minutes. Thank you.')
      clinic = True
    elif answer == '2':
      print('YOU: No, that\'s not poisonous. I\'m sure your dog will be fine. Goodbye.')
    elif answer == '3':
      print('YOU: No, it\'s not venemous, but it can still be dangerous. Where is the bite? CALLER: Um, I-I think it\'s on his nose.')
      print()
      print('1. Okay, you need to get to the clinic as soon as possible.')
      print('2. Oh, your dog will be fine! Goodbye. (HANG UP)')
      print('3. Okay, if it is bleeding a lot, you should probably get to the clinic, but other wise, you should be fine.')
      answer = input('> ')
      if answer == '1':
        print('YOU: Okay, you need to get to the clinic as soon as possible. CALLER: Okay, I\'ll be there in a few minutes. Thank you.')
        clinic = True
      elif answer == '2':
        print('YOU: Oh, your dog will be fine! Goodbye.')
      elif answer == '3':
        print('YOU: Okay, if it is bleeding a lot, you should probably get to the clinic, but otherwise, you should be fine.')
        if random.randint(1,2) == 1:
          print('CALLER: Yeah, It\'s bleeding a lot. I\'ll be there in a few minutes.')
          clinic = True
        else:
          print('CALLER: No, it isn\'t bleeding too much. Thank you.')
  elif answer == '2':
    print(f'YOU: Kill the snake! CALLER: Oh, okay... I\'ll try. Thank you.')
  elif answer == '3':
    print('YOU: Where is the bite? CALLER: Um, I-I think it\'s on his nose.')
    print()
    print('1. Okay, you need to get to the clinic as soon as possible.')
    print('2. Oh, your dog will be fine! Goodbye. (HANG UP)')
    print('3. Okay, if it is bleeding a lot, you should probably get to the clinic, but other wise, you should be fine.')
    answer = input('> ')
    if answer == '1':
      print('YOU: Okay, you need to get to the clinic as soon as possible. CALLER: Okay, I\'ll be there in a few minutes. Thank you.')
      clinic = True
    elif answer == '2':
      print('YOU: Oh, your dog will be fine! Goodbye.')
    elif answer == '3':
      print('YOU: Okay, if it is bleeding a lot, you should probably get to the clinic, but otherwise, you should be fine.')
      if random.randint(1,2) == 1:
        print('CALLER: Yeah, It\'s bleeding a lot. I\'ll be there in a few minutes.')
        clinic = True
      else:
        print('CALLER: No, it isn\'t bleeding too much. Thank you.')
  if clinic:
    earned = random.randint(170, 300)
    print(f'The caller arrives, and their dog is taken care of. You earn {earned} dollars.')
    return earned
  else:
    return 0

def call3():
  print(f'YOU: Hello, West Valley Clinic, how may I help you? CALLER: Hello, I just found a {randomDog()} in the middle of the road. He doesn\'t look too good, I think he\'s bleeding in some places. What should I do?')
  print()
  print('1. Okay, you need to get to the clinic as soon as possible.')
  print('Does it have a collar?')
  answer = input('> ')
  if answer == '1':
    print('YOU: Okay, you need to get to the clinic as soon as possible. CALLER: Um, I don\'t have a crate or anything. Can I just put the dog in my trunk?')
    print()
    print('1. Uh, sure, why not!')
    print('2. No, the dog will die if you do that!')
    print('3. If you feel safe putting the dog in you trunk, that\'s fine, but you may have to clean your trunk later.')
    answer = input('> ')
    if answer == '1':
      print('YOU: Uh, sure, why not! CALLER: Okay, I\'ll be there in a few minutes. Thank you.')
      clinic = True
    elif answer == '2':
      print('YOU: No, the dog will die if you do that! CALLER: Oh! Sorry, I didn\'t know that. *krkshksshhsshhhh* (muffled): Hey! Hey come back here! I\'m trying to save you! *CRASH*')
    elif answer == '3':
      print(f'YOU: If you feel safe putting the dog in you trunk, that\'s fine, but you may have to clean your trunk later. CALLER: Okay, I\'ll be there in a few minutes. Thank you.')
      clinic = True
  elif answer == '2':
    print('YOU: Does it have a collar? CALLER: Uh, yeah, it has a collar.')
    print()
    print('1. Okay, you need to get to the clinic as soon as possible.')
    print('2. Try calling the phone number on the collar.')
    answer = input('> ')
    if answer == '1':
      print('YOU: Okay, you need to get to the clinic as soon as possible. CALLER: Okay, I\'ll be there in a few minutes. Thank you.')
      clinic = True
    elif answer == '2':
      print('YOU: Try calling the phone number on the collar. CALLER: Okay. Bye.')

def call4(money):
  print(f'YOU: Hello, West Valley Clinic, how may I help you? CALLER: Hello, this is the IRS. We have noticed some irregularities in your tax filings. You owe a substantial amount of money and it needs to be paid immediately to avoid severe consequences.')
  print()
  print('1. Oh no, I wasn\'t aware of any issues with my taxes.')
  print('2. Oops! How can I fix that?')
  input('> ')
  print('CALLER: We can help you resolve this quickly. Just provide us with your bank details.')
  print()
  print('1. Oh, okay. (provide details)')
  print('2. No, I don\'t feel comfortable sharing those details over the phone.')
  answer = input('> ')
  if answer == '1':
    print('YOU: Oh, okay. (provide details) CALLER: Thank you for your cooperation. Your money will be deducted shortly.')
    print('The call ends.')
    print(f'You lost ${2000 - (2000 - money)}.')
    return (2000 - (2000 - money)) - ((2000 - (2000 - money))*2)
  elif answer == '2':
    print('YOU: No, I don\'t feel comfortable sharing those details over the phone. CALLER: It is important that you comply to avoid illegal actions.')
    print()
    print('1. Okay. (provide details)')
    print('2. I\'m sorry, but I can\'t do that.')
    answer = input('> ')
    if answer == '1':
      print('YOU: Okay. (provide details) CALLER: Thank you for your cooperation. Your money will be deducted shortly.')
      print('The call ends.')
      print(f'You lost ${2000 - (2000 - money)}.')
      return (2000 - (2000 - money)) - ((2000 - (2000 - money))*2)
    elif answer == '2':
      print('YOU: I\'m sorry, but I can\'t do that. CALLER: Suit yourself. Remember, the consequences are on you.')
      print('The call ends.')
  return 0