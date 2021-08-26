
def group_missing_elements(input_list):
    from itertools import groupby
    from operator import itemgetter

    ranges = []

    for k, g in groupby(enumerate(input_list), lambda x: x[0] - x[1]):
        group = (map(itemgetter(1), g))
        group = list(map(int, group))
        if group[0] == group[-1]:
            ranges.append(str(group[0]))
        else:
            ranges.append(f"{group[0]}->{group[-1]}")
    return ranges

def get_missing_elements(input_list, lower, upper):
    all_list = [i for i in range(lower,upper+1)]
    difference = sorted(list(set(all_list)-set(input_list)))
    return difference


if __name__ == "__main__":
    # assuming only integer will be given     
    input_string = input("Enter a list element separated by space ")
    lower = int(input("Enter lower limit "))
    upper = int(input("Enter upper limit "))
    input_list = [int(i) for i in input_string.split()]
    output = get_missing_elements(input_list, lower, upper)
    print(group_missing_elements(output))
