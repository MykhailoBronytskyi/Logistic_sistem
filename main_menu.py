'''The interface of notebook'''

import sys
from notebook import Note, Notebook


class Menu:
    '''Display a menu and respond to choices when run.'''
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            '1': self.show_notes,
            '2': self.search_notes,
            '3': self.add_note,
            '4': self.modify_note,
            '5': self.quit,
        }

    def display_many(self):
        print(
            '''
Notebook Menu:

1. Show all Notes
2. Search Notes
3. Add Note
4. Modify Note
5. Quit
'''
        )
    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_many()
            choice = input('Enter an option: ')
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f'{choice} is not a valid choice')

    def show_notes(self, notes=None):
        '''Shows information about given notes. If notes
        are not given, it prints information about all the notes'''
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(f'{note.id}: {note.tags}\n{note.script}')
    
    def search_notes(self):
        '''Serches notes that contains some text'''
        filter = input('Search for: ')
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        '''Creates new note and add to the notebook'''
        script = input('Enter your script: ')
        self.notebook.new_note(script)
        print('Your note has been sucsesfully added.')

    def modify_note(self):
        '''Modifies created note'''
        id = input('Enter a note id: ')
        script = input('Enter a script: ')
        tags = input('Enter tags: ')
        if script:
            self.notebook.modify_script(id, script)
        if tags:
            self.notebook.modify_tags(id, script)

    def quit(self):
        '''Sophtly quit the notebook'''
        print('Thanks for using notebook today.')
        sys.exit(0)

if __name__=='__main__':
    # Menu().run()
    import doctest
    doctest.testmod()
