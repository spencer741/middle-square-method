'''
[Middle-square method (1946)](https://en.wikipedia.org/wiki/Middle-square_method)

Weakness Note from link ...
For a generator of n-digit numbers, the period can be no longer than 8n. If the middle n digits are all zeroes, the generator then outputs zeroes forever. If the first half of a number in the sequence is zeroes, the subsequent numbers will be decreasing to zero. While these runs of zero are easy to detect, they occur too frequently for this method to be of practical use. The middle-squared method can also get stuck on a number other than zero.

'''

#note, an already_seen list is not included in the original middle square method and will not be used.

def Middle_Square(seed, listlength):
    print("Middle_Square")
    numlist = []
    for i in range(listlength):
        seedlength = len(str(seed))
        # The value of n must be even in order for the method to work ... 
        # It is acceptable to pad the seeds with zeros to the left in order to create an even valued n-digit (eg: 540 → 0540).
        if (seedlength % 2 != 0):  
            seedlength += 1
            seed = str(int(seed)).zfill(seedlength)
        #print("seedlen", seedlength)
        seed = str(int(seed) * int(seed)).zfill(2 * seedlength) #fill leading zeros if seed*seed is less than (2*seed) digits long
        #print("newseed", seed)
        half = int(seedlength / 2)
        seed = seed[(half):(seedlength + half)]
        #print("finalseed", seed)
        #print(seed)
        numlist.append(seed)
    #print(numlist)
    return(numlist)
