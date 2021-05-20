def revert_values(func):
    def wrapper(no1,no2):
        if no1<no2:
            (no1,no2)=(no2,no1)
        return func(no1,no2)
    return wrapper





@revert_values
def div(no1,no2):
    return no1/no2
print(div(10,20))
@revert_values
def sub(no1,no2):
    return no1-no2
print(sub(10,20))