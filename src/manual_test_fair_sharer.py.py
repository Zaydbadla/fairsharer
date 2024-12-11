import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from fair_sharer import fair_sharer

result = fair_sharer([0, 1000, 800, 0], 1)
print(result)  # Erwartetes Ergebnis: [100, 800, 900, 0]

