# given string = abba

def longestPlaindrome(input_string):
    n = len(input_string)
    maximux = 1
    biggest_plaindrome = ''

    for i in range(n):
        for j in range(i,n):
            status = checkPalindrome(input_string[i:j+1])
            if status == 0:
                length_of_string = len(input_string[i:j+1])
                if length_of_string > maximux:
                    maximux = length_of_string
                    biggest_plaindrome = input_string[i:j+1]
                    #print('current biggest palindrome is: ', biggest_plaindrome)
    print('longest string is: ', biggest_plaindrome)
    print('length of longest string is: ', maximux)

# return 0 status shows that input string in palindrome. 1 is not
def checkPalindrome(string):
    if string[:] == string[::-1]:
        return 0
    else:
        return 1

if __name__ == '__main__':
    print('Enter the string: ')
    input_string = input()
    longestPlaindrome(input_string)