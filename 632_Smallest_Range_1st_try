import time

def readData(address):
	file = open(address,'r')
	importData = []
	nums = []
	for item in file:
		importData.append(item)
	
	allData = importData[0].split('],[')
	
	for i in range(0,len(allData)):
		nums.append(allData[i])
		nums[i] = nums[i].split(',')

	nums[0][0] = '95387'
	nums[-1][-1] = '100000'
	
	for i in range(0,len(nums)):
		for j in range(0,len(nums[i])):
			nums[i][j] = int(nums[i][j])

	return nums


def smallestRange(nums):
        
	diff = 200000
	candidateSmall = 0
	candidateLarge = 0
       
	allData = []
	for row in nums:
		for item in row:
			if item not in allData:
				allData.append(item)
	allData.sort()
    

		
	for i in range(len(allData)-1,-1,-1):
		for j in range(i, len(allData)):
			#if allData[j] - allData[i] > diff:	
			#	break
			
			if allData[j] - allData[i] <= diff:
			
			#else:
				newDiff = allData[j] - allData[i]
				n = 0
				for row in nums:
					for item in row:
						if item <= allData[j] and item >= allData[i]:
							n = n + 1
							break
					if n == len(nums):
						diff = newDiff
						candidateSmall = allData[i]
						candidateLarge = allData[j]
				
	return ([candidateSmall,candidateLarge])
    

	
def main():
	address = 'D:\\Xudong\\Xudong_work_and_study\\xudong leetcode\\632_smallest_range\\data.txt'
	nums = readData(address)
	
	time_a = time.time()
	result = smallestRange(nums)
	time_b = time.time()
	print (time_b-time_a)
	print (result)
	
main()
