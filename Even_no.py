#Yvonne Karimi
#BSCIT-05-0072/2024

numbers = (input("Enter a number:")).split()
def even_numbers(numbers):
    even = []
    for num in numbers:
        num = int(num)
        if num % 2 == 0:
            even.append(num)
    return even
print("The even numbers are:", even_numbers(numbers))
