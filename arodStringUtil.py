

#BEGIN define a function that checks if parentheses are valid
#meaning if you have an opening you need a closing bracket
def valid_pars(s: str) -> bool: 
    closes = { "(":")" , "[":"]" , "{":"}" }
    opens = []
    for par in s:
        if par in closes.keys() :
            opens.append(par)
        elif opens == []:
            return False
        elif par != closes[opens.pop()] :
            return False
    return opens == []

# str_1 = "()[]{}"    #true
# str_2 = "{){}["     #false
# str_3 = "{[]}"      #true

# print(valid_pars(str_1))      #Test str_1
# print(valid_pars(str_2))      #Test str_2
# print(valid_pars(str_3))      #Test str_3
#END define a function that checks if parentheses are valid


#BEGIN function to reverse the spelling of each item in the list "one" -> "eno"
def rev_list(list):
    rev_list = []
    for i in list:
        rev_list.append(i[::-1])
    return rev_list

# sample_list = [ "one" , "two" , "three" ]     #test string
# print(rev_list(sample_list))                  
#END function to reverse the spelling of each item in the list "one" -> "eno"

#BEGIN function to return a right angle triangle of "S" stacked height
def triangle(height):
    triangle = ""
    for i in range(height):
        triangle += f"{'S ' * i}\n"
    return triangle

#print(triangle(10))       #should produce a right triangle of "S"s stacked height tall
#print(triangle(12))       #should produce a right triangle of "S"s stacked height tall

#END function to return a right angle triangle of "S" stacked height






