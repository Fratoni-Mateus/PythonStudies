# def count_substring(string, substring):
#     index = 0
#     total = 0
#     while index < len(string):
#         if string[index:index+len(substring)] == substring:
#             total += 1
#         index += 1
#     return total

def count_substring(string, target):
    total = 0
    index = 0
    while index < len(string):
        if string[index : index + len(target)] == target:
            total += 1
            index += len(target)   # <- This is the key line
        else:
            index += 1
    return total

def locate_first(string, target):
    total = 0
    index = 0
    pos = 0
    while index < len(string):
        if string[index : index + len(target)] == target:
            total += 1
            pos = index
            index += len(target)
        else:
            index += 1
    if total == 0:
        pos = -1
    return pos

# def locate_first(string, sub):
#     index = 0
#     while index < len(string):
#         if string[index : index + len(sub)] == sub:
#             return index
#         else:
#             index += 1
#     return -1

# Here are a couple function calls to test with.

# This one should return 1
print(locate_first('cookbook', 'ook'))

# This one should return -1
print(locate_first('all your bass are belong to us', 'base'))
# Here's a call you can test it with. This should print 4:
print(count_substring('love, love, love, all you need is love', 'love'))

print(count_substring('AAAA', 'AA'))
