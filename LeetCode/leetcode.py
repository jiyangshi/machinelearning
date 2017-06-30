class Solution( object ):
    def __init__( self ):
        print( "Welcome to LeetCode World" )

    def twoSum( self, nums, target ):
        """
        :type nums: list[int]
        :type target: int
        :rtype: list[int]
        """

        length = len( nums )
        for i in range( length ):
            minus = target - nums[i]
            if minus in nums[0:i]:
                return [nums.index( minus ), i]
            subnums = nums[(i+1):length]
            if minus in subnums:
                return [i, i+1+subnums.index( minus )]


    def lengthOfLongestSubstring( self, s ):
        """
        :type s: str
        :type: int
        """

        length = len( s )
        compares = []
        for i in range( length - 1 ):
            j = i + 1
            while s[j] not in s[i:j]:
                if j == length - 1:
                    j = j + 1
                    break
                j = j + 1
            compares.append( j - i )
        maxindex = compares.index( max( compares ) )
        return s[maxindex:(maxindex+compares[maxindex])]

