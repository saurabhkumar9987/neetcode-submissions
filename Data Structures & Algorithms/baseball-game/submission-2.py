class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stck = [] 
        for op in operations:
            if op == "+":
                stck.append(stck[-1] + stck[-2])
            elif op == "D":
                stck.append(2 * stck[-1])
            elif op == "C":
                stck.pop()
            else:
                stck.append(int(op))
        return sum(stck)


        