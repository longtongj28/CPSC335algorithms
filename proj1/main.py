from math import ceil


class Problem:
    def __init__(self):
        self.num_nodes = int(input("Enter how many pairs of nodes: "))
        self.node_list = self.produce_nodes()

    def produce_nodes(self):
        res = []
        for i in range(self.num_nodes):
            res.append('O')
            res.append('X')
        return res
    
    def print_organized(self):
        if (self.num_nodes <= 0): return
        indices = ''
        res = ''
        for i in range(len(self.node_list)):
            indices = indices + str(i) + ' '
            res = res + self.node_list[i] + ' '
        print(indices.strip())
        print(res.strip())
        print('')

    def solve(self): return self.swap_disks()

    def swap_disks(self):
        n = self.num_nodes
        s = self.node_list
        if (n <= 0 or len(s) == 0):
            print('Enter a number greater than 0!')
            return

        swaps = 0
        for j in range(ceil(n/2)):
            print('iteration: ' + str(j+1))
            i = 0
            while i < len(s):
                if (s[i] == 'O' and s[i+1] == 'X'):
                    s[i+1], s[i] = s[i], s[i+1]
                    swaps += 1
                    self.print_organized()
                i += 2
            k = len(s) - 2
            while k > 0:
                if s[k] == 'X' and s[k-1] == 'O':
                    s[k-1], s[k] = s[k], s[k-1]
                    swaps += 1
                    self.print_organized()
                k -= 2
        print("Final: ")
        print(f'After {swaps} swaps.')
        self.print_organized()

        return self.node_list, swaps

def main():
    p = Problem()

    print('\nOriginal input: ')
    p.print_organized()

    answer = p.solve()
    print(answer)

if __name__ == '__main__':
    main()