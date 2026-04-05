from bloom_filter import BloomFilter
import time
import math

def load_passwords(filename, limit=None):
    #Load passwords from a file, one per line.
    data=[]
    with open(filename, "r") as f:
        #returns the list of passwords with a specified limit
        for i, line in enumerate(f):
            hashes = line.strip().split(":")[0]
            data.append(hashes)
            if limit and i + 1 >= limit:
                break
    return data

def main():
    n=1000000
    p=0.01
    #m and k are calculated using number of passwords (n) 
    #and desired false positive rate (p)
    m=int(math.ceil(-(n*math.log(p))/(math.log(2)**2)))
    k=int(round((m/n)*math.log(2)))
    print("m=",m,"k=",k)
    passwords=load_passwords("pwnedpasswords.txt",n*2)
    #stored contains the first n passwords used in the filter
    stored=passwords[:n]

    BloomF=BloomFilter(m, k)

    #times how long it takes to insert the passwords
    start = time.time()
    for password in stored:
        BloomF._set_bit(password)
    end = time.time()
    print(round(end-start,100),"seconds to insert the passwords")
    
    #times how long it takes to query 1000 passwords that are always in there
    start = time.time()
    positiveTest=stored[:1000]
    for item in positiveTest:
        if not BloomF._check_bit(item):
            print("False negative:", item)
    end = time.time()
    print()
    print(round(end-start,100),"seconds to query 1000 passwords")

    #tests other half of the passwords that were not inserted to see  
    #the number of false positives
    start = time.time()
    FalsePosTest=passwords[n:2*n]
    FalsePosCount=0
    for item in FalsePosTest:
        if BloomF._check_bit(item):
            FalsePosCount+=1
    end = time.time()
    print()
    print(round(end-start,100),"seconds to test false positives")
    print("Number of False Positives:",FalsePosCount)

    print("False Positive Rate:",FalsePosCount/len(FalsePosTest))
    print()
    print("Memory usage:",(m/8)/1e+6,"megabytes")


    

if __name__ == "__main__":
    main()
