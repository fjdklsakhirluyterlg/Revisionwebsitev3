class tax:
    def __init__(self, country, amount, self_employed=False):
        self.country = country
        self.amount = amount
        self.self_employed = False
    
    def calculate_annual_from_monthy(self):
        self.amount * 12

    def calculate_annual_from_weekly(self):
        self.amount * 52.1429
    
    def calculate_uk_tax(self):
        ALLOWANCE = 12750