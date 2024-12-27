import torch
import multiprocessing as mp
import time
import psutil
from itertools import count

def cpu_stress(process_num):
    """Function to stress a single CPU core"""
    print(f"Starting CPU stress process {process_num}")
    while True:
        _ = sum(1 * 1 for i in count(1))

def gpu_stress(gpu_id):
    """Function to stress a single GPU"""
    print(f"Starting GPU stress on device {gpu_id}")
    device = torch.device(f'cuda:{gpu_id}')
    
    # Create large tensors
    size = 5000
    while True:
        # Matrix multiplication is computationally intensive
        matrix1 = torch.randn(size, size, device=device)
        matrix2 = torch.randn(size, size, device=device)
        torch.matmul(matrix1, matrix2)
        torch.cuda.synchronize(device)

def main():
    # Get number of CPU cores
    cpu_cores = psutil.cpu_count(logical=True)
    
    # Get number of available GPUs
    gpu_count = torch.cuda.device_count()
    print(f"Found {gpu_count} GPUs and {cpu_cores} CPU cores")
    
    # Start GPU stress processes
    gpu_processes = []
    for gpu_id in range(gpu_count):
        p = mp.Process(target=gpu_stress, args=(gpu_id,))
        p.start()
        gpu_processes.append(p)
    
    # Start CPU stress processes
    cpu_processes = []
    for i in range(cpu_cores):
        p = mp.Process(target=cpu_stress, args=(i,))
        p.start()
        cpu_processes.append(p)
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping stress test...")
        for p in gpu_processes + cpu_processes:
            p.terminate()
            p.join()

if __name__ == "__main__":
    main()
