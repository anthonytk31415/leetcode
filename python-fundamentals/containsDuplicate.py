containsDuplicate


# def containsDuplicate(nums): 
    # container = set()
    # for x in nums: 
    #     if x not in container: 
    #         container.add(x)
    #     else: 
    #         return True
    # return False

def containsDuplicate(nums): 
    container =  {}
    for x in nums: 
        if x not in container: 
            container[x] = None
        else: 
            return True
    return False


# def containsDuplicate(nums): 
#     return len(nums) != len(set(nums))