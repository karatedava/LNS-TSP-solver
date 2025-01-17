import unittest
import solution_generator
import optimization

class TestSolutionGenerator(unittest.TestCase):

    def test_generate_solution_ascending(self):
        num_cities = 5
        expected_solution = [0, 1, 2, 3, 4]
        self.assertEqual(solution_generator.generate_solution_ascending(num_cities), expected_solution)

    def test_generate_solution_random(self):
        num_cities = 5
        solution = solution_generator.generate_solution_random(num_cities)
        # Test that the solution contains all cities from 0 to num_cities - 1
        self.assertEqual(len(solution), num_cities)
        self.assertEqual(set(solution), set(range(num_cities)))

    def test_generate_solution_greedy(self):
        distance_matrix = [
            [0, 2, 9, 10],
            [1, 0, 6, 4],
            [15, 7, 0, 8],
            [6, 3, 12, 0]
        ]
        solution = solution_generator.generate_solution_greedy(distance_matrix)
        # Check that the solution contains all cities
        self.assertEqual(len(solution), len(distance_matrix))
        self.assertEqual(set(solution), set(range(len(distance_matrix))))
        
        # Check that solution starts with city 0
        self.assertEqual(solution[0], 0)

class TestOptimization(unittest.TestCase):

    def test_three_opt(self):

        d_mat1 = [
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1]
        ]
        d_mat2 = [
            [0,1,1,-1,1,1,1],
            [-1,0,1,1,1,1,1],
            [1,-1,0,1,1,1,1],
            [1,1,1,0,-1,1,1],
            [1,1,1,1,0,1,-1],
            [1,1,1,1,1,0,1],
            [1,1,1,1,1,1,0]
        ]

        test_inputs = (
            [[0,1,2,3,4],d_mat1,1,1,1],
            [[0,1,2,3,4,5,6],d_mat2,2,1,0] # --> i=0, j=2, k=4
            # A = [] B = [0,1,2] C = [3,4] D = [5,6]
        )
        expected_outputs = (
            test_inputs[0][0],
            [2,1,0,3,4,5,6]
        )

        for test_input,expected_output in zip(test_inputs,expected_outputs):
            function_output = optimization.tsp_opt.three_opt(test_input[0],test_input[1],test_input[2],test_input[3],test_input[4])
            self.assertEqual(function_output,expected_output)


if __name__ == '__main__':
    unittest.main()
