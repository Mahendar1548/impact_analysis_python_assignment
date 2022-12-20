no_of_ways_to_attend_classes = 0
no_of_ways_to_absent_on_last_day = 0


def calculate_no_of_permutations_possible(abs_cons_flag_count, current_str_len, required_string_len):
    global no_of_ways_to_attend_classes
    global no_of_ways_to_absent_on_last_day

    if abs_cons_flag_count == 4:
        return

    if current_str_len == required_string_len:
        no_of_ways_to_attend_classes += 1
        if abs_cons_flag_count > 0:
            no_of_ways_to_absent_on_last_day += 1

        return

    calculate_no_of_permutations_possible(
        abs_cons_flag_count + 1, current_str_len + 1, required_string_len)
    calculate_no_of_permutations_possible(
        0, current_str_len + 1, required_string_len)


if __name__ == "__main__":
    n = int(input())
    calculate_no_of_permutations_possible(0, 0, n)
    print(f"{no_of_ways_to_absent_on_last_day}/{no_of_ways_to_attend_classes}")
