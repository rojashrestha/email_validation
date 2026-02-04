email = input("Enter your email address: ")

k = 0   # space error
j = 0   # uppercase error
d = 0   # invalid character error 

# Wrong email 1 → minimum length check
if len(email) < 6:
    print("Wrong email 1: Email too short")

# Wrong email 2 → first character must be alphabet
elif not email[0].isalpha():
    print("Wrong email 2: Email must start with an alphabet")

# Wrong email 3 → must contain exactly one '@'
elif ("@" not in email) or (email.count("@") != 1):
    print("Wrong email 3: Email must contain exactly one '@'")

# Wrong email 4 → '.' must be at -3 OR -4 (but not both)
elif not ((email[-4] == ".") ^ (email[-3] == ".")):
    print("Wrong email 4: Invalid domain position")

else:
    # character-by-character validation
    for i in email:
        if i.isspace():          # space not allowed
            k = 1
        elif i.isupper():        # uppercase not allowed
            j = 1
        elif i.islower():        # lowercase allowed
            continue
        elif i.isdigit():        # digits allowed
            continue
        elif i in ["_", ".", "@"]:  # allowed special chars
            continue
        else:                    # any other character is invalid
            d = 1

    # Wrong email 5 → character validation failed
    if k == 1 or j == 1 or d == 1:
        print("Wrong email 5: Invalid characters found")
    else:
        print("Valid Email ")
