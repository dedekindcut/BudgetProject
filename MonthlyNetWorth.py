from AssetLiability import AssetLiability


class MonthlyNetWorth:

    def __init__(self, month, year, previous_assets, previous_liabilities):
        self.month = month
        self.year = year
        self.assets = previous_assets
        self.liabilities = previous_liabilities

    # returns net assets
    def sum_assets(self):
        total_assets = 0

        for asset in self.assets:
            total_assets += asset.balance

        return total_assets

    # returns net liabilities
    def sum_liabilities(self):
        total_liabilities = 0

        for liability in self.liabilities:
            total_liabilities += liability.balance

        return total_liabilities

    # calculates and returns net worth
    def net_worth(self):
        return self.sum_assets() - self.sum_liabilities()

    # returns True if you're in debt
    def is_in_debt(self):
        return self.net_worth() < 0

    # adds an asset to the instance array
    # returns net assets
    def add_asset(self, balance, interest_rate, name, category):
        new_asset = AssetLiability(balance, interest_rate, name, category)
        self.assets.append(new_asset)
        return self.sum_assets()

    # adds a liability to the instance array
    # returns net liabilities
    def add_liability(self, balance, interest_rate, name, category):
        new_liability = AssetLiability(balance, interest_rate, name, category)
        self.liabilities.append(new_liability)
        return self.sum_liabilities()
