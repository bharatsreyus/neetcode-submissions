class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            if s == '':
                s = '_EMPTY_'
            encoded = encoded + s + '#!#'
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        for word in s.split('#!#'):
            if word != '':
                if word == '_EMPTY_':
                    word = ''
                decoded.append(word)
        print(decoded)
        return decoded