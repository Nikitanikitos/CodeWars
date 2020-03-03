def dir_reduc(plan):
    sides = {"NORTH": "SOUTH", "SOUTH": "NORTH", "WEST": "EAST", "EAST": "WEST"}
    new_plan = []
    for side in plan:
        if new_plan and sides[side] == new_plan[-1]:
            new_plan.pop()
        else:
            new_plan.append(side)
    return new_plan
