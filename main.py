original_list=[1,5,11,9,12,23]

flag=False
i=0
while(i<5):

    if(original_list[i]>original_list[i+1]):
        flag=False
        break
    elif(i==4 and original_list[i]<original_list[i+1]):
        flag=True
        break

    i+=1

if(flag==False):
    or1=sorted(original_list)
    print("False")
    print("Sorted List:")
    print(or1)
else:
    print("True")
    print("Original List")
    print(original_list)



