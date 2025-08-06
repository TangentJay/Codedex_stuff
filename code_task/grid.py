# code_task/grid.py
'''
* Author: TanB
* Created: 7/30/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
def decoding(data_points):
    max_x = max(point[0] for point in data_points)

    max_y = max(point[2] for point in data_points)

    grid = [[''   for _ in range(max_x + 1)]   for _ in range(max_y + 1)]

    for x, char, y in data_points:
        grid[y][x] = char

    for row in grid:
        print(''.join(row))


data_points = [(0, '', 0),
               (0, '', 1),
               (0, '', 2),
               
               (1, '', 1),
               (1, '', 2),
               (2, '', 1),
               (2, '', 2),
               (3, '', 2)]

 #█▀▀▀


decoding(data_points)