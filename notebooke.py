import datetime

# 为所有新的备注储存下一个可用的ID
last_id = 0


class Note:
    def __init__(self, memo, tags=''):
        self.tags = tags
        self.memo = memo
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, m_filter):
        return m_filter in self.tags or m_filter in self.memo


class Notebook:
    def __init__(self):
        """Initialize a empty note list"""
        self.notes = []

    def _find_note(self, note_id):
        if str(note_id) > str(last_id):
            print("Please input right note id ")
            return
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note

    def new_note(self, memo, tags=''):
        """Add a new note to notebook"""
        self.notes.append(Note(memo, tags))

    def remove_note(self, note_id):
        del self.notes[int(note_id) - 1]

    def modify_memo(self, note_id, memo):
        """Change the note's memo with given id"""
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        else:
            return False

    def modify_tags(self, note_id, tags):
        """Change the note's tags with given id"""
        self._find_note(note_id).tags = tags

    def search(self, m_filter):
        return [note for note in self.notes if note.match(m_filter)]
