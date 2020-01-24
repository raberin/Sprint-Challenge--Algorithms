'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # Base Case
    if len(word) < 2:
        return 0
    # Recursive Case
    # If found th, add 1 and recurse slicing 2 of the letters
    elif word[0] + word[1] == 'th':
        return count_th(word[2:]) + 1
    # If didnt found, recurse only slicing 1 character
    else:
        return count_th(word[1:])


print(count_th('thfeafdfadsthafddafth'))
