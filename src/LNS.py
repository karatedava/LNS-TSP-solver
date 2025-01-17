import os
from .optimization import *

class LNS():

    # general settings #
    max_steps:int = 5000
    max_nonimproving_iter:int = 500

    # simulated annealing settings #
    temp:int = 100
    min_temp:int = 100
    cooling_scheme:str = 'linear_aditive'
    cooling_c:float = 0.95

    # destroy / repair settings
    # TODO
    
    def __init__(self,settings:dict) -> None:
        self.set_params(settings)
        pass

    def set_params(self,settings:dict) -> None:
        """
        sets the LNS parameters according to user specified settings
        """

        self.max_steps = settings['max_steps']
        self.max_nonimproving_iter = settings['max_nonimproving_iter']
        self.temp = settings['temp']
        self.min_temp = settings['min_temp']
        self.cooling_scheme = settings['cooling_scheme']
        self.cooling_c = settings['cooling_c']

    def run(self,initial_tour,dist_matrix,time_limit,report:bool=False):
        """
        runs the LNS on a given instance\n
        returns the minimized tour, time it took
        """

        best_tour_found = initial_tour
        prev_best_tour = best_tour_found
        current_tour = initial_tour
        current_temp = self.temp
        non_improving_iter = 0
        step = 0

        report_fill = 'distance\tstep\ttemp\ttime\n'

        def cooling():
            nonlocal step
            nonlocal current_temp
            if self.cooling_scheme == 'linear':
                current_temp = self.temp - self.cooling_c * step
            elif self.cooling_scheme == 'exp':
                current_temp = self.temp * round(self.cooling_c**step,3)
            elif self.cooling_scheme == 'quadratic':
                current_temp = round(self.temp / (1 + self.cooling_c * step**2),1)
            elif self.cooling_scheme == 'log':
                current_temp = self.temp / (1 + self.cooling_c * math.log(step+1))
            elif self.cooling_scheme == 'linear_aditive':
                current_temp = self.min_temp + (self.temp - self.min_temp) * ((self.max_steps - step) / self.max_steps)
        
        start_time = time.time()
        current_time = 0
        while step <= self.max_steps and non_improving_iter <= self.max_nonimproving_iter and current_temp > self.min_temp:
            
            print(f'step: {step}\t temp:{current_temp:.2f}\t time:{current_time:.2f}')
            if report:
                report_fill += f'{tsp_opt.tour_distance(best_tour_found,dist_matrix)}\t{step}\t{current_temp}\t{current_time}\n'

            destroyed_tour, removed_cities = tsp_opt.random_subtour_removal(current_tour,n_remove=10)

            repaired_tour = tsp_opt.greedy_insertion(destroyed_tour,removed_cities,dist_matrix)

            exploited_solution = tsp_opt.local_search_2opt(repaired_tour,dist_matrix)

            best_tour_found = tsp_opt.get_shorter_tour(best_tour_found,exploited_solution,dist_matrix)

            current_tour = tsp_opt.SA_acceptance(exploited_solution, current_tour, dist_matrix, current_temp)

            cooling()

            step += 1

            if prev_best_tour == best_tour_found:
                non_improving_iter += 1
            else:
                non_improving_iter = 0

            prev_best_tour = best_tour_found

            current_time = time.time() - start_time
            if current_time >= time_limit:
                break
        
        if report:
            # Ensure the directory exists
            os.makedirs('benchmarking', exist_ok=True)
            
            # Write the data to the file
            with open('benchmarking/report.dat', 'w') as file:
                file.write(report_fill)

        return best_tour_found, current_time
