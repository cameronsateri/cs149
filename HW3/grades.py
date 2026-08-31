scores = []
lowest = 100
scores.append(int(input("score 1: ")))
scores.append(int(input("score 2: ")))
scores.append(int(input("score 3: ")))
scores.append(int(input("score 4: ")))
if lowest >= scores[0]:
    lowest = scores[0]
if lowest >= scores[1]:
    lowest = scores[1]
if lowest >= scores[2]:
    lowest = scores[2]
if lowest >= scores[3]:
    lowest = scores[3]
low = str(lowest) + "."
scores.remove(lowest)
av = sum(scores) / len(scores)
av = round(av, 2)
av = str(av) + "%."
finish = str(scores[0]) + ", " + str(scores[1]) + ", and " + str(scores[2]) + "."
print("\nThe final score for the course is ", av,
      " Dropped lowest score ", low,
      "\nThe remaining scores are ", finish, sep="")
