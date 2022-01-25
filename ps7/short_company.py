def short_company(C, P, n, k):
        '''
        Input:  C | Tuple of s = |C| strings representing names of companies
                P | Tuple of s lists each of size nk representing prices
                n | Number of days of price information
                k | Number of prices in one day
        Output: c | Name of a company with highest shorting value
                S | List containing a longest subsequence of 
                | decreasing prices from c that doesn't skip days
        '''
        
        S = []

        # For each company
        for i in range(len(C)):
                all_prices = P[i]
                memo = [None for _ in range(len(all_prices))]       # memoize (longest subseq length, child pointer) for each price
                
                # Top-down recursive checks into each price till the end
                def analyse_price(j):
                        if memo[j] == None:
                                f = min(j + (k - 1) - (j % k) + k, n*k - 1)
                                j_subseq_length, j_child = 1, None

                                for subseq_price_index in range(j + 1, f + 1):
                                        next_subseq_length, next_child = analyse_price(subseq_price_index)

                                        # If subsequent price is lower and has a longer subsequence length
                                        if (all_prices[j] > all_prices[subseq_price_index] ) and (next_subseq_length + 1 > j_subseq_length):
                                                j_subseq_length, j_child = next_subseq_length + 1, subseq_price_index

                                memo[j] = (j_subseq_length, j_child)
                        return memo[j]

                best_length, subseq_head = 0, 0
                # Fill memo for each price
                for j in range(len(all_prices)):
                        subseq_length, child = analyse_price(j)
                        if subseq_length > best_length:
                                best_length, subseq_head = subseq_length, j
                
                # If this company's length is longer than curr best, update
                if best_length > len(S):
                        c, S = C[i], []
                        while subseq_head != None:
                                S.append(all_prices[subseq_head])
                                subseq_length, subseq_head = analyse_price(subseq_head)

                
        S = tuple(S)
        return (c, S)