def if_your_happy(phrase):
    return f"If you're happy and you know it, {phrase}\n" 


def show_it():
    return if_your_happy("and you really want to show it")


def verse(phrase):
    ret = if_your_happy(phrase) * 2
    ret = ret + show_it() + if_your_happy(phrase)
    return ret


print(verse("clap your hands"))
print(verse("slap your knees"))
print(verse("turn around"))
print(verse("pat your head"))
print(verse("do all four"))
