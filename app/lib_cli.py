class CliInputOutputPrompt():

    NOTE_PROMPT = ("note_title", "note_body")

    USER_MESSAGES = {
        NOTE_PROMPT[0]: "Введите заголовок заметки: ",
        NOTE_PROMPT[1]: "Введите содержание заметки: ",
    }
    INIT_MSG_CONTENT = ("Какое действие вы хотите совершить?",
                        "1. Создать новую заметку",
                        "2. Посмотреть список заметок по названииям",
                        "3. Вывести текст заметки на экран",
                        "4. Изменить заметку",
                        "5. Удалить заметку",
                        "6. Посмотреть заметки в интервале дат создания")

    USER_CHOICE_MSG = ("Введите номер действия: ",
                       "Введен неправильный номер. Попробуйте еще раз.")

    NOTE_CHANGE_MSG = ("Что вы хотите изменить?",
                       "1. Название заметки",
                       "2. Текст заметки")
    
    DATE_MSG = ("Дата и время вводится в формате YYYY mm dd HH MM SS",
                "Введите начальную дату: ",
                "Введите конечную дату: ")
    
    WRONG_INPUT_MSG = "Введенная дата не соответствует формату"
    
    # def chooseMethod(cls, function_list):
    #     cls.msgToUser(cls.INIT_MSG_CONTENT)
    #     return cls.userChoice(cls.USER_CHOICE_MSG[0], function_list)

    @classmethod
    def chooseTitleOrBody(cls):
        cls.msgToUser (cls.NOTE_CHANGE_MSG)
        return cls.userChoice(cls.USER_CHOICE_MSG[0], cls.NOTE_PROMPT)

    # Вызывает метод, соответствующий выбору пользователя.
    @classmethod
    def userChoice(cls, user_choice_msg, used_list):
        try:
            user_response_int = int(cls.promptUserForString(user_choice_msg))
            if user_response_int <= 0 or user_response_int > len(used_list):
                print(cls.USER_CHOICE_MSG[1])
                return cls.userChoice(user_choice_msg, used_list)
            else: return used_list[user_response_int - 1]
        except:
            print (cls.USER_CHOICE_MSG[1])
            return cls.userChoice(user_choice_msg, used_list)

    # Выводит в консоль вопрос к пользователю, что он хочет
    @classmethod
    def msgToUser(message):
        print("\n".join(message))

    @classmethod
    def getNewText(cls, user_choice):
        new_text = None
        if user_choice == cls.NOTE_PROMPT[0]:
            new_text = cls.promptUserForString(cls.USER_MESSAGES[cls.NOTE_PROMPT[0]])
        if user_choice == cls.NOTE_PROMPT[1]:
            new_text = cls.promptUserForString(cls.USER_MESSAGES[cls.NOTE_PROMPT[1]])
        return new_text

    # 1.1, (внутри 1.1.1) из строки юзера возвращает словарь с названием и текстом заметки
    @classmethod
    def getCliInputStream(cls):
        cli_input_stream = {}
        for np in cls.NOTE_PROMPT:
            cli_input_stream[np] = cls.promptUserForString(cls.USER_MESSAGES[np]) # 1.1.1
        return cli_input_stream
    
    # 1.1.1 юзеру выводится message, возвращается его ввод str
    @classmethod
    def promptUserForString(cls, message):
        user_string = input(message)
        return user_string

    # 2.2 выводит названия заметок
    def printNoteTitles(note_titles):
        for i in note_titles:
            print(i)

    # 3.1 Спрашивает юзера, какую заметку он хочет посмотреть и возвращает строку
    #  с названием заметки
    @classmethod
    def whichNoteUserWants(cls):
        chosen_title = cls.promptUserForString(cls.USER_MESSAGES[cls.NOTE_PROMPT[0]])
        return chosen_title
    
    # 3.3 
    @classmethod
    def PrintBodyOfTheChosenNote(cls, json_data):
        if json_data == None: return
        else:
            note_body = json_data['note_body']
            print(f'Текст выбранной заметки:\n{note_body}')

    @classmethod
    def getDatesFromUser(cls):
        print(cls.DATE_MSG[0])
        startDate = cls.promptUserForString(cls.DATE_MSG[1])
        endDate = cls.promptUserForString(cls.DATE_MSG[2])
        return startDate, endDate

    def printNotesAndDates(dates: dict):
        for k, v in dates.items():
            print(f"{k} - {v}")