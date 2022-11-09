 
 #!/usr/bin/python

heroes= ["Spiderman", "Batman", "Black Panther", "Wonder Woman", "Storm"]

# PART 1
# Print out your favorite character from this list! The output would look something like:
# My favorite character is Black Panther!

print("my fav character is " + heroes[1])


# PART 2
# Ask the user to pick a number between 1 and 100.
# Convert the input into an integer.


number = int(input("pick num 1 - 100"))


nums= [1, -5, 56, 987, 0]
nums.append(number)

print(max(nums))



l = [1,2,3,4]
s = [100,200,400]

l.extend(s)
print(l)



# PART 3
# check out https://docs.python.org/3/library/functions.html or go to Google
# use a built-in function to find which integer in nums is the biggest.
# then, print out that number!
