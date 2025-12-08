with open("resources/f7_1", 'r') as file:

    split_count = 0

    tree = list()

    for l in file:

        tree.append(list(l.strip()))

    for i in range(1, len(tree)):

        for j in range(len(tree[i])):

            if tree[i-1][j] == '|':
                if tree[i][j] == '^':
                    tree[i][j-1] = '|'
                    tree[i][j+1] = '|'
                    split_count += 1
                else:
                    tree[i][j] = '|'
            elif tree[i-1][j] == 'S':
                if tree[i][j] == '^':
                    tree[i][j-1] = '|'
                    tree[i][j+1] = '|'
                    split_count += 1
                else:
                    tree[i][j] = '|'

for l in tree:
    print(l)

print(split_count)