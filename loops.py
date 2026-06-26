# while loop

i = 1
while i <= 10:
    print(i)
    i += 1


# guess game

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3

# while guess != secret_word and guess_count < guess_limit:
#     guess = input("Enter guess: ")
#     guess_count += 1

# if guess == secret_word:
#     print("You Win!")
# else:
#     print("Out of gusses, You LOSE!")



# for loop

friends = ["Kevin", "Karen", "Jim", "Oscar", "Carry"]
len(friends)

for letter in "Star Academy":
    print(letter)

for friend in friends:
    print(friend)

for index in range(len(friends)):
    print(friends[index])

for index in range(3, 10):  # print from 3 to 9, not including 10
    print(index)

