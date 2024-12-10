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
        max_index = values.index(max(values))  # Finde den Index des höchsten Wertes
        left_index = (max_index - 1) % n  # Linker Nachbar (zyklisch)
        right_index = (max_index + 1) % n  # Rechter Nachbar (zyklisch)

        # Teile den Wert auf
        transfer = values[max_index] * share
        values[max_index] -= 2 * transfer  # Ziehe den doppelten Transferwert vom Max-Wert ab
        values[left_index] += transfer  # Addiere zum linken Nachbarn
        values[right_index] += transfer  # Addiere zum rechten Nachbarn

        # Debug-Ausgabe
        print(f"Iteration: {_ + 1}")
        print(f"Max Index: {max_index}, Transfer: {transfer}")
        print(f"Values: {values}")
