import random

def iter(env, pos):

    # -1 = moving left
    # 1 = moving right
    performance_points = 0
    action = ""
    print("\n---------------------------------------------------------")
    print("Environment : "+str(env)+"\tStart Position : "+str(pos))
    print("Starting simulation...\n")
    for i in range(10):
        if env[pos] == 1:
            # print("Dirty Room scanned at "+str(pos)+". Cleaned Room.")
            env[pos] = 0
            performance_points += 1
            action = "SUCK"
            print("\tAction : "+action+"\t\tEnvironment : "+str(env)+"\tPosition : "+str(pos)+"\tPerformance : "+str(performance_points))
            continue;
        
        movement = random.choice([-1, 1])
        if movement == -1:
            # print("Agent moved left.")
            action = "LEFT"
        else:
            # print("Agent moved right.")
            action = "RIGHT"
        if pos+movement==1 or pos+movement==0:
            pos = pos+movement
        
        print("\tAction : "+action+"\t\tEnvironment : "+str(env)+"\tPosition : "+str(pos)+"\tPerformance : "+str(performance_points))
        
    return performance_points


def main():

    config = [[0, 0], [1, 0], [0, 1], [1, 1]]
    performance = {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 0}
    for env in config:
        e = env[:]
        e1 = env[:]
        performance_points = 0
        performance_points = iter(e, 0)
        performance_points = iter(e1, 1)
        performance[tuple(env)] = performance_points
    print("---------")
    print("REPORT\n---------")
    for i in performance:
        print("Configuration : " + str(i) + "   ::   Performance Points : " + str(performance[i]))


if __name__ == "__main__":
    main()