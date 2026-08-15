import time

def optimize_performance(data):
    start_time = time.time()
    processed_data = [process_item(item) for item in data]
    end_time = time.time()
    print(f'Processing took {end_time - start_time:.2f} seconds')
    return processed_data

def process_item(item):
    # Simulate a processing operation
    return item * 2

if __name__ == '__main__':
    sample_data = range(1000000)
    result = optimize_performance(sample_data)