'''
Contains Duplicate
Given an integer array nums, return true if any value appears at least
twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation: All elements are unique

'''

def containsDuplicate(arr):
    seen = set()
    for num in arr:
        if(num in seen):
            return True
        seen.add(num)
    return False

def main():
    arr = list(map(int,input("Enter the numbers: ").split()))
    result = containsDuplicate(arr)
    print(result)

if __name__ == '__main__':
    main()