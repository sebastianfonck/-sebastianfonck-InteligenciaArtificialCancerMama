import numpy as np
import pandas as pd

import tools

#data = tools.cargar_aborto_autorizado()
#tools.mostrar_info(data)

todos = tools.cargar_todos_los_datasets()
for key in todos:
    tools.mostrar_info(todos[key], key)

