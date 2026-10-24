class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # priceは100以下なので、最低金額として初期値は100より大きく
        current_minimum = 1000
        
        # 最低でも利益は0なので、初期値を0に
        current_profit = 0

        for price in prices:
            # もし今売ったら得するか考える
            # 今までの組み合わせの理論値より高く売れるなら、ここまでであり得る最高利益を更新
            if price - current_minimum > current_profit:
                current_profit = price - current_minimum
            elif price - current_minimum <= 0:
                current_minimum = price
            else:
                continue
        
        return current_profit