import numpy as np
def random_predict(number:int=1) -> int:
    """Случайно угадываем число

    Args:
        number (int, optional): Число, которое загадали.

    Returns:
        int: Число попыток
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break #выход из цикла
    return count



def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_list = [] #список для сохранения количества попыток угадывания
    np.random.seed(1) #указываем сид для воспроизводимости
    random_array = np.random.randint(1, 100, size=(1000)) #загадываем список чисел
    for number in random_array:
        count_list.append(random_predict(number))
        
    score = int(np.mean(count_list)) # находим среднее количество попыток
    
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return(score)

if __name__ == '__main__':
    score_game(random_predict)