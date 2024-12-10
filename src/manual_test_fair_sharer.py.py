import sys
import os

# Den Ordner "src" zum Suchpfad hinzufügen
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fair_sharer import fair_sharer

result = fair_sharer([0, 1000, 800, 0], 1)
print(result)  #[100, 800, 900, 0]