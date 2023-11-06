# O(n)
# Space: 

def averageWaitingTime(customers):
    end_time = 0
    sum_wait_time = 0
    for cust in customers: 
        arr, time_needed = cust
        start_time = max(end_time, arr)
        end_time = start_time + time_needed
        sum_wait_time += (end_time - arr)

    return sum_wait_time/len(customers)
