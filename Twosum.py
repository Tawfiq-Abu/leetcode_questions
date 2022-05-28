def twoSum( nums, target) :
    '''
    logic used here was that the current number the loop is on minus the target would give you the number that when added to the current loop number would give you the target
    '''
    for i in range(len(nums)):
        # get the array of numbers that added to nums[i] would give you the target
        # the filtered list should start from the current loop to the end
        second_number_array = list(filter(lambda x: x == target-nums[i], nums[i+1:]))
        print(second_number_array)
        # if the second number array returned something or it's not empty
        if second_number_array:
            second_number = second_number_array[0]
            # we want to check if the the second number appears in the nums array twice
            if nums.count(second_number) > 1:
                # if it does then we want to find the second occurence of the number's index
                return [i, nums.index(second_number, i+1)]
            else:
                return [i, nums.index(second_number)]
                    
        else:
            continue

testarray = [3,2,6]
print(twoSum(testarray,6))