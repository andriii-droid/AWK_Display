from nicegui import ui
from course_type import CourseType as ct

class AWKTable:
    columns = [
        {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True, 'align': 'left'},
        {'name': 'totAtt', 'label': 'Anwesenheit Absolut', 'field': 'totAtt', 'sortable': True},
        {'name': 'relAtt', 'label': 'Anwesenheit Relativ', 'field': 'relAtt', 'sortable': True},
    ]

    def __init__(self, course, type, *, coach=False):
        self.type = type
        self.course = course
        self.coach = coach
        title = "Spieler"
        if self.coach: 
            title = "Trainer"
        table = ui.table(columns=self.columns, rows=self.get_rows(), row_key='name', title=title).classes('w-3/4')

        table.add_slot('header', r'''
            <q-tr :props="props">
                <q-th auto-width />
                <q-th v-for="col in props.cols" :key="col.name" :props="props">
                    {{ col.label }}
                </q-th>
            </q-tr>
        ''')

        table.add_slot('body', r'''
            <q-tr :props="props">
                <q-td auto-width>
                    <q-btn size="sm" color="accent" round dense
                       @click="props.expand = !props.expand"
                        :icon="props.expand ? 'remove' : 'add'" />
                </q-td>
                <q-td @click="props.expand = !props.expand" v-for="col in props.cols" :key="col.name" :props="props">
                    {{ col.value }}
                </q-td>
            </q-tr>
            
            <q-tr v-show="props.expand" :props="props">
                <q-td colspan="4" class="q-pa-none">
                    <div class="q-pa-md">
                        <div class="row items-center justify-center q-gutter-md">
                            
                            <div v-for="item in props.row.details_list" :key="item.day" 
                                class="column items-center" 
                                style="width: 100px;">
                                
                                <div class="text-weight-bold text-uppercase text-caption text-accent">
                                    {{ item.day }}
                                </div>
                                <div class="text-h6 text-white">{{ item.abs }}</div>
                                <div :class="parseFloat(item.rel) >= 80 ? 'text-positive' : 
                                            parseFloat(item.rel) >= 50 ? 'text-warning' : 'text-negative'" 
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
                'totAtt': p.get_sum_abs(self.type),
                'relAtt': f"{p.get_sum_rel(self.type)}%",
                'details_list': self.get_details_list(p)
            } for p in self.course.players if self.coach == p.coach
        ]
    
    def get_details_list(self, player):
        details_list = [
            {'day': 'Wettkampf', 'abs': player.get_sum_abs(ct.competition), 'rel': f'{player.get_sum_rel(ct.competition)}%'},
            {'day': '', 'abs': '|', 'rel': ''},
            {'day': 'Training', 'abs': player.get_sum_abs(ct.exercise), 'rel': f'{player.get_sum_rel(ct.exercise)}%'},
                ]
        
        if player.course.get_num_carried_courses(ct.tuesday):
            details_list.append({'day': 'Dienstag', 'abs': player.get_sum_abs(ct.tuesday), 'rel': f'{player.get_sum_rel(ct.tuesday)}%'})

        if player.course.get_num_carried_courses(ct.wednesday):
            details_list.append({'day': 'Mittwoch', 'abs': player.get_sum_abs(ct.wednesday), 'rel': f'{player.get_sum_rel(ct.wednesday)}%'})
        
        if player.course.get_num_carried_courses(ct.friday):
            details_list.append({'day': 'Freitag', 'abs': player.get_sum_abs(ct.friday), 'rel': f'{player.get_sum_rel(ct.friday)}%'})

        return details_list