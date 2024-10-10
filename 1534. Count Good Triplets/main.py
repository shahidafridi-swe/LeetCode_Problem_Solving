class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        n = len(arr)
        result = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    # print(arr[i], arr[j], arr[k])
                    if abs(arr[i]-arr[j]) <= a and abs(arr[j]-arr[k])<= b and abs(arr[i]-arr[k]) <= c:
                        # print('>>',arr[i], arr[j], arr[k])
                        result +=1
        #         print('k end')
        #     print('j end')
        # print('i end')
        
        return result