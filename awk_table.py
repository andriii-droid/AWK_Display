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
        table = ui.table(columns=self.columns, rows=self.get_rows(), row_key='name', title=title).classes('w-200')

        # Header Slot
        table.add_slot('header', r'''
            <q-tr :props="props">
                <q-th auto-width />
                <q-th v-for="col in props.cols" :key="col.name" :props="props">
                    {{ col.label }}
                </q-th>
            </q-tr>
        ''')

        # Body Slot with Expansion logic
        table.add_slot('body', r'''
            <q-tr :props="props">
                <q-td auto-width>
                    <q-btn size="sm" color="accent" round dense
                        :icon="props.expand ? 'remove' : 'add'" />
                </q-td>
                <q-td @click="props.expand = !props.expand" v-for="col in props.cols" :key="col.name" :props="props">
                    {{ col.value }}
                </q-td>
            </q-tr>
            
            <q-tr v-show="props.expand" :props="props">
                <q-td colspan="4" class="bg-blue-grey-10 q-pa-none">
                    <div class="q-pa-md">
                        <div class="row items-center justify-center q-gutter-md">
                            
                            <div v-for="item in props.row.details_list" :key="item.day" 
                                class="column items-center" 
                                style="width: 100px;">
                                
                                <div class="text-weight-bold text-uppercase text-caption text-accent">
                                    {{ item.day }}
                                </div>
                                <div class="text-h6 text-white">{{ item.abs }}</div>
                                <div :class="parseFloat(item.rel) >= 80 ? 'text-positive' : 'text-warning'" 
                                    class="text-caption text-weight-bold">
                                    {{ item.rel }}
                                </div>
                            </div>

                        </div>
                    </div>
                </q-td>
            </q-tr>
''')

    def get_rows(self):
        return [
            {
                'name': p.name,
                'totAtt': p.get_sum_abs(ct.exercise),
                'relAtt': f"{p.get_sum_rel(ct.exercise)}%",
                # Hier die Liste für den Loop im Slot
                'details_list': [
                    {'day': 'Match', 'abs': 1, 'rel': '100%'},
                    {'day': 'Dienstag', 'abs': 1, 'rel': '100%'},
                    {'day': 'Mittwoch', 'abs': 1, 'rel': '100%'},
                    {'day': 'Freitag', 'abs': 1, 'rel': '100%'},
                ]
            } for p in self.course.players
        ]