def process_input(filename):
    # process input file
    with open(filename) as f:
        data = f.read().split('\n')
        return data

# expense_list is a list of strings of numbers
def solve(expense_list):
    int_expense_list = map(int, expense_list)
    int_expense_list.sort(reverse=True) # sort descending
    print int_expense_list
    smallest_entry = int_expense_list[-1]
    for entry in int_expense_list:
        closest_complement = 2020 - entry
        while closest_complement > smallest_entry:
            closest_complement -= 1
            if closest_complement >= smallest_entry and closest_complement in int_expense_list:
                first_complement = closest_complement
                second_complement = 2020 - entry - first_complement
                if second_complement in int_expense_list:
                    print('found: {0} + {1} + {2}'.format(entry, first_complement, second_complement))
                    return entry * first_complement * second_complement

def main(filename):
    print(solve(process_input(filename)))

if __name__ == '__main__':
  main('example.txt')
  main('input.txt')