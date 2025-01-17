# general libraries
import sys
import json

# our custom files
from src.LNS import *
from src import solution_generator

#############################
# SEARCH ALGORITHM SETTINGS #
#############################
LNS_SETTINGS = {

    ### general ###
    'max_steps':100,
    'max_nonimproving_iter':40,

    'temp':100,
    'min_temp':2.0,
    'cooling_scheme':'exp', # choose from : ['linear', 'exp', 'quadratic', 'log', 'linear_aditive']
    'cooling_c' : 0.95,
}

#############################
#       SETTINGS  END       #
#############################




def read_instance_json(file_path):
    with open(file_path) as f:
        return json.load(f)
    
def write_instance_json(solution, file_path):
    with open(file_path, 'w') as f:
        json.dump(solution, f)

def main():

    if len(sys.argv) != 3:
        print('USAGE: python3 main.py <instance-file-path> <solution-file-path>')
        return
    
    instance_path = sys.argv[1]
    output_path = sys.argv[2]

    instance = read_instance_json(instance_path)
    matrix = instance['Matrix']
    time_limit = instance['Timeout']



    tour = solution_generator.generate_solution_random(len(matrix))

    Search = LNS(LNS_SETTINGS)
    predicted_tour, time_needed = Search.run(
        initial_tour=tour,
        dist_matrix=matrix,
        time_limit=time_limit,
        report=True
        )

    print('\n\n ---------------------------------------------- \n')
    print(f'initial tour distance: {tsp_opt.tour_distance(tour,matrix)}')
    print(f'locally minimzed tour distance: {tsp_opt.tour_distance(predicted_tour,matrix)}')
    print(f'time needed: {time_needed:.2f}\t time limit: {time_limit}')

    
    ### writing the new solution to json file
    instance['GlobalBest'] = predicted_tour
    instance['GlobalBestVal'] = tsp_opt.tour_distance(predicted_tour,matrix)
    write_instance_json(instance, output_path)

if __name__ == "__main__":
    main()