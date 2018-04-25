from Schedule import Schedule

class Generator:
    
    def generate(self):
        pass
    
    def generate(self, schedule):
        if isinstance(schedule, Schedule):
            print('git')
        else:
            print('niegit')

    def generate(self, week):
        if isinstance(week, Week):
             print('git')
        else:
            print('niegit')           
