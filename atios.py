# this function is implementation of myAtoi(string s) function, which converts a string to a 32-bit signed integer

def atios(input_str):
    # N is length of the string
    N = len(input_str)
    temp = []
    if N > 0 and N < 200:
        # check if first elemenet is alphbet then return 0
        if input_str[0].isalpha():
            input_str = 0
            return(input_str)
        # check if input string contains negative number.
        else:
            if input_str[0] == '-':
                temp.append(input_str[0])
            for i in range(N):
                if input_str[i].isdigit():
                    temp.append(input_str[i])
            str = "".join(temp)
            string = int(str)
            if  string > (pow(2, 31) -1):
                return (pow(2, 31) -1)
            elif string < (pow(-2, 31)):
                return (pow(-2, 31))
            else:
                return string
    else:
        print('length of string does not match the required criteria')


if __name__ == '__main__':
    input_str = input().strip()
    output = atios(input_str)
    print(output)