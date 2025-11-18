class NotesManager:
    def __init__(self, filename="notes.txt"):
        self.filename = filename

    def add_note(self, text):
        with open(self.filename, "a") as file:
            file.write(text + "\n")

    def read_notes(self):
        try:
            with open(self.filename, "r") as file:
                return file.readlines()
        except FileNotFoundError:
            return []

manager = NotesManager()
manager.add_note("Learn Python OOP")
print(manager.read_notes())
