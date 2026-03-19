from nicegui import ui
from course_type import CourseType as ct

class AWKTable:
    columns = [
        {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True, 'align': 'left'},
        {'name': 'totAtt', 'label': 'Anwesenheit Absolut', 'field': 'totAtt', 'sortable': True},
        {'name': 'relAtt', 'label': 'Anwesenheit Relativ', 'field': 'relAtt', 'sortable': True},
    ]

    def __init__(self, course, title):
        self.course = course
        ui.table(columns=self.columns, rows=self.get_rows(), row_key='name', title=title).classes('w-200')


    def get_rows(self):
        return [
            {
                'name': p.name, 
                'totAtt': p.get_sum_abs(ct.exercise),
                'relAtt': f"{p.get_sum_rel(ct.exercise)}%"
            } 
            for p in self.course.players
        ]