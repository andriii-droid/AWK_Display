from nicegui import ui

class Page:
    def __init__(self, course_name):
        self.course_name = course_name

    # Remove @classmethod - pass the container as an argument instead
    def show_content(self, container):
        print(f"DEBUG: Rendering {self.course_name} into {container}")
        container.clear()
        with container:
            ui.label(f'Kurs: {self.course_name}').classes('text-h4 text-primary')
            ui.label('This should now be visible!')

    @staticmethod
    def show_home(container):
        print(f"DEBUG: Rendering Home into {container}")
        container.clear()
        with container:
            ui.label('TTC Uster Dashboard').classes('text-h3')
            ui.label('Select a course above.')