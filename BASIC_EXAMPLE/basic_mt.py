import threading
import time

def calc_square(numbers):
    print("\nCalculating Square of numbers:\n")
    for n in numbers:
        time.sleep(0.2)
        print('Square of %i : %i' %(n, (n*n)))

def calc_cube(numbers):
    print("\nCalculating Cube of numbers:\n")
    for n in numbers:
        time.sleep(0.2)
        print('Cube of %i : %i' %(n,(n*n*n)))


# --- Multi Threading --- #
# Done in 0.8 secs

if __name__ == "__main__":
    user_input = [2,3,8,9]
    t = time.time()
    
    t1 = threading.Thread(target=calc_square,args=(user_input,))
    t2 = threading.Thread(target=calc_cube,args=(user_input,))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    print('\n\nDone in:\t',time.time()-t)

# ------ This part is for Normal running --- #
# Done in 1.67 sec
#         
# if __name__ == "__main__":
#     user_input = [2,3,8,9]  
#     t = time.time()
#     calc_square(user_input)   
#     calc_cube(user_input)
#     print('\n\nDone in:\t',time.time()-t)