from abc import abstractmethod
from django.conf import settings
from os import path
import json


class CheckBase:
    name = ''

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

    def save_file(self, data):
        file_name = path.join(settings.BASE_DIR, f'reports/data/{settings.DB_ENGINE}_{self.name}.json')
        with open(file_name, 'w') as fs:
            json.dump(data, fs)

    def run(self):
        data = self.check_all()
        self.save_file(data)
