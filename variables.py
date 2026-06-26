from math import *;

character_name = "Yuvraj"
character_age = 26
is_male = True

print("There once a man named " + character_name + ", ");
print(f"he is {character_age} years old.");


character_name = "Mike"
character_age = "36"

print("There once a man named " + character_name + ", ");
print(f"he is {character_age} years old.");

# f-strings (formatted string literals) are the modern and preferred way to insert variables into strings in Python (Python 3.6+).


# Strings
phrase = "Next Academy"
print(phrase.isupper());
print(len(phrase));
print(phrase.index("A"));
print(phrase.replace("Next", "Wobble"));

# Numbers
print(3 * 4 + 5);
print(3 * (4 + 5));
print(10 % 3); # remainder

my_num = -5;
# print(my_num + " my favorite Number!"); TypeError
print(str(my_num) + " my favorite Number!");
print(abs(my_num));
print(pow(3, 2));
print(max(4, 6));
print(min(4, 6));
print(round(3.2));
print(floor(3.7));
print(sqrt(36));