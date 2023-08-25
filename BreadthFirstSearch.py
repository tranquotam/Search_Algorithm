from collections import deque
# Dưới đây liệt kê chi tiết tất cả tám chuyển động có thể có từ một ô
# (di chuyển trên, phải, dưới, trái và bốn đường chéo)
# Hàm kiểm tra xem có an toàn khi đi đến vị trí (x, y) không
# từ vị trí hiện tại. 
# Hàm trả về false nếu (x, y) không phải là tọa độ ma trận hợp lệ hoặc (x, y) đại diện cho nước
# Hoặc Vị trí (x, y) đã được xử lý.
def isSafe(Matrix, x, y, Proc):
    return (x >= 0) and (x < len(Proc)) and \
        (y >= 0) and (y < len(Proc[0])) and \
        (Matrix[x][y] == 1 and not Proc[x][y])
 
row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]

def BreadthFirstSearch(Matrix, Proc, i, j):
 
    # tạo một hàng đợi trống và nút nguồn xếp hàng
    Q = deque()
    Q.append((i, j))
 
    # đánh dấu nút nguồn là đã xử lý
    Proc[i][j] = True
 
    # vòng lặp cho đến khi hàng đợi trống
    while Q:
        x, y = Q.popleft()
 
        # kiểm tra tất cả tám chuyển động có thể có từ ô hiện tại
         # và xếp hàng từng chuyển động hợp lệ
        for k in range(8):
            #bỏ qua nếu vị trí không hợp lệ, hoặc đã được xử lý hoặc có nước
            if isSafe(Matrix, x + row[k], y + col[k], Proc):
                # bỏ qua nếu vị trí không hợp lệ hoặc đã có
                 # đã xử lý, hoặc bao gồm nước
                Proc[x + row[k]][y + col[k]] = True
                Q.append((x + row[k], y + col[k]))
 
 
if __name__ == '__main__':
 
    Matrix = [
        [1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
        [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
    ]
 
    (m, n) = (len(Matrix), len(Matrix[0]))
 
  # lưu trữ nếu một ô được xử lý hay không
    Proc = [[False for x in range(n)] for y in range(m)]
 
    island = 0
    for i in range(m):
        for j in range(n):
            # bắt đầu BFS từ mỗi nút chưa xử lý và số đảo tăng dần
            if Matrix[i][j] == 1 and not Proc[i][j]:
                BreadthFirstSearch(Matrix, Proc, i, j)
                island = island + 1
 
    print("Tong so dao la: ", island,"isLands")
    print()