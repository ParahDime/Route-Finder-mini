#energy travel calculations (in knapsack)
class travel_dp:
    def __init__(self, travel, budget):
        self.travel_costs = travel
        self.energy_budget = budget

    def max_visitable_locations(self, costs, budget):
    #cost is a dict (name, amount)
    #budget, total amount
        costs = list(self.travel.values())
        n = len(costs)
        budget = self.budget

        # dp[i][b] = max locations using first i items with budget b
        dp = [[0] * (budget + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            cost = costs[i - 1]

            for b in range(budget + 1):
                if cost <= b:
                    dp[i][b] = max(
                        dp[i - 1][b],            # skip this location
                        dp[i - 1][b - cost] + 1  # take this location
                    )
                else:
                    dp[i][b] = dp[i - 1][b]

        return dp[n][budget]
    #run a dp table
    #which locations are under the budget
    #return an amount
        pass