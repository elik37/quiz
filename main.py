def main() -> None:
    questions_and_answers: list = [
        {
            'question': 'Что лежит у меня в кармане',
            'answer': 'кольцо',
        },
        {
            'question': 'Как називается тюнинг ателье Мерседес',
            'answer': 'АМГ',
        },
        {
            'question': 'Кто самая ссасная жинка в мире',
            'answer': 'Мєл',
        },
        {
            'question': 'Кто самий пиздатий мижик в мире',
            'answer': 'Шепард',
        },
        {
            'question': 'Сколько пива нужно, что бы одурманить Дмитрия',
            'answer': 'Два литра',
        },
    ]
    user_name: str = input('Введите своё имя: ')
    print(f'Привет {user_name}, сейчас я буду опрашивать вас!')
    print('\n')
    score: int = 0

    for element in questions_and_answers:
        print(element['question'])
        user_answer: str = input('Введите ответ: ')

        if element['answer'] == user_answer:
            score += 1
            print('Это правельный ответ, ви заработали 1 балл')
        else:
            score -= 1
            print('Ваш ответ не верен, мы отнимает 1 балл')

        print('\n')
        print(f'Ваш счёт составляет: {score} баллов')

    print(f'Ваш результат: {score}')


if __name__ == '__main__':
    main()
