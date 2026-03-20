from nicegui import ui
from awk_table import AWKTable as awkt

class Page:
    def __init__(self, course):
        self.course = course

    def show_content(self, container):
        container.clear()
        with container:
            ui.label(f'{self.course.name}').classes('text-h4 text-white')

            with ui.tabs().classes('w-full h-full') as tabs:
                one = ui.tab('Anwesenheiten')
                two = ui.tab('Zeitleiste')
            with ui.tab_panels(tabs, value=two).classes('w-full'):
                with ui.tab_panel(one):
                    awkt(self.course)
                    awkt(self.course, coach=True)
                with ui.tab_panel(two):
                    ui.label('Second tab')


    @staticmethod
    def show_home(container):
        container.clear()
        with container:
            ui.label('TTC Uster Dashboard').classes('text-h3')
            #TODO SHow overall statistic or choose a course