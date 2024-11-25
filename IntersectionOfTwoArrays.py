def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    nums1_d = {}
    for element in nums1:
        if element in nums1_d:
            nums1_d[element] += 1 
        else:
            nums1_d[element] = 1
    nums2_d = {}

    for element in nums2:
        if element in nums2_d:
            nums2_d[element] += 1 
        else:
            nums2_d[element] = 1
    output = []

    for element in set(nums1):
        if element in nums2_d:
            for j in range(min(nums1_d[element],nums2_d[element])):
                output.append(element)
        
    return output