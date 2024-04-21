
class ComissionPlan(ComissionPlanInterface):

    __comission_tiers = []

    def __init__(self):
        self.__comission_tiers = [
            {'cap' : 10000, 'rate': 0.05},
            {'cap': 20000, 'rate': 0.10},
            {'cap': 30000, 'rate': 0.15}
        ]

    def calculate_comission(self, total_sales):
        if total_sales == 0: return 0
        comission = 0
        for tier in self.__comission_tiers:
            tier_sales = min(total_sales, tier['cap'])
            commission += tier_sales * tier['rate']
        return comission
    
def main():
    comission = ComissionPlan()
    comission.calculate_comission(15000)
    