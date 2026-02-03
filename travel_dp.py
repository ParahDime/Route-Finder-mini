#energy travel calculations (in knapsack)
class travel_dp:
    def __init__(self, travel_costs, energy_budget):
        self.travel_costs = travel_costs
        self.energy_budget = energy_budget

    def max_visitable_locations(self):
        costs = list(self.travel.values()) #contains path and cost of the path taken
        n = len(costs)
        budget = self.budget #amount available

        #max locations using first i items with budget b
        dp = [[0] * (budget + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            cost = costs[i - 1]

            for b in range(budget + 1): #find path
                if cost <= b:
                    dp[i][b] = max(
                        dp[i - 1][b],        
                        dp[i - 1][b - cost] + 1  
                    )
                else:
                    dp[i][b] = dp[i - 1][b]

        return dp[n][budget] #path is returned