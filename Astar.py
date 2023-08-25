from queue import PriorityQueue
GRAPH = {\
            'Arad': {'Sibiu': 140, 'Zerind': 75, 'Timisoara': 118},\
            'Zerind': {'Arad': 75, 'Oradea': 71},\
            'Oradea': {'Zerind': 71, 'Sibiu': 151},\
            'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vikea': 80},\
            'Timisoara': {'Arad': 118, 'Lugoj': 111},\
            'Lugoj': {'Timisoara': 111, 'Mehadia': 70},\
            'Mehadia': {'Lugoj': 70, 'Drobeta': 75},\
            'Drobeta': {'Mehadia': 75, 'Craiova': 120},\
            'Craiova': {'Drobeta': 120, 'Rimnicu Vikea': 146, 'Pitesti': 138},\
            'Rimnicu Vikea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},\
            'Fagaras': {'Sibiu': 99, 'Bucharest': 211},\
            'Pitesti': {'Rimnicu Vikea': 97, 'Craiova': 138, 'Bucharest': 101},\
            'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},\
            'Giurgiu': {'Bucharest': 90},\
            'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},\
            'Hirsova': {'Urziceni': 98, 'Eforie': 86},\
            'Eforie': {'Hirsova': 86},\
            'Vaslui': {'Iasi': 92, 'Urziceni': 142},\
            'Iasi': {'Vaslui': 92, 'Neamt': 87},\
            'Neamt': {'Iasi': 87}\
        }

def a_star(Start, destination):
    #Đường đi tối ưu từ Xuất phát đến đích sử dụng phương pháp phỏng đoán khoảng cách đường thẳng
    #Start: Bắt đầu tên thành phố
    #destination: Tên thành phố điểm đến
    # Trả Giá trị kinh nghiệm, chi phí và đường dẫn để truyền tải tối ưu

    straight_line = {\
                        'Arad': 366,\
                        'Zerind': 374,\
                        'Oradea': 380,\
                        'Sibiu': 253,\
                        'Timisoara': 329,\
                        'Lugoj': 244,\
                        'Mehadia': 241,\
                        'Drobeta': 242,\
                        'Craiova': 160,\
                        'Rimnicu Vikea': 193,\
                        'Fagaras': 176,\
                        'Pitesti': 100,\
                        'Bucharest': 0,\
                        'Giurgiu': 77,\
                        'Urziceni': 80,\
                        'Hirsova': 151,\
                        'Eforie': 161,\
                        'Vaslui': 199,\
                        'Iasi': 226,\
                        'Neamt': 234\
                    }
    
    priority_queue, visited = PriorityQueue(), {}
    priority_queue.put((straight_line[Start], 0, Start, [Start]))
    visited[Start] = straight_line[Start]
    while not priority_queue.empty():
        (heuristic, cost, vertex, path) = priority_queue.get()
        if vertex == destination:
            return heuristic, cost, path
        for next_node in GRAPH[vertex].keys():
            current_cost = cost + GRAPH[vertex][next_node]
            heuristic = current_cost + straight_line[next_node]
            if not next_node in visited or visited[next_node] >= heuristic:
                visited[next_node] = heuristic
                priority_queue.put((heuristic, current_cost, next_node, path + [next_node]))

def main():
    Start = 'Arad'
    End = 'Bucharest'
    if Start not in GRAPH or End not in GRAPH:
        print('ERROR: Thanh pho khong ton tai!')
    else:
        print("=======================================================")    
        print("Chuong trinh thuat toan A star cho bai toan Romania")
        print("Arad ==> Bucharest")
        print("=======================================================")
        heuristic, cost, optimal_path = a_star(Start, End)
        print(' -> '.join(city for city in optimal_path))
        print('Khoang cach cua Arad ==> Bucharest:', heuristic)
        

if __name__ == '__main__':
    main()