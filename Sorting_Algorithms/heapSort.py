def max_Heap(alist, n , i):
    leftChild = 2*i+1
    rightChild = 2*i+2
    largest = i

    if leftChild < n and alist[leftChild] > alist[i]:
        largest = leftChild

    if rightChild< n and alist[rightChild]>alist[i]:
        largest = rightChild

    if largest != i :
        temp = alist[largest]
        alist[largest] = alist[i]
        alist[i] = temp

        max_Heap(alist, n , largest)

def build_Max_Heap(alist):
    for i in range(len(alist)//2-1,-1,-1):
        max_Heap(alist , len(alist), i)
def heapSort(alist):
    build_Max_Heap(alist)

    for i in range(len(alist)-1 , -1 , -1):
        temp = alist[0]
        alist[0] = alist[i]
        alist[i] = temp
        max_Heap(alist , i , 0)

alist=[]
n=int(input("enter the length of your list: "))

for i in range(n):
    alist.append(int(input("enter a number:")))

print("sorting.....")
heapSort(alist)
print(alist)