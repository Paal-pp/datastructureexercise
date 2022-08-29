class data_structure_exercise(object):
    def findMaxConsecutiveOnes_485(self):
        nums = [1, 1, 0, 1,0,1,1,1]
        num_Num = 0
        maxnum = 0
        for num in nums:
            if num == 1:
                num_Num = num_Num + 1
            else:
                maxnum = max(maxnum, num_Num)
                num_Num = 0
        maxnum = max(maxnum, num_Num)
        print(maxnum)
        return maxnum

    def findPoisonedDuration_495(self):
        timeSeries = [1, 4]
        duration = 2
        ans, expired = 0, 0
        for i in range(len(timeSeries)):
            if timeSeries[i] >= expired:
                ans += duration
            else:
                ans += timeSeries[i] + duration - expired
            expired = timeSeries[i] + duration
        print(ans)
        return ans

    def thirdMax_414(self):
        nums = [1, 2]
        nums.sort(reverse=True)
        diff = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                diff += 1
                if diff == 3:  # 此时 nums[i] 就是第三大的数
                    return nums[i]
        return nums[0]
        # nums = [1,2]
        # frist_max = 0
        # sencond_max = 0
        # thirth_max =0
        # for num in nums:
        #     if num > frist_max:
        #         thirth_max = sencond_max
        #         sencond_max =frist_max
        #         frist_max =num
        #     else:
        #         if num >sencond_max:
        #             thirth_max = sencond_max
        #             sencond_max=num
        #         else:
        #             if num >thirth_max:
        #                 thirth_max=num
        # if thirth_max== 0:
        #     if sencond_max ==0:
        #         thirdMax=frist_max
        #     else:
        #         thirdMax =sencond_max
        # else:
        #     thirdMax=thirth_max
        # print(frist_max)
        # print(sencond_max)
        # print(thirdMax)
        return thirdMax

    def shuffle_1470(self):
        '''
        注释是参考答案
        '''
        nums = [2, 5, 1, 3, 4, 7]
        n = 3
        nums_list =[0]*(2*n)
        ans =[]
        for i in range(n):
            # nums_list[2*i]=nums[i]
            # nums_list[2*i+1] = nums[i+n]
            ans.append(nums[i])
            ans.append(nums[i+n])
        print(ans)
        # print(nums_list)
        return  ans





if __name__ == "__main__":
    main_class=data_structure_exercise()
    # q485 = main_class.findMaxConsecutiveOnes_485()
    # q495 = main_class.findPoisonedDuration_495()
    # q1470= main_class.shuffle_1470()
    # q414 = main_class.thirdMax_414()