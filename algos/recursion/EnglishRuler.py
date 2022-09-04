'''
Basic algo:
 interval logic:
 to print any interval mark recursively :

 get_interval (L-1)
 print L
 get interval (L-1)

 Till L is 0

 '''


def draw_scale(tick_number, tick_label=''):
    # tick number denotes tick to be printed
    # tick_lable denotes the major numbering of inches

    str_to_print = '-' * tick_number  # number of time a tick has to be printed
    if tick_label:
        str_to_print += ' ' + tick_label

    print(str_to_print)


def print_english_ruler(major_tick_length, inches_of_ruler):
    draw_scale(major_tick_length, '0')  # draw first label of 0 with major tick length
    for i in range(1, inches_of_ruler + 1):
        draw_intervals(major_tick_length - 1)
        draw_scale(major_tick_length, str(i))


def draw_intervals(tick_length):
    if tick_length > 0:
        draw_intervals(tick_length - 1)
        draw_scale(tick_length)
        draw_intervals((tick_length - 1))


if __name__ == "__main__":
    print_english_ruler(major_tick_length=5, inches_of_ruler=5)
