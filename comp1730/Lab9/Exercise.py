import random
import time
import matplotlib.pyplot as plt
def plot_time(func, steps):
    seq = [ random.random() for i in range(steps) ]
    elapsed_times = []
    for n in range(2,steps):
        start_time = time.time()
        # run 10 times to reduce fluctuation
        for i in range(10):
            func(seq[:n])
        end_time = time.time()
        elapsed_times.append((end_time - start_time)/10)
    plt.plot(range(2,steps),elapsed_times)
    plt.show()
    print("Total runtime: " + str(sum(elapsed_times)) + " seconds")


def largest_difference(sequence):
    max_diff = abs(sequence[0]-sequence[1])
    for i in range(len(sequence)-1):
        for j in range(i+1, len(sequence)):
            diff = abs(sequence[i] - sequence[j])
            if max_diff < diff:
                max_diff = diff
    return max_diff

def smallest_difference(sequence):
    min_diff = abs(sequence[0]-sequence[1])
    for i in range(len(sequence)-1):
        for j in range(i+1, len(sequence)):
            diff = abs(sequence[i] - sequence[j])
            if min_diff > diff:
                min_diff = diff
    return min_diff

def smallest_difference2(sequence):
    if len(sequence) < 2:
        return 0  # Handling edge case where the sequence has fewer than 2 elements.

    # Sort the sequence.
    sequence.sort()

    # Initialize min_diff with the difference of the first two elements.
    min_diff = abs(sequence[1] - sequence[0])

    # Iterate through sorted sequence to find the smallest difference.
    for i in range(1, len(sequence) - 1):
        # Compute difference between consecutive elements.
        diff = abs(sequence[i + 1] - sequence[i])

        # Update min_diff if a smaller difference is found.
        if diff < min_diff:
            min_diff = diff

    return min_diff


# plot_time(smallest_difference,300)
# plot_time(smallest_difference2,300)
strTest='abcccc'
findStr='ccc'
print(strTest.count(findStr))
print(strTest.find(findStr))