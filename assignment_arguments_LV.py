# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
# part 1: greeting
def greet(name, template="Hello, <name>!"):
    return template.replace("<name>", name)


# part 2: force = mass * gravity
def force(mass, body="earth"):
    bodies = {"sun": 274, "jupiter": 24.94, "neptune": 11.15,
              "saturn": 10.44, "earth": 9.798, "uranus": 8.87,
              "venus": 8.87, "mars": 3.71, "mercury": 3.7,
              "moon": 1.62, "pluto": 0.58}
    for x, y in bodies.items():
        bodies[x] = round(y, 1)
    return mass*bodies[body]


# part 3: pull
def pull(m1, m2, d):
    return (6.674*10**-11)*((m1*m2)/((d)**2))
