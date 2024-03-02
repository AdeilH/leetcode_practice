from typing import List

heights1 = [1,8,6,2,5,4,8,3,7]
heights2 = [1,1]

def container_with_most_water(heights: List[int]) -> int:
    area = 0
    length_heights = len(heights)
    j = length_heights - 1
    area = 0
    for i in range(length_heights):
        length = j - i 
        if i >= j:
            break
        if heights[i] > heights[j]:
            area = max(area, length*heights[j])
            print(heights[i], heights[j], area)
            j-=1
        elif heights[j] > heights[i]:
            area = max(area, length*heights[i])
            print(heights[i], heights[j], area)
        else:
            area = max(area, length*heights[i])
            print(heights[i], heights[j], area)
    return area
print(container_with_most_water(heights1))
print(container_with_most_water(heights2))