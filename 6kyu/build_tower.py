def tower_builder(n_floors):
    build = []
    i = 1
    width_floor = 1
    while i <= n_floors:
        build.append('{0:^{width}}'.format('*' * width_floor, width=n_floors * 2 -1))
        width_floor = i * 2 + 1
        i += 1
    return build

tower = (tower_builder(10))
for floor in tower:
    print(floor)