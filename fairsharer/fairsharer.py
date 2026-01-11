def fair_sharer(values, num_iterations, share=0.1):
    """Runs num_iterations.
    In each iteration the highest value in "values" gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neighbor of the rightmost field.

    Examples:
    fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]

    Args:
    values:
        1D array of values (list or numpy array)
    num_iterations: Integer to set the number of iterations
    share: Fraction of the value to be shared (default 0.1)
    """
    values_new = list(values)
    n = len(values_new)

    for _ in range(num_iterations):
        max_value = max(values_new)
        index = values_new.index(max_value)

        share_amount = max_value * share
        left = (index - 1) % n
        right = (index + 1) % n

        values_new[left] += share_amount
        values_new[right] += share_amount
        values_new[index] -= 2 * share_amount

    return values_new

