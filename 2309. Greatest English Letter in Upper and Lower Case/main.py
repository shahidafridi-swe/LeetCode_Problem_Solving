class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        sSet = set(s)

        for i in range(25,-1,-1):
            # print(i, '<- i')
            # print(ord('a')+i)
            # print(chr(ord('a')+i), (chr(ord('A')+i)))

            if (chr(ord('a')+i) in sSet) and (chr(ord('A')+i) in sSet):
                # print(chr(ord('a')+i), (chr(ord('A')+i)))
                return chr(ord('A')+i)
        return ''