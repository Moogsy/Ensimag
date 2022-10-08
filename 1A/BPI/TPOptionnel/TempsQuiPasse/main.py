import time
start = time.perf_counter()
time.sleep(10)
end = time.perf_counter()
print(f"Real time: {end - start} seconds")
