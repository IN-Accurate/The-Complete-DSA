'''
Reverse the array elements
Input: arr[] = [1, 4, 3, 2, 6, 5]  
Output:  [5, 6, 2, 3, 4, 1]
'''

def reverseArray(arr):
    i,j=0,len(arr)-1
    while(i<j):
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr    

def main():
    arr = list(map(int, input("Enter the numbers: ").split()))
    reverseArray(arr)
    print("The reversed array is: ")
    for num in arr:
        print(num,end=" ")

if __name__ == "__main__":
    main()