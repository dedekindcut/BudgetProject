

# general asset or liability used in projections and net worth calculation
class AssetLiability:

    def __init__(self, balance, interest_rate, name, category):
        self.balance = balance
        self.interest_rate = interest_rate
        self.name = name
        self.category = category

    # returns future value of asset or liability in a number of years
    def future_value(self, years):
        factor = pow((1 + self.interest_rate / 100), years)
        return self.balance * factor
