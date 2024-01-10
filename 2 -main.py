#day 2- even numbers
#222
#$program that covertstemperature to kelvim
celcius = 13
kelvin = celcius + 273.15
print("the temp is:", kelvin)
##4444
#a function reversing a string
original_text = "gooood"
reversed_text = "".join(reversed(original_text))#join reverses the character and puts it into a string
print(f" reverse text: {reversed_text}")
##66666
#check if a given string is a pangram
import string
def is_pangram(text):
    text1 =("we are going out")
    text2 = ("home is best")
    print(f"{text1} is not a pangram: {is_pangram(text1)}")##incomplete