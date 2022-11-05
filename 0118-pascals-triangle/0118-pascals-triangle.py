class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        new_list = []

        for i in range(numRows):
            temp = []
            for j in range(0,i+1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(new_list[i-1][j-1] + new_list[i-1][j])
            new_list.append(temp)
        
        return new_list