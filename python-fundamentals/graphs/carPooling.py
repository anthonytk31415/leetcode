# trips[i] = [numPassengers, from, to]


# keep the current capacity set; 
# if you reach the last i, return true
# nlogn

def carPooling(trips, capacity):

    tracker = []
    for passenger, trip_from, trip_to in trips: 
        tracker.append((passenger, trip_from))
        tracker.append((-passenger, trip_to))
    tracker.sort(key = lambda x: x[1])

    # print(tracker)
    cur_capacity = 0
    cur_location = None
    for p, trip in tracker: 
        if cur_location != trip: 
            cur_location = trip
            if cur_capacity > capacity: 
                return False
        cur_capacity += p
    return True

trips = [[2,1,5],[3,3,7]]
capacity = 4
# trips = [[2,1,5],[3,3,7]]
# capacity = 5

# trips = [[4,5,6],[6,4,7],[4,3,5],[2,3,5]]
# capacity = 13

print(carPooling(trips, capacity))