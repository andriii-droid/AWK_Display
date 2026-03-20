from course import Course
from player import Player
from course_type import CourseType as ct
from awk_table import AWKTable as awkt
from page import Page

from nicegui import ui

ex = [1,1,1,1]
typ = ["T", "T", "T", "Wettkampf"]
day = ["MI", "FR", "DI", "SA"]
dat = ["12.3", "23.3", "24.3", "26.3"]

cs = [Course(executed=ex, types=typ, days=day, dates=dat, name="Test")]
Player(cs[0], [1,0,1,1], "Andri", coach=False)
Player(cs[0], [0,1,0,1], "Adrian", coach=False)


@ui.page('/')
def main_page():
    with ui.header().classes('items-center bg-accent px-4'):
        ui.label('TTC Uster').classes('text-h6 font-bold text-white')
        ui.space()
        
        with ui.button(icon='menu').props('flat').classes('text-black'):
            with ui.menu() as menu:
                ui.menu_item('Home', on_click=lambda: Page.show_home(content_area))
                ui.separator()

    for course in cs:
        with menu:
            ui.menu_item(f'{course.name}', 
                     on_click=lambda: course.page.show_content(content_area))
        
    content_area = ui.column().classes('w-full items-center p-4 mt-2')

    Page.show_home(content_area)

ui.run(dark=True)

