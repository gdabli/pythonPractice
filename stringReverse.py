# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.

def reverseString(input_string):
    l = []
    s = ""
    l = input_string.split()
    # reverse the string
    l = [str for str in reversed(l)]
    # add one space after every value
    l = [str + " " for str in l]
    # create new string from reversed string
    s = s.join(l)
    # remove extra whitespaces
    s = s.strip()
    print(s)


if __name__ == '__main__':
    s = "  Bob    Loves  Alice   "
    print("input string is: ", s)
    reverseString(s)
