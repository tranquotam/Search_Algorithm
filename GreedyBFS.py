map = {
        'arad': ['sibiu', 'zerind', 'timisoara'],
        'sibiu': ['oradea', 'fagaras', 'rimnicu'],
        'zerind': ['arad', 'oradea'],
        'timisoara': ['arad', 'lugoj'],
        'oradea': ['zerind', 'sibiu'],
        'fagaras': ['sibiu', 'bucharest']
        }

def GreedyBFS(map, start, end):
    # duy trì một hàng đợi các đường dẫn
    queue = []
    # đẩy đường dẫn đầu tiên vào hàng đợi
    queue.append([start])
    while queue:
        # lấy đường dẫn đầu tiên từ hàng đợi
        path = queue.pop(0)
        # lấy nút cuối cùng từ đường dẫn
        node = path[-1]
        # tìm thấy đường dẫn
        if node == end:
            return path
        # liệt kê tất cả các nút liền kề, tạo một đường dẫn mới và đẩy nó vào hàng đợi
        for adjacent in map.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
            
           
start = "arad"
end = "bucharest"
print(GreedyBFS(map, start, end))