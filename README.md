# Research_Algo_Ex5

### Q1 - Iterator - q1.py

   This question is about creating a custom iterator for making subsets of a given list, by the following conditions;
        
        1. each subset's sum must not be over the given value (C).
        2. must not creating all subsets first' only on-the-run.
        
   The function bounded_subsets returns a list of lists of valid subsets from the given list, that accepts the aboe conditions.
    
### Q2 - Strategy - q2.py
   This question is about the OOP principle of Strategy - multiple ways to solve a problem.
   The problem i chose to work on is the Connected Components of a given Graph.
   The algorithms that problem can be solved with are:
        
        1. BFS - Breadth First Search
        2. DFS - Depth First Search
    
   Both are compatable with the main function connectedComponents which accepts one of the above as an argument 'algorithm'.
        
   The possible output types of this strategy are:
        
        1. sizes of components
        2. the components by themselves
    
   Both are compatable with the main function connectedComponents which accepts one of the above as an argument 'output_type'.

    

### Q3: CodinGame

![image](https://user-images.githubusercontent.com/71274563/204548747-af7c7e81-475a-4942-99f0-2b188074d45b.png)



    import sys
    import math

    def get(num):


        global best_cost
        global rooms

        room_best = best_cost.get(num, None)

        if room_best is not None:
            return room_best
        else:
            room = rooms[num]
            s1 = s2 = 0
    
            if room['rid1'] == 'E':
                s1 = int(room['money'])
            else:
                s1 = int(room['money']) + get(room['rid1'])
            
            if room['rid2'] == 'E':
                s2 = int(room['money'])
            else:
                s2 = int(room['money']) + get(room['rid2'])
    
            best_cost_number = (s1, s2) [s1 < s2]
            best_cost[num] = best_cost_number
    
        return best_cost_number

    rooms = {}

    best_cost = {}


    n = int(input())
    for i in range(n):
        rid, money, rid1, rid2 = input().split()

        rooms[rid] = {'money': money, 'rid1': rid1, 'rid2': rid2}

    print(get('0'))
