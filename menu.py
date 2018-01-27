import sys
from notebooke import Notebook, Note
from notebooke import last_id


class Menu:
    """Display a menu and respond to choices when run"""
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit,
            "6": self.input_error
        }

    def display_menu(self):
        print("\nMenu is :")
        for key in self.choices:
            if self.choices[key] != self.input_error:
                print(key + ' ' + str(self.choices[key].__name__))

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nEnter an option ")
            """如果输入option大于等于6，则执行self.error"""
            action = self.choices.get(choice, self.input_error)
            if action:
                action()
            else:
                assert action != 0

    def show_notes(self, notes=None):
        print("\nAll notes in notebook are:")
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(str(note.id) + ' ' + str(note.memo))

    def _show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(str(note.id) + ' ' + str(note.memo))

    def search_notes(self):
        m_filter = input("\nSearch for: ")
        notes = self.notebook.search(m_filter)
        self._show_notes(notes)

    def add_note(self):
        memo = input("Enter a memo: ")
        """If input equal 'q!', end this inputting"""
        if memo == 'q!':
            return
        self.notebook.new_note(memo)
        print("Your note has been added")

    def modify_note(self):
        id = input("Enter a note id: ")
        if id > str(last_id):
            print("Please input right note id ")
            return False
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        sys.exit(0)

    def input_error(self):
        print("Please print right option")


if __name__ == "__main__":
    Menu().run()