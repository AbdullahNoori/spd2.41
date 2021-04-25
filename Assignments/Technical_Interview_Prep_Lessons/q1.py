class Solution:
    # solution # 1
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numbers = [5, 3, 6, 8, 2, 4, 7]
        target = 10

        for i, number in enumerate(numbers[:-1]):  # note 1
            complementary = target - number
            if complementary in numbers[i+1:]:  # note 2
                print("Your Solution is: {} and {}".format(number, complementary))
                break
        else:  
            print("No solutions exist")
        