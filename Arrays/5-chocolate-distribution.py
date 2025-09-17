def solve(arr,m):
    arr.sort()
    ans=float("inf")
    length=len(arr)
    # i in range 0 to length-m + 1 - 1 = 0 to length - m
    # this is because m sized window means when the last window,
    # i starts at length-m, the end of the window is at i+m-1 = length - 1 ,
    # that is, the last element
    for i in range (length-m+1): 
        ans = min(ans,(arr[i+m-1]-arr[i]))
    return ans

def main():
    arr = list(map(int,input("Enter the numbers: ").split()))
    m = int(input("Enter the number of students: "))
    ans = solve(arr,m)
    print("Answer: ",ans)

if __name__ == "__main__":
        main()

'''
Given an array arr[] of n integers where arr[i] represents the 
number of chocolates in ith packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 

Each student gets exactly one packet.
The difference between the maximum and minimum number of chocolates in the packets given to the students is minimized.
Examples:

Input: arr[] = {7, 3, 2, 4, 9, 12, 56}, m = 3 
Output: 2 
Explanation: If we distribute chocolate packets {3, 2, 4}, we will get the minimum difference, that is 2. 

Input: arr[] = {7, 3, 2, 4, 9, 12, 56}, m = 5 
Output: 7
Explanation: If we distribute chocolate packets {3, 2, 4, 9, 7}, we will get the minimum difference, that is 9 - 2 = 7. 
'''