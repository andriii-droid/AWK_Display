from nicegui import ui

class Page:
    def __init__(self, course):
        self.course = course

    def show_content(self, container):
        container.clear()
        with container:
            ui.label(f'Kurs: {self.course.name}').classes('text-h4 text-primary')
            ui.label('This should now be visible!')

    @staticmethod
    def show_home(container):
        container.clear()
        with container:
            ui.label('TTC Uster Dashboard').classes('text-h3')
            ui.label('Select a course above.')