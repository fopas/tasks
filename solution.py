def make_expression(total, current_num, expression):
    if current_num == -1:
        if eval(expression) == total:
            print(expression)
        return
    make_expression(total, current_num - 1, expression + "+" + str(current_num))
    make_expression(total, current_num - 1, expression + "-" + str(current_num))
    make_expression(total, current_num - 1, expression + "" + str(current_num))


total = 200
make_expression(total, 8, "9")
