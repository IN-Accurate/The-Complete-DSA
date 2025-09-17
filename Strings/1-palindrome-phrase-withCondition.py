
def cleanUpData(s,newStr):
        for character in s:
             if(character.isalnum()):
                  newStr += character.lower()
        return newStr

# instead of above code, we can use the following join directly:

'''
    return "".join(ch.lower() for ch in s if ch.isalnum())
'''

def isPalindrome(newStr):
    i,j=0,len(newStr)-1
    while(i<j):
         if(newStr[i]!=newStr[j]):
            return False
         i += 1
         j -= 1
    return True

def main():
    s = input("Enter the phrase with alphanumeric and special characters: ")
    newStr = ""
    newStr=cleanUpData(s,newStr)
    if(isPalindrome(newStr)):
        print(True)
    else:
        print(False)
    
if __name__ == '__main__':
    main()

'''
A phrase is a palindrome if, after converting all 
uppercase letters into lowercase letters and removing
all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''