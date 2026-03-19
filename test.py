from course import Course
from player import Player
from course_type import CourseType as ct
from awk_table import AWKTable as awkt

from nicegui import ui

ex = [1,1,1,1]
typ = ["T", "T", "T", "Wettkampf"]
day = ["MI", "FR", "DI", "SA"]
dat = ["12.3", "23.3", "24.3", "26.3"]

f = Course(executed=ex, types=typ, days=day, dates=dat)
andri = Player(f, [1,0,1,1], "Andri", coach=False)


@ui.page('/')
def home_page():
    with ui.row().classes('w-full items-center'):
        ui.label('AWK Display').classes('mr-auto text-2xl font-bold')
        with ui.button(icon='menu'):
            with ui.menu() as menu:
                ui.menu_item('Go to Settings', lambda: ui.navigate.to('/settings'))

# 2. Define the Second Page
@ui.page('/settings')
def settings_page():
    ui.label('Settings Page')
    ui.button('Go Back Home', on_click=lambda: ui.navigate.to('/'))


ui.run(dark=True)