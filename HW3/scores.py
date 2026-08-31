score_list = (10, 0, 5, 5, 15)
total = sum(score_list)
zeros = score_list.count(0)
average = round(total / len(score_list), 1)
last_score = score_list[-1]
print("Total points:", total)
print("Average points:", average)
print("Number of 0 point games:", zeros)
print("Last game score:", last_score)