def is_even(number):
    return number % 2 == 0

def even_number_of_evens(numbers):
    evens = sum([1 for n in numbers if is_even(n)])
    return False if evens == 0 else is_even(evens)
    
    # count = 0
    # for number in numbers:
    #     if is_even(number):
    #         count += 1
    
    # print("for input {} even number count is {} ".format(numbers, count))
    # if count == 0: return False
    
    # if is_even(count):
    #     return True
    # else:
    #     return False

        
assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([1,3,9]) == False, "Three odd numbers"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 6]) == False, "Multiple numbers, three are even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four are even"
assert even_number_of_evens([0,2,4,6,8,10]) == True, "Six even numbers"
print("All tests passed!")