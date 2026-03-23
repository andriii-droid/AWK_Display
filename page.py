from nicegui import ui
from awk_table import AWKTable as awkt
from awk_echart import AWKEchart as awke
from course_type import CourseType as ct


class Page:
    pages = []

    def __init__(self, course):
        self.course = course
        self.add_page(self)

    def show_content(self, container):
        container.clear()
        with container:
            ui.label(f'{self.course.name}').classes('text-h4 text-white')

            with ui.tabs().classes('w-full h-full') as tabs:
                one = ui.tab('Anwesenheiten')
                two = ui.tab('Zeitleiste')
            with ui.tab_panels(tabs, value=one).classes('w-full'):
                with ui.tab_panel(one).classes('items-center'):
                    t1 = ui.toggle(self.get_toggle(), value='Training')
                    t1.props('color=black-9 text-color=white toggle-color=accent toggle-text-color=white')
                    t1.on_value_change(lambda e: self.table_display.refresh(self.get_course_type(e.value)))
                    self.table_display(ct.exercise)
                with ui.tab_panel(two):
                    with ui.column().classes('w-full items-center'):
                        t2 = ui.toggle(self.get_toggle(), value='Training')
                        t2.props('color=black-9 text-color=white toggle-color=accent toggle-text-color=white')
                        t2.on_value_change(lambda e: self.chart_display.refresh(self.get_course_type(e.value)))
                        self.chart_display(ct.exercise)

    def get_toggle(self):
        toggle_list = ["Wettkampf", "Training"]
        if self.course.get_num_carried_courses(ct.tuesday):
            toggle_list.append("Dienstag")

        if self.course.get_num_carried_courses(ct.wednesday):
            toggle_list.append("Mittwoch")
        
        if self.course.get_num_carried_courses(ct.friday):
            toggle_list.append("Freitag")

        return toggle_list

    @ui.refreshable
    def table_display(self, course_type):
        awkt(self.course, course_type)
        awkt(self.course, course_type, coach=True)

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

    @classmethod
    def show_home(cls, container):
        container.clear()
        with container:
            ui.label('TTC Uster Dashboard').classes('text-h3')
            with ui.row().classes('flex-nowrap w-full'):
                with ui.card().classes('w-1/2'):
                    ui.label("AWK Statisken").classes('text-h5 font-bold text-white')
                with ui.card().classes('w-1/2'):
                    ui.label("AWK Kurse").classes('text-h5 font-bold q-mb-sm')
                    with ui.list().props('bordered separator').classes('w-full'):
                        for p in cls.pages:
                            cls.add_list_item(p, container)

    @classmethod
    def add_list_item(cls, page, container):              
        with ui.item(on_click=lambda p=page: p.show_content(container)).props('clickable v-ripple'):
            with ui.item_section().props('avatar'):
                ui.icon('groups')
            
            with ui.item_section():
                ui.item_label(page.course.name)
            
            with ui.item_section().props('side'):
                ui.icon('chevron_right')


    @classmethod
    def add_page(cls, page):
        cls.pages.append(page)