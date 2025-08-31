"""
Problem Statement -> Given an array of numbers representing the height of vertical lines, find two lines that,
along with the x-axis, can form a container holding the maximum amount of water.
"""
from typing import List

def largest_container(heights: List[int]) -> int:
    """
    Calculates the maximum amount of water a container can hold.

    Args:
        heights (List[int]): A list of integers representing the height of each vertical line.

    Returns:
        int: The maximum amount of water that can be contained.

    Example:
        i/p -> heights = [2, 7, 8, 3, 7, 6]
        o/p -> 24
    """
    left, right = 0, len(heights) - 1
    max_water = 0

    # The core logic is to use two pointers to calculate the area and then move the pointer
    # of the shorter line inwards to find a potentially larger area.
    while left < right:
        # Calculate the area between the two current lines.
        current_water = min(heights[left], heights[right]) * (right - left)
        max_water = max(max_water, current_water)
        
        # To potentially find a larger area, we must move the pointer of the shorter line.
        # Moving the pointer of the taller line will only decrease the width and not increase
        # the height, so the area will always be smaller.
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_water

# A detailed breakdown of the principle.
"""
Underlying Principle -> Two Pointer Problem

1. Two Pointers: Start with a pointer at the beginning (left) and one at the end (right) of the array. This gives us the widest possible container initially.

2. Calculate and Compare:
   - The water held is determined by the shorter of the two lines (as the water level is limited by the lower height) multiplied by the distance between them.
   - We calculate this area and update our `max_water` if the current area is larger.

3. The "Greedy" Movement:
   - To find a larger area, we need to try and increase the limiting height.
   - We move the pointer associated with the shorter line inward.
   - The reason for this is that moving the pointer of the taller line will definitely decrease the width of the container, and since the height is still limited by the (now-new) shorter line, the area cannot increase.
   - By moving the shorter pointer, we have a chance of finding a taller line that can create a larger area.

Why it works:
This two-pointer approach efficiently explores potential containers. By starting with the widest container and systematically narrowing the search based on the "greedy" principle of moving the shorter pointer, we can find the maximum area in a single pass with an optimal O(n) time complexity and O(1) space complexity.
"""