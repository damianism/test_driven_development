# def count_upper_case(message):
#     countUpper = 0
#     countLower = 0
#     for c in message:
#         if c.isupper():
#             countUpper += 1
#     return countUpper

def count_upper_case(message):
    return sum([1 for c in message if c.isupper()]) 

assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("Damian A Rodbari, Student!") == 4, "One upper case expected, got {}".format(count_upper_case("Damian A Rodbari, Student!"))
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("£$%%^") == 0, "Special characters"

myList = [1,2,3]
print(sum(myList, 200))

print("All the tests passed")