def element_majoritar(nums):
    majoritar = None
    count = 0

    for num in nums:
        if count == 0:
            majoritar = num
            count = 1
        elif num == majoritar:
            count += 1
        else:
            count -= 1

    return majoritar
# Exemplu de utilizare:
nums = [2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]
majoritar = element_majoritar(nums)
print("Elementul majoritar în șirul dat este:", majoritar)