#Să se determine al k-lea cel mai mare element al unui șir de numere cu n elemente (k < n).
# De ex. al 2-lea cel mai mare element din șirul [7,4,6,3,9,1] este 7.
def maxim(arr):
    maxi1 = arr[0]
    maxi2 = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > maxi1:
            maxi2 = maxi1
            maxi1 = arr[i]
        elif arr[i] > maxi2:
            maxi2 = arr[i]
    return maxi2

arr = [7,4,6,3,9,1]
print(maxim(arr))