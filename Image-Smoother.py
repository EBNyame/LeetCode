class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        columns = len(img[0])
        new  = [[0] * columns for _ in range(rows)]

        for r in range(len(img)):
            for c in range(len(img[0])):
                count = 0
                total = 0
                for a in (r, r + 1, r -1):
                    if a >= 0 and a < rows:
                        for b in (c, c + 1, c - 1):
                            if  b >= 0 and b < columns:
                                total += img[a][b]
                                count += 1
                average = total // count
                new[r][c] = average
        return new   