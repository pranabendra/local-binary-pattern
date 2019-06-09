def generate(window_size):
    def count_transition(num, window_size):
        d = ('{0:0'+str(window_size)+'b}').format(num)
        #print(d)
        b = num >> 1
        k = d[0] + ('{0:0'+str(window_size - 1)+'b}').format(b)
        #print(k)
        e = int(k,2)
        c = num ^ e
        #print(bin(c))
        return ('{0:0'+str(window_size)+'b}').format(c).count('1');

    count = 0
    ref = []
    for i in range(2**window_size):
        if count_transition(i, window_size) <= 2:
            count += 1
            ref.append(i)
            #print(i)
    #print(count)
    assert(count == len(ref))

    return count, ref;
