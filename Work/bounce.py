# bounce.py
#
# Exercise 1.5

height = 100.0 # meters

bounce = 1
while bounce < 11:
    height = height * 3/5
    print(bounce, round(height, 4))
    bounce = bounce + 1
    