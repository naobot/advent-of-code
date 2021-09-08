import re

def process_input(filename):
    # process input file
    with open(filename) as f:
        data = f.read().split('\n')
        return data

def solve(data):
    violations = []

    for entry in data:
        password = entry.split(':')[1].strip()
        letter = re.search(r'[a-z]+(?=:)', entry).group(0)
        letter_min = int(re.search(r'\d+(?=-)', entry).group(0))
        letter_max = int(re.search(r'(?<=-)\d+', entry).group(0))

        #import pdb; pdb.set_trace()

        found_letters = re.findall(letter, password)
        if len(found_letters) > letter_max or len(found_letters) < letter_min:
            violations.append(password)

    print(str(len(violations)) + ' violation(s) found')
    print(str(len(data) - len(violations)) + ' valid password(s)')

def main(filename):
    solve(process_input(filename))

if __name__ == '__main__':
  main('example.txt')
  main('input.txt')