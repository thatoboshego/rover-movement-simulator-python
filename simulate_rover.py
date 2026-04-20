import math
import sys

def movement(filename):
        
    roverPosition = (0.0, 0.0)
    degree = 0
    count = 0
    
    with open(filename, 'r', errors='ignore') as f:
        print(f"I'm at {roverPosition} facing {degree} degrees")

        for i in f:
            count += 1
            contents = i.split()

            if len(contents) != 4:
                print(f"I've encountered an instruction I don't understand, aborting (instruction {count})")
                sys.exit()

            if contents[0].lower() == "move":
                distance = float(contents[1])
                angle = math.radians(degree)

                dx = distance * math.sin(angle)
                dy = distance * math.cos(angle)

                if contents[-1].lower() == "forward":
                    roverPosition = (roverPosition[0] + dx, roverPosition[1] + dy)

                elif contents[-1].lower() == "backward":
                    roverPosition = (roverPosition[0] - dx, roverPosition[1] - dy)

            elif contents[0].lower() == "turn":
                amount = float(contents[1])

                if contents[-1].lower() == "clockwise":
                    degree += amount
                elif contents[-1].lower() == "counterclockwise":
                    degree -= amount

                degree = degree % 360

            if contents[0].lower() == "move":
                print(f"Moving {contents[1]} {contents[2].lower()} {contents[-1].lower()} (instruction {count})")

            if contents[0].lower() == "turn":
                print(f"Turning {contents[1]} {contents[2].lower()} {contents[-1].lower()} (instruction {count})")
            
            if roverPosition[0]<0 and roverPosition[0]>-0.0005:
                roverPosition = (abs(roverPosition[0]), roverPosition[1])
            
            print(f"I'm at ({roverPosition[0]:.2f}, {roverPosition[1]:.2f}) facing {degree:.2f} degrees")


movement(sys.argv[1])
