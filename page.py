from nicegui import ui
from awk_table import AWKTable as awkt
from awk_echart import AWKEchart as awke
from course_type import CourseType as ct


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
                    with ui.column().classes('w-full items-center'):
                        t = ui.toggle(['Wettkampf', 'Training', 'Dienstag', 'Mittwoch', 'Freitag'], value='Training')
                        t.props('color=black-9 text-color=white toggle-color=accent toggle-text-color=white')
                        t.on_value_change(lambda e: self.chart_display.refresh(self.get_course_type(e.value)))
                        self.chart_display(ct.exercise)
                    
    @ui.refreshable
    def chart_display(self, course_type):
        awke(self.course, course_type)

    def get_course_type(self, str_type):
        mapping = {
            'Wettkampf': ct.competition,
            'Training': ct.exercise,
            'Dienstag': ct.tuesday,
            'Mittwoch': ct.wednesday,
            'Freitag': ct.friday
        }
        return mapping.get(str_type, ct.exercise)

    @staticmethod
    def show_home(container):
        container.clear()
        with container:
            ui.label('TTC Uster Dashboard').classes('text-h3')
            #TODO SHow overall statistic or choose a course