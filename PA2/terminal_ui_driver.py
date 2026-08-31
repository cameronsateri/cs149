"""
PA2 Driver for terminal_ui testing.

Author: CS 149 Instructors
Version 08-01-2018, 10-28-22 
"""
import terminal_ui

if __name__ == '__main__':
    solutions = []
    print("Testing Terminal UI\n")
    solutions = ["tofutti", "magnetism", "edifice",
                 "grinder", "groundling", "thesaurus", "bull"]
    test_int = int(terminal_ui.prompt_for_int("Enter integer 1-12", 12))
    print("Your integer was ", str(test_int))
    test_string = terminal_ui.prompt_for_string("Enter string", 2)
    print("Your string was " + test_string)
    terminal_ui.prompt_n_display_hints(solutions[1])

