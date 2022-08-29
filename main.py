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




if __name__ == "__main__":
    main_class=data_structure_exercise()
    # q485 = main_class.findMaxConsecutiveOnes_485()
    # q495 = main_class.findPoisonedDuration_495()