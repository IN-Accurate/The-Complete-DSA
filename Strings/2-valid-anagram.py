def solve(s1,s2):
    freq={}
    for ch in s1:
        freq[ch] = freq.get(ch,0)+1
    
    for ch in s2:
        freq[ch] = freq.get(ch,0)-1
    
    for key,val in freq.items():
        if val!=0:
            return False
    return True


def main():
    s1=input("Enter the first string: ")
    s2=input("Enter the second string: ")
    print(solve(s1,s2))

if __name__ == '__main__':
    main()