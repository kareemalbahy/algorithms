def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,p,l):
    splitPoint = partition(alist,p,l)
    quickSortHelper(alist,p,splitPoint-1)
    quickSortHelper(alist,splitPoint+1,l)

def partition(alist,p,l):
    pivot = alist[p]
    leftMark = p+1
    rightMark = l
    done = False

    while not done:
        while leftMark<rightMark and alist[leftMark]<=pivot:
            leftMark+=1
        while rightMark>leftMark and alist[rightMark]>=pivot:
            rightMark-=1
        
        if leftMark>rightMark:
            done = True
        else:
            temp=alist[rightMark]
            alist[rightMark]=alist[leftMark]
            alist[leftMark]=temp

    alist[p]=alist[rightMark]
    alist[rightMark]=pivot

    return rightMark

alist=[]
n=int(input("enter the length of your list: "))

for i in range(n):
    alist.append(int(input("enter a number:")))

print("sorting.....")
quickSort(alist)
print("done")
print(alist)