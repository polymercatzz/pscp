"""[Midterm 2023] Niwarn World"""
import math
def num_x(num_n):
    """cal x"""
    return 2+(math.log2(num_n**2)/(2*num_n*math.log2(num_n)))

def num_y(num_n, num_s):
    """cal y"""
    return (math.sin(math.radians(30))+(2*num_s)**0.5)/(num_x(num_n)+3)

def num_z(num_k):
    """cal z"""
    return num_y(num_k, num_k)**2+((8456*num_x(num_k)**4)/(24*num_k))

def main(num_n, num_s, num_k):
    """[Midterm 2023] Niwarn World"""
    result_x = num_x(num_n)
    result_y = num_y(num_n, num_s)
    result_z = num_z(num_k)
    print("X: %.1f, Y: %.1f, Z: %.1f"%(result_x, result_y, result_z))

main(float(input()), float(input()), float(input()))
