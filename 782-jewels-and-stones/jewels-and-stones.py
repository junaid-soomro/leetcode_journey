class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_that_are_jewels = 0
        for char in stones:
            for val in jewels:
                if char == val:
                    stones_that_are_jewels += 1

        return stones_that_are_jewels