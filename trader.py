import csv
import json
from random import uniform
from argparse import ArgumentParser


class WorkWithData:
    def __init__(self, filename_config: str, filename_current_status: str, filename_history: str, args: dict):
        self.filename_config = filename_config
        self.filename_current_status = filename_current_status
        self.data_config = self.read_config()
        self.filename_history = filename_history
        self.data_status = self.read_status()
        self.args = args
        self.history_data = self.read_history()

    # читаем конфиг
    def read_config(self) -> dict:
        with open(self.filename_config, 'r') as file:
            data_config = json.load(file)
        return data_config

    # читаем текущие данные
    def read_status(self) -> dict:
        with open(self.filename_current_status, 'r') as file:
            data_status = json.load(file)
            if data_status == {}:
                data_status = {"course": self.data_config['course'],
                               "account_uah": self.data_config['account_uah'],
                               "account_usd": self.data_config['account_usd'],
                               }
        return data_status

    # запись последней операции
    def write_status(self) -> None:
        with open(self.filename_current_status, 'w') as file:
            json.dump(self.data_status, file)

    # читаем файл с историей
    def read_history(self) -> list:
        history_data = []
        with open(self.filename_history, 'r') as file:
            reader = csv.DictReader(file)
            for index, row in enumerate(reader):
                row['number'] = index
                history_data.append(row)
        return history_data

    # записываем историю операций
    def write_history(self) -> None:
        fieldnames = ['number', 'course', 'account_uah', 'account_usd', 'type_operation']
        with open(self.filename_history, 'w') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if self.data_status != {}:
                writer.writeheader()
                writer.writerows(self.history_data)
                writer.writerow({"number": self.history_data[-1]['number'] + 1 if self.history_data != [] else 0,
                                 "course": self.data_status['course'],
                                 "account_uah": self.data_status['account_uah'],
                                 "account_usd": self.data_status['account_usd'],
                                 "type_operation": self.args['TypeOperation']
                                 })

    # операция NEXT
    def change_course(self):
        course_delta = uniform(-self.data_config['delta'], self.data_config['delta'])
        self.data_status['course'] = round(float(self.data_status['course']) + course_delta, 2)

    # операции с продажей/покупкой BUY, SELL, BUY ALL, SELL ALL
    def buy_sell_money(self):
        balance_uah = float(self.data_status['account_uah'])
        balance_usd = float(self.data_status['account_usd'])
        course = self.data_status['course']
        if self.args['TypeOperation'] == 'BUY' and self.args['amount'] != 'ALL':
            if float(self.args['amount']) * course <= balance_uah:
                self.data_status['account_uah'] = balance_uah - float(self.args['amount']) * course
                self.data_status['account_usd'] = balance_usd + float(self.args['amount'])
            else:
                print(f"UNAVAILABLE, REQUIRED BALANCE UAH {float(self.args['amount']) * course},"
                      f"\nAVAILABLE {balance_uah}")
        elif self.args['TypeOperation'] == 'BUY' and self.args['amount'] == 'ALL':
            residual = divmod(balance_uah, course)
            self.data_status['account_uah'] = round(residual[1], 2)
            self.data_status['account_usd'] = balance_usd + residual[0]
        elif self.args['TypeOperation'] == 'SELL' and self.args['amount'] != 'ALL':
            if float(self.args['amount']) <= balance_usd:
                self.data_status['account_uah'] = balance_uah + float(self.args['amount']) * course
                self.data_status['account_usd'] = balance_usd - float(self.args['amount'])
            else:
                print(f"UNAVAILABLE, REQUIRED BALANCE USD {float(self.args['amount'])},"
                      f"\nAVAILABLE {balance_usd}")
        elif self.args['TypeOperation'] == 'SELL' and self.args['amount'] == 'ALL':
            self.data_status['account_uah'] = balance_uah + balance_usd * course
            self.data_status['account_usd'] = 0.0

    # операция RESTART
    def restart_trader(self):
        with open(self.filename_history, 'w'):
            pass
        self.data_status.clear()


def change_operation(data_worker):
    if args['TypeOperation'] == 'RATE':     # операция RETE
        print(data_worker.data_status['course'])
    elif args['TypeOperation'] == 'AVAILABLE':     # операция AVAILABLE
        print(
            f"Account UAH: {data_worker.data_status['account_uah']} "
            f"\nAccount USD: {data_worker.data_status['account_usd']}")
    elif args['TypeOperation'] == 'BUY' or args['TypeOperation'] == 'SELL':
        data_worker.buy_sell_money()
    elif args['TypeOperation'] == 'NEXT':
        data_worker.change_course()
    elif args['TypeOperation'] == 'RESTART':
        data_worker.restart_trader()


filename_config = 'config.json'
filename_current_status = 'current_status.json'
filename_history = 'history.csv'

args = ArgumentParser()
args.add_argument('TypeOperation')
args.add_argument('amount', nargs='?', default=0)
args = vars(args.parse_args())

data_worker = WorkWithData(filename_config, filename_current_status, filename_history, args)
change_operation(data_worker)
data_worker.write_status()
data_worker.write_history()
