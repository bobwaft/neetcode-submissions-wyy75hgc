class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        combined = []
        columns = [[] for _ in range(9)]
        boxes = [[] for _ in range(9)]
        for row in board:
            rowCounter = Counter(row)
            rowCounter["."] = 0
            if (rowCounter.most_common(1)[0][1] > 1):
                return False
            combined.extend(row)
        i = 0
        j = 0
        for square in range(len(combined)):
            columns[square%9].append(combined[square])
            boxes[(i//3)*3+(j//3)].append(combined[square])
            j += 1
            if (j == 9):
                j = 0
                i += 1
        for column in columns:
            columnCounter = Counter(column)
            columnCounter["."] = 0
            if (columnCounter.most_common(1)[0][1] > 1):
                return False
        for box in boxes:
            boxCounter = Counter(box)
            boxCounter["."] = 0
            if (boxCounter.most_common(1)[0][1] > 1):
                return False
            print(box)
        return True
                            
            