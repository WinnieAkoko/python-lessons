train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# fh to celcius
def f_to_c(f_temp):
    c_temp = f_temp - 32 * 5 / 9
    return c_temp


f100_in_celcius = f_to_c(100)
print(f100_in_celcius)


# Celsius to Fh
def c_to_f(c_temp):
    f_temp = c_temp * (9 / 5) + 32
    return f_temp


co_in_fehrenheit = c_to_f(0)
print(co_in_fehrenheit)


# using force
def get_force(mass, acceleration):
    return mass * acceleration


train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies" + " " + str(train_force) + "Newtons of force" + ".")

# New formula
c = 3 * 10 ** 8


def get_energy(mass, c):
    return mass * c ** 2


bomb_energy = (get_energy(bomb_mass, c))
print("A 1kg bomb supplies" + "  " + str(bomb_energy) + " " + "energy")


# Do the work function
def get_work(mass, acceleration, distance):
    work = get_force(mass, acceleration) * distance
    return work


train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does" + str(train_work) + "of work over" + str(train_distance) + "meters")

