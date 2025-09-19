def main():
    s = input("Enter the string: ")
    ans=""
    ans +=s[0]
    prev=s[0]
    for i in range (1,len(s)):
            if(s[i]!=prev):
                 ans+=s[i]
                 prev=s[i]
            i +=1
    print("New string after removing duplicate chars: ",ans)
if __name__ == '__main__':
    main()