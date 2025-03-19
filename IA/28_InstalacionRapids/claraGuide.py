# Se necesita docker en wsl:ubuntu
# Una vez instalado, en caso de error hay que modificar un archivo
#  $ sudo nano /etc/systemd/system/docker.service.d/override.conf
# Eliminar este codigo # --add-runtime=/usr/bin/nvidia-container-runtime #
# Hacer pull de la imagen de docker con Nvidia Clara:
# $ export dockerImage=nvcr.io/nvidia/clara-train-sdk:v4.1
# $ docker pull $dockerImage
# Instalar cuda en docker (necesitamos la ruta de nuestra distribucion disponible en https://catalog.ngc.nvidia.com/orgs/nvidia/containers/cuda/tags)
# sudo docker run --rm --gpus all nvcr.io/nvidia/cuda:12.6.0-base-ubuntu20.04 nvidia-smi
# Esto deberá devolver lo mismo que nvidia-smi en la consola ubuntu
# Iniciar el contenedor:
# sudo docker run -it --rm --gpus all --shm-size=1G --ulimit memlock=-1 --ulimit stack=67108864 --ipc=host --net=host --mount type=bind,source=/mnt/c/Users/alumno/Desktop/Alvaro_IABIGDATA/IA_BigData/IA/28_InstalacionRapids/,target=/workspace/data $dockerImage /bin/bash
# Una vez iniciado veremos algo como esto:
# =============
# == PyTorch ==
# =============

# NVIDIA Release 21.10 (build 28019337)
# PyTorch Version 1.10.0a0+0aef44c

# Container image Copyright (c) 2021, NVIDIA CORPORATION & AFFILIATES. All rights reserved.

# Copyright (c) 2014-2021 Facebook Inc.
# Copyright (c) 2011-2014 Idiap Research Institute (Ronan Collobert)
# Copyright (c) 2012-2014 Deepmind Technologies    (Koray Kavukcuoglu)
# Copyright (c) 2011-2012 NEC Laboratories America (Koray Kavukcuoglu)
# Copyright (c) 2011-2013 NYU                      (Clement Farabet)
# Copyright (c) 2006-2010 NEC Laboratories America (Ronan Collobert, Leon Bottou, Iain Melvin, Jason Weston)
# Copyright (c) 2006      Idiap Research Institute (Samy Bengio)
# Copyright (c) 2001-2004 Idiap Research Institute (Ronan Collobert, Samy Bengio, Johnny Mariethoz)
# Copyright (c) 2015      Google Inc.
# Copyright (c) 2015      Yangqing Jia
# Copyright (c) 2013-2016 The Caffe contributors
# All rights reserved.

# NVIDIA Deep Learning Profiler (dlprof) Copyright (c) 2021, NVIDIA CORPORATION & AFFILIATES.  All rights reserved.

# Various files include modifications (c) NVIDIA CORPORATION & AFFILIATES.  All rights reserved.

# This container image and its contents are governed by the NVIDIA Deep Learning Container License.
# By pulling and using the container, you accept the terms and conditions of this license:
# https://developer.nvidia.com/ngc/nvidia-deep-learning-container-license
# WARNING: Detected NVIDIA NVIDIA GeForce RTX 4060 GPU, which is not yet supported in this version of the container
# ERROR: No supported GPU(s) detected to run this container

# NOTE: MOFED driver for multi-node communication was not detected.
#       Multi-node communication performance may be reduced.

# root@docker-desktop:/opt/nvidia/medical# <Aquí se navega a /workspace/data y se ejecutan los ficheros que hagan falta para entrenar los modelos>

# ---CONCLUSIONES---
# *Nvidia clara-train-sdk no se puede utilizar con las gráficas GeForce RTX 4060 porque todavía no esta soportado por la version del contenedor*


import os
import torch
import numpy as np
from monai.data import DataLoader, Dataset
from monai.transforms import Compose, AddChannel, ScaleIntensity, RandSpatialCrop, ToTensor
from monai.networks.nets import UNet
from monai.losses import DiceLoss
from torch.optim import Adam

# 1. Configuración del entrenamiento
batch_size = 4
num_epochs = 10
learning_rate = 1e-4
output_dir = "/workspace/output"  # Ruta para guardar el modelo entrenado

# Crear el directorio de salida si no existe
os.makedirs(output_dir, exist_ok=True)

# 2. Generar datos sintéticos
def generate_synthetic_data(num_samples=16, image_size=(128, 128, 128)):
    """
    Genera imágenes y máscaras sintéticas en 3D.
    """
    images = []
    masks = []

    for _ in range(num_samples):
        # Generar una imagen sintética (ruido aleatorio)
        image = np.random.rand(*image_size).astype(np.float32)
        images.append(image)

        # Generar una máscara sintética (un cubo en el centro)
        mask = np.zeros(image_size, dtype=np.float32)
        center = (image_size[0] // 2, image_size[1] // 2, image_size[2] // 2)
        size = 32  # Tamaño del cubo
        mask[
            center[0] - size // 2 : center[0] + size // 2,
            center[1] - size // 2 : center[1] + size // 2,
            center[2] - size // 2 : center[2] + size // 2,
        ] = 1
        masks.append(mask)

    return images, masks

# Generar 16 imágenes y máscaras sintéticas
images, masks = generate_synthetic_data()

# 3. Definir transformaciones para preprocesar las imágenes
transforms = Compose([
    AddChannel(),  # Añadir un canal (las imágenes médicas suelen ser 3D)
    ScaleIntensity(),  # Normalizar la intensidad de la imagen
    RandSpatialCrop((96, 96, 96)),  # Recortar la imagen a un tamaño fijo
    ToTensor()  # Convertir a tensor de PyTorch
])

# 4. Crear un dataset y un DataLoader
train_data = [{"image": img, "mask": mask} for img, mask in zip(images, masks)]
train_dataset = Dataset(data=train_data, transform=transforms)
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

# 5. Definir el modelo (U-Net de MONAI)
model = UNet(
    spatial_dims=3,  # 3D
    in_channels=1,  # Un canal de entrada (imágenes en escala de grises)
    out_channels=1,  # Un canal de salida (máscara binaria)
    channels=(32, 64, 128, 256),  # Número de filtros en cada capa
    strides=(2, 2, 2),  # Reducción de tamaño en cada capa
    num_res_units=2  # Unidades residuales
).to("cuda")

# 6. Configurar el optimizador y la función de pérdida
optimizer = Adam(model.parameters(), lr=learning_rate)
loss_fn = DiceLoss()  # Pérdida basada en el coeficiente de Dice

# 7. Entrenar el modelo
for epoch in range(num_epochs):
    model.train()
    epoch_loss = 0

    for batch in train_loader:
        inputs = batch["image"].to("cuda")
        targets = batch["mask"].to("cuda")

        # Forward pass
        outputs = model(inputs)
        loss = loss_fn(outputs, targets)

        # Backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        epoch_loss += loss.item()

    print(f"Época {epoch + 1}/{num_epochs}, Pérdida: {epoch_loss / len(train_loader)}")

# 8. Guardar el modelo entrenado
torch.save(model.state_dict(), os.path.join(output_dir, "unet_model_monai.pth"))
print(f"Modelo entrenado guardado en '{os.path.join(output_dir, 'unet_model_monai.pth')}'")