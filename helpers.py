class todo:
    id: int
    title: str
    description: str
    color: str
    checked: bool

    def __init__(self, id: int, title: str, description: str, color: str):
        self.id = id
        self.title = title
        self.description = description
        self.color = color
        self.checked = False # Every new item begins as unchecked

# We could write this class in our app.py file but for organization we
# will add a helper file for classes and functions. 
# Create a new file named helpers.py and add the following class: