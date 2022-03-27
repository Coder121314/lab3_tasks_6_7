"""
module contains class Notebook
and corresponding tests
"""

class Note:
    """
    class for objects of note type
    """
    def __init__(self, memo, creation_date, tags=""):
        self.memo = memo
        self.creation_date = creation_date
        self.tags = tags
    
    def match(self, search_filter:str):
        """
        method checks if the text in note matches
        """
        if self.memo == search_filter:
            return True
        return False
    
    def tag_match(self, search_filter:str):
        """
        checks if there is object with
        mentioned tags
        """
        if search_filter in self.tags:
            return True
        return False


class Notebook:
    """
    class for objects of notebook type
    """
    def __init__(self, notes:list):
        self.notes = notes

    def search(self, filter:str) -> list:
        """
        searching elements in the list
        that satisfy the condition
        """
        return [elem for elem in self.notes if elem.match(filter)]
    
    def new_note(self, memo, creation_date, tags=""):
        """
        method creates a new note 
        """
        self.notes.append(Note(memo, creation_date, tags))
    
    def modify_memo(self, note_id, memo):
        """
        method modifies memo of given note
        """
        import ctypes
        obj = ctypes.cast(note_id, ctypes.py_object).value
        obj.memo = memo

    def modify_tags(self, note_id, tags):
        """
        method modifies tags
        """
        import ctypes
        obj = ctypes.cast(note_id, ctypes.py_object).value
        obj.tags = tags

def Note_test():
    """"
    test for Note class
    """
    note = Note('some info', '25.03.2022', tags='general_info, neutral_info')
    assert(note.memo == 'some info')
    assert(note.creation_date == '25.03.2022')
    assert(note.match('some info') is True)
    assert(note.match('some other info') is False)
    assert(note.tag_match('general_info') is True)
    assert(note.tag_match('neutral_info') is True)
    assert(note.tag_match('other_info') is False)
    print("...Note_test       Passed")

def Notebook_test():
    """
    test for Notebook class
    """
    note_1 = Note('info 1', '25.03.2022', tags='general_info, neutral_info')
    note_2 = Note('info 2', '26.03.2022', tags='neutral_info')
    note_3 = Note('info 3', '27.03.2022', tags='general_info, special_info')
    notebook = Notebook([note_1, note_2, note_3])
    assert(notebook.notes == [note_1, note_2, note_3])
    assert(isinstance(notebook.notes[0], Note) is True)
    assert(isinstance(notebook.notes[0], object) is True)
    assert(len(notebook.search('info 2')) == 1)
    assert(len(notebook.search('info 5')) == 0)
    notebook.new_note('info 4', '01.04.2022', tags="new_info")
    assert(len(notebook.notes) == 4)
    notebook.modify_memo(id(notebook.notes[0]), 'info 1.1')
    assert(notebook.notes[0].memo == 'info 1.1')
    notebook.modify_tags(id(notebook.notes[1]), "modified_tag")
    assert(notebook.notes[1].tags == "modified_tag")
    print("...Notebook_test      Passed")


if __name__ == "__main__":
    Note_test()
    Notebook_test()



