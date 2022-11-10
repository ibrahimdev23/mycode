#!/usr/bin/env python3


#the first input asks the user to type in: y n to start the game
start = input(
  "Do you want to find out what type of bender from 'Avatar' you are? press y or n ")
#the bender types are save inside a list of objects.
bender_types = [{
  "A": "You are an Air Bender 💨 "
}, {
  "E": "You are an Earth Bender 🪨 "
}, {
  "F": "You are a Fire Bender 🔥 "
}, {
  "W": "You are a Water Bender 🌊 "
}, {
  "L": "You are a Lava Bender 🌋 "
}, {
  "M": "You are a Metal Bender ⚙️"
}]
#the game runs inside a function that will only run if the user typed in 'y' at the beginning
def startGame():
  list_len = len(bender_types)
  while list_len > 0:
    if place == "K" and fav_pet == "L" and fav_avatar == "K" and fav_item == "S":
      print(bender_types[1]["E"])
      list_len -= 1
      break
    elif place == "A" and fav_pet == "F" and fav_avatar == "R" and fav_item == "A":
      print(bender_types[0]["A"])
      list_len -= 1
      break
    elif place == "B" and fav_pet == "W" and fav_avatar == "K" and fav_item == "I":
      print(bender_types[2]["F"])
      list_len -= 1
      break
    elif place == "S" and fav_pet == "E" and fav_avatar == "S" and fav_item == "K":
      print(bender_types[3]["W"])
      list_len -= 1
      break
    elif place == "K" and fav_pet == "W" and fav_avatar == "W" and fav_item == "K":
      print(bender_types[4]["L"])
      list_len -= 1
      break
    else:
      print(bender_types[5]["M"])
      list_len -= 1
      break
#if the user choose 'y' then the user will be asked for more inputs. The inputs allowed are only one character. which are shown by the [].
if start == 'y':
  place = input(
    'pick a place: [k]yoshi Island, [A]ir Nomand Temple, [B]a Sing Se, [S]pirit World '
  ).upper(
  )  #the input is converted to Uppercase to match the letters inside of the startGame()
  fav_pet = input(
    "pick a pet: [L]ion turtle, [F]lying bison, [W]inged lemur, [E]lepant koi "
  ).upper()
  fav_avatar = input(
    "pick a past Avatar: [K]yoshi, [R]oku, [W]an, [S]zeto ").upper()
  fav_item = input(
    "Pick a favorite item: [S]okka's boomerang, [I]roh's jasmine tea, [A]ang's staff, [K]atara's necklace "
  ).upper()
  # the game function runs if the user picks 'y'
  startGame()
elif start == 'n':
  print(
    "Sorry this is the only game we ave. Please check back latter for more games."
  )
else:
  print("Please restart and type in:  y or n")
