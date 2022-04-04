
def max_num (x, y, z):
    return max([x, y, z])
        

print(max_num(45, 12, 62))


def mult_list(*args):
    start = args[0]
    if len(args) > 1:
        for i in args:
            start *= i
    return start

print(mult_list(2, 5, 0))


def rev_string(string): #had to look this one up
    return string[::-1]

print(rev_string('Courtney'))

def fib(n): #def got lost with this one. 
    start = n[0]
    if len(n) > 1:
        for i in n[1:]:
