class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #time_to_target[i] = (target-position[i]) / speed[i]
        #cars with same time_to_target are one fleet
        #every car with unique time_to_target is one fleet
        ttt = []
        cars = sorted(zip(position, speed), reverse=True)
        for p,s in cars:
            val = (target - p)/s
            ttt.append(val)
            if len(ttt) >= 2 and ttt[-1] <= ttt[-2]:
                ttt.pop()
        return len(ttt) 