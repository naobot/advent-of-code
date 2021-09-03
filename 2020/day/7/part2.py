import copy
import re

bag_rules = {}

# bag_string is a string like "2 pale blue"
# returns { 'pale blue' : 2 }
# returns None if contains no bags
def process_bag_num(bag_string):
    bag_colour = re.search(r'[a-z]+\s[a-z]+', bag_string).group(0)
    if re.search(r'[0-9]+', bag_string):
        bag_num = int(re.search(r'[0-9]+', bag_string).group(0))
        return { 'colour' : bag_colour, 'num' : bag_num }

def get_bag_num(current_bag):
    contains = bag_rules[current_bag]
    if contains:
        total_within = 0
        for bag in contains:
            bag_colour = bag['colour']
            total_within += (1 + get_bag_num(bag_colour)) * bag['num'] 
        return total_within
    else:
        return 0

# process input file
with open('input.txt') as f:
    for line in f:
        # remove 'bag(s)' strings and final periods
        clean_line = re.sub(r'(bags?|\.)', '', line)
        bag_rule_key = re.split(r'contain ', clean_line)[0].strip()
        bag_rule_list = [bag.strip() for bag in re.split(r'contain ', clean_line)[1].split(',')]
        bag_rules[bag_rule_key] = []
        for bag in bag_rule_list:
            if process_bag_num(bag):
                bag_rules[bag_rule_key].append(process_bag_num(bag))

print(get_bag_num('shiny gold'))

