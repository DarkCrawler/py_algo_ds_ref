'''
Core logic for Binary Seach is simple
Its based on dividing a sorted array based on < > of search value
The non recursive method uses a while loop
'''


def binary_search(num_to_search):
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 22, 33, 44, 55, 66, 77, 88, 99, 111, 234, 345, 456]
    # binary_search_using_for_loop(num_list, num_to_search)
    binary_search_using_recursion(0, len(num_list) - 1, num_list, 55)


def binary_search_using_for_loop(num_list, num_to_search):
    low = 0
    high = len(num_list) - 1

    success_index = -1
    while (low <= high):
        mid = round((high + low) / 2)
        print(mid, '--', num_list[mid], '---', low, '---', high)
        if num_to_search == num_list[mid]:
            success_index = mid
            break

        elif num_to_search > num_list[mid]:
            low = mid + 1

        else:
            high = mid - 1

    if success_index != -1:
        print(f'number found aat index :: {mid}')


def binary_search_using_recursion(low, high, arr, search_num):
    mid = (high + low) // 2
    if (low >= high):
        print('Number not present')
        return

    elif search_num == arr[mid]:
        print(f'Number found at index :: {mid}')

    elif search_num > arr[mid]:
        binary_search_using_recursion(low=mid + 1, high=high, arr=arr, search_num=search_num)

    else:
        binary_search_using_recursion(low=low, high=mid - 1, arr=arr, search_num=search_num)


if __name__ == "__main__":
    binary_search(55)
