from course import Course
from player import Player
from course_type import CourseType as ct
from awk_table import AWKTable as awkt
from page import Page
from create_awk import CreateAWK as cawk

from nicegui import ui


print(len([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
files = cawk()

@ui.page('/')
def main_page():
    with ui.header().classes('items-center bg-accent px-4'):
        ui.label('TTC Uster').classes('text-h6 font-bold text-white')
        ui.space()
        
        with ui.button(icon='menu').props('flat').classes('text-black'):
            with ui.menu() as menu:
                ui.menu_item('Home', on_click=lambda: Page.show_home(content_area))
                ui.separator()

    for course in files.course:
        with menu:
            ui.menu_item(f'{course.name}', 
                     on_click=lambda: course.page.show_content(content_area))
        
    content_area = ui.column().classes('w-full items-center p-4 mt-2')

    Page.show_home(content_area)

ui.run(dark=True)

