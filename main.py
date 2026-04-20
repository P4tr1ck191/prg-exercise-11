import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


values = random_numbers(10)  # 10 čísel v rozsahu 0–100
print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]


def selection_sort (numbers):
    numbers = numbers[:]
    for pozice_ukladani in range(len(numbers)):
        min_idx = pozice_ukladani
        for pozice_prochazena in range(pozice_ukladani + 1, len(numbers)):
            if numbers[pozice_prochazena] < numbers[min_idx]:
                min_idx = pozice_prochazena

            index_highlight1 = pozice_ukladani
            index_highlight2 = pozice_prochazena
            colors = ["steelblue"] * len(numbers)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(numbers)), numbers, color=colors)
            plt.title("Selection")
            plt.pause(0.1)


        numbers[pozice_ukladani], numbers[min_idx] = numbers[min_idx], numbers[pozice_ukladani]
    plt.ioff()
    plt.show()
    return numbers

numbers = [5, 1, 4, 2, 8]
print("Původní seznam: ", numbers)
print("Seřazený seznam: ", selection_sort(numbers))



def bubble_sort(numbers):
    numbers = numbers[:]
    for serazeno_od_konce in range(len(numbers)):
        for pozice_porovnavani in range(len(numbers) - 1 - serazeno_od_konce):
             if numbers[pozice_porovnavani] > numbers[pozice_porovnavani + 1]:
                 numbers[pozice_porovnavani], numbers[pozice_porovnavani + 1] = numbers[pozice_porovnavani + 1], numbers[pozice_porovnavani]

    return numbers

numbers = random_numbers(20)
print("Původní seznam: ", numbers)
print("Seřazený seznam: ", bubble_sort(numbers))






