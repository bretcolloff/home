

def main(argv=None):
    with open("maze.txt") as file:
        maze = [list(line.strip()) for line in file]

        # print maze
        for line in maze:
            print (''.join(line))

        # Find the starting point.
        location = None
        for row in range(0, len(maze)):
            for col in range(0, len(maze[row])):
                if maze[row][col] == "S":
                    location = (row, col)

        routes = []
        routes.append([location])

        finished = False
        while not finished:
            # a = [b] + [1,2,3] // [b, 1, 2, 3]
            for route in list(routes):
                # print(route)
                (x, y) = route[0]
                if maze[x][y] == 'E':
                    # print finished maze
                    for datum in route:
                        (x, y) = datum
                        maze[x][y] = '.'

                    print ("----- SOLUTION -------")
                    for line in maze:
                        print (''.join(line))
                    return
                else:
                    routes.remove(route)

                # add new directions
                up = (x, y-1)
                down = (x,y+1)
                left = (x-1, y)
                right = (x+1, y)

                if x > 0 and maze[left[0]][left[1]] != '#' and not left in route:
                    newroute = [left] + list(route)
                    routes.append(newroute)
                if x < 21 and maze[right[0]][right[1]] != '#' and not right in route:
                    newroute = [right] + list(route)
                    routes.append(newroute)
                if y > 0 and maze[up[0]][up[1]] != '#' and not up in route:
                    newroute = [up] + list(route)
                    routes.append(newroute)
                if y < 21 and maze[down[0]][down[1]] != '#' and not down in route:
                    newroute = [down] + list(route)
                    routes.append(newroute)

if __name__ == '__main__':
  main()
