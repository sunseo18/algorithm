# 그래프 연결된 간선들 알려주는 함수
def bfs_result(n, wires_array, removed_wires):
    wires_array[removed_wires[0]][removed_wires[1]] = 0
    wires_array[removed_wires[1]][removed_wires[0]] = 0
    result_array = []
    visited = [False] * (n+1)
    
    node_no_list = []
    for node in range(1, n+1):
        # print("시작지점: "+ str(node))
        node_no = 0
        queue = [node]
        
        while queue:
            node = queue.pop(0)

            if not visited[node]:
                # print(f"{str(node)} 방문")
                node_no += 1
                visited[node] = True
                
                for i in range(1, n+1):
                    if wires_array[node][i] == 1 and not visited[i]:
                        queue.append(i)
                        
        if node_no != 0:
            node_no_list.append(node_no)
            # print(node_no_list)
            
    wires_array[removed_wires[0]][removed_wires[1]] = 1
    wires_array[removed_wires[1]][removed_wires[0]] = 1

    if len(node_no_list) > 2:
        return None
    else:
        return abs(node_no_list[0] - node_no_list[1])
    
def solution(n, wires):
    min = 10000000
    wires_length = len(wires)
    wires_array = [[0 for _ in range(n+1)] for _ in range(n+1)]
        
    for wire in wires:
        wires_array[wire[0]][wire[1]] = 1
        wires_array[wire[1]][wire[0]] = 1
    
    for i in range(wires_length):
        removed_wire = wires[i]
        result = bfs_result(n, wires_array, removed_wire)
    
        if result < min:
            min = result

    return min