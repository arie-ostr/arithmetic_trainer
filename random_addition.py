import random
import time 

answer = ""

results = []
#[{"q": "123+23-23", "a":True, time_ms: "34243"}]


def add_result(res_list,
               question_str:str,
                 is_correct:bool,
                   time_ms:int)->None : 
    
    res_list.append({
        "question_str" : question_str,
        "is_correct":  is_correct,
        "time_ms" : time_ms

    })

def get_results_average_time(results_dict):
    """
        gives the average time for calculation
    """
    count = len(results)
    total = 0

    for item in results_dict:
        if item["is_correct"] == True:
            total += item["time_ms"]
    
    return float(total)/count

def get_accuracy(results_dict):
    """gives you accuracy"""
    correct_len = len([i for i in results_dict if i["is_correct"]==True])
    return correct_len/len(results_dict)


if __name__ == "__main__":
    #todo - add a time trial
    remaining_questions = int(input("how_many tries?"))
    tries = remaining_questions


while answer != "q" and remaining_questions > 0:
    remaining_questions -= 1

    print("solve this, or type q to quit")
    a = random.randint(-1000,1000)
    b = random.randint(-1000,1000)
    c = random.randint(-1000,1000)

    msg = f"{a}+{b}+{c}"
    msg = msg.replace("+-"," - ") #buggy!
    msg = msg.replace("+"," + ")
    start_time = time.time()
    
    user_input = input(f"{msg} ? > ")
    answer = int(user_input)

    if answer == a+b+c :
        end_time =time.time()
        total_time = int((end_time - start_time) * 1000)
        print(f" success!! , did in {str(total_time)} ms")
        is_correct = True
              
    elif answer != "":
        ans_actual = str(a+b+c)
        print(f"failure ans is actually : {ans_actual}")
        is_correct=False
        total_time=None

    add_result(results,msg,is_correct,total_time)

avg_time = get_results_average_time(results)
print(f"average time for currect guesses: {avg_time} ms")

accuracy = get_accuracy(results)


print(f"accuracy for trial: {accuracy:.3%}")
print(f"total number of questions "
      f"{(tries- remaining_questions)} out of "
      f"{tries}")
print("\nthanks for playing!")