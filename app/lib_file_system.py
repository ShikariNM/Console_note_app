import os
import json
from glob import glob
from datetime import datetime



class FileSystemHandler:
    STORAGE_DIR = "data"
    FILE_FORMAT = ".json"
    FILE_DOESNT_EXIST_MESSAGE = "Такой заметки не существует"

    def __init__(self):
        pass

    # 1.4 Создает папку 'data', если не создана; создает в этой папке файл с именем
    # строкаДатаВремяВФорматеID.json и кладет в него json строку с данными заметки
    @classmethod
    def saveNote(cls, write_data):
        file_name = cls.getFileName(write_data[1]) # 1.4.1
        try:
            os.mkdir(cls.STORAGE_DIR)
        except FileExistsError:
            pass
        finally:
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(write_data[0])

    # 1.4.1 Возвращает имя файла - строку типа 'data/строкаДатаВремяВФорматеID.json'
    @classmethod
    def getFileName(cls, note_id):
        file_name = cls.STORAGE_DIR + "/" + note_id + cls.FILE_FORMAT
        return file_name

    # Записывает в словарь файлы формата json из текущего каталога
    @classmethod
    def createListNote(cls):
        list_note_dict = {}
        i = 0   
        for file in glob("*.json"):
            list_note_dict.update({i: os.path.basename(file).split(".")[0]})
            i += 1
        return list_note_dict
    
    # Создает словарь из времени создания и имени файла, сортирует и записывает в новый список
    @classmethod
    def createListNoteWithDate(cls):
        list_note = cls.createListNote()
        list_note_date = {}
        for i in range(0, len(list_note)):
            list_note_date.update({list_note[i]: os.path.getmtime(os.getcwd() + "\\" + list_note[i] + ".json")})
       
        sorted_values = sorted(list_note_date.values())
        sort_list_note = {}
        for i in sorted_values:
            for k in list_note_date.keys():
                if list_note_date[k] == i:
                    sort_list_note[k] = list_note_date[k]
                    break

        return sort_list_note
    
   

class FileSystemReader(FileSystemHandler):
    STORAGE_DIR_FULL = os.getcwd() + "/data"
    NOTE_DT_FORMAT = "%Y%m%d%H%M%S%f"
    NOTE_RM_MSG = "Заметка удалена."

    def __init__(self, id):
        self.file_id = id
        self.file_name = ""

    # # x (внутри x.1 и x.2) принимает экземпляр класса с ID и именем из x.1,
    # # принимает и возвращает данные из файла
    # @classmethod
    # def getJsonById(cls, file_id):
    #     file = cls.getFileFactory(file_id)  # x.1
    #     json_data = file.readFile()         # x.2
    #     return json_data

    # # x.1 Создает экземпляр файла. Исходя из входящего ID, автоматически присваивает этот
    # # ID соотв аргументу и присваивает строку 'data/строкаДатаВремяВФорматеID.json'
    # # аргументу "Имя"
    # @classmethod
    # def getFileFactory(cls, file_id):
    #     file_obj = cls(file_id)
    #     file_obj.file_name = file_obj.getFileName(file_obj.file_id) # 1.4.1
    #     return file_obj

    # # x.2 Проверяет есть можно ли выполнить метод открытия файла
    # # (существует ли такой файл) и выполняет, если можно
    # def readFile(self):
    #     try:
    #         return self.getFileContents() # x.2.1
    #     except FileNotFoundError:
    #         return self.FILE_DOESNT_EXIST_MESSAGE

    
    @classmethod
    def getFileContents(cls, file):
        with open(f'{cls.STORAGE_DIR_FULL}/{file}', 'r') as current_file:
            file_contents = json.loads(current_file.read())
        return file_contents
    
    # 2.1 Возвращает имена заметок из файлов
    @classmethod
    def listOfNoteTitles(cls):
        note_titles = []
        for file in os.listdir(cls.STORAGE_DIR_FULL):
            with open(f'{cls.STORAGE_DIR_FULL}/{file}', 'r') as current_file:
                note_titles.append(json.loads(current_file.read())['note_title'])
        return note_titles
    
    # 3.2 Принимает название заметки и возвращает словарь с содержимым заметки
    # или сообщение, что заметка не существует
    @classmethod
    def getJsonByNoteTitle(cls, title: str):
        for file in os.listdir(cls.STORAGE_DIR_FULL):
            json_data = cls.getFileContents(file)
            if json_data["note_title"] == title:
                return  json_data
            else: continue
        print(cls.FILE_DOESNT_EXIST_MESSAGE)

    # 5.1 Принимает название заметки и удаляет ее
    @classmethod
    def delNote(cls, title):
        note_id = cls.getIDByTitle(title) # 5.1.1
        if note_id == None: return
        else: 
            file_name = cls.getFileName(note_id)
            os.remove(file_name)
            print(cls.NOTE_RM_MSG)

    # 5.1.1 Возвращает ID заметки, получая на вход название
    @classmethod
    def getIDByTitle(cls, title):
        for file in os.listdir(cls.STORAGE_DIR_FULL):
            if cls.getFileContents(file)["note_title"] == title:
                return cls.getFileContents(file)["note_id"]
            else: continue
        print(cls.FILE_DOESNT_EXIST_MESSAGE)

    @classmethod
    def lookForNotesByDates(cls, dates):
        list_of_notes = {}
        for file in os.listdir(cls.STORAGE_DIR_FULL):
            cr_date_str = cls.getFileContents(file)["note_creation_dt"]
            cr_date = datetime.strptime(cr_date_str, cls.NOTE_DT_FORMAT)
            if dates[0] <= cr_date and cr_date <= dates[1]:
                list_of_notes[cr_date] = cls.getFileContents(file)["note_title"]
            else: continue
        if len(list_of_notes) > 0: return list_of_notes
        else: print(cls.FILE_DOESNT_EXIST_MESSAGE)