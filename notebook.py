'''Module for creating and opetation with e-notes'''
import datetime


class Note:
    '''Represent a note in the notebook. Match against a
    string in searches and store tags for each note.
    >>> note = Note('Hello world', 'My note')
    >>> print(note.script, note.tags, note.id)
    Hello world My note 1
    '''

    def __init__(self, script: str, tags: str):
        '''initialize a note with memo and optional
        space-separated tags. Automatically set the note's
        creation date and a unique id.'''
        self.script = script
        self.tags = tags
        self.creation_date = datetime.date.today()
        Notebook.last_id += 1
        self.id = Notebook.last_id


    def match(self, filter: str):
        '''Determine if this note matches the filter
        text. Return True if it matches, False otherwise.

        Search is case sensitive and matches both text and
        tags.'''
        return filter in self.script or filter in self.tags


class Notebook:
    '''Represent a collection of notes that can be tagged,
    modified, and searched.
    >>> book = Notebook()
    >>> book.notes
    []
    >>> book.new_note('Hello world!', 'My note one')
    >>> book.new_note('Hello Python!', 'My note two')

    >>> [(note.script, note.id) for note in book.notes]
    [('Hello world!', 2), ('Hello Python!', 3)]

    >>> print(book._find_note(2).script)
    Hello world!

    >>> book.modify_script(2, 'Hello, John')
    True
    >>> book.modify_script(5, 'Hello, John')
    False

    >>> [(note.script, note.id) for note in book.notes]
    [('Hello, John', 2), ('Hello Python!', 3)]

    >>> [(note.script, note.tags) for note in book.search('Hello')]
    [('Hello, John', 'My note one'), ('Hello Python!', 'My note two')]
    '''

    last_id = 0

    def __init__(self):
        '''Initialize a notebook with an empty list.'''
        self.notes = []

    def new_note(self, script: str, tags=''):
        '''Create a new note and add it to the list.'''
        self.notes.append(Note(script, tags))

    def _find_note(self, note_id):
        '''Find the note with the given id and change its
        memo to the given value.'''
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
            return None

    def modify_script(self, note_id: int, upgrade_var: str, _switch='script'):
        '''Find the note with the given id and change its script or
        tags to the given value.'''
        note = self._find_note(note_id)

        if note:
            if _switch == 'script':
                note.script = upgrade_var
            elif _switch == 'tags':
                note.tags = upgrade_var
            # print(note.script, note.tags)
            return True
        return False

    def modify_tags(self, note_id: int, tags: str):
        '''Find the note with the given id and change its
        tags to the given value.'''
        self.modify_script(note_id, upgrade_var=tags, _switch='tags')

    def search(self, filter: str):
        '''Find all notes that match the given filter
        string.'''
        return [note for note in self.notes if note.match(filter)]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
