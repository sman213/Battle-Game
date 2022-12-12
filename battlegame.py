wizard = "Wizard"
elf = "Elf"
human = "Human"
wizard_hp = 70
elf_hp = 80
human_hp = 50
wizard_damage = 150
elf_damage = 100
human_damage = 20 
dragon_hp = 300
dragon_damage = 50
print("1. Wizard")
print("2. Elf")
print("3. Human")
option = input("Choose your character:")
while True:
    if option == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        print("you have chosen the character",character,"hp:",my_hp,"damage",my_damage) 
        break  
    elif option == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        print("you have chosen the character",character,"hp:",my_hp,"damage",my_damage)
        break
    elif option == "3":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        print("you have chosen the character",character,"hp:",my_hp,"damage",my_damage)
        break
    else: option != "1, 2, or 3"
    print("Unknown Character")
    break
  
while True:
   dragon_hp = dragon_hp - my_damage
   my_hp = my_hp - dragon_damage
   print("The", character, "damaged the Dragon!")
   print("The Dragon's hitpoints are now", dragon_hp)
   if dragon_hp <= 0:
       print("The Dragon has lost the battle!")
       break 
   print("The Dragon strikesback at", character)
   print("The", character, "hitpoints are now", my_hp)
   if my_hp <= 0:
       print("Your character has lost the battle!")
       break
