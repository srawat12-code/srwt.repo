def count_frequencies(list):
    freq_dict = {}
    for item in list:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict

my_list = [1,2,2,3,3,3, 'a', 'a', 'a', 'a']
print(count_frequencies(my_list))