import sys

sys.stdin = open('inputfile.txt','r')
n = sys.stdin.read().splitlines()
testcase = int(n[0])
n.remove(n[0])

nums = []
for i in range(len(n)):
    nums.append(int(n[i]))

#퀵 정렬 사용
pivot = nums[len(nums)//2]
lp = nums[0]
rp = nums[len(nums)-1]

indexL = 0
indexR = len(nums) - 1

print(pivot)

for j in range(len(nums)):
    if(indexL <= indexR):
        if(nums[indexL] >= pivot and nums[indexR] <= pivot):
            if(nums[indexL] == pivot):
                nums[indexL] = rp
                nums[indexR] = lp
                indexL += 1
                rp = nums[indexR]
                lp = nums[indexL]
            elif(nums[indexR] == pivot):
                nums[indexL] = rp
                nums[indexR] = lp
                rp = nums[indexR]
                indexR -= 1
                lp = nums[indexL]
            else:
                nums[indexL] = rp
                nums[indexR] = lp
                indexL += 1
                indexR -= 1
                rp = nums[indexR]
                lp = nums[indexL]
        elif(nums[indexL] >= pivot and nums[indexR] > pivot):
            indexR -=1
            rp = nums[indexR]
        elif(nums[indexL] < pivot and nums[indexR] <= pivot):
            indexL +=1
            lp = nums[indexL]
        elif((nums[indexL] < pivot and nums[indexR] > pivot) or indexL == indexR):
            indexR -=1
            rp = nums[indexR]
            indexL +=1
            lp = nums[indexL]
        else:
            if(indexL > indexR + 1):
                break
    print(nums)
    print(indexL, indexR)
    # else:
        # for l in range(len(nums)):
        #     if(nums[l] > nums[l+1]):
                    
        # return

# for k in range(len(nums)):
    # print(nums[k])