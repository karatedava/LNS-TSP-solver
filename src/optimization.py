import random
import time
import math

class tsp_opt():

    @staticmethod
    def safe_exp(value, bound=100):
        """
        prevents 'math error' when the value of exp can be too small / large
        """
        if value > bound:
            return 1
        elif value < (-bound):
            return 0
        else:
            return math.exp(value)
        
    @staticmethod
    def tour_distance(tour,dist_matrix):
        """
        Calulates the total tour distance (cyclic)
        """
        distance = sum(dist_matrix[tour[i-1]][tour[i]] for i in range(len(tour)))
        return distance
    
    @staticmethod
    def tour_distance_noncyclic(tour,dist_matrix):
        """
        Calulates the total tour distance (non-cyclic)
        """
        distance = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        return distance
    
    @staticmethod
    def incremental_distance_eval_2opt(tour,dist_matrix,i,j):
        """
        incremental evaluation of distance after 2-opt operation (cyclic)
        """

        dist = 0

        if i > 0:
            dist += dist_matrix[tour[i-1]][tour[i]]
        if j < len(tour) - 1:
            dist += dist_matrix[tour[j]][tour[j+1]]
        if i == 0 or j == len(tour) - 1:
            dist += dist_matrix[tour[0]][tour[-1]]
        
        return dist
    
    @staticmethod
    def incremental_distance_eval_2opt_noncyclic(tour,dist_matrix,start,end):
        """
        incremental evaluation of distance after 2-opt operation (non-cyclic)
        """
        dist = dist_matrix[tour[start]][tour[end]]
        return dist

    @classmethod
    def get_shorter_tour(cls,tour_A, tour_B, dist_matrix):
        """
        returns shorter tour
        """
        if cls.tour_distance(tour_A,dist_matrix) < cls.tour_distance(tour_B,dist_matrix):
            return tour_A
        return tour_B
    
    #############
    # OPERATORS #
    #############

    @staticmethod
    def two_opt(tour, i, j):
        """
        swaps two edges in the route
        returns new route after swap
        """
        if i < j and 0 <= i < len(tour) and 0 <= j < len(tour):
            new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
            return new_tour
        else:
            return tour

    @classmethod
    def three_opt(cls,tour, dist_matrix, i, j, k):
        
        """
        ChatGPT code with some modifications

        Performs a 3-opt move by evaluating all possible re-connections 
        between the three segments.
        
        Parameters:
        - tour: Current tour (list of cities)
        - i, j, k: Indices that divide the tour into three segments
        - dist_matrix: Distance matrix to evaluate tour length

        Returns:
        - new_tour: A new tour with the best 3-opt move applied
        """
        if len({i, j, k}) != 3:
            return tour
        
        i, j, k = sorted([i, j, k])
        if j < i + 2:
            j = i + 2
        if k < j + 2:
            k = j + 2
        
        if len(tour) <= k:
            return tour

        A, B, C, D = tour[:i], tour[i:j+1], tour[j+1:k+1], tour[k+1:]

        options = (
            A + B[::-1] + C + D,
            A + B[::-1] + C[::-1] + D,
            A + B + C[::-1] + D,
            A + C + B + D,
            A + C[::-1] + B + D,
            A + C + B[::-1] + D,
            A + C[::-1] + B[::-1] + D
        )

        best_sol = min(options, key=lambda x:cls.tour_distance(x,dist_matrix))
        return best_sol
    
    ##############################
    #  DESTROY / REPAIR METHODS  #
    ##############################

    @staticmethod
    def _random_eject_(tour):
        """
        ejects random city\n
        returns ejected city index
        """
        return random.randint(0, len(tour) - 1)
    
    @staticmethod
    def _eject_nearby_city_(inserted_city_idx):
        """
        ejects neighbouring city\n
        returns ejected city index
        """
        if inserted_city_idx > 0:
            return inserted_city_idx - 1
        else:
            return inserted_city_idx + 1
    
    @staticmethod
    def _eject_worst_city_(tour, dist_matrix):
        """
        finds the worst edge in the tour\n
        ejects the first city of that edge\n 
        returns ejected city index
        """
        worst_city_idx = None
        worst_distance = -float('inf')
        for i in range(len(tour) - 1):
            edge_distance = dist_matrix[tour[i]][tour[i + 1]]
            if edge_distance > worst_distance:
                worst_distance = edge_distance
                worst_city_idx = i
        return worst_city_idx
    
    @staticmethod
    def _random_insertion_(tour):
        """
        returns random index to insert city in
        """
        return random.randint(1, len(tour) - 1)
    
    @staticmethod
    def _find_best_insertion_(tour, city_index, dist_matrix):

        """
        returns the index where to insert a city in a greedy manner
        """

        best_position = None
        best_increase = float('inf')

        for i  in range(len(tour) - 1):
            increase = (dist_matrix[tour[i]][city_index] + dist_matrix[city_index][tour[i + 1]] - dist_matrix[tour[i]][tour[i + 1]])
            if increase < best_increase:
                best_increase = increase
                best_position = i + 1
        return best_position

    @classmethod
    def ejection_chain(
        cls, tour, dist_matrix, max_chain_lenght=3, 
        ejection = 'random', insertion = 'random'
        ):

        """
        Performs the ejection chain operations\n
        returns new tour and ejected cities respecrivelly
        """

        new_tour = tour[:]
        ejected_cities = []
        city_to_eject = cls.random_eject(new_tour)

        for _ in range(max_chain_lenght):
            
            # select city to eject
            if ejection == 'random':
                city_to_eject = cls._random_eject_(new_tour)
            elif ejection == 'nearby':
                city_to_eject = cls._eject_nearby_city_(city_to_eject)
            elif ejection == 'worst':
                city_to_eject = cls._eject_worst_city_(new_tour,dist_matrix)

            ejected_cities.append(new_tour[city_to_eject])

            # find best insertion point for ejected city
            city = new_tour.pop(city_to_eject)
            if insertion == 'random':
                insertion_pos = cls._find_best_insertion_(new_tour, city, dist_matrix)
            elif insertion == 'best':
                insertion_pos = cls._random_insertion_(new_tour)

            new_tour.insert(insertion_pos, city)

        return new_tour, ejected_cities

    @staticmethod
    def random_subtour_removal(tour, n_remove=5):
        """
        randomly selects a subtour of lenght 'n_remove'\n
        returns the removed remaining tour and removed cities
        """
        remove_idxs = random.sample(range(len(tour)),n_remove)

        remaining_solution = [city for i, city in enumerate(tour) if i not in remove_idxs]
        removed_cities = [tour[i] for i in remove_idxs]
        
        return remaining_solution, removed_cities

    @staticmethod
    def greedy_insertion(partial_tour,cities_to_insert, dist_matrix):
        """
        inserts cities in a greedy manner into partial tour\n
        returns the complete tour 
        """
        completed_tour = partial_tour[:]

        for city in cities_to_insert:
            best_pos = None
            best_increase = float('inf')

            for i in range(len(completed_tour)):
                prev_city = completed_tour[i]
                next_city = completed_tour[(i + 1) % len(completed_tour)]
            
                increase = (
                    dist_matrix[prev_city][city] +
                    dist_matrix[city][next_city] -
                    dist_matrix[prev_city][next_city]
                )

                if increase < best_increase:
                    best_increase = increase
                    best_pos = i + 1
        
            completed_tour.insert(best_pos,city)

        return completed_tour
    
    @classmethod
    def local_search_2opt(cls, tour, dist_matrix):
        
        """
        applies 2-opt to exploint current tour.

        Parameters:
        - tour: sequence of cities.
        - dist_matrix: 2D list of distances.

        Returns:
        - tour: improved tour.
        """

        improved = True
        while improved:
            improved = False
            for i in range(len(tour) - 1):
                for j in range(i + 2, len(tour)):
                    new_tour = cls.two_opt(tour,i,j)
                    evaluated_dist = cls.incremental_distance_eval_2opt(new_tour,dist_matrix,i,j) - cls.incremental_distance_eval_2opt(tour,dist_matrix,i,j)
                    if evaluated_dist < 0:
                        tour = new_tour
                        improved = True
        return tour
    
    @classmethod
    def local_search_3opt(cls, tour, dist_matrix):
        """
        applies 3-opt to exploint current tour.

        Parameters:
        - tour: sequence of cities.
        - dist_matrix: 2D list of distances.

        Returns:
        - tour: improved tour.
        """

        improved = True
        while improved:
            improved = False
            for i in range(len(tour) - 1):
                for j in range(i + 2, len(tour)):
                    for k in range(j + 2, len(tour)):
                        new_tour = cls.three_opt(tour,dist_matrix,i,j,k)

                        if cls.tour_distance(new_tour,dist_matrix) < cls.tour_distance(tour,dist_matrix):
                            tour = new_tour
                            improved = True
        return tour
    
    @classmethod
    def SA_acceptance(cls, new_tour,current_tour,dist_matrix,temp):

        """
        rejects / accepts the new tour in probabilistic manner dependent on the temperature
        returns the newly accepted tour or the original tour
        """

        D_dist = cls.tour_distance(new_tour,dist_matrix) - cls.tour_distance(current_tour,dist_matrix)
        acceptance_prob = cls.safe_exp((-D_dist)/temp)

        if acceptance_prob >= random.random():
            return new_tour
        else:
            return current_tour

