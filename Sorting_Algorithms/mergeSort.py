def mergeSort(alist):
    #split
    lefthalf=[]
    righthalf=[]
    #base case
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        #recursion
        mergeSort(lefthalf)
        mergeSort(righthalf)

    #merge
    i=0
    j=0
    k=0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            alist[k]=lefthalf[i]
            i=i+1
        else:
            alist[k]=righthalf[j]
            j=j+1
        k=k+1

    #copy the rest
    while i < len(lefthalf):
        alist[k]=lefthalf[i]
        i=i+1
        k=k+1

    while j < len(righthalf):
        alist[k]=righthalf[j]
        j=j+1
        k=k+1
alist=[]
n=int(input("enter the length of your list: "))

for i in range(n):
    alist.append(int(input("enter a number:")))

print("sorting.....")
mergeSort(alist)
print(alist)