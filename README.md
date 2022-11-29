# Research_Algo_Ex5


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
