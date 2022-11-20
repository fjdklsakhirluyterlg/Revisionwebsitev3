class tax:
    def __init__(self, country, amount):
        self.country = country
        self.amount = amount
    
    def calculate_annual_from_monthy(self):
        self.amount * 12

    def calculate_annual_from_weekly(self):
        self.amount * 52.1429
    