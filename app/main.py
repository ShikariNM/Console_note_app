import lib
import lib_cli
import lib_file_system

# 1
def createNoteFromCliInput():
    cli_input_stream = lib_cli.CliInputOutputPrompt.getCliInputStream() # 1.1
    note_obj = lib.Note.createNote(cli_input_stream)                    # 1.2
    file_system_stream = note_obj.getFileSystemStream()                 # 1.3
    lib_file_system.FileSystemHandler.saveNote(file_system_stream)      # 1.4

# 2
def showNoteTitles():
    note_titles = lib_file_system.FileSystemReader.listOfNoteTitles() # 2.1
    lib_cli.CliInputOutputPrompt.printNoteTitles(note_titles)         # 2.2 

# 3
def showNoteBody():
    chosen_title = lib_cli.CliInputOutputPrompt.whichNoteUserWants()                # 3.1
    json_data = lib_file_system.FileSystemReader.getJsonByNoteTitle(chosen_title)   # 3.2
    lib_cli.CliInputOutputPrompt.PrintBodyOfTheChosenNote(json_data)                # 3.3

# 4
def editNote():
    chosen_title = lib_cli.CliInputOutputPrompt.whichNoteUserWants()
    json_data = lib_file_system.FileSystemReader.getJsonByNoteTitle(chosen_title)
    if json_data == None: return
    else:
        user_choice = lib_cli.CliInputOutputPrompt.chooseTitleOrBody()
        note = lib.Note.createNoteFromJson(json_data)
        new_text = lib_cli.CliInputOutputPrompt.getNewText(user_choice)
        new_data = note.changeNote(user_choice, new_text)
        lib_file_system.FileSystemHandler.saveNote(new_data)

# 5
def deleteNote():
    chosen_title = lib_cli.CliInputOutputPrompt.whichNoteUserWants()
    lib_file_system.FileSystemReader.delNote(chosen_title)

# 6
def  listOfNotesByDate():
    input_str_dates = lib_cli.CliInputOutputPrompt.getDatesFromUser()
    dates = lib.Note.convertStrToDate(input_str_dates)
    dict_of_notes = lib_file_system.FileSystemReader.lookForNotesByDates(dates)
    if dict_of_notes == None: return
    else:
        final_dict = lib.Note.sortDictOfDates(dict_of_notes)
        lib_cli.CliInputOutputPrompt.printNotesAndDates(final_dict)

x = lib_cli.CliInputOutputPrompt
def initialFunction():
    print()
    try:
        user_response_int = int(input(x.USER_CHOICE_MSG[0]))
        if user_response_int not in range(1, 7):
            print(x.USER_CHOICE_MSG[1])
            return initialFunction()
        else:
            if user_response_int == 1: createNoteFromCliInput()
            elif user_response_int == 2: showNoteTitles()
            elif user_response_int == 3: showNoteBody()
            elif user_response_int == 4: editNote()
            elif user_response_int == 5: deleteNote()
            else: listOfNotesByDate()
    except:
        print (x.USER_CHOICE_MSG[1])
        return initialFunction()

if __name__ == '__main__':
    print()
    x.msgToUser(x.INIT_MSG_CONTENT)
    initialFunction()