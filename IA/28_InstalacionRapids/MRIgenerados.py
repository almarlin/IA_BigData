import numpy as np
import nibabel as nib

# Crear una imagen 3D sintética (128x128x128)
image_data = np.random.rand(128, 128, 128)

# Crear una máscara sintética (por ejemplo, dos clases)
label_data = np.zeros((128, 128, 128))
label_data[64:96, 64:96, 64:96] = 1  # Clase 1 en una región 3D

# Guardar las imágenes como archivos .nii
image_nii = nib.Nifti1Image(image_data, np.eye(4))
label_nii = nib.Nifti1Image(label_data, np.eye(4))

nib.save(image_nii, 'mri.nii')
nib.save(label_nii, 'label.nii')
nib.save(image_nii, 'mri_val.nii')
nib.save(label_nii, 'label_val.nii')
