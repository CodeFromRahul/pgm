import random as rand

def select_number():
    
    no = [1, 6] 
    face_no = rand.choice(no)
    return  rand.choice( no )

def simulate_dice(iterations = 100):
    
    # count of the number of cards
    no_of_1 = 0
    no_of_6 = 0 

    for i in range(1, iterations + 1):
        no  = select_number()
        if no == 1: 
            no_of_1 += 1
        else:
            no_of_6 += 1
        if (i % (iterations / 10)) == 0:
            print(f"Iteration: {i} \t {no} ")
    
    print(f"Proportion of 1: {no_of_1 / iterations}\nProportion of 6: {no_of_6/ iterations}")
    
    print(f"\nThe Ratio of 6 to 1 is {no_of_6 / no_of_1}\n")

def main():
    simulate_dice(10)
    simulate_dice(1000)
    simulate_dice(10000)
    simulate_dice(100000)

if __name__ == "__main__":
    main()
