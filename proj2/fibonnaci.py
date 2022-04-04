from math import ceil


class Fibonnaci:
    def __init__(self):
        self.num_terms = 15
        self.golden_constant = (1 + 5**0.5)/2
        self.answers = [0 for x in range(20)]

    def solve_recursively(self, num):
        if (num == 0 or num == 1):
            self.answers[num] = num
            return num
        answer = self.solve_recursively(num-2) + self.solve_recursively(num-1)
        self.answers[num] = answer
        return answer

    def get_answers(self):
        return self.answers

    def calculate_fibonnaci(self, num):
        return ((1 + 5**0.5)**num - (1 - 5**0.5)**num)/(2**num*5**0.5)

    def get_input(self):
        a = ""
        while (not isinstance(a, int)):
            try:
                a = int(input("Enter a positive integer: "))
            except:
                continue
        return a

    def solve_fib_from_prev_num(self):
        p = self.get_input()
        n = self.get_input()
        fp = self.calculate_fibonnaci(p)
        fn = fp*((1+5**0.5)/2)**(n-p)
        print(fn)
    
    def solve_fib_n_plus_1(self, num):
        prev = self.calculate_fibonnaci(num-1)
        return prev*(1+5**0.5)/2

    def get_ratio(self, num):
        print('The golden ratio is: ' + str(self.golden_constant))
        return (self.calculate_fibonnaci(num)/self.calculate_fibonnaci(num-1))



def main():
    p = Fibonnaci()
    print(f'The 15th term is exactly {p.solve_recursively(14)}')

    p.solve_fib_from_prev_num()
    print('\n')

    print(f'The 15th term is approximately {p.solve_fib_n_plus_1(14)}')
    print('\n')

    p.solve_recursively(19)
    print(f'The first 20 (n=0 to n=19) terms are {p.get_answers()}')
    print('\n')

    print(f'The ratio of the n=2 and n=3 term is: {p.get_ratio(3)}')
    print(f'The ratio of the n=29 and n=30 term is: {p.get_ratio(30)}')

if __name__ == '__main__':
    main()