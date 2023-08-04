# Exercise 1.18
# Regular expression to swap string

import re

s = 'Today is 08-04-2023, I want to go to Mars in 08-04-2043.'
date_pattern = re.compile(r'\d+-\d+-\d+')
date_group_pattern = re.compile(r'(\d+)-(\d+)-(\d+)')

print(re.findall(date_pattern, s))

print('After changing format: ')
print(re.sub(date_group_pattern, r'\3-\1-\2', s))
