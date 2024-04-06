def sum_then_print(message, *numbers, suffix_message):
    total = 0
    for n in numbers:
        total = total + n
    print(f"{message} {total} {suffix_message}")

sum_then_print("total nilai:", 2, 3, 4, 5, 4, suffix_message="selesai!")

def print_data(*params):
    print(f"type: {type(params)}, data: {params}")
    for i in range(len(params)):
        print(f"param {i}: {params[i]}")

print_data("hello python", 123, [5, True, ("yesn't")], {"iwak", "peyek"})