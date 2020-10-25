#ASCII - using numbers to represent text
    #it's a ways for computer to store characters easily
    #in its memory by convertiving them to numbers
    # uppercase A is always asigned the number 65
    # ! is always number 33
    # ASCII Charactars - 128 
    # Unicode Charactars - 1,114,112
    # Lowercase a (97) - uppercase A (65) = 32
    # Lowercase b (98) - uppcaser B (66) = 32
    
    #turning decimal numbers into bianary code 
        #10110110

        #188 
        # 128 64 32 16 8 4 2 1 - what numbers add to 182
        #  1   0  1  1 0 1 1 0 - fills those numbers in with 1 and the rest 0

        # every single key on your keyboard has a number translated with it 

#practice example ord() is how you find the valie
# s = input("Enter value: ")  # this line requires Python 3.x, use raw_input() instead of input() in Python 2.x

# l1=[c for c in s]   # in Python, a string is just a sequence, so we can iterate over it!
# l2=[ord(c) for c in s]

# print(l1)
# print(l2)
print("*************************************")
def funnyString(s):
    r = s[::-1] #reverse string [::-1]
    # l = len(s)

    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(r[i] - ord(r[i-1]))):
            return "Not Funny"
    
    return "Funny"

    # j = [arr2[0] for b in arr2]


print(funnyString("acxz"))