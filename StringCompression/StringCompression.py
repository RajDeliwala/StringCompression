'''
Cracking the coding interview
Chapter 1 - Arrays and Strings page 91
String Compression
----------------------------------------
Problem Statement: Implement a method to perform basic string compression using the counts of repeated chracters.
example:
    input: aabcccccaaa
    output: a2b1c5a3
Constraits or Questions you need to ask:
-Assume the string has only uppercase and lowercase letters a-z
Solution notes:
- start by making the entire string lowercase

'''

#First attempt, brute force method, sikke son we got a O(n) where n is the number of characters in the string
def string_comp(string):
    #Force entire string into lowercase, initalize result string
    string = string.lower()
    result = ""
    #Use dictionary to hold key and value pairs of Char and num_of_times
    d = dict()

    #run loop to iteratre through every char in the string and update values within the hash map
    for char in string:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    #Print key and values into result from dictionary
    for key,value in d.items():
        result += key
        result += str(value)
    #Logic for if the original string is shorter than the result string
    if(len(string) < len(result)):
        print(string)
    else:
        print(result)
        
#print(string_comp("aabbbccc"))



#Implementation not using additonal data structure
def string_comp_noDS(string):
    #Initialize a result string and count variable
    result = ""
    count = 1

    #Iterate through the string and count up the matching chracters
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            count += 1
        else:
            result += string[i] + str(count)
            count = 1
    result += string[i] + str(count)
    if len(result) >= len(string):
        print(string)
    else:
        print(result)

print(string_comp_noDS("aaabbbbcccc"))