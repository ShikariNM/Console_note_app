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
        newData = note.changeNote(user_choice, new_text)
        lib_file_system.FileSystemHandler.saveNote(newData)

# 5


# if __name__ == '__main__':
# createNoteFromCliInput()

editNote()
# showNoteBody()
# showNoteTitles()