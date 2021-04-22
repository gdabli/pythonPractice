# this program find the longest substring without repeating characters in given string
# e.g. abcdabcdbb, abcabc, abcefghiefghi

def longestSubstring(input_string):
    maxlenght  = 1
    longest_substring = ''
    N = len(input_string)

    for i in range(N):
        for j in range(i, N):
            # check if first character matches
            if input_string[i] == input_string[j]:
                length = len(input_string[i:j])
                # check if input string and next one is equal 
                if input_string[i:j] == input_string[j:j+length]:
                    print('till now longest input string is: ', input_string[i:j])
                    print('its length is: ', len(input_string[i:j]))
                    if length > maxlenght:
                        maxlenght = length
                        longest_substring = input_string[i:j]
    print('longest substring is: ', longest_substring)
    print('string length: ', maxlenght)


if __name__ == '__main__':
    print('please type input string: ')
    input_string = input() 
    longestSubstring(input_string)
