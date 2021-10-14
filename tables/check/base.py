import json
from abc import abstractmethod
from os import path

import matplotlib.pyplot as plt
from django.conf import settings


class CheckBase:
    name = ''
    graph_title = ''

    @abstractmethod
    def check_rows(self, row):
        pass

    def check_all(self):
        print(f"Benchmarking {settings.DB_ENGINE} {self.name}")
        data = []
        for rows in settings.ROWS_LIST:
            print(f'Testing inset time {rows}')
            time_taken = self.check_rows(rows)
            print(f'completed in {time_taken}')
            data.append(dict(
                rows=rows,
                time=time_taken,
            ))
        return data

    def file_name(self, engine, ):
        return path.join(settings.BASE_DIR, f'reports/data/{engine}_{self.name}.json')

    def save_file(self, data):
        file_name = self.file_name(settings.DB_ENGINE)
        with open(file_name, 'w') as fs:
            json.dump(data, fs)

    def run(self):
        data = self.check_all()
        self.save_file(data)

    def create_graph(self):
        my_colors = ('#047495', '#fac205', '#003045', '#63b2e0')
        fig, ax = plt.subplots()
        ax.set_ylabel('Time(s)')
        ax.set_xlabel('Rows')
        index = []
        values = []
        for engine in settings.DB_ENGINES:
            file_name = self.file_name(engine, )
            if not path.isfile(file_name):
                continue
            with open(file_name, 'r') as fs:
                data = json.load(fs)
                # x = list(map(lambda item: item['rows'], data))
                # y = list(map(lambda item: item['time'], data))
                values.append(data[0]['time'])
                index.append(engine)
                # ax.plot(x, y, label=engine)
        ax.set_title(self.graph_title)
        ax.bar(index, values, color=my_colors)
        ax.legend()
        file_name = path.join(settings.BASE_DIR, f'reports/graphs/{self.name}.png')
        plt.savefig(path.join(settings.BASE_DIR, f'reports/graphs/{self.name}.png'), format='png')
        print('file saved', file_name)
