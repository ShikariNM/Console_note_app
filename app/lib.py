import json
from datetime import datetime

# from tkinter.tix import ListNoteBook


class UserInputPrompt:
    @classmethod
    def promptUserForString(cls, message):
        user_string = input(message)
        return user_string


class Note:
    NOTE_ID_FORMAT = "%Y%m%d%H%M%S"
    NOTE_DT_FORMAT = "%Y%m%d%H%M%S%f"
    NOTE_INPUT_STREAM_FORMAT = ("note_title", "note_body")

    def __init__(self) -> None:
        self.note_title = ""
        self.note_body = ""
        self.note_creation_dt = datetime.now()
        self.note_last_modification_dt = datetime.now()
        self.note_id = self._noteIdFormat() # 1.3.2

    # 1.3.2 Принимает на вход некоторую датувремя и преобразует в строку формата ID
    def _noteIdFormat(self):
        _note_id = self.note_creation_dt.strftime(self.NOTE_ID_FORMAT)
        return _note_id

    # 1.2 Создает экзепляр заметки, присваивает его аргументам значения из словаря 1.1
    # (имя заметки, название заметки) и возвращает экземпляр заметки
    @classmethod
    def createNote(cls, input_stream):
        new_note = Note()
        new_note.note_title = input_stream[cls.NOTE_INPUT_STREAM_FORMAT[0]]
        new_note.note_body = input_stream[cls.NOTE_INPUT_STREAM_FORMAT[1]]
        return new_note

    # 1.3 (внутри 1.3.1, 1.3.2) Возвращает tuple: json строку с данными заметки
    # и строкуДатаВремяВФорматеID, полученные другими методами
    def getFileSystemStream(self):
        return self._convertToJson(), self._noteIdFormat()

    # 1.3.1 (внутри 1.3.1.1) Используя словарь с данными заметки возвращает его в виде
    # json строки
    def _convertToJson(self):
        attr_dict = self._convertToDict() # 1.3.1.1
        attr_json = json.dumps(attr_dict)
        return attr_json

    # 1.3.1.1 (внутри 1.3.1.1.1) Создает словарь с данными заметки.
    # Имя и тело берет из аргуменнтов экземпляра остальное из других методов
    def _convertToDict(self):
        note_as_dict = {}
        note_as_dict.update(
            {
                "note_title": self.note_title,
                "note_body": self.note_body,
                "note_id": self.note_id, # получается из 1.3.2
                "note_creation_dt": self._formatDateTimeToString(self.note_creation_dt),# 1.3.1.1.1
                "note_last_modification_dt": self._formatDateTimeToString(              # 1.3.1.1.1
                    self.note_last_modification_dt
                ),
            }
        )
        return note_as_dict

    # 1.3.1.1.1 Принимает на вход некоторую датувремя и преобразует в строку формата DT
    def _formatDateTimeToString(self, _note_date_time):
        _note_date_time_string = _note_date_time.strftime(self.NOTE_DT_FORMAT)
        return _note_date_time_string

    @classmethod
    def createNoteFromJson(cls, note_data):
        note = Note()
        for key in note_data:
            setattr(note, key, note_data[key])
        return note

    def changeNote(self, user_choice, newText):
        if user_choice == self.NOTE_INPUT_STREAM_FORMAT[0]:
            self.note_title = newText
        if user_choice == self.NOTE_INPUT_STREAM_FORMAT[1]:
            self.note_body = newText
        self.note_last_modification_dt = self._formatDateTimeToString(datetime.now())
        return json.dumps(self.__dict__), self.__dict__["note_id"]