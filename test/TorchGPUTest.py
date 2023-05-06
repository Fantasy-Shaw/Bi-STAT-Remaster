import torch

if __name__ == "__main__":
    print("Torch version:", torch.__version__)
    print("CUDA:", torch.cuda.is_available())
    print("CUDNN:", torch.has_cudnn)
    print("GPU Name:", torch.cuda.get_device_name(0))
