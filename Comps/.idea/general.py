# General oral exam questions
import math;
a = [4, 17, 54, 67, 0, -12, 5, 22, 2, 17, 33, 6, 17, 9, 20]
b = [i*i % 101 for i in range(52)]

# Write some functions

# Find the sum of the elements of the array
def sum(numbers):
    count = 0
    for element in numbers:
        count += element

    return count

print("The sum of a is " + str(sum(a)))


# Determine how many prime numbers are in the array
def isPrime(number):
    if number <= 0:
        return False
    if number == 1:
        return True
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True


def countPrimes(numbers):
    count = 0
    for element in numbers:
        if isPrime(element):
            count += 1

    return count

print("The number of primes is " + str(countPrimes(a)))




# What is the smallest difference that can be created between two distinct elements?

def smallest_difference(numbers):
    smallest_difference = 99999999999999
    for element in numbers:
        for compared_element in numbers[(numbers.index(element) + 1):]:
            if compared_element == element:
                continue
            if abs(element - compared_element) < smallest_difference:
                smallest_difference = abs(element - compared_element)
                #print(smallest_difference)

    return smallest_difference

print("The smallest difference is " + str(smallest_difference(a)))


# sort the array

def quicksort(numbers):

    if len(numbers) <= 1:
        return numbers

    pivot = numbers.pop(0)
    right_list = []
    left_list = []

    for i in range(len(numbers)):
        if numbers[i] < pivot:
            left_list.append(numbers[i])
        else:
            right_list.append(numbers[i])

    return quicksort(left_list) + [pivot] + quicksort(right_list)

print("The quicksorted list is " + str(quicksort(a)))




