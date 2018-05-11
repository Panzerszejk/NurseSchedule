class Exporter:
    def export(self,days):
        f = open('workfile.txt', 'w')
        for i in range(35):
            f.write(''.join(days[i]))
