class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use hashmap - str encoding (instead of sorted chars) vs list of words that has that encoding

        encodingVsWords = defaultdict(list)

        # encoding - a list of 26 size. each index stores count of letters from a to z.

        for word in strs:
            encoding = [0] * 26
            for ch in word:
                encoding[ord('a') - ord(ch)] += 1

            encodingVsWords[tuple(encoding)].append(word)

        return list(encodingVsWords.values())