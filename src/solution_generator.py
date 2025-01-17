import random

def generate_solution_ascending(num_cities):
    """ Generate an initial solution by ascending index. """
    return list(range(num_cities))

def generate_solution_random(num_cities):
    """ Generate an initial solution by randomly selecting cities. """
    solution = list(range(num_cities))
    random.shuffle(solution)
    return solution

def generate_solution_greedy(distance_matrix):
    """ Generate an initial solution using a greedy approach. """
    num_cities = len(distance_matrix)
    unvisited = set(range(1, num_cities))
    solution = [0]  # Start from city 0

    while unvisited:
        current_city = solution[-1]
        # Find the closest unvisited city
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        solution.append(next_city)
        unvisited.remove(next_city)
    
    return solution


# half and half
def mix_solution_ascending_random(num_cities):
    """ Generate a mixed solution using ascending and random (split by half). """
    solution = [None] * num_cities
    visited = set()

    # front half in ascending order
    half = num_cities // 2
    for i in range(half):
        solution[i] = i
        visited.add(i)

    # back half in random order (excluding visited cities)
    unvisited = [city for city in range(num_cities) if city not in visited]
    random.shuffle(unvisited)
    for i in range(half, num_cities):
        solution[i] = unvisited.pop()

    return solution

def mix_solution_ascending_greedy(distance_matrix):
    """ Generate a mixed solution using ascending and greedy (split by half). """
    num_cities = len(distance_matrix)
    solution = [None] * num_cities
    visited = set()

    # front half in ascending order
    half = num_cities // 2
    for i in range(half):
        solution[i] = i
        visited.add(i)

    # back half in greedy order (excluding visited cities)
    current_city = half - 1
    for i in range(half, num_cities):
        unvisited = [city for city in range(num_cities) if city not in visited]
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        solution[i] = next_city
        visited.add(next_city)
        current_city = next_city

    return solution

def mix_solution_random_ascending(num_cities):
    """ Generate a mixed solution using random and ascending (split by half). """
    solution = [None] * num_cities
    visited = set()

    # front half in random order
    half = num_cities // 2
    unvisited = list(range(num_cities))
    random.shuffle(unvisited)
    for i in range(half):
        city = unvisited.pop()
        solution[i] = city
        visited.add(city)

    # back half in ascending order (excluding visited cities)
    for i in range(half, num_cities):
        city = min([c for c in range(num_cities) if c not in visited])
        solution[i] = city
        visited.add(city)

    return solution

def mix_solution_random_greedy(num_cities, distance_matrix):
    """ Generate a mixed solution using random and greedy (split by half). """
    solution = [None] * num_cities
    visited = set()

    # front half in random order
    half = num_cities // 2
    unvisited = list(range(num_cities))
    random.shuffle(unvisited)
    for i in range(half):
        city = unvisited.pop()
        solution[i] = city
        visited.add(city)

    # back half in greedy order (excluding visited cities)
    current_city = solution[half - 1]
    for i in range(half, num_cities):
        unvisited = [city for city in range(num_cities) if city not in visited]
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        solution[i] = next_city
        visited.add(next_city)
        current_city = next_city

    return solution

def mix_solution_greedy_ascending(distance_matrix):
    """ Generate a mixed solution using greedy and ascending (split by half). """
    num_cities = len(distance_matrix)
    solution = [None] * num_cities
    visited = set()

    # front half in greedy order
    current_city = 0
    for i in range(num_cities // 2):
        unvisited = [city for city in range(num_cities) if city not in visited]
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        solution[i] = next_city
        visited.add(next_city)
        current_city = next_city

    # back half in ascending order (excluding visited cities)
    for i in range(num_cities // 2, num_cities):
        city = min([c for c in range(num_cities) if c not in visited])
        solution[i] = city
        visited.add(city)

    return solution

def mix_solution_greedy_random(num_cities, distance_matrix):
    """ Generate a mixed solution using greedy and random (split by half). """
    solution = [None] * num_cities
    visited = set()

    # front half in greedy order
    current_city = 0
    for i in range(num_cities // 2):
        unvisited = [city for city in range(num_cities) if city not in visited]
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        solution[i] = next_city
        visited.add(next_city)
        current_city = next_city

    # back half in random order (excluding visited cities)
    unvisited = [city for city in range(num_cities) if city not in visited]
    random.shuffle(unvisited)
    for i in range(num_cities // 2, num_cities):
        solution[i] = unvisited.pop()

    return solution

def mix_solution_ascending_random_greedy(num_cities, distance_matrix):
    """ Generate a mixed solution using ascending, random, and greedy (split by thirds). """
    solution = [None] * num_cities
    visited = set()

    # first 1/3 in ascending order
    third = num_cities // 3
    for i in range(third):
        solution[i] = i
        visited.add(i)

    # second 1/3 in random order (excluding visited cities)
    unvisited = [city for city in range(num_cities) if city not in visited]
    random.shuffle(unvisited)
    for i in range(third, 2 * third):
        solution[i] = unvisited.pop()
        visited.add(solution[i])

    # last 1/3 in greedy order (excluding visited cities)
    current_city = solution[2 * third - 1]
    for i in range(2 * third, num_cities):
        unvisited = [city for city in range(num_cities) if city not in visited]
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        solution[i] = next_city
        visited.add(next_city)
        current_city = next_city

    return solution

def mix_solution_ascending_greedy_random(num_cities, distance_matrix):
    """ Generate a mixed solution using ascending, greedy, and random (split by thirds). """
    solution = [None] * num_cities
    visited = set()

    # first 1/3 in ascending order
    third = num_cities // 3
    for i in range(third):
        solution[i] = i
        visited.add(i)

    # second 1/3 in greedy order (excluding visited cities)
    current_city = solution[third - 1]
    for i in range(third, 2 * third):
        unvisited = [city for city in range(num_cities) if city not in visited]
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        solution[i] = next_city
        visited.add(next_city)
        current_city = next_city

    # last 1/3 in random order (excluding visited cities)
    unvisited = [city for city in range(num_cities) if city not in visited]
    random.shuffle(unvisited)
    for i in range(2 * third, num_cities):
        solution[i] = unvisited.pop()

    return solution

def mix_solution_random_ascending_greedy(num_cities, distance_matrix):
    """ Generate a mixed solution using random, ascending, and greedy (split by thirds). """
    solution = [None] * num_cities
    visited = set()

    # first 1/3 in random order
    third = num_cities // 3
    unvisited = list(range(num_cities))
    random.shuffle(unvisited)
    for i in range(third):
        city = unvisited.pop()
        solution[i] = city
        visited.add(city)

    # second 1/3 in ascending order (excluding visited cities)
    for i in range(third, 2 * third):
        city = min([c for c in range(num_cities) if c not in visited])
        solution[i] = city
        visited.add(city)

    # last 1/3 in greedy order (excluding visited cities)
    current_city = solution[2 * third - 1]
    for i in range(2 * third, num_cities):
        unvisited = [city for city in range(num_cities) if city not in visited]
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        solution[i] = next_city
        visited.add(next_city)
        current_city = next_city

    return solution

def mix_solution_random_greedy_ascending(num_cities, distance_matrix):
    """ Generate a mixed solution using random, greedy, and ascending (split by thirds). """
    solution = [None] * num_cities
    visited = set()

    # first 1/3 in random order
    third = num_cities // 3
    unvisited = list(range(num_cities))
    random.shuffle(unvisited)
    for i in range(third):
        city = unvisited.pop()
        solution[i] = city
        visited.add(city)

    # second 1/3 in greedy order (excluding visited cities)
    current_city = solution[third - 1]
    for i in range(third, 2 * third):
        unvisited = [city for city in range(num_cities) if city not in visited]
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        solution[i] = next_city
        visited.add(next_city)
        current_city = next_city

    # last 1/3 in ascending order (excluding visited cities)
    for i in range(2 * third, num_cities):
        city = min([c for c in range(num_cities) if c not in visited])
        solution[i] = city
        visited.add(city)

    return solution

def mix_solution_greedy_ascending_random(num_cities, distance_matrix):
    """ Generate a mixed solution using greedy, ascending, and random (split by thirds). """
    solution = [None] * num_cities
    visited = set()

    # first 1/3 in greedy order
    current_city = 0
    third = num_cities // 3
    for i in range(third):
        unvisited = [city for city in range(num_cities) if city not in visited]
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        solution[i] = next_city
        visited.add(next_city)
        current_city = next_city

    # second 1/3 in ascending order (excluding visited cities)
    for i in range(third, 2 * third):
        city = min([c for c in range(num_cities) if c not in visited])
        solution[i] = city
        visited.add(city)

    # last 1/3 in random order (excluding visited cities)
    unvisited = [city for city in range(num_cities) if city not in visited]
    random.shuffle(unvisited)
    for i in range(2 * third, num_cities):
        solution[i] = unvisited.pop()

    return solution

def mix_solution_greedy_random_ascending(num_cities, distance_matrix):
    """ Generate a mixed solution using greedy, random, and ascending (split by thirds). """
    solution = [None] * num_cities
    visited = set()

    # first 1/3 in greedy order
    current_city = 0
    third = num_cities // 3
    for i in range(third):
        unvisited = [city for city in range(num_cities) if city not in visited]
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        solution[i] = next_city
        visited.add(next_city)
        current_city = next_city

    # second 1/3 in random order (excluding visited cities)
    unvisited = [city for city in range(num_cities) if city not in visited]
    random.shuffle(unvisited)
    for i in range(third, 2 * third):
        solution[i] = unvisited.pop()
        visited.add(solution[i])

    # last 1/3 in ascending order (excluding visited cities)
    for i in range(2 * third, num_cities):
        city = min([c for c in range(num_cities) if c not in visited])
        solution[i] = city
        visited.add(city)

    return solution

# odd and even index
def mix_solution_ascending_random_alternate(num_cities):
    """ Generate a mixed solution using ascending and random (alternating even/odd index). """
    solution = [None] * num_cities
    visited = set()

    # even index in ascending order
    for i in range(0, num_cities, 2):
        solution[i] = i
        visited.add(i)

    # odd index in random order (excluding visited cities)
    unvisited = [city for city in range(num_cities) if city not in visited]
    random.shuffle(unvisited)

    for i in range(1, num_cities, 2):
        solution[i] = unvisited.pop()

    return solution

def mix_solution_ascending_greedy_alternate(distance_matrix):
    """ Generate a mixed solution using ascending and greedy (alternating even/odd index). """
    num_cities = len(distance_matrix)
    solution = [None] * num_cities
    visited = set()

    # even index in ascending order
    for i in range(0, num_cities, 2):
        solution[i] = i
        visited.add(i)

    # odd index in greedy order (excluding visited cities)
    current_city = 0
    for i in range(1, num_cities, 2):
        unvisited = [city for city in range(num_cities) if city not in visited]
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        solution[i] = next_city
        visited.add(next_city)
        current_city = next_city

    return solution

def mix_solution_random_greedy_alternate(num_cities, distance_matrix):
    """ Generate a mixed solution using random and greedy (alternating even/odd index). """
    solution = [None] * num_cities
    visited = set()

    # even index in random order
    unvisited = list(range(num_cities))
    random.shuffle(unvisited)

    for i in range(0, num_cities, 2):
        city = unvisited.pop()
        solution[i] = city
        visited.add(city)

    # odd index in greedy order (excluding visited cities)
    current_city = 0
    for i in range(1, num_cities, 2):
        unvisited = [city for city in range(num_cities) if city not in visited]
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        solution[i] = next_city
        visited.add(next_city)
        current_city = next_city

    return solution

def mix_solution_random_ascending_alternate(num_cities):
    """ Generate a mixed solution using random and ascending (alternating even/odd index). """
    solution = [None] * num_cities
    visited = set()

    # even index in random order
    unvisited = list(range(num_cities))
    random.shuffle(unvisited)
    for i in range(0, num_cities, 2):
        city = unvisited.pop()
        solution[i] = city
        visited.add(city)

    # odd index in ascending order (excluding visited cities)
    for i in range(1, num_cities, 2):
        city = min([c for c in range(num_cities) if c not in visited])
        solution[i] = city
        visited.add(city)

    return solution

def mix_solution_greedy_ascending_alternate(distance_matrix):
    """ Generate a mixed solution using greedy and ascending (alternating even/odd index). """
    num_cities = len(distance_matrix)
    solution = [None] * num_cities
    visited = set()

    # even index in greedy order
    current_city = 0
    for i in range(0, num_cities, 2):
        unvisited = [city for city in range(num_cities) if city not in visited]
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        solution[i] = next_city
        visited.add(next_city)
        current_city = next_city

    # odd index in ascending order (excluding visited cities)
    for i in range(1, num_cities, 2):
        city = min([c for c in range(num_cities) if c not in visited])
        solution[i] = city
        visited.add(city)

    return solution

def mix_solution_greedy_random_alternate(num_cities, distance_matrix):
    """ Generate a mixed solution using greedy and random (alternating even/odd index). """
    solution = [None] * num_cities
    visited = set()

    # even index in greedy order
    current_city = 0
    for i in range(0, num_cities, 2):
        unvisited = [city for city in range(num_cities) if city not in visited]
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        solution[i] = next_city
        visited.add(next_city)
        current_city = next_city

    # odd index in random order (excluding visited cities)
    unvisited = [city for city in range(num_cities) if city not in visited]
    random.shuffle(unvisited)
    for i in range(1, num_cities, 2):
        solution[i] = unvisited.pop()

    return solution