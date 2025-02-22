from solution import Solution 

def main():
    solution = Solution()
    
    nums = list(map(int, input("Enter the sorted array elements (separated by spaces): ").split()))
    
    k = solution.removeDuplicates(nums)
    
    print("Number of unique elements:", k)
    print("Modified array:", nums[:k])


if __name__ == "__main__":
    main()
