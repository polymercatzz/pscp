"TheFunctionWithin"
def fun_f(num_x):
    "cal fun f"
    result = 2*num_x
    return result
def fun_g(num_x):
    "cal fun g"
    result = (3*num_x**4)-(num_x**3)+(2*num_x**2)+10
    return result
def fun_h(num_x, num_y, num_z):
    "cal fun h"
    result = ((num_z+num_x)**2)-(num_x*num_y)+(num_y**2)
    return result
def fun_i(num_a, num_b, num_c, num_d):
    "cal fun i"
    result = (num_a**2+num_b**2-num_c**2)\
/((num_d**2)-(2*num_a*num_d)+(2*num_a))
    return result
def main():
    "main"
    num_a = float(input())
    num_b = float(input())
    num_c = float(input())
    num_d = float(input())
    result_1 = fun_f(fun_f(num_a))
    result_2 = fun_g(fun_f(num_a-num_b))
    result_3 = fun_h(fun_f(num_a+num_b), fun_f(num_a+num_c),\
fun_g(fun_f(num_d**2)))
    result_4 = fun_i(fun_h(fun_f(num_a+num_b), fun_f(num_a-num_c), \
fun_g(fun_f(num_d**2))), fun_g(fun_f(num_a-num_b)), \
fun_f(fun_f(fun_f(fun_f(fun_f(num_c))))), num_d**8)
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)
main()
