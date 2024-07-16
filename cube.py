# Define the cube state (simplified representation for 3x3x3 Rubik's Cube)
# We use numbers 0-53 to represent each sticker on the cube
solved_state = list(range(48))

_movement = {
    "U": {
        "corners": [0, 2, 8, 6],
        "edges": [1, 5, 7, 3],
        "faces": [38, 37, 36, 29, 28, 27, 20, 19, 18, 11, 10, 9]
    }, 
    "R": {
        "corners": [],
        "edges": [28, 30, 34, 32],
        "faces": [20, 23, 26, 47, 50, 53, 42, 39, 36, 2, 5, 8]
    }, 
    "D": {
        "corners": [45, 47, 53, 51],
        "edges": [46, 50, 52, 48],
        "faces": [24, 25, 26, 33, 34, 35, 42, 43, 44, 15, 16, 17]
    }, 
    "L": {
        "corners": [9, 11, 17, 15],
        "edges": [10, 14, 16, 12],
        "faces": [0, 3, 6, 18, 21, 24, 45, 48, 51, 44, 41, 38]
    }, 
    "F": {
        "corners": [],
        "edges": [],
        "faces": []
    }, 
    "B": {
        "corners": [],
        "edges": [],
        "faces": []
    }, 
}


movement = {
    "F": '(17,19,24,22)(18,21,23,20)(6,25,43,16)(7,28,42,13)(8,30,41,11)',
    "B": "(33,35,40,38)(34,37,39,36)(3,9,46,32)(2,12,47,29)(1,14,48,27)",
    "L":"(9,11,16,14)(10,13,15,12)(1,17,41,40)(4,20,44,37)(6,22,46,35)",
    "R": "(25,27,32,30)(26,29,31,28)(3,38,43,19)(5,36,45,21)(8,33,48,24)",
    "U": "(1,3,8,6)(2,5,7,4)(9,33,25,17)(10,34,26,18)(11,35,27,19)",
    "D": "(41,43,48,46)(42,45,47,44)(14,22,30,38)(15,23,31,39)(16,24,32,40)"
}

# Define the R move (Right face 90 degrees clockwise) with all affected stickers
def move(state, corners, edges, faces):
    new_state = state[:]
    for i in range(4):
        next = (i+1) % 4
        new_state[corners[i]] = state[corners[next]]
        new_state[edges[i]] = state[edges[next]]
        new_state[faces[i*3]] = state[faces[next*3]]
        new_state[faces[i*3+1]] = state[faces[next*3+1]]
        new_state[faces[i*3+2]] = state[faces[next*3+2]]
    
    return new_state

def new_move(state, permutations):
    new_state = state[:]
    for permutation in permutations:
        for i, k in enumerate(permutation):
            next = (i+1) % len(permutation)
            new_state[permutation[next]] = state[k]
    return new_state


def make_move(state, direction=["R", "L", "U", "D", "F", "B", "R'", "L'", "U'", "D'", "F'", "B'"]):
    tmp = movement[direction[0]]
    permutations = [[int(j)-1 for j in i[:-1].split(",")] for i in tmp.split("(")[1:]]
    # print(permutations)
    if "'" in direction:
        # _movement = movement[direction[0]]
        permutations = [list(reversed(permutation)) for permutation in permutations]
        # _movement["edges"] = list(reversed(_movement["edges"]))
        # _movement["corners"] = list(reversed(_movement["corners"]))
        # _movement["faces"] = list(reversed(_movement["faces"]))
        return new_move(state, permutations)
    return new_move(state, permutations)
