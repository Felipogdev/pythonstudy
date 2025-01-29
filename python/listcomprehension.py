
nums = [-1,2,6,10,-5,3,93,0]

oddNums = [num for num in nums if num % 2 != 0]
evenNums = [num for num in nums if num % 2 == 0]
positiveNums = [num for num in nums if num > 0]
negativeNums = [num for num in nums if num < 0]

print(oddNums)
print(evenNums)
print(positiveNums)
print(negativeNums)