from dataclasses import dataclass
from math import asin, cos, radians, sin, sqrt, tan

@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

    def distance_to(self, other):
        r = 6371  # Earth radius in kilometers
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (sin((phi_2 - phi_1) / 2)**2
             + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2)**2)
        return 2 * r * asin(sqrt(h))


class bankuser:
    user = {}
    bankrupt = []
    def add_user(self, name, money, account):
        self.user[name] = [money, account]
    def debers(self):
        for name in self.user:
            if self.user[name][0] <= 0:
                self.bankrupt.append(name)
    def interest(self):
        for name in self.user:
            if self.user[name][1] == "Gold":
                self.user[name][0] = (self.user[name][0])*1.08
            elif self.user[name][1] == "Silver":
                self.user[name][0] = (self.user[name][0])*1.06
            elif self.user[name][1] == "Bronze":
                self.user[name][0] = (self.user[name][0])*1.04
            elif self.user[name][1] == "Standard":
                self.user[name][0] = (self.user[name][0])*1.02

class Bank(): 
    crisis = False
    def create_atm(self, money, moneylimit):
        while not self.crisis:
            if money <= moneylimit:
                yield f"£{money}"
            else:
                yield f"£{money} is not avaible to you, please withdraw a max of £{moneylimit}"
        
        while self.crisis:
            newmoneylimit = 40
            if money <= newmoneylimit:
                yield f"£{money}"
            else:
                if moneylimit >= newmoneylimit:
                    yield f"£{money} is not avaible to you, please withdraw a max of £{newmoneylimit}"
                else:
                    yield f"£{money} is not avaible to you, please withdraw a max of £{moneylimit}"