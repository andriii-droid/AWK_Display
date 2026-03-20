from nicegui import ui
from awk_table import AWKTable as awkt

class Page:
    def __init__(self, course):
        self.course = course

    def show_content(self, container):
        container.clear()
        with container:
            ui.label(f'{self.course.name}').classes('text-h4 text-primary')
            awkt(self.course)
            awkt(self.course, coach=True)

    @staticmethod
    def show_home(container):
        container.clear()
        with container:
            ui.label('TTC Uster Dashboard').classes('text-h3')
            #TODO SHow overall statistic or choose a course