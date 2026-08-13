import time

def time_execution(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Execution time for {func.__name__}: {end_time - start_time:.4f} seconds')
        return result
    return wrapper

@time_execution
def calculate_score(level, time_taken):
    base_score = 1000
    return base_score - (level * 50) - (time_taken * 10)

@time_execution
def generate_leaderboard(scores):
    return sorted(scores.items(), key=lambda item: item[1], reverse=True)

@time_execution
def level_completion(level, time_taken):
    return calculate_score(level, time_taken) > 500
