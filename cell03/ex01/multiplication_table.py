print('Enter a number:')
number_entered = int(input())
num = 0
i = num
if i < 12:
    while i<12:
        i +=1
        result = int(i)*int(number_entered)
        print(i,"x",number_entered,"=",result)
