class CalculateMoney:
    def sum_price_count(self, price: [int, float], count: [int, float], discount: int = None):
        result = round(count * price, 2)
        if discount:
            result = round(result * (1 - (discount / 100)), 2)
        return result

    def sum_price(self, prices: list, discount: int = None):
        result = sum(prices)
        if discount:
            result = round(result * (1 - (discount / 100)), 2)
        return result
