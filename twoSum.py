def twoSum(lst, target):

    dictionary = {i: lst[i] for i in range(len(lst))}

    values = list(dictionary.values())

    for key, item in dictionary.items():

        difference = target - item

        if difference in values and difference != item:
            idx = values.index(difference)
            print([key, idx])
            return [key, idx]

    print('No such avaliable')

if __name__ == '__main__':
    twoSum([3, 2, 1, 4, 5], -2)