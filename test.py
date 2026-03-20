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
    # 1. Create a LOCAL container for THIS specific browser session
    content_area = ui.column().classes('w-full items-center border p-4')
    
    # 2. Navigation
    with ui.row().classes('w-full justify-center bg-blue-1 p-2'):
        # We use a lambda to pass the 'content_area' into the methods
        ui.button('Dashboard', on_click=lambda: Page.show_home(content_area))
        ui.button('Nachwuchs', on_click=lambda: page_nachwuchs.show_content(content_area))

    # 3. Initial Render
    Page.show_home(content_area)

ui.run(dark=True)