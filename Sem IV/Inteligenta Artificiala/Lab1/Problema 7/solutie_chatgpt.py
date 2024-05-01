def kth_largest_element(arr, k):
    sorted_arr = sorted(arr, reverse=True)
    if k <= len(sorted_arr):
        return sorted_arr[k - 1]
    else:
        return None

# Exemplu de utilizare:
sir = [7, 4, 6, 3, 9, 1]
k = 2
kth_largest = kth_largest_element(sir, k)
if kth_largest is not None:
    print(f"Al {k}-lea cel mai mare element din șirul {sir} este: {kth_largest}.")
else:
    print(f"Șirul are mai puțin de {k} elemente.")