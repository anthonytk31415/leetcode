from math import inf
def taskSchedulerII(tasks, space):
    i, curDay, tracker = 0, 1, {}
    while i < len(tasks):
        task = tasks[i]
        if task in tracker and curDay < tracker[task]: curDay = tracker[task]
        tracker[task] = curDay + space + 1
        i += 1
        if i < len(tasks): curDay += 1
    return curDay



tasks = [1,2,1,2,3,1]
space = 3
# tasks = [5,8,8,5]
# space = 2


# space = 100000

print(taskSchedulerII(tasks, space))
