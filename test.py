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

f = Course(executed=ex, types=typ, days=day, dates=dat, name="Test")
andri = Player(f, [1,0,1,1], "Andri", coach=False)

page_nachwuchs = Page(f)

@ui.page('/')
def main_page():
    with ui.header().classes('items-center bg-blue-9 px-4'):
        ui.label('TTC Uster').classes('text-h6 font-bold text-white')
        
        ui.space() # Pushes the following button to the right
        
        with ui.button(icon='menu').props('flat'):
            with ui.menu() as menu:
                ui.menu_item('Home', on_click=lambda: Page.show_home(content_area))
                
        
    def append_item(page):
        item_count = len(menu.default_slot.children)
        # Re-enter the menu context to add a new child
        with menu:
            ui.menu_item(f'{page.course.name}', 
                     on_click=lambda: page.show_content(content_area))
            
    append_item(page_nachwuchs)
        

    content_area = ui.column().classes('w-full items-center p-4 mt-2')

    Page.show_home(content_area)

ui.run(dark=True)

