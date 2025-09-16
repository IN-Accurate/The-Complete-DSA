'''
Maximum and minimum of an array using minimum number of comparisons
Input: arr[] = {3, 5, 4, 1, 9}
Output: Minimum element is: 1
              Maximum element is: 9
'''
def solve(arr):
        minElement=float("inf")
        maxElement=float("-inf")
        for num in arr:
                if(num<minElement):
                        minElement=num
                elif(num>maxElement):
                        maxElement=num
        return minElement,maxElement

def main():
        arr = list(map(int,input("Enter the numbers: ").split()))
        minElement,maxElement = solve(arr)
        print("Max element: ",maxElement,"\nMin element: ",minElement)

if __name__ == "__main__":
        main()