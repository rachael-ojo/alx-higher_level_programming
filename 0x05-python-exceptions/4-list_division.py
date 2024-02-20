#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            try:
                num1 = my_list_1[i] if i < len(my_list_1) else 0
                num2 = my_list_2[i] if i < len(my_list_2) else 0

                if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
                    if num2 != 0:
                        result_list.append(num1 / num2)
                    else:
                        print("division by 0")
                        result_list.append(0)
                else:
                    print("wrong type")
                    result_list.append(0)
            except IndexError:
                print("out of range")
                result_list.append(0)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        return result_list
