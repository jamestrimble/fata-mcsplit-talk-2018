import math

ee0_str = "1--4; 1--5; 2--3; 2--5; 3--5;"
ee1_str = "a--b; a--c; a--e; b--d; b--f; c--d; c--e; c--f; d--f; e--f;"
vv0 = range(5)
vv1 = range(6)

def read_edges(ee_str, start_char):
    start_char_code = ord(start_char)
    edge_starts = range(0, len(ee_str), 6)
    edge_strings = [ee_str[start:(start+4)] for start in edge_starts]
    return [set([ord(s[0])-start_char_code, ord(s[3])-start_char_code]) for s in edge_strings]

ee0 = read_edges(ee0_str, "1")
ee1 = read_edges(ee1_str, "a")

start_angles = [2 * math.pi * i / len(vv0) for i in vv0]
end_angles = [2 * math.pi * (i+0.75) / len(vv0) for i in vv0]

def position(angle):
    angle = .655 * math.pi - angle
    radius = 2
    return (radius * math.cos(angle), radius * math.sin(angle))

def vtx_pos(v0, v1):
    start_x, start_y = position(start_angles[v0])
    end_x, end_y = position(end_angles[v0])
    x = start_x + (end_x - start_x) * v1 / (len(vv1)-1)
    y = start_y + (end_y - start_y) * v1 / (len(vv1)-1)
    return (x, y)

def print_nodes():
    for i in vv0:
        for j in vv1:
            letter = "abcdef"[j]
            x, y = vtx_pos(i, j)
            print "\\node[draw, circle, fill=white, inner sep=.3pt] (N{}{}) at ({},{}) {{\\scriptsize {}{}}};".format(
                    i+1, letter, x, y, i+1, letter)

def print_edges():
    for i in vv0:
        for j in vv1:
            for k in vv0:
                for l in vv1:
                    if k>i:
                        letter_j = "abcdef"[j]
                        letter_l = "abcdef"[l]
                        if (set([i,k]) in ee0) == (set([j,l]) in ee1):
                            print "\\draw [lledge] (N{}{}) -- (N{}{});".format(
                                    i+1, letter_j, k+1, letter_l)

print "\\vspace{-.5cm}"
print "\\begin{center}\\begin{tikzpicture}[scale=1.15]"

print_nodes()
print_edges()
print ee0
print ee1

print "\\end{tikzpicture}\\end{center}"
