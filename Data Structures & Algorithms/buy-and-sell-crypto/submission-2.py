class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # priceは100以下なので、最低金額として初期値は100より大きく
        current_minimum = 1000
        
        # 最低でも利益は0なので、初期値を0に
        current_profit = 0

        for price in prices:
            # この時点で売れば、今までの検討した組み合わせより高く売れる場合は、暫定理論利益値を更新
            if price - current_minimum > current_profit:
                current_profit = price - current_minimum
            # この時点の暫定最安取得値と同じか下回る金額の場合は暫定最安取得値を更新
            # 上とは独立した処理なので、厳密には別のifが確実だが、この場合はcurrent_profitが0以上というのが保証されているため、上のIF文と同時に成り立つことはありえないため、elifにする
            elif price - current_minimum <= 0:
                current_minimum = price
            else:
                continue
        
        return current_profit