# As input data, you have a list of strings.

# Write a method double_string() for counting the number of strings from the list, 
# represented in the form of the concatenation of two strings from this arguments  list

def double_string(data):
    count = 0
    for i in range(len(data)):
        for j in range(len(data)):
            if i != j and data[i] + data[j] in data[i] * 2:
                count += 1
    return count
