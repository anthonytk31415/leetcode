from math import inf
def sampleStats(count):


    sample_min = inf
    sample_max = -inf
    max_freq = 0
    mode = None
    total_sum = 0
    total_count = sum(count)
    median_set = set()
    if total_count % 2 == 0: 
        median_set.add(total_count // 2)
        median_set.add(total_count // 2 +1)
    else: 
        median_set.add(total_count // 2 + 1)

    median_sum = 0

    total_count = 0
    for i, c in enumerate(count): 

        if c > 0: 
            for x in median_set: 
                if total_count + 1 <= x <= total_count + c: 
                    median_sum += i

            total_count += c
            total_sum += i*c 
            sample_min = min(sample_min, i) 
            sample_max = max(sample_max, i)
            
        if c > max_freq:   
            mode = i
            max_freq = c

    print(total_count)

    return [sample_min, sample_max, total_sum / total_count, median_sum/len(median_set), mode]

count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

print(sampleStats(count))