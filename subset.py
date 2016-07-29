DEBUG=False

if DEBUG:
    f = open('debug.txt', 'w')
    f.write("---------------------------------\n")

def subSet(n):
    
    # Debug
    global DEBUG
    if DEBUG:
        global f
        f.write(str(n)+"\n")

    # Sanity checks
    if type(n) != type([]):
        print("n must always be a list. Passed in: ",n)
        exit()
    if len(n) == 0:
        print("n must be non zero length. Passed in: ", n)
        exit()

    # Base case
    if len(n) == 1:
        return(n)

    # Recursive step. Idea is that for a list [a, b, c, ..., n], the resulting ordered subsets will
    # always be of the form [a, subSet([b,c,...,n])] or [ab, subSet[c,..., n]]
    else:
        # Get results of form [a, subSet([b,c,...n])
        subSetResults = subSet(n[1:])
        resultsOfForm_a = []
        for i in subSetResults:
            if type(i) == type([]):
                foo = [n[0]]
                temp = foo.copy()
                temp.extend(i)
            else:
                temp = [n[0], i]
            resultsOfForm_a.append(temp)

        # Get results of form [ab, subSet([c,...,n])]
        k = [str(n[0])+str(n[1])]
        k.extend(n[2:])
        resultsOfForm_ab = subSet(k)
        
        return resultsOfForm_a + resultsOfForm_ab


results = subSet(['a', 'b', 'c', 'd', 'e', 'f'])
for item in results:
    print(item)


