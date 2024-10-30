import h5py

# Intentar abrir el archivo HDF5
file_name = 'mlp_model.h5'

with h5py.File(file_name, 'r') as f:
    # Listar todas las claves en el archivo
    def print_structure(name, obj):
        if isinstance(obj, h5py.Group):
            print(f"Grupo: {name}")
        elif isinstance(obj, h5py.Dataset):
            print(f"Dataset: {name} - Shape: {obj.shape}, Dtype: {obj.dtype}")

    f.visititems(print_structure)