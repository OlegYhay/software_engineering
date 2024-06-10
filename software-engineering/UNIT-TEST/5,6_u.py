import re


def strip_punctuation_ru(data):
    return re.sub(r'[^\w\s]', '', data).strip()


def test_strip_punctuation_ru():
    tests = [
        ("Добрый, вечер!", "Добрый вечер"),
        ("Макасины?  Дешевые.", "Макасины Дешевые"),
    ]
    passed = True
    for data, expected in tests:
        result = strip_punctuation_ru(data)
        if result != expected:
            print(f"Тест для '{data}'. Ожидается: '{expected}', Получено: '{result}'")
            passed = False
    if passed:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    test_strip_punctuation_ru()

    data = input("Введите текст: ")
    result = strip_punctuation_ru(data)
    print(f"Текст без знаков препинания: {result}")
