def print_reques(item_dict, left_width, right_width):
    for k, v in item_dict.items():
        # print(k.ljust(leftWidth, ' ') + str(v).rjust(rightWidth))
        print(k.ljust(left_width, ' ') + str(v).ljust(left_width))