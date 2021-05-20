# list comprehentions are used for creating  new list from other iterables
# they consist of brackets containing the expressions
# which is executed for each element

# numbers=[1,4,5,2,3,47]
# print(numbers)
# squares=[]
#
# for n in numbers:
#     squares.append(n**2)
# print(squares)

numbers=[1,4,5,2,3,47]
squares=[n**2 for n in numbers]
print(squares)