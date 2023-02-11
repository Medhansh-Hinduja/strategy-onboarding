def find_min_index(arr):
    '''
    Find index where minimum value first occurs in array
    eg. [1, 33, 1, -2, 0] => 3
    eg. [0, 0, 0, 0, 0] => 0

    @param array of integers
    @returns integer index of minimum integer
    '''

    # insert code here
    minvalue = min(arr) # minimum value in the array

    # finding the first index whose value matches the min value and returning that index
    for i in range(len(arr)):
        if (arr[i] == minvalue):
            return i
            


def reverse_str_arr(string):
    '''
    Return array of string characters, but in reverse order
    eg. "abc" => ['c', 'b', 'a']
    eg. "abba" => ['a', 'b', 'b', 'a']
    eg. "!!-.2" => ['2', '.', '-', '!', '!']

    @param string
    @returns array of characters
    '''

    # insert code here

    arr = list(string) # convert the string to a list of characters
    arr.reverse() # reverse the list
    return arr