from audioop import tostereo
import math
import datetime
from stat import ST_INO
from tracemalloc import start

def how_many_sec(m, s):
    total = m * 60 + s
    return total

# print(how_many_sec(42, 42))

def km_to_mi(km):
    result = km/1.61
    return result

# print(km_to_mi(10))

def average_speed(s, m, sec):
    t = how_many_sec(m, sec)
    s = s * 1000
    result = s / t
    return f"{result*2.236936} mph\n{result*3.6} kmh"

# print(average_speed(10, 42, 42))

def sphere_volume(r):
    volume = 4/3 * math.pi * r**3
    return volume

# print(sphere_volume(5))

def books_cost(copy, price, discount):
    price_fixed = price - ((price*discount)/100)
    result = price_fixed+3 + ((copy-1)*(price_fixed+0.75))
    return result

# print(books_cost(60, 24.95, 40))

def back_to_home(start_hour, start_minute):
    run_time = ((8*60+15)+3*(7*60+12)+(9*60+45)) / 60
    end_minute = start_minute + run_time - 60
    if 0 <= end_minute < 60:
        return f"{start_hour+1}:{int(end_minute)}"
    
# print(back_to_home(6, 52))

def back_to_home_enchanted(start_hour, start_minute):
    run_time = ((8*60+15)+3*(7*60+12)+(9*60+45)) / 60
    end_hour, end_minute = divmod(start_minute + run_time, 60)

    return f"Orario di arrivo: {int(end_hour + start_hour)}:{int(end_minute)}"

# print(back_to_home_enchanted(6, 52))

def somma_stringa(stringa):
    # s="85721"
    result = 0
    for numero in stringa:
        result += int(numero)
        
    return result

# print(somma_stringa("5321"))

def calcola_binario(stringa):
    result = 0
    stringa = stringa[::-1]
    
    for i in range(len(stringa)-1, -1, -1):
        result += int(stringa[i])*2**i
        
    return result

# print(calcola_binario("00101"))

def str_to_float(string):
    return float(string)

# print(str_to_float("42.52"))    

def floating_point_cubroot(n: str):
    if not n.count("^"):
        n += "^1"
    mantissa = abs(float(n.split("x")[0]))
    base, esp = int(n.split("x")[1].split("^")[0]), int(n.split("x")[1].split("^")[1])
    if n[0] == "-": 
        return -(mantissa*base**esp)**(1/3)
    
    return (mantissa*base**esp)**(1/3)
    
# print(floating_point_cubroot("-2.7x10"))

def floating_point_to_int(n):
    if not n.count("^"):
        n += "^1"
    mantissa = abs(float(n.split("x")[0]))
    base, esp = int(n.split("x")[1].split("^")[0]), int(n.split("x")[1].split("^")[1])
    if n[0] == "-": 
        return -int(mantissa*base**esp)
    
    return int(mantissa*base**esp)

def second_grade_equation(a, b, c):
    a, b, c = floating_point_to_int(a), floating_point_to_int(b), floating_point_to_int(c)
    delta = b**2 - 4*a*c
    
    if delta > 0:
        result = [(-b+math.sqrt(delta))/2*a, (-b-math.sqrt(delta))/2*a]
        return result
    if delta == 0:
        return -b/(2*a)
    if delta < 0 and a < 0:
        return "Vx€R"
    if delta < 0 and a > 0:
        return None

# print(second_grade_equation(25, -20, 4))

def five_num_sum(a, b, c, d, e):
    to_sum = [a, b, c, d, e]
    even = list(filter(lambda x: x if x % 2 == 0 else None, to_sum))
    odd = list(filter(lambda x: x if x not in even else None, to_sum))
    print(even, odd)
    
    return sum(even)-sum(odd)

# print(five_num_sum(1,2,3,4,5))

def vote_sum(a, b, c):
    votes_sanity = list(filter(lambda x: 1 if 0<=x<=30 else 0, [a,b,c]))
    if sum(votes_sanity) != 3:
        return -1
    return a+b+c

# print(vote_sum(10, 50, -1))

def valid_date(d, m, y):
    months_lenght = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    
    if y % 100 == 0:
        if y % 400 == 0:
            months_lenght[2] += 1
    elif y % 4 == 0:
        months_lenght[2] += 1
    
    if 0 < m < 13:
        if 0 < d <= months_lenght[int(m)]:
            return True
        
    return False

# print(valid_date(12, 2, 1891))

def strippa(string, to_strip):
    result = 0
    for i in string:
        if i in to_strip:
            result += 1
        else:
            break
    return result

def custom_strip(string, to_strip = " "):
    if len(to_strip):
        to_strip = list(to_strip)
        
    len_prefix = strippa(string, to_strip)
    len_suffix = strippa(string[::-1], to_strip)    
    
    return string[len_prefix:-len_suffix]

# print(custom_strip("   banana  "))

    