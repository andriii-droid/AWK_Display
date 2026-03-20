from course_type import CourseType as ct
from nicegui import ui

class AWKEchart:

    
    def __init__(self, course, *, coach=False):
        self.course = course

        mark_data = []
        for index in self.course.get_indices_where_not_carried(ct.exercise):
            mark_data.append([
                {'xAxis': self.course.get_date_array(ct.exercise)[max(0, index - 1)]}, 
                {'xAxis': self.course.get_date_array(ct.exercise)[index]}
            ])

        self.background_series = {
            'type': 'line',
            'silent': True,
            'z': -1,
            'animation': False, 
            'emphasis': {
                'disabled': True 
            },
            'blur': {
                'itemStyle': {
                    'opacity': 1,     
                },
                'lineStyle': {
                    'opacity': 1       
                }
            },
            'markArea': {
                'silent': True,       
                'itemStyle': {
                    'color': 'rgba(255, 0, 0, 0.2)',
                    'opacity': 1       
                },
                'emphasis': {
                    'itemStyle': {
                        'color': 'rgba(255, 0, 0, 0.2)', 
                        'opacity': 1
                    }
                },
                'blur': {
                    'itemStyle': {
                        'opacity': 1   
                    }
                },
                'data': mark_data
            }
        }

        series = [
            {
                'name': p.name,
                'type': 'line',
                'data': [0, *p.get_step_arr(ct.exercise)],
                'smooth': True,
                'emphasis': {'focus': 'series'} 
            } for p in self.course.players
        ]

        series.append(self.background_series)

        options = {
            'title': {'text': 'Trainingsbeteiligung'},
            'tooltip': {
                'trigger': 'item',  
                'formatter': '{a}: {c}' 
                },    
            'legend': {'data': [player.name for player in self.course.players],
                    'type': 'scroll',
                        'orient': 'vertical',
                        'top': 50,
                        'left': 0,
                        'data': [p.name for p in self.course.players],
                        'selected': {p.name: not p.coach for p in self.course.players}},
            'xAxis': {
                'type': 'category',
                'data': ["", *self.course.get_date_array(ct.exercise)],
            },
            'yAxis': {
                'type': 'value',
                'name': 'Anwesenheit',
                'max': self.course.get_num_carried_courses(ct.exercise)
            },
            'series': series,
            'emphasis': {
            'focus': 'series'
            },
        }

        ui.echart(options=options).classes('w-full h-196')

