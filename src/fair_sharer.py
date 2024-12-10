def fair_sharer(values, num_iterations, share=0.1):
    """
    Verteilt die höchste Zahl über die Nachbarn.

    Args:
        values (list): Eine Liste von Zahlen.
        num_iterations (int): Anzahl der Iterationen.
        share (float): Anteil, der verteilt wird.

    Returns:
        list: Neue Liste nach den Iterationen.
    """
    for _ in range(num_iterations):
        max_value = max(values)
        max_index = values.index(max_value)

        left_index = (max_index - 1) % len(values)
        right_index = (max_index + 1) % len(values)

        values[max_index] -= 2 * max_value * share
        values[left_index] += max_value * share
        values[right_index] += max_value * share
        values = [int(value) for value in values]


    return values
