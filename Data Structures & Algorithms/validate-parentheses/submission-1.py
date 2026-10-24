from collections import deque

bracket_pairs = {"(": ")", "{" : "}", "[" : "]"}

class Solution:
    def isValid(self, s: str) -> bool:
        
        q = deque()
        for char in s:
            # ネストが深くなる
            if char in bracket_pairs:
                q.append(char)
            # ネストが浅くなる
            # 直前の未解消のブラケットと一致して閉じる必要がある
            else:
                # キューが空なのに閉じる側のブラケットがきたので、例外
                if not q:
                    return False
                unclosed_bracket = q.pop()
                # ペアになるかを見る
                # ネストが無事閉じる
                if bracket_pairs[unclosed_bracket] == char:
                    continue
                # 例外発生
                else:
                    return False
        
        # 全ての文字を処理してキューが綺麗に消えた（閉じたブラケットのペアが作れた）
        if not q:
            return True 
        else:
            return False


