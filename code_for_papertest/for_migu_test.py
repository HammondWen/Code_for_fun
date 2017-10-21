import string


def fun(str):
    str=str+'0'
    status = True
    count = 0
    for s in range(len(str)-1):
        print str[s]
        if(str[s].islower()==status):
            count=count+1
        else:
            if str[s+1]=='0':
                return count+2
            else:
                if str[s].islower()==str[s+1].islower():
                    status= not status
                    count=count+2
                else:
                    count=count+2
    return count

def main():
    s=[]
    n=raw_input()
    for i in n:
        s.append(raw_input())
        c=0
    for str in s:
        c=c+fun(str)
    print (c)


main()
