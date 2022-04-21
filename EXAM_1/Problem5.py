# Author: Anna Mikhailova
# Date: 09/30/21
# Purpose: Define a function cs1_asterisk_prefix that takes a positive integer n
# as a parameter and prints n lines of text where each line has some number of asterisks (*)
# followed by “cs1”. The number of asterisks in each line should be as follows:
# 1. The first line should have one asterisk before the string “cs1”. So the first line should
# be “*cs1”.
# 2. In every subsequent line that number of asterisks preceding “cs1” should increase by
# one. So the second line should be “**cs1”, third line should be “***cs1” and the
# pattern continues for the subsequent lines of text.

# Purpose: this function prints out n lines of text where the i-th line has i asterisks followed by "cs1".
# Parameters: this function takes a positive integer n that specifies how many lines to print
def cs1_asterisk_prefix(n):
    string = "cs1"
    line = 1
    while line <= n:
        string = "*" + string
        print(string)
        line += 1

line_count = int(input("How many lines would you like to print?"))
cs1_asterisk_prefix(line_count)