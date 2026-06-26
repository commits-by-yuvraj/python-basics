is_male = True;
is_tall = False;

if is_male and is_tall: # we also can use --> or
    print("You are a male or tall or both");
elif is_male and not(is_tall):
    print("You are a short male");
elif not(is_male) and is_tall:
    print("You are a male but are tall");
else:
    print("You are either not male nor tall or both");


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(max_num(3, 40, 5));
    