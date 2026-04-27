import time
import statistics
import sys
import os
sys.path.append(os.getcwd())
from neuro_edu.engine import UltimateClassroom

def run_benchmark():
    print("Starting ACLAS Neuro-Edu Performance Benchmark...")
    
    # 1. Initialization Latency
    start_time = time.perf_counter()
    classroom = UltimateClassroom()
    classroom.setup(50)
    init_time = time.perf_counter() - start_time
    print(f"OK: Initialization (50 agents): {init_time:.4f}s")
    
    # 2. Simulation Step (Tick) Latency
    ticks = 100
    tick_times = []
    for _ in range(ticks):
        start_tick = time.perf_counter()
        classroom.broadcast("Benchmark instruction", 0.5, {"logic": 0.5})
        tick_times.append(time.perf_counter() - start_tick)
    
    avg_tick = statistics.mean(tick_times)
    ticks_per_sec = 1.0 / avg_tick
    print(f"OK: Simulation Performance: {avg_tick:.6f}s/tick ({ticks_per_sec:.2f} ticks/s)")
    
    # 3. Training Latency (1 epoch)
    start_train = time.perf_counter()
    classroom.run_training(epochs=1)
    train_time = time.perf_counter() - start_train
    print(f"OK: Training Performance (1 epoch, 50 agents): {train_time:.4f}s")
    
    print("\nBenchmark Results Summary:")
    print("| Metric | Value |")
    print("|---|---|")
    print(f"| Init Time | {init_time:.4f}s |")
    print(f"| Avg Tick | {avg_tick:.6f}s |")
    print(f"| Ticks/sec | {ticks_per_sec:.2f} |")
    print(f"| Train/Epoch | {train_time:.4f}s |")

if __name__ == "__main__":
    run_benchmark()
