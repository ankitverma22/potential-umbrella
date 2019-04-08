
def getconvert(open,close,n, s= []):
    # base case
    if (close==n):
        print(" ".join(s))
        return

    else:

        if(open>close):
            s.append (")")
            getconvert(open,close+1,n,s)
            s.pop()

        if(open<n):
            s.append("(")
            getconvert(open+1,close,n,s)
            s.pop()
    return

if __name__ == '__main__':
    getconvert(0,0,2)



