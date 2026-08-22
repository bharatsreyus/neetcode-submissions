# [
#     ["1","2",".",".","3",".",".",".","."],
#     ["4",".",".","5",".",".",".",".","."],
#     [".","9","1",".",".",".",".",".","3"],
#     ["5",".",".",".","6",".",".",".","4"],
#     [".",".",".","8",".","3",".",".","5"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".",".",".",".",".",".","2",".","."],
#     [".",".",".","4","1","9",".",".","8"],
#     [".",".",".",".","8",".",".","7","9"]
# ]
class Solution:

    def isUnique(self, arr: List[str]):
        
        numberArr = [x for x in arr if x != '.']
        uniqueCount = len(set(numberArr))
        
        if len(numberArr) != uniqueCount:
            return False
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:

        window1,window2, window3 = [],[],[]
        window4,window5, window6 = [],[],[]
        window7,window8, window9 = [],[],[]
        rowHashTable = defaultdict(list)
        colHashTable = defaultdict(list)
        for i in range(9):
            rowHashTable[i] = board[i]
            
            for j in range(3):
                colHashTable[j].append(board[i][j])
                if i < 3:
                    window1.append(board[i][j])
                elif i < 6:
                    window4.append(board[i][j])
                else:
                    window7.append(board[i][j])

            for j in range(3,6):
                colHashTable[j].append(board[i][j])
                if i < 3:
                    window2.append(board[i][j])
                elif i < 6:
                    window5.append(board[i][j])
                else:
                    window8.append(board[i][j])

            for j in range(6,9):
                colHashTable[j].append(board[i][j])
                if i < 3:
                    window3.append(board[i][j])
                elif i < 6:
                    window6.append(board[i][j])
                else:
                    window9.append(board[i][j])

        for i in range(9):
            if not self.isUnique(rowHashTable[i]):
                return False
            if not self.isUnique(colHashTable[i]):
                return False
        if not self.isUnique([item for sublist in window1 for item in sublist]):
            return False
        if not self.isUnique([item for sublist in window2 for item in sublist]):
            return False
        if not self.isUnique([item for sublist in window3 for item in sublist]):
            return False
        if not self.isUnique([item for sublist in window4 for item in sublist]):
            return False
        if not self.isUnique([item for sublist in window5 for item in sublist]):
            return False
        if not self.isUnique([item for sublist in window6 for item in sublist]):
            return False
        if not self.isUnique([item for sublist in window7 for item in sublist]):
            return False
        if not self.isUnique([item for sublist in window8 for item in sublist]):
            return False
        if not self.isUnique([item for sublist in window9 for item in sublist]):
            return False
            
        return True

