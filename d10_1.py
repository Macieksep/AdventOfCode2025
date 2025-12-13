result = 0

curr_min = 990
vis = {}

def click(curr_lights, button):
    for i in button:

        i = int(i)

        if curr_lights[i] == '#':
            curr_lights[i] = '.'
        else:
            curr_lights[i] = '#'

    return curr_lights

def steps_finder(curr_lights, curr_steps, buttons, indicator):

    global curr_min, vis

    st = tuple(curr_lights)
    if st in vis and vis[st] <= curr_steps:
        return
    vis[st] = curr_steps

    if curr_steps >= curr_min:
        return

    if curr_lights == indicator:
        curr_min = curr_steps
        return

    for b in buttons:
        temp_lights = curr_lights.copy()
        click(temp_lights, b)
        steps_finder(temp_lights,curr_steps + 1, buttons, indicator)

with open('resources/f10_1', 'r') as file:

    for l in file:
        param = l.strip().split(' ')[:-1]

        indicator = list(param[0][1:len(param[0])-1])

        buttons = list()

        for i in param[1:]:
            buttons.append(i[1:len(i)-1].split(','))

        start_lights = ['.']*len(indicator)

        vis = {}
        steps_finder(start_lights, 0, buttons, indicator)

        result += curr_min

        curr_min = 990

    print(result)