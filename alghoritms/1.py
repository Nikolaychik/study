def insertion_sort(input_list):
    if type(input_list) != list:
        raise Exception("Got not valid argument type. List required.")

    position = 1
    for i in range(len(input_list) - 1):
        current_position = position
        current_element = input_list.pop(current_position)
        previous_elements_len = len(input_list[:position])

        for i in range(previous_elements_len):
            previous_element = input_list[current_position-1]

            if current_element <= previous_element:
                current_position -= 1

        input_list.insert(current_position, current_element)
        position += 1

    return input_list

print(insertion_sort([10,1231,13,13,4,4,213,555,7,5,5,5, 434, 3, 1,2]))
