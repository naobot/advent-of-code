def process_input(filename):
    # process input file
    with open(filename) as f:
        data = f.read().split('\n')
        return data

# expense_list is a list of strings of numbers
def solve(expense_list):
    for entry in expense_list:
        complement = str(2020 - int(entry))
        if complement in expense_list:
            return int(entry) * int(complement)

def main(filename):
    print(solve(process_input(filename)))

if __name__ == '__main__':
  main('example.txt')
  main('input.txt')