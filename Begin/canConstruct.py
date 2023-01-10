class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        i = 0
        while i < len(ransomNote):
            j = 0
            while j < len(magazine):
                if ransomNote[i] == magazine[j]:
                    ransomNote = "".join([ransomNote[:i], ransomNote[i + 1 :]])
                    magazine = "".join([magazine[:j], magazine[j + 1 :]])
                    i -= 1
                    break
                j += 1
            i += 1
        if ransomNote == "":
            return True
        else:
            return False
