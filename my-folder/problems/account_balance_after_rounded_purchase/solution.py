class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        if purchaseAmount % 10 == 5:
            return 100-(purchaseAmount+5)
        if purchaseAmount%10 < 5:
            # print()
            return 100-(purchaseAmount - purchaseAmount%10)
        else:
            return 100-(purchaseAmount + 10-purchaseAmount%10)