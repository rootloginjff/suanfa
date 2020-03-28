from collections import deque

maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,1,0,0,1],
    [1,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

dirs = [
    lambda x,y :(x-1,y),
    lambda x,y :(x,y+1),
    lambda x,y :(x+1,y),
    lambda x,y :(x,y-1)
]

def deep_search_maze(x1,y1,x2,y2):
    stack = []
    stack.append((x1,y1))
    maze[x1][y1] = 2
    while len(stack) > 0:
        current_node = stack[-1]
        if current_node == (x2,y2):
            print(stack)
            return True
        for d in dirs:
            next_node = d(*current_node)
            if maze[next_node[0]][next_node[1]] == 0:
                stack.append(next_node)
                maze[next_node[0]][next_node[1]] = 2
                break
        else:
            stack.pop()
    else:
        print("无路")
        return False

def guang_search_maze(x1,y1,x2,y2):
    q = deque()
    q.append((x1,y1,-1))
    maze[x1][y1] = 2
    traceback = []
    while len(q) > 0:
        current_node = q.popleft()
        traceback.append(current_node)
        if current_node[:2] == (x2,y2):
            path = []
            i = len(traceback)-1
            while i>=0:
                path.append(traceback[i][0:2])
                i = traceback[i][2]
                traceback.pop()

            path.reverse()
            print(path)
            return True

        for d in dirs:
            next_x, next_y = d(current_node[0], current_node[1])
            if maze[next_x][next_y] == 0:
                q.append((next_x, next_y, len(traceback)-1))
                maze[next_x][next_y] = 2

    else:
        print("无路")
        return False

# deep_search_maze(1,1,8,8)
guang_search_maze(1,1,8,8)