def board1():
    temp = [
        ['#', 'c1', 'c2'],
        ['c3', 0, 0],
        ['c4', 0, 0]
    ]
    constraints = {
        'c1': {'down': 11},
        'c2': {'down': 3},
        'c3': {'right': 3},
        'c4': {'right': 11}
    }

    return temp, constraints


def board2():
    temp = [
        ['#', 'c1', 'c2', 'c3'],
        ['c4', 0, 0, 0],
        ['c5', 0, 0, 0],
        ['c6', 0, 0, 0],
    ]
    constraints = {
        'c1': {'down': 19},
        'c2': {'down': 12},
        'c3': {'down': 7},
        'c4': {'right': 20},
        'c5': {'right': 10},
        'c6': {'right': 8}
    }
    return temp, constraints


def board3():
    temp = [
        ['#', 'c1', 'c2', '#', '#'],
        ['c3', 0, 0, 'c4', '#'],
        ['c5', 0, 0, 0, 'c6'],
        ['#', 'c7', 0, 0, 0],
        ['#', '#', 'c8', 0, 0]
    ]
    constraints = {
        'c1': {'down': 17},
        'c2': {'down': 23},
        'c3': {'right': 15},
        'c4': {'down': 6},
        'c5': {'right': 20},
        'c6': {'down': 16},
        'c7': {'right': 17},
        'c8': {'right': 10}
    }
    return temp, constraints


def board4():
    temp = [
        ['#', 'd1', 'd2', '#', '#'],
        ['d3', 0, 0, 'd4', '#'],
        ['d5', 0, 0, 0, 'd6'],
        ['#', 'd7', 0, 0, 0],
        ['#', '#', 'd8', 0, 0]
    ]
    constraints = {
        'd1': {'down': 11},
        'd2': {'down': 9},
        'd3': {'right': 4},
        'd4': {'down': 17},
        'd5': {'right':11},
        'd6': {'down': 9},
        'd7': {'right': 23},
        'd8': {'right': 8}
    }
    return temp, constraints


def board5():
    temp = [
        ['#', '#', 'c1', 'c2', 'c3', '#', 'c4', 'c5'],
        ['#', 'c6', 0, 0, 0, 'c7', 0, 0],
        ['c8', 0, 0, 0, 0, 0, 0, 0],
        ['c9', 0, 0, 'c10', 0, 0, 'c11', '#'],
        ['#', 'c12', 0, 0, 'c13', 0, 0, 'c14'],
        ['#', 'c15', 'c16', 0, 0, 'c17', 0, 0],
        ['c18', 0, 0, 0, 0, 0, 0, 0],
        ['c19', 0, 0, 'c20', 0, 0, 0, '#'],
    ]

    constraints = {
        'c1': {'down': 20},
        'c2': {'down': 3},
        'c3': {'down': 23},
        'c4': {'down': 12},
        'c5': {'down': 16},
        'c6': {'down': 5, 'right': 12},
        'c7': {'down': 24, 'right': 16},
        'c8': {'right': 41},
        'c9': {'right': 3},
        'c10': {'down': 24, 'right': 13},
        'c11': {'down': 11},
        'c12': {'right': 17},
        'c13': {'down': 23, 'right': 10},
        'c14': {'down': 16},
        'c15': {'down': 14},
        'c16': {'down': 5, 'right': 16},
        'c17': {'down': 17, 'right': 11},
        'c18': {'right': 42},
        'c19': {'right': 10},
        'c20': {'right': 22}

    }
    return temp, constraints



def board6():
    temp = [
        ['#', '#', '#', 'c1', 'c2', '#', '#', 'c3', 'c4', '#'],  # 0
        ['#', 'c5', 'c6', 0, 0, '#', 'c7', 0, 0, 'c8'],  # 1
        ['c9', 0, 0, 0, 0, 'c10', 'c11', 0, 0, 0],  # 2
        ['c12', 0, 0, 'c13', 0, 0, 0, 0, 0, 0],  # 3
        ['#', 'c14', 0, 0, 'c15', 0, 0, 'c16', 0, 0],  # 4
        ['#', 'c17', 0, 0, 'c18', 'c19', 'c20', 0, 0, '#'],  # 5
        ['c21', 0, 0, 'c22', 0, 0, 'c23', 0, 0, 'c24'],  # 6
        ['c25', 0, 0, 0, 0, 0, 0, 'c26', 0, 0],  # 7
        ['c27', 0, 0, 0, '#', 'c28', 0, 0, 0, 0],  # 8
        ['#', 'c29', 0, 0, '#', 'c30', 0, 0, '#', '#'],  # 9
    ]
    constraints = {
        'c1': {'down': 17},
        'c2': {'down': 19},
        'c3': {'down': 7},
        'c4': {'down': 44},
        'c5': {'down': 3},
        'c6': {'down': 37, 'right': 17},
        'c7': {'right': 10},
        'c8': {'down': 23},
        'c9': {'right': 20},
        'c10': {'down': 6},
        'c11': {'right': 15, 'down': 3},
        'c12': {'right': 5},
        'c13': {'down': 3, 'right': 25},
        'c14': {'right': 8},
        'c15': {'right': 3},
        'c16': {'down': 10, 'right': 15},
        'c17': {'down': 13, 'right': 3},
        'c18': {'down': 7},
        'c19': {'down': 5},
        'c20': {'right': 17},
        'c21': {'right': 9},
        'c22': {'down': 10, 'right': 3},
        'c23': {'down': 16, 'right': 6},
        'c24': {'down': 11},
        'c25': {'right': 38},
        'c26': {'down': 3, 'right': 17},
        'c27': {'right': 7},
        'c28': {'right': 12},
        'c29': {'right': 4},
        'c30': {'right': 3},
    }

    return temp, constraints



