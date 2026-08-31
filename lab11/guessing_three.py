import random
secret_num = random.randint(1, 100)
my_num = 0
trial_count = 0
while secret_num != my_num and trial_count != 3:
    my_num = input("Guess a number: ")
    if my_num == secret_num:
        print("\nYou guess it right!"
              "The number I was thinking of is: ", secret_num)
    trial_count += 1    #trial_count = trial_coun + 1.
if trial_count == 3:
    print("Your 3 trials are over!")
x = 0
while x < 5:
    print("Fall Break -> almost there (*--*)")
    x = x + 1