room = 75 #m^2
bucket_of_paint = 15 #m^2
paint_cost = 4300 #ft

one_paint = room / bucket_of_paint
two_paint = one_paint * 2

all_cost = two_paint * paint_cost
print(all_cost, "-Ft-ba kerülne Tobornak a festék \n")

work = 13 #minutes
hour = 60
cost_hour = hour // work
painter_cost_hour = two_paint // cost_hour
print(painter_cost_hour)