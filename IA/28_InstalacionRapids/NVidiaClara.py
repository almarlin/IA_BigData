import torch
from monai.networks.nets import UNet
from monai.losses import DiceLoss
from monai.metrics import DiceMetric
from monai.transforms import (
    Compose,
    LoadImage,
    AddChannel,
    ScaleIntensity,
    Resize,
    RandRotate,
    RandFlip,
    ToTensor,
)
from monai.data import Dataset, DataLoader
from monai.utils import set_determinism

# 1. Configuración inicial
set_determinism(seed=42)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 2. Definir transformaciones
train_transforms = Compose([
    LoadImage(image_only=True),
    AddChannel(),
    ScaleIntensity(),
    Resize((128, 128, 128)),
    RandRotate(range_x=15, prob=0.5),
    RandFlip(prob=0.5),
    ToTensor(),
])

val_transforms = Compose([
    LoadImage(image_only=True),
    AddChannel(),
    ScaleIntensity(),
    Resize((128, 128, 128)),
    ToTensor(),
])

# 3. Cargar datos (ejemplo sintético)
# Nota: Reemplazar con rutas reales del dataset BraTS
train_data = [{"image": "path/to/mri.nii", "label": "path/to/label.nii"} for _ in range(10)]
val_data = [{"image": "path/to/mri_val.nii", "label": "path/to/label_val.nii"} for _ in range(2)]

train_ds = Dataset(data=train_data, transform=train_transforms)
train_loader = DataLoader(train_ds, batch_size=2, shuffle=True)

val_ds = Dataset(data=val_data, transform=val_transforms)
val_loader = DataLoader(val_ds, batch_size=1)

# 4. Inicializar modelo, pérdida y optimizador
model = UNet(
    spatial_dims=3,
    in_channels=1,
    out_channels=2,  # 1 clase de tumor + fondo
    channels=(16, 32, 64, 128, 256),
    strides=(2, 2, 2, 2),
).to(device)

loss_function = DiceLoss(to_onehot_y=True)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)

# 5. Entrenamiento
max_epochs = 5
val_interval = 1

for epoch in range(max_epochs):
    model.train()
    epoch_loss = 0
    for batch in train_loader:
        inputs, labels = batch["image"].to(device), batch["label"].to(device)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = loss_function(outputs, labels)
        loss.backward()
        optimizer.step()
        epoch_loss += loss.item()
    print(f"Epoch {epoch + 1}/{max_epochs}, Loss: {epoch_loss:.4f}")

    # Validación
    if (epoch + 1) % val_interval == 0:
        model.eval()
        metric = DiceMetric(include_background=False)
        with torch.no_grad():
            for val_batch in val_loader:
                inputs, labels = val_batch["image"].to(device), val_batch["label"].to(device)
                outputs = model(inputs)
                metric(y_pred=outputs, y=labels)
        metric_value = metric.aggregate().item()
        print(f"Dice Score: {metric_value:.4f}")
        metric.reset()

