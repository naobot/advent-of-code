import copy
import re

bag_rules = {}

# process input file
with open('input.txt') as f:
    for line in f:
        # remove 'bag(s)' strings and final periods
        # number of bags also does not matter so remove those too
        clean_line = re.sub(r'(bags?|\.|[0-9])', '', line)
        bag_rule_key = re.split(r'contain ', clean_line)[0].strip()
        bag_rule_value = [bag.strip() for bag in re.split(r'contain ', clean_line)[1].split(',')]
        bag_rules[bag_rule_key] = bag_rule_value

# EXAMPLE BAG RULES
# bag_rules = {
#     'light red': ['bright white', 'muted yellow'],
#     'dark orange': ['bright white', 'muted yellow'],
#     'bright white': ['shiny gold'],
#     'muted yellow': ['shiny gold', 'faded blue'],
#     'shiny gold': ['dark olive', 'vibrant plum'],
#     'dark olive': ['faded blue', 'dotted black'],
#     'vibrant plum': ['faded blue', 'dotted black'],
#     'faded blue': [],
#     'dotted black': []
# }

bag_rules_to_check = copy.deepcopy(bag_rules)

# returns true if any item in list a is found in list b
def intersects(a, b):
    return len(set(a).intersection(set(b))) > 0

contains = []
cannot_contain = []

while len(bag_rules_to_check) > 0:
    for bag_colour in bag_rules.keys():
        if bag_colour in list(bag_rules_to_check.keys()):
            if 'shiny gold' in bag_rules[bag_colour] or intersects(contains, bag_rules[bag_colour]):
                contains.append(bag_colour)
                bag_rules_to_check.pop(bag_colour)
            elif not bag_rules[bag_colour]: # dead end
                cannot_contain.append(bag_colour)
                bag_rules_to_check.pop(bag_colour)
            elif not intersects(bag_rules_to_check.keys(), bag_rules[bag_colour]): # contains no unchecked colours
                cannot_contain.append(bag_colour)
                bag_rules_to_check.pop(bag_colour)

print(len(contains))
