class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # priceは100以下なので、最低金額として初期値は100より大きく
        current_minimum = 1000
        
        # 最低でも利益は0なので、初期値を0に
        current_profit = 0

        for price in prices:
            # 今までの全ての額より同じか安い
            # このタイミングで売るのは明らかに0円以下の得
            # もし、売るのがこの先なら、売るのは前でなく今なので、可能な最安取得金額を更新
            if current_minimum >= price:
                current_minimum = price
            else:
                # もし今売ったら得するか考える
                # 今までの組み合わせの理論値より高く売れるなら、ここまでであり得る最高利益を更新
                if price - current_minimum > current_profit:
                    current_profit = price - current_minimum
        
        return current_profit