# Tóm Tắt Cấu Trúc Dữ Liệu trong `util.py`

File `util.py` cung cấp các cấu trúc dữ liệu và hàm tiện ích hỗ trợ cho việc triển khai các thuật toán tìm kiếm trong Pacman.

---

## 1. Stack (Ngăn xếp)
**Mô tả:** Container hoạt động theo nguyên tắc **LIFO** (Last-In-First-Out - Vào sau ra trước).

| Phương thức | Mô tả |
|-------------|-------|
| `push(item)` | Đẩy phần tử vào đỉnh stack |
| `pop()` | Lấy và xóa phần tử ở đỉnh stack |
| `isEmpty()` | Kiểm tra stack có rỗng không |

**Ứng dụng:** Thuật toán **DFS** (Depth-First Search).

---

## 2. Queue (Hàng đợi)
**Mô tả:** Container hoạt động theo nguyên tắc **FIFO** (First-In-First-Out - Vào trước ra trước).

| Phương thức | Mô tả |
|-------------|-------|
| `push(item)` | Thêm phần tử vào cuối hàng đợi |
| `pop()` | Lấy và xóa phần tử đầu tiên trong hàng đợi |
| `isEmpty()` | Kiểm tra hàng đợi có rỗng không |

**Ứng dụng:** Thuật toán **BFS** (Breadth-First Search).

---

## 3. PriorityQueue (Hàng đợi ưu tiên)
**Mô tả:** Hàng đợi ưu tiên sử dụng **heap** để truy xuất phần tử có độ ưu tiên thấp nhất với độ phức tạp **O(1)**.

| Phương thức | Mô tả |
|-------------|-------|
| `push(item, priority)` | Thêm phần tử với độ ưu tiên chỉ định |
| `pop()` | Lấy và xóa phần tử có độ ưu tiên thấp nhất |
| `isEmpty()` | Kiểm tra hàng đợi có rỗng không |

> **Lưu ý:** Không hỗ trợ thay đổi độ ưu tiên của phần tử đã thêm, nhưng có thể thêm cùng phần tử với các độ ưu tiên khác nhau.

**Ứng dụng:** Thuật toán **UCS** (Uniform Cost Search), **A\***.

---

## 4. PriorityQueueWithFunction
**Mô tả:** Kế thừa từ `PriorityQueue`, tự động tính độ ưu tiên thông qua hàm được cung cấp.

| Phương thức | Mô tả |
|-------------|-------|
| `__init__(priorityFunction)` | Khởi tạo với hàm tính độ ưu tiên |
| `push(item)` | Thêm phần tử (độ ưu tiên được tính tự động) |

**Ứng dụng:** Thay thế trực tiếp cho Stack/Queue trong các thuật toán cần hàm đánh giá.

---

## 5. Counter
**Mô tả:** Mở rộng từ `dict`, chuyên biệt cho việc đếm với giá trị mặc định là **0**.

| Phương thức | Mô tả |
|-------------|-------|
| `incrementAll(keys, count)` | Tăng tất cả keys lên cùng một giá trị |
| `argMax()` | Trả về key có giá trị cao nhất |
| `sortedKeys()` | Trả về danh sách keys sắp xếp theo giá trị giảm dần |
| `totalCount()` | Tổng tất cả giá trị |
| `normalize()` | Chuẩn hóa để tổng = 1 |
| `divideAll(divisor)` | Chia tất cả giá trị cho divisor |
| `copy()` | Tạo bản sao |

**Toán tử hỗ trợ:**
- `+` / `-` : Cộng/trừ hai Counter
- `*` : Tích vô hướng (dot product)

---

## 6. Các Hàm Tiện Ích

### Hàm Khoảng Cách
| Hàm | Mô tả |
|-----|-------|
| `manhattanDistance(xy1, xy2)` | Tính khoảng cách Manhattan giữa 2 điểm |

### Hàm Xác Suất
| Hàm | Mô tả |
|-----|-------|
| `normalize(vectorOrCounter)` | Chuẩn hóa vector hoặc Counter |
| `sample(distribution, values)` | Lấy mẫu từ phân phối xác suất |
| `nSample(distribution, values, n)` | Lấy n mẫu từ phân phối |
| `flipCoin(p)` | Trả về True với xác suất p |
| `chooseFromDistribution(distribution)` | Chọn từ phân phối |

### Hàm Ma Trận & Grid
| Hàm | Mô tả |
|-----|-------|
| `nearestPoint(pos)` | Tìm điểm lưới gần nhất (làm tròn) |
| `arrayInvert(array)` | Đảo ngược ma trận (transpose) |
| `matrixAsList(matrix, value)` | Chuyển ma trận thành danh sách tọa độ |

### Hàm Khác
| Hàm | Mô tả |
|-----|-------|
| `sign(x)` | Trả về 1 hoặc -1 tùy theo dấu của x |
| `lookup(name, namespace)` | Lấy method/class từ module đã import |
| `pause()` | Tạm dừng chờ người dùng nhấn Enter |

---

## 7. TimeoutFunction
**Mô tả:** Class xử lý timeout cho các hàm, sử dụng signal (chỉ hoạt động trên Unix).

| Thành phần | Mô tả |
|------------|-------|
| `__init__(function, timeout)` | Khởi tạo với hàm và thời gian timeout (giây) |
| `__call__(*args)` | Gọi hàm với timeout |
| `TimeoutFunctionException` | Exception khi timeout |

---

## Sơ đồ Kế thừa

```
dict
 └── Counter

PriorityQueue
 └── PriorityQueueWithFunction

Exception
 └── TimeoutFunctionException
```

---

## Tổng kết Ứng dụng trong Thuật toán Tìm kiếm

| Cấu trúc | Thuật toán |
|----------|------------|
| `Stack` | DFS (Depth-First Search) |
| `Queue` | BFS (Breadth-First Search) |
| `PriorityQueue` | UCS, A*, Greedy Search |
| `manhattanDistance` | Heuristic cho A* |

---

# Các Bài Tập Cần Thực Hiện trong `search.py`

File `search.py` yêu cầu bạn triển khai **4 thuật toán tìm kiếm** cho Pacman. Mỗi hàm cần trả về danh sách các hành động (actions) để đưa Pacman từ vị trí xuất phát đến đích.

---

## Bài 1: Depth First Search (DFS)

**Hàm:** `depthFirstSearch(problem)`

**Mô tả:** Tìm kiếm theo chiều sâu - duyệt node sâu nhất trước.

**Yêu cầu:**
- [ ] Triển khai thuật toán Graph Search (tránh duyệt lại state đã thăm)
- [ ] Sử dụng `util.Stack` làm cấu trúc dữ liệu fringe
- [ ] Trả về danh sách actions từ start đến goal

**Gợi ý:**
```python
# Các phương thức của problem cần dùng:
problem.getStartState()      # Lấy state bắt đầu
problem.isGoalState(state)   # Kiểm tra state có phải goal không
problem.getSuccessors(state) # Trả về [(successor, action, cost), ...]
```

**Test:** `python pacman.py -l tinyMaze -p SearchAgent`

---

## Bài 2: Breadth First Search (BFS)

**Hàm:** `breadthFirstSearch(problem)`

**Mô tả:** Tìm kiếm theo chiều rộng - duyệt node nông nhất trước.

**Yêu cầu:**
- [ ] Triển khai thuật toán Graph Search
- [ ] Sử dụng `util.Queue` làm cấu trúc dữ liệu fringe
- [ ] Đảm bảo tìm được đường đi ngắn nhất (số bước ít nhất)

**Test:** `python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs`

---

## Bài 3: Uniform Cost Search (UCS)

**Hàm:** `uniformCostSearch(problem)`

**Mô tả:** Tìm kiếm chi phí đồng nhất - duyệt node có tổng chi phí thấp nhất trước.

**Yêu cầu:**
- [ ] Triển khai thuật toán Graph Search
- [ ] Sử dụng `util.PriorityQueue` với priority = tổng chi phí đường đi
- [ ] Đảm bảo tìm được đường đi có chi phí tối thiểu

**Lưu ý:** UCS khác BFS ở chỗ nó xét chi phí của mỗi bước, không chỉ số bước.

**Test:** `python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs`

---

## Bài 4: A* Search

**Hàm:** `aStarSearch(problem, heuristic=nullHeuristic)`

**Mô tả:** Tìm kiếm A* - kết hợp chi phí thực tế và heuristic để định hướng tìm kiếm.

**Yêu cầu:**
- [ ] Triển khai thuật toán Graph Search
- [ ] Sử dụng `util.PriorityQueue` với priority = g(n) + h(n)
  - `g(n)` = chi phí từ start đến node hiện tại
  - `h(n)` = heuristic ước lượng chi phí từ node đến goal
- [ ] Hỗ trợ nhận heuristic function làm tham số

**Test:** `python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic`

---

## Template Code Gợi Ý

```python
def genericSearch(problem, fringe):
    """
    Template chung cho các thuật toán tìm kiếm.
    fringe: Stack (DFS), Queue (BFS), hoặc PriorityQueue (UCS, A*)
    """
    visited = set()  # Tập các state đã thăm
    
    # Mỗi node trong fringe: (state, actions_to_reach_state)
    start = problem.getStartState()
    fringe.push((start, []))
    
    while not fringe.isEmpty():
        state, actions = fringe.pop()
        
        if problem.isGoalState(state):
            return actions
        
        if state not in visited:
            visited.add(state)
            
            for successor, action, cost in problem.getSuccessors(state):
                if successor not in visited:
                    new_actions = actions + [action]
                    fringe.push((successor, new_actions))
    
    return []  # Không tìm thấy đường đi
```

---

## Bảng Tổng Hợp

| Thuật toán | Cấu trúc dữ liệu | Độ phức tạp | Tối ưu? | Đầy đủ? |
|------------|------------------|-------------|---------|---------|
| DFS | `Stack` | O(b^m) | ❌ | ❌ |
| BFS | `Queue` | O(b^d) | ✅ (chi phí đều) | ✅ |
| UCS | `PriorityQueue` | O(b^(C*/ε)) | ✅ | ✅ |
| A* | `PriorityQueue` | Phụ thuộc h | ✅ (h admissible) | ✅ |

> **Chú thích:** b = branching factor, d = depth of solution, m = max depth, C* = optimal cost, ε = min step cost
