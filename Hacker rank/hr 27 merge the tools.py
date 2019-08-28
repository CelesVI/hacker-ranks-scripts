import textwrap

def merge_the_tools(string, k):
    strdiv = textwrap.wrap(string, k)
    fut = []  
    for i in range(len(strdiv)):
        newlist = []
        for j in range(k):
            if (strdiv[i][j] not in newlist):
                newlist.append(strdiv[i][j])
        f = "".join(newlist)
        fut.append(f)
    print(*fut, sep="\n")
 
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
