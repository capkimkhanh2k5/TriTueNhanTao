import heapq

class State:
    def __init__(self, water_levels, path_cost, heuristic):
        self.water_levels = water_levels
        self.path_cost = path_cost
        self.heuristic = heuristic
    
    def __lt__(self, other):
        return (self.path_cost + self.heuristic) < (other.path_cost + other.heuristic)

def pour_water(state, from_bucket, to_bucket, max_capacity):
    poured_water = min(state.water_levels[from_bucket], max_capacity - state.water_levels[to_bucket])
    new_water_levels = state.water_levels.copy()
    new_water_levels[from_bucket] -= poured_water
    new_water_levels[to_bucket] += poured_water
    return State(new_water_levels, state.path_cost + poured_water, 0)

def heuristic(state, target):
    return sum(abs(level - target[i]) for i, level in enumerate(state.water_levels))

def astar_search(N, M, capacities):
    initial_state = State([0] * N, 0, heuristic([0] * N, [M] + [0] * (N-1)))
    priority_queue = [initial_state]
    
    while priority_queue:
        current_state = heapq.heappop(priority_queue)
        
        if current_state.water_levels[0] == M:
            return current_state.water_levels
        
        for i in range(N):
            for j in range(N):
                if i != j:
                    next_state = pour_water(current_state, i, j, capacities[j])
                    next_state.heuristic = heuristic(next_state, [M] + [0] * (N-1))
                    heapq.heappush(priority_queue, next_state)

    return None

# Nhập dữ liệu
N = int(input("Nhập số lọ nước: "))
M = int(input("Nhập số lít nước cần múc: "))
capacities = list(map(int, input("Nhập dung tích của các lọ nước: ").split()))

print("OK")
# Gọi hàm A* search
result = astar_search(N, M, capacities)

# In kết quả
if result:
    print("Cách múc nước:")
    print(result)
else:
    print("Không có đáp án")

