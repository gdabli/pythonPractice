#You are given a string s. You can convert s to a palindrome by adding characters in front of it.
#Return the shortest palindrome you can find by performing this transformation.

def shorttestPalindrome(input_string):
    '''
    the logic to find shortest palindrome first find longest plaindrome in
    given string and then reverse the remaining string and append at the start of the string.
    '''
    # let say that longest palindrome is first element of the string
    longest_plaindrome = input_string[0]
    # get longest plaindrome in given string
    for i in range(len(input_string)):
        for j in range(i+1, len(input_string)):
            string = input_string[i:j]
            result = checkPlaindrome(string)
            if result == 0:
                if len(string) > len(longest_plaindrome):
                    longest_plaindrome = string
                    last_index = j
    #print('longest plaindrome is: ', longest_plaindrome)
    # now get the remaining string that is not palindrome
    str = input_string[last_index:]
    #print('remaining string: ', str)
    # now reverse the string
    str = str[::-1]
    print('shortest palindrome: ', str + input_string)

def checkPlaindrome(string):
    if string[:] == string[::-1]:
        return 0
    else:
        return -1

if __name__ == '__main__':
    input_string = "aacecaaab"
    shorttestPalindrome(input_string)