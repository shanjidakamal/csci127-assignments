def greeter(name):
    return "Hello" +name+" ! "
print(greeter("Stan"))


def make_abba(abba):
    a="hello"
    b="world"
    result=a+b+b+a
    return result

print(make_abba("helloworldworldhello"))
          

def lastFirst(firstName, lastName):
    separator = ', '
    result = lastName + separator + firstName
    return result

print(lastFirst('Shanjida', 'Kamal'))
print(lastFirst('csci', '127'))
print(lastFirst('World', 'Hello'))


