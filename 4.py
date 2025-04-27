# Мажоритарный элемент списка — это элемент, который встречается в списке более чем ⌊n/2⌋ раз, где n — длина списка.
# Реализуйте функцию is_majority_element(), которая принимает два аргумента в следующем порядке:
# nums — отсортированный по неубыванию список положительных целых чисел (1 ≤ len(nums) ≤ 10⁶),
# target — целое число (1 ≤ target ≤ 10⁶).
# Функция должна возвращать значение True, если число target является мажоритарным элементом списка nums, и False в противном случае.
def is_majority_element(numbers: list[int], target: int) -> int:
    left, right = 0, len(numbers) - 1
    first_enter = last_enter = -1
    while left <= right:
        middle = left + (right - left) // 2
        elem = numbers[middle]
        if  first_enter == -1:
            if elem == target and (middle == 0 or numbers[middle - 1] != target):
                first_enter = middle
                left, right = 0, len(numbers) - 1
                continue
        else:
            if elem == target and (middle == len(numbers) - 1 or numbers[middle + 1] != target):
                last_enter = middle
                return last_enter - first_enter + 1 > len(numbers) // 2
        if first_enter == -1:
            if elem >= target:
                right = middle - 1
            else:
                left = middle + 1
        else:
            if elem <= target:
                left = middle + 1
            else:
                right = middle - 1
    return False


# Тимур участвует в соревнованиях по боксу и готовится сразиться с бесчисленным количеством соперников.
# У каждого из них, включая Тимура, есть показатель силы.
# Показатель силы Тимура равен power, а показатель силы его соперников определяется по следующему правилу:
# показатель силы первого соперника равен 1, второго — 4, третьего — 9 и так далее,
# показатель силы i-го соперника равен i².
#
# Тимур может победить соперника только в том случае, если его показатель силы больше или равен показателю силы соперника.
# При этом после каждой победы показатель силы Тимура уменьшается на величину показателя силы побежденного соперника:
# после победы над первым соперником его показатель силы уменьшается на 1,
# над вторым — на 4, над третьим — на 9 и так далее.
#
# Реализуйте функцию count_victories(), которая принимает один аргумент:
#
# - power — целое число, показатель силы Тимура (power ≥ 1).
#
# Функция должна определять, какое наибольшее количество соперников может победить Тимур,
# и возвращать полученный результат.

def count_victories(power: int) -> int:
    right = 1
    while (right * (right + 1) * (2 * right + 1)) // 6 < power:
        right *= 2
    left = right // 2
    while left <= right:
        middle = right - (right - left) // 2
        if (middle * (middle + 1) * (2 * middle + 1)) // 6 == power:
            return middle
        if (middle * (middle + 1) * (2 * middle + 1)) // 6 > power:
            right = middle - 1
        else:
            left = middle + 1
            result = middle
    return result

# Реализуйте функцию sort_limited_numbers(), которая принимает один аргумент:
#
# nums — список, содержащий только целые числа в диапазоне от −100 до 100 включительно (1 ≤ len(nums) ≤ 10⁶).
#
# Функция должна выполнять сортировку списка nums по невозрастанию путем его изменения.

def sort_limited_numbers(numbers: list[int]) -> None:
    max_value, min_value = max(numbers), min(numbers)

    counts = [0] * (max_value - min_value + 1)

    for num in numbers:
        counts[max_value - num] += 1
    ind = 0
    for num in range(len(counts)):
        for _ in range(counts[num]):
            numbers[ind] = max_value - num
            ind += 1

# Реализуйте функцию valid_nums_in_segments(), которая принимает два аргумента в следующем порядке:
#
# nums — список целых чисел (1 ≤ len(nums) ≤ 10⁶)
# segments — список кортежей, каждый из которых состоит из двух целых чисел (1 ≤ len(segments) ≤ 10⁵)
#
# Функция должна на отрезках списка nums, перечисленных в списке segments, находить все элементы,
# которые больше своего левого соседа.
# Например, если список segments имеет вид [(1, 3), (7, 8)], то функция должна выполнять поиск
# подходящих значений среди следующих элементов:
#
# nums[1], nums[2], nums[3]
# nums[7], nums[8]
#
# Полученные результаты функция должна вернуть в виде списка, первым элементом которого является
# количество элементов, которые больше своего левого соседа, на первом отрезке списка nums,
# вторым — на втором, третьим — на третьем и так далее.
#
# Примечание. Гарантируется, что в каждом кортеже из списка segments первый элемент не больше второго.

def valid_nums_in_segments(numbers: list[int], sigments: list[int]) -> list[int]:
    len_numbers = len(numbers)
    p = [0] * (len_numbers + 1)

    for i in range(2, len_numbers + 1):
        p[i] = p[i - 1] + 1 if numbers[i - 2] < numbers[i - 1] else p[i - 1]

    result = [0] * len(sigments)

    for i in range(len(sigments)):
        l, r = sigments[i]
        result[i] = p[r + 1] - p[l + 1]

    return result

# Тимур любит печатать английские слова, но его клавиатура работает не совсем исправно:
# при нажатии на клавишу один раз символ может напечататься несколько раз.
# Например, при попытке напечатать слово "python" у Тимура может получиться текст "pyytttthonnn".
#
# Реализуйте функцию could_type(), которая принимает два аргумента в следующем порядке:
#
# word — строка из строчных английских букв (1 ≤ len(word) ≤ 10⁶)
# typed — строка из строчных английских букв (1 ≤ len(typed) ≤ 10⁶)
#
# Функция должна возвращать значение True, если текст typed мог быть напечатан Тимуром
# при попытке напечатать слово word. В противном случае функция должна вернуть значение False.

def could_type(word: str, typed: str) -> bool:
    left = 0
    right = 0

    while left < len(word):
        if right == len(typed):
            return False
        while word[left] != typed[right]:
            right += 1
            if right == len(typed):
                return False
        if typed[right - 1] != word[left - 1]:
            return False

        if word[left] == typed[right]:
            left += 1
            right += 1

    end = right
    right = len(typed) - 1
    while right > end - 1:
        if typed[right] != word[-1]:
            return False
        right -= 1

    return True