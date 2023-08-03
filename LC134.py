class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        poss = []
        length = len(gas)
        for i in range(length):
            if gas[i] >= cost[i]:
                poss.append(i)
        
        for i in poss:
            tank = gas[i]
            temp = i
            for j in range(length - 1):
                tank = tank - cost[i%length] + gas[(i + 1)%length]
                if tank < 0: break
                i = i + 1
            if tank - cost[i%length] >= 0: return temp
        
        return -1
