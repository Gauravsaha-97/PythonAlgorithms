class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for j in range(len(board)):
            for i in range(len(board[0])):
                if board[j][i]==word[0] and self.searchWord(board,j,i,0,word):
                    return True
        return False
    def searchWord(self, board,j,i,idx,word):
        if idx==len(word):
            return True
        if j<0 or j>=len(board) or i<0 or i>=len(board[j]) or board[j][i]!=word[idx]:
            return False
        
        tmp = board[j][i]
        board[j][i]=" "
        found = self.searchWord(board, j+1,i,idx+1,word) or self.searchWord(board, j-1,i,idx+1,word) or self.searchWord(board, j,i+1,idx+1,word) or self.searchWord(board, j,i-1,idx+1,word)
        board[j][i]= tmp
        return found