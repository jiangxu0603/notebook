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
            "4": self.remove_note,
            "5": self.modify_note,
            "6": self.quit,
            "7": self.input_error
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
            """如果输入option不正确，则执行self.error"""
            action = self.choices.get(choice, self.input_error)
            if action:
                action()
            else:
                pass

    def show_notes(self):
        notes = self.notebook.notes
        if not notes:
            print("There is nothing in notebook")
        else:
            print("\nAll notes in notebook are:")
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

    def remove_note(self):
        m_id = input("Please enter the note's id you want to remove from notebook ")
        self.notebook.remove_note(m_id)
        print("Delete success")

    def modify_note(self):
        m_id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(m_id, memo)
        if tags:
            self.notebook.modify_tags(m_id, tags)

    def quit(self):
        sys.exit(0)

    def input_error(self):
        print("Please print right option")


if __name__ == "__main__":
    Menu().run()