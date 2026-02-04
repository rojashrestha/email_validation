#some of the importaant string concepts in python



#reverse a string
string="Roja Shrestha"
reversed_string=string[::-1]
print("Reversed String:",reversed_string)



#Count word in sentences 
string="Roja Shrestha"
string1="RojaShrestha"
print("the total charater in the string is:",len(string))
print(len(string1))



#len() count the charater in the strings 
string2="roja is learning python"
string2.split()
word_count=len(string2.split())
print("the total word in the string2 is:",word_count)
string2.count("")



#Replace "hello world" to "HELLO_WORLD"
text="hello world"
print(text.capitalize())
text2=text.upper()
print(text2.replace(" ", "_"))



#Palindrome
check_palindrome="roja"

if check_palindrome==check_palindrome[::-1]:
    print("the text is palindrom")
    
else:
    print("the text is not palindrom")
