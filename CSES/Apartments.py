n, m, k = map(int, input().split())
desired_sizes = list(map(int, input().split()))
apartment_sizes = list(map(int, input().split()))

desired_sizes.sort()
apartment_sizes.sort()

i, j = 0, 0
count = 0

while i < n and j < m:
    if abs(desired_sizes[i] - apartment_sizes[j]) <= k:
        count += 1
        i += 1
        j += 1
    elif apartment_sizes[j] < desired_sizes[i] - k:
        # Apartment too small, move to the next apartment
        j += 1
    else:
        # Applicant's requirement too high, move to the next applicant
        i += 1

# Print the number of matches
print(count)