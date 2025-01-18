# LNS-TSP Solver

## Overview
LNS-TSP Solver is an easy-to-read implementation of a metaheuristic approach to solving the Traveling Salesman Problem (TSP). Designed for educational purposes and fun, it demonstrates how to achieve near-optimal solutions efficiently.

### What is the Traveling Salesman Problem?
The TSP involves constructing the shortest possible path that visits a set of points (e.g., cities) exactly once and returns to the starting point. For instance, imagine planning a road trip across the US to visit major landmarks. To save time and fuel, you aim to construct the shortest possible route.

While an exhaustive enumeration of all possible tours can solve the problem, it becomes computationally impractical for larger instances. For example, 10 cities already yield 10! (3,628,800) possible tours. Instead, this solver uses metaheuristic techniques that find high-quality solutions in significantly less time, though optimality is not guaranteed.

---

## Features
- **Exploration:** Uses destroy/repair methods to remove large parts of the solution and reinsert them in a modified way.
- **Exploitation:** Refines repaired solutions to locate local minima in the configuration space.
- **Simulated Annealing:** Wraps the search process to avoid premature convergence to local minima.
- **Customizability:** Operators for exploration and exploitation are highly customizable, with support for adding new methods.
  - Includes cyclic ejection chains for high-level destruction.
  - Offers simple swap, 2-opt, and other refinement techniques.

---

## Input and Output Formats
- **Input:**
  - A JSON file containing:
    - Coordinates (`X`, `Y`) of each city.
    - Distance matrix (`N x N`), where `N` is the number of cities.
    - Total distance of the current tour.
    - Computation time in seconds.
  - Example input files can be found in the `testing_data` folder.

- **Output:**
  - A JSON file in the same format as the input, with the updated solution.

---

## Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:karatedava/LNS-TSP-solver.git
   cd LNS-TSP-solver
   ```

---

## Execution
1. Open `main.py` to modify basic parameters, if needed.
2. Run the solver with your/testing input file:
   ```bash
   python3 main.py <input_file> <output_file>
   ```

---

## Example
- Input:
  ```json
  {
      "Coordinates": [[0, 0], [1, 1], [2, 2]],
      "Matrix": [[0, 1.4, 2.8], [1.4, 0, 1.4], [2.8, 1.4, 0]],
      "GlobalBestVal": 5.6,
      "Timeout": 0.5
  }

---

## License
This project is open-source.


