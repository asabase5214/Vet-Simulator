import random

def randomDog():
  return random.choice(['pitbull', 'great dane', 'dalmation', 'husky', 'french bulldog', 'german shepherd', 'pomeranian', 'rottweiler', 'bulldog', 'beagle', 'poodle', 'boxer', 'shiba inu', 'black lab', 'basset hound', 'dachshund', 'golden retriever', 'german short-haired pointer', 'chihuahua', 'shih tzu', 'terrier', 'chow chow', 'german spitz', 'doberman', 'bullmastiff', 'bloodhound', 'great pyrenees', 'komondor'])

def call1():
  clinic = False
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
  clinic = False
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
  clinic = False
  print(f'YOU: Hello, West Valley Clinic, how may I help you? CALLER: Hello, I just found a {randomDog()} in the middle of the road. He doesn\'t look too good, I think he\'s bleeding in some places. What should I do?')
  print()
  print('1. Okay, you need to get to the clinic as soon as possible.')
  print('2. Does it have a collar?')
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
      print('YOU: No, the dog will die if you do that! CALLER: Oh! Sorry, I didn\'t know that. *krkshksshhsshhhh* (muffled): Hey! Hey come back here! I\'m trying to save you- *CRASH*')
      print('Call ended')
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
  if clinic:
    earned = random.randint(40, 100)
    print(f'The caller arrives, and their dog is taken care of. You earn {earned} dollars.')
    return earned

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

def call5():
  clinic = False
  print(f'YOU: Hello, West Valley Clinic, how may I help you? CALLER: Hello. I have a cat named Emmie. She has been acting strangely lately, not eating or drinking, barely sleeping. What should I do?')
  print()
  print('1. That doesn\'t sound very good. Bring to the clinic when you can, and we\'ll see what we can do.')
  print('2. Uh oh. Sounds like your cat is going to die. I\'m sorry. If you want you could, like, come here, and we could kill her with our... what\'re they called? Ah, yes we could euthanize her if ya like.')
  answer = input('> ')
  if answer == '1':
    print('YOU: That doesn\'t sound very good. Bring to the clinic when you can, and we\'ll see what we can do. CALLER: Is tommorrow at 8:30 am okay? YOU: Yes that\'s fine. CALLER: Okay, thank you. Goodbye.')
    clinic = True
  elif answer == '2':
    print('YOU: Uh oh. Sounds like your cat is going to die. I\'m sorry. If you want you could, like, come here, and we could kill her with our... what\'re they called? Ah, yes we could euthanize her if ya like. CALLER: What?! No! Emmie! I can\'t bear the thought of losing her! I\'ve had for eleven years. She\'s helped me through some terrible times. [pauses] I wish I could have spent more time with her. I\'m sorry. Goodbye.')
  if clinic:
    earned = random.randint(40, 100)
    print(f'The caller arrives, and their cat is taken care of. You earn {earned} dollars.')
    return earned
  return 0

def call6():
  clinic = False
  print('YOU: Hello, West Valley Clinic, how may I help you? CALLER: Hello, I have an eight-year-old cat who has been consistantly losing weight over the past few days. I would like to schedule an appointment for her with you. When is the soonest convienient time?')
  print()
  print('1. Will monday, at 10 work for you? (suggest a convenient time)')
  print('2. Your cat is probably fine. I do not think that it is neccassary to schedule an appointment.')
  answer = input('> ')
  if answer == '1':
    print('YOU: Will monday, at 10 work for you? CALLER: Yeah, that works. Thank you.')
    clinic = True
  elif answer == '2':
    print(f'YOU: Your cat is probably fine. I do not think that it is neccassary to schedule an appointment. CALLER: Okay, if you say so. Goodbye.')
  if clinic:
    earned = random.randint(40, 100)
    print(f'The caller arrives, and their elderly cat is taken care of. You earn {earned} dollars.')
    return earned
  return 0

def call7():
  clinic = False
  print('YOU: Hello, West Valley Clinic, how may I help you? CALLER: Hello, I have a two-week old puppy named Bella. I wanted to know if symptoms of vomiting and diarrhea are concerning at this age.')
  print()
  print('1. Um, yeah, you should probably get that checked out.')
  print('2. No, that\'s very normal for puppies at that age. You shouldn\'t be concerned.')
  answer = input('> ')
  if answer == '1':
    print('YOU: Um, yeah, you should probably get that checked out. CALLER: Alright. I will be there soon. Thank you.')
    clinic = True
  elif answer == '2':
    print(f'YOU: No, that\'s very normal for puppies at that age. You shouldn\'t be concerned. CALLER: Okay, thank you. Goodbye.')
  if clinic:
    earned = random.randint(40, 100)
    print(f'The caller arrives, and Bella is taken care of. You earn {earned} dollars.')
    return earned
  return 0

def call8():
  clinic = False
  print(f'YOU: Hello, West Valley Clinic, how may I help you? CALLER: Hello, my cat just had a litter of kittens. I was going to ask about the cost of spaying and neutering at you clinic?')
  print()
  print('1. Spaying or neutering here at West Valley can cost between $50 and $200, depending on the size and weight of your cat.')
  print('2. I think Larry said that it costs, like 15 or 20 dollars.')
  answer = input('> ')
  if answer == '1':
    print('YOU: Spaying or neutering here at West Valley can cost between $50 and $200, depending on the size and weight of your cat. CALLER: Okay, thank you. Goodbye.')
    clinic = True
  elif answer == '2':
    print(f'YOU: I think Larry said that it costs, like 15 or 20 dollars. CALLER: Okay, thank you. Goodbye.')
  if clinic:
    earned = random.randint(50, 200)
    print(f'The caller arrives, and their cat is taken care of. You earn {earned} dollars.')
    return earned
  else:
    print('The cat owner arrives, and finds out that it actually costs between 50 and 200 dollars to spay and neuter a cat. They are very upset. They leave the clinic, and you do not earn any money.')
    return 0

def call9():
  clinic = False
  print(f'YOU: Hello, West Valley Clinic, how may I help you? CALLER: Hello! My dog, Genevieve, just got bit by another dog at the dog park! I don\'t know what to do, and I don\'t know when the last time Geny got her rabies shot! Is she going to be okay?!')
  print()
  print('1. Woah, calm down. Did the dog that bit her have an owner?')
  print('2. Yup, sounds like rabies! If you don\'t show up here soon, your dog will die!')
  answer = input('> ')
  if answer == '1':
    print('YOU: Woah, calm down. Did the dog that bit her have an owner? CALLER: Y-Yeah, it did.')
    print()
    print('1. Okay, unless the dog that bit her is foaming at the mouth, you should be fine. Although, depending on where the bite is, you should get it looked at just in case.')
    print('2. Then go talk to the owner and ask if the dog has rabies.')
    answer = input('> ')
    if answer == '1':
      print('YOU: Okay, unless the dog that bit her is foaming at the mouth, you should be fine. Although, depending on where the bite is, you should get it looked at just in case. CALLER: Okay, thank you. I am going to be there soon, just in case. Goodbye.')
      clinic = True
    elif answer == '2':
      print('YOU: Then go talk to the owner and ask if the dog has rabies. CALLER: Um, okay. [pause] The owner says his dog doesn\'t have rabies. Thank you. Goodbye.')
  elif answer == '2':
    print(f'YOU: Yup, sounds like rabies! If you don\'t show up here soon, your dog will die! CALLER: Oh no! Geny, come here, girl. Come here! I\'m going to be there soon. Thank you.')
    clinic = True
  if clinic:
    earned = random.randint(50, 200)
    print(f'The caller arrives, and their dog is taken care of. You earn {earned} dollars.')
    return earned
  return 0

def call10():
  clinic = False
  print('YOU: Hello, West Valley Clinic, how may I help you? CALLER: Hello, I was calling about my dog, Benjamin, who has been scratching excessively for a few days. I\'m worried he has fleas.')
  print()
  print('1. That does sound like fleas, but has he had any flea medicine lately?')
  print('2. Yup, sounds like fleas. Get here quick!')
  print('3. No, I don\'t think he has any fleas.')
  answer = input('> ')
  if answer == '1':
    print('YOU: That does sound like fleas, but has he had any flea medicine lately? CALLER: No, I\'ve never given him flea medicine. You know what, I\'ll just come by this afternoon. Thank you.')
    clinic = True
  elif answer == '2':
    print('YOU: Yup, sounds like fleas. Get here quick! CALLER: Oh! Okay, thank you. I\'m on my way.')
    clinic = True
  elif answer == '3':
    print(f'YOU: No, I don\'t think he has any fleas. CALLER: Oh, good, I\'m relieved. Thank you.')
  if clinic:
    earned = random.randint(20, 70)
    print(f'The caller arrives, and their dog is taken care of. You earn {earned} dollars.')
    return earned
  return 0

def call11():
  clinic = False
  print(f'YOU: Hello, West Valley Clinic, how may I help you? CALLER: Hello, I wanted to ask about the process of getting an animal microchipped.')
  print()
  print('1. To get your animal microchipped, we will put the animal to sleep, and then perform a small surgery to open up the animal, usually between the sholder blades, and insert a microchip into the animal. After that, we will show you how to register your animal\'s microchip.')
  print('2. To get your animal microchipped, we actually don\'t put the animal to sleep. We use a needle to inject a microchip into the animal. After that, we will show you how to register your animal\'s microchip.')
  answer = input('> ')
  if answer == '1':
    print('YOU: To get your animal microchipped, we will put the animal to sleep, and then perform a small surgery to open up the animal, usually between the sholder blades, and insert a microchip into the animal. After that, we will show you how to register your animal\'s microchip. CALLER: Okay, thank you. Can I schedule a microchipping for my dog on Wednesday? YOU: Yes, that\'s fine. CALLER: Okay, thank you. Goodbye.')
  elif answer == '2':
    print(f'YOU: To get your animal microchipped, we actually don\'t put the animal to sleep. We use a needle to inject a microchip into the animal. After that, we will show you how to register your animal\'s microchip. CALLER: Okay, thank you. Can I schedule a microchipping for my dog on Wednesday? YOU: Yes, that\'s fine. CALLER: Okay, thank you. Goodbye.')
    clinic = True
  if clinic:
    earned = random.randint(25, 50)
    print(f'The caller arrives, and their dog is taken care of. You earn ${earned}.')
    return earned
  else:
    print('The dog owner arrives, and found that they were very much misinformed about the process of getting an animal microchipped. They are very upset, and they refuse to pay. You lose $35 for the cost of the microchip.')
    return -35