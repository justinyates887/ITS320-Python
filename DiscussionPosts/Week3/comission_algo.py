class CommissionAlgorithm(ComissionAlgorithmInterface):

    def __init__(self, base_commission=0, base_commission_rate=0.05):
        self.base_commission = base_commission
        self.base_commission_rate = base_commission_rate

    def calculate_commission(self, total_sales):
        commission = self.base_commission
        commission_rate = self.base_commission_rate

        while total_sales > 0:
            tier_sales = min(total_sales, 10000)
            commission += tier_sales * commission_rate
            commission_rate = min(commission_rate + 0.05, 0.20)
            total_sales -= tier_sales

        return commission

def main():
    commission = CommissionAlgorithm()
    commission.calculate_commission(15000)

main()
