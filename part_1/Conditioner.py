t_room, t_cond = map(int, input().split())
regime = str(input())
output = t_room
if regime == "freeze":
    output = t_cond if t_cond < t_room else t_room
elif regime == "heat":
    output = t_cond if t_cond > t_room else t_room
elif regime == "auto":
    output = t_cond
else:
    output = t_room

print(output)
