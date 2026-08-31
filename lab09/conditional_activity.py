def should_I_go(is_drivable):
    #return 'Yes' if they said either yes or maybe
    #return 'No' if their answer was anything else
    if is_drivable == "yes" or "maybe":
        return "Yes"
    else:
        return "No"

    
if __name__ == "__main__":
    #ask name
    name = input("What is your name? ")
    
    #ask place
    place = input("What is the place? ")
    
    #ask drivable?
    is_drivable = input("Is it drivable? ")
    
    #call the function and store the returned value in the give variable 
    answer = should_I_go(is_drivable)
    
    print("Will I be able to goto", place, "with", name, "?")
    print(answer)
    