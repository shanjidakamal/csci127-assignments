#1
def capitalize(name):
    """
    input: name --> a string in the form "first last"
    output: returns a string with each of the two words capitalized
    note: this is the one we started in class
    """
    capitalize_name= name. title()
    return capitalize_name

print(capitalize("james bond"))

#2       
def init(first, last):
    """
    Input: name --> a string in the form "first last"
    Returns: a string in the form "F. Last" where it's a capitalized first inital 
    and capitalized last name
    """
    first= first
    last = last
    init_name= first[0].capitalize() + "." + last.capitalize()
    return init_name

print(init("john", "hamm"))
       
#3   
def part_pig_latin(name):
    """
    Input: A string that is a single lower case word
    Returns: that string in fake pig latin -> move the first letter of the word to the end and add "ay"
    so: "hello" --> "ellohay"
    """
    j= "hello"
    part_pig_latin= j[1:] +"ay"
    return part_pig_latin

print(part_pig_latin("hello"))
    
#4
#makeoutword
def make_out_word(out, word):
  return out[:2] + word + out[2:]

print(make_out_word('<<>>', 'Yay'))
print(make_out_word('<<>>', 'WooHoo'))
print(make_out_word('[[]]', 'word'))

#5
#maketags
def make_tags(tag, word):
  return "<" + tag + ">" + word + "</" + tag + ">"

print(make_tags('i', 'Yay'))
print(make_tags('i', 'Hello')) 
print(make_tags('cite', 'Yay')) 