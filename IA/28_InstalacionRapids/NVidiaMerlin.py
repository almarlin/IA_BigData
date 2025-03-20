
# Utilizar el contenedor de nvidiaMerlin: sudo docker run --gpus all -it --rm     -v /mnt/c/Users/alumno/Desktop/Alvaro_IABIGDATA/IA_BigData/IA/28_InstalacionRapids:/workspace     nvcr.io/nvidia/merlin/merlin-pytorch:nightly
# Importar las librerias correctas
# Instalarlas en el contenedor: pip install nvtabular / pip install hugectr
# Comprobaciones:
# # Verificar versión de PyTorch
# python -c "import torch; print('Versión de PyTorch:', torch.__version__); print('¿CUDA está disponible?:', torch.cuda.is_available())"

# # Verificar el nombre de la GPU
# python -c "import torch; print('Nombre de la GPU:', torch.cuda.get_device_name(0))"
# # Verificar CUDF
# python -c "import cudf; df = cudf.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]}); print(df)"
# 


import torch
import cudf
from nvtabular import Workflow, ColumnSelector, Dataset
from nvtabular.ops import FillMissing, Normalize, Categorify
from dask.distributed import Client

# 1. Verificar PyTorch y la GPU
print("=" * 40)
print("Verificando PyTorch y la GPU...")
print(f"Versión de PyTorch: {torch.__version__}")
print(f"¿CUDA está disponible?: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"Nombre de la GPU: {torch.cuda.get_device_name(0)}")
print("=" * 40)

# 2. Verificar cuDF
print("Verificando cuDF...")
df = cudf.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
print("DataFrame de cuDF:")
print(df)
print("=" * 40)

# 3. Verificar Dask y configurar el cliente
print("Verificando Dask...")
# Iniciar un cliente Dask
client = Client()
print(f"Cliente Dask iniciado: {client}")

# 4. Verificar NVTabular
print("Verificando NVTabular...")

# Crear datos de ejemplo
data = cudf.DataFrame({
    "user_id": [1, 2, 3, 4, 5],
    "movie_id": [10, 20, 30, 40, 50],
    "rating": [5, 4, 3, 2, 1]
})

# Convertir el DataFrame de cuDF en un Dataset de NVTabular
dataset = Dataset(data)

# Definir las columnas categóricas y continuas
cat_columns = ["user_id", "movie_id"]
cont_columns = ["rating"]

# Crear un workflow
workflow = Workflow(
    # Preprocesamiento para columnas categóricas
    cat_columns >> Categorify() >> FillMissing(fill_val=0),
    # Preprocesamiento para columnas continuas
    cont_columns >> Normalize()
)

# Aplicar el workflow
workflow.fit(dataset)
processed_data = workflow.transform(dataset)

print("Datos procesados con NVTabular:")
print(processed_data.compute())  # Convertir el Dataset de vuelta a un DataFrame para imprimir
print("=" * 40)

print("¡Todas las verificaciones se completaron con éxito!")
