a_integer = ord('a')

def index(letter):
        return ord(letter) - a_integer

def count_anagram_substrings(T, S):
        '''
        Input:  T | String
                S | Tuple of strings S_i of equal length k < |T|
        Output: A | Tuple of integers a_i:
                | the anagram substring count of S_i in T
        '''
        string_length, substring_length = len(T), len(S[0])        
        table_map = {}
        curr_table = [0] * 26

        # Create frequency tables
        for i in range(string_length):

                # Index of current letter from main string
                curr_letter_index = index(T[i])

                # Removing previous letter if current substring range is more than length of S[i]
                if i >= substring_length:
                        before_first_letter_index = index(T[i-substring_length])
                        curr_table[before_first_letter_index] -= 1                

                # Adds 1 to current frequency table
                curr_table[curr_letter_index] += 1

                # Adding current freq table to table map
                curr_key = tuple(curr_table)
                if curr_key not in table_map:
                        table_map[curr_key] = 1
                else:
                        table_map[curr_key] += 1

        A = [0] * len(S)
        # Compare each Si with table map
        for i in range(len(S)):

                curr_substring = S[i]
                curr_table = [0] * 26
                for j in range(len(curr_substring)):
                        curr_letter_index = index(curr_substring[j])
                        curr_table[curr_letter_index] += 1
                        
                curr_key = tuple(curr_table)
                if curr_key in table_map:

                        A[i] += table_map[curr_key]

        return tuple(A)