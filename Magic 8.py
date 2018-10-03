answer1 = raw_input("what is ur name: ")
answer2 = raw_input("what is ur age: ")
answer3 = raw_input("what is ur sex: ")

def game(answer1,answer2,answer3):
    if answer1 == "Dhaval":
        print "name is Dhaval"
    else:
        print "empty"
if answer2 == "40":
    print "age is 40"
else:
    print "empty"
if answer3 == "M":
    print "sex is male"
else:
    print "empty"

game(answer1,answer2,answer3)