def speed():
    distance = float(input("what is the value of distance? "))
    time = float(input("what is the value of time? "))
    print("speed is", distance/time, "m/s")

def average_time():
    intial_time = float(input("what is the value of initial_time? "))
    final_time = float(input("whta is the value of final_time? "))
    constant = float(input("what is the value of constant?" ))
    print("average_time", intial_time+final_time/constant, "sec")

def mass():
    force = float(input("what is the value of force? "))
    acceleration = float(input("what is the value of acceleration? "))
    print("mass", force/acceleration, "kg")

def workdone():
    force = float(input("what is the value of force? "))
    distance = float(input("what is the value of distance? "))
    print("workdone", force*distance, "Joule")

def simple_interest():
    principal = float(input("what is the value of principal? "))
    rate_of_interest = float(input("what is the value of rate_of_interest? "))
    time_period = float(input("what is the value of time? "))
    print("simple_interest", principal*rate_of_interest* time_period)

welcome = int(input(
    "type 1 to calculate speed\n"
    "type 2 to calculate average time\n"
    "type 3 to calculate mass\n" 
    "type 4 to calculate workdone\n"
    "type 5 to calculate simple interest\n"
))

if welcome == 1:
    speed()
elif welcome == 2:
    average_time()
elif welcome == 3:
    mass()
elif welcome == 4:
    workdone()
elif welcome == 5:
    simple_interest()

else:
    print("wrong input, please try again")

welcome

