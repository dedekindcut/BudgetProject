

# general asset or liability used in projections and net worth calculation
class AssetLiability:

    def __init__(self, balance, interest_rate, name, category):
        self.balance = balance
        self.interest_rate = interest_rate
        self.name = name
        self.category = category
