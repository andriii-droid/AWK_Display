from course_type import CourseType as ct
from nicegui import ui
import copy

class AWKEchart:

    template_background_series = {
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
            }
        }
    }
    
    def __init__(self, course, *, coach=False):
        self.course = course
        ui.echart(options=self.get_options(ct.exercise)).classes('w-full h-196')

    def get_mark_data(self, type):
        '''get the data to color the echart red'''
        mark_data = []
        for index in self.course.get_indices_where_not_carried(ct.exercise):
            mark_data.append([
                {'xAxis': self.course.get_date_array(type)[max(0, index - 1)]}, 
                {'xAxis': self.course.get_date_array(type)[index]}
            ])
        return mark_data
    
    def get_series(self, type):
        '''return the series for the echart'''
        background_series = copy.deepcopy(self.template_background_series)
        background_series['markArea']['data'] = self.get_mark_data(type)

        series = [
            {
                'name': p.name,
                'type': 'line',
                'data': [0, *p.get_step_arr(type)],
                'smooth': True,
                'emphasis': {'focus': 'series'} 
            } for p in self.course.players
        ]

        series.append(background_series)
        return series
    
    def get_options(self, type):
            '''return the options dict for echart'''
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
                    'data': ["", *self.course.get_date_array(type)],
                },
                'yAxis': {
                    'type': 'value',
                    'name': 'Anwesenheit',
                    'max': self.course.get_num_carried_courses(type)
                },
                'series': self.get_series(type),
                'emphasis': {
                'focus': 'series'
                },
            }
            return options


