def merge_bookings(B1, B2):
    Bcombined, curr_time = [], 0
    B1_len, B2_len = len(B1), len(B2)
    B1_index, B2_index = 0, 0

    while B1_len + B2_len > B1_index + B2_index:
        # Setting values
        if B1_index < B1_len:
            k1, s1, t1 = B1[B1_index]
        if B2_index < B2_len:
            k2, s2, t2 = B2[B2_index]

        # B1 done
        if B1_index == B1_len:
            k, s, curr_time = k2, max(s2, curr_time), t2
            B2_index += 1
        # B2 done
        elif B2_index == B2_len:
            k, s, curr_time = k1, max(s1, curr_time), t1
            B1_index += 1
        else:
            if curr_time <= min(s1, s2):
                curr_time = min(s1, s2)
            if t1 <= s2:
                k, s, curr_time = k1, curr_time, t1
                B1_index += 1
            elif t2 <= s1:
                k, s, curr_time = k2, curr_time, t2
                B2_index += 1
            elif curr_time < s2:
                k, s, curr_time = k1, curr_time, s2
            elif curr_time < s1:
                k, s, curr_time = k2, curr_time, s1
            else: 
                k, s, curr_time = k1 + k2, curr_time, min(t1, t2)
                if curr_time == t1:
                    B1_index += 1
                if curr_time == t2:
                    B2_index += 1
        Bcombined.append((k, s, curr_time))
    
    Bfinal = [Bcombined[0]]
    # Removing adjacent with same k 
    for k1, s1, t1 in Bcombined[1:]:
        k2, s2, t2 = Bfinal[-1]
        if k1 == k2 and s1 == t2:
            Bfinal.pop()
            Bfinal.append((k1, s2, t1))
        else:
            Bfinal.append((k1, s1, t1))    

    return Bfinal

def satisfying_booking(R):
    '''
    Input:  R | Tuple of |R| talk request tuples (s, t)
    Output: B | Tuple of room booking triples (k, s, t)
              | that is the booking schedule that satisfies R
    '''
    if len(R) == 1:
        s, t = R[0]
        return ((1, s, t),)
    mid = len(R) // 2
    R1, R2 = R[:mid], R[mid:]
    B1 = satisfying_booking(R1)
    B2 = satisfying_booking(R2)
    B = merge_bookings(B1, B2)
    return tuple(B)
