class LargestSumSubarray:
    def __init__(self):
        self.v = []
        self.inputs = [(10, 2, -5, 1, 9, 0, -4, 2, -2),
                       (-7, 1, 8, 2, -3, 1),
                       (9, 7, 2, 16, -22, 11),
                       (6,1, 9, -33, 7, 2, 9, 1, -3, 8, -2, 9, 12, -4)]

    def sum(self, v):
        n = len(v)
        answer = 0
        for i in range(n):
            answer = answer + v[i]
        return answer

    def solve_all(self):
        for arr in self.inputs:
            self.solve(arr)

    def solve(self,v):
        self.v = v
        n=len(v)
        b,e = 0,1 
        for i in range(n-1): 
            for j in range(n): 
                if self.sum(v[i:j]) > self.sum(v[b:e]): 
                    b, e = i, j
        self.print_subarray((b,e))
        return (b, e)

    def print_subarray(self, indices):
        print(self.v[indices[0]:indices[1]])

def main():
    p2 = LargestSumSubarray()
    p2.solve([-3, -5, 5, -1, -3, 1, 5, -6])
    p2.solve_all()

if __name__ == '__main__':
    main()