import torch

# Assuming your image tensor shape is currently (Height, Width, Channels)
image_hwc = torch.randn(224, 224, 3) 

# Convert HWC to PyTorch's expected CHW format
image_chw = image_hwc.permute(2, 0, 1)  # Target Shape: (3, 224, 224)
