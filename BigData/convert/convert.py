import json
import pandas as pd
import os
# # JSON Business
# file_path = r"G:\Descargas\yelp_academic_dataset_business.json"
# labels_business = [
#     "business_id",
#     "name",
#     "city",
#     "review_count",
#     "categories",
#     "stars",
#     "longitude",
#     "latitude",
# ]
# data = []
# with open(file_path, "r",encoding="utf-8") as f:
#     for i, line in enumerate(f):
#         try:
#             data.append(json.loads(line))  # Cargar cada línea como JSON
#         except json.JSONDecodeError as e:
#             print(f"Error en la línea {i+1}: {e}")
#             print(f"Línea problemática: {line}")


# # Convertir a DataFrame solo si no hubo errores
# if data:
#     df = pd.DataFrame(data)
#     print("Datos cargados correctamente")
#     print(df.info())  # Mostrar estructura del DataFrame

#     df = df[labels_business]
#     df = df.fillna("NULL")
#     # Reemplazar barras invertidas "\" en todas las columnas de tipo string
#     df = df.apply(lambda x: x.str.replace(r"\\", "", regex=True) if x.dtype == "object" else x)
#     df["categories"] = df["categories"].apply(lambda x: x.split(", ") if isinstance(x, str) else x)
#     # Asegurar que las comas y comillas estén correctamente escapadas
#     df["name"] = df["name"].apply(lambda x: json.dumps(x)[1:-1] if isinstance(x, str) else x)

#     df.to_json("business_clean.json",orient="records",lines=True)

# JSON Review
file_path = r"G:\Descargas\yelp_academic_dataset_review.json"
output_dir = r"yelp_split_reviews"
os.makedirs(output_dir, exist_ok=True)

labels_review = [
    "review_id",
    "user_id",
    "business_id",
    "stars",
    "text",
    "cool",
    "review_date"  # Cambiar el nombre aquí
]

chunk_size = 200 * 1024 * 1024  # 200MB en bytes
current_chunk = 1
data = []
current_size = 0

with open(file_path, "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        try:
            review = json.loads(line)
            
            # Normalizar votos
            if "votes" in review:
                votes = review["votes"]
                review["funny"] = votes.get("funny", 0)
                review["useful"] = votes.get("useful", 0)
                review["cool"] = votes.get("cool", 0)
                del review["votes"]

            # Renombrar "date" a "review_date"
            review["review_date"] = review.pop("date", None)
            
            data.append(review)
            current_size += len(line.encode("utf-8"))
            
            if current_size >= chunk_size:
                df = pd.DataFrame(data)[labels_review]
                df = df.fillna("NULL")
                df = df.apply(lambda x: x.str.replace(r"\\", "", regex=True) if x.dtype == "object" else x)
                output_file = os.path.join(output_dir, f"review_clean_part{current_chunk}.json")
                df.to_json(output_file, orient="records", lines=True)
                print(f"Chunk {current_chunk} guardado ({current_size / (1024 * 1024):.2f} MB)")
                
                # Reset para el siguiente chunk
                current_chunk += 1
                data = []
                current_size = 0
        
        except json.JSONDecodeError as e:
            print(f"Error en la línea {i+1}: {e}")
            print(f"Línea problemática: {line}")

# Guardar cualquier dato restante
if data:
    df = pd.DataFrame(data)[labels_review]
    df = df.fillna("NULL")
    df = df.apply(lambda x: x.str.replace(r"\\", "", regex=True) if x.dtype == "object" else x)
    output_file = os.path.join(output_dir, f"review_clean_part{current_chunk}.json")
    df.to_json(output_file, orient="records", lines=True)
    print(f"Último chunk {current_chunk} guardado ({current_size / (1024 * 1024):.2f} MB)")

print("División y limpieza completadas.")