class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) != r*c or len(mat) == r and len(mat[0]) == c:
            return mat

        flat_list = []
        for i in mat:
            for j in i:
                flat_list.append(j)

        reshaped_list = []
        i = 0
        while r > 0:
            new_list = []
            for iter in range(c):
                new_list.append(flat_list[i])
                i += 1
            reshaped_list.append(new_list)
            r -= 1
        
        return reshaped_list


