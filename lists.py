lucky_number = [4, 6, 8, 23, 9];
friends = ["Kevin", "Karen", "Jim", "Oscar", "Carry"];

# friends.extend(lucky_number);
friends.append('Toby');
friends.insert(1, "Kellen");
friends.remove("Toby");

# friends.clear();  # removes all elements

friends.pop();
lucky_number.sort();
lucky_number.reverse();

friends2 = friends;
friends3 = friends.copy();

# = → creates a reference (same object)
# .copy() → creates a new list (different object)

# print(friends[1:3]); # include the index from 1 upto 3 
# print(friends);
# print(friends.index("Karen"));
# print(lucky_number);
print(friends2);