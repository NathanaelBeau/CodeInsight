def test(x: list) -> list:
    max_sum = float('-inf')
    result_list = []
    for sub_list in x:
        current_sum = sum(sub_list)
        if current_sum > max_sum:
            max_sum = current_sum
            result_list = sub_list
    return result_list