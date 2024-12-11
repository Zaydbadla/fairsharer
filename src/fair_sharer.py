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
        max_index = values.index(max(values))
        share_value = values[max_index] * share
        values[max_index] -= 2 * share_value
        values[(max_index - 1) % len(values)] += share_value #wraps around 
        values[(max_index + 1) % len(values)] += share_value
    return values