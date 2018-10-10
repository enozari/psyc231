def sort2(a, b):
    numeric_types = [int, float]
    if ((type(a) not in numeric_types) |
    (type(b) not in numeric_types)):
        print("Unsupported file type!")
        return
    if a <= b:
        return [a, b]
    else:
        return [b, a]
    
def my_prod(lst):
    prod = 1
    for num in lst:
        prod *= num
    return prod