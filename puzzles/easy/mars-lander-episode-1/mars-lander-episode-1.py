import sys

# the standard input according to the problem statement.
surface_n = int(input())  # the number of points used to draw the surface of Mars.
previous_y = -1
flat_y = -1
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    if land_y == previous_y:
        flat_y = land_y
    previous_y = land_y

# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    print(x, y, h_speed, v_speed, fuel, rotate, power, file=sys.stderr, flush=True)

    # 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).
    # 这里的数应该也是39.77，但测试中发现加速度不会即时生效，这是惯性导致的，下个问题再思考，这里使用了偏差值
    if(v_speed < -32):
        a = 4-3.771
        t = (v_speed + 39.77) / a
        s = 40 * t + a * t * t / 2
        print(y - flat_y, a,t,s, file=sys.stderr, flush=True)
        if s < (y - flat_y):
            print("0 4")
        else:
            print("0 0")
    else:
        print("0 0")
