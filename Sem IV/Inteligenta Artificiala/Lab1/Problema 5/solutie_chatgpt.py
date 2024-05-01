def valoare_repetata(nums):
    frecventa = {}
    for num in nums:
        frecventa[num] = frecventa.get(num, 0) + 1

    for num, count in frecventa.items():
        if count == 2:
            return num


# Exemplu de utilizare:
nums = [1, 2, 3, 4, 2]
valoare_repetata = valoare_repetata(nums)
print("Valoarea care se repetă de două ori în șirul dat este:", valoare_repetata)
