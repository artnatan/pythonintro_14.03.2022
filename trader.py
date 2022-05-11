import csv
import json
from random import uniform
from argparse import ArgumentParser
from typing import Union


class WorkWithData:
    def __init__(self, filename_config: str, filename_current_status: str, filename_history: str):
        self.filename_config = filename_config
        self.filename_current_status = filename_current_status
        self.data_config = self.read_config()
        self.filename_history = filename_history
        self.data_status = self.read_status()
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
    def write_history(self, type_operation) -> None:
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
                                 "type_operation": type_operation
                                 })

    # операция NEXT
    def change_course(self) -> None:
        course_delta = uniform(-self.data_config['delta'], self.data_config['delta'])
        self.data_status['course'] = round(float(self.data_status['course']) + course_delta, 2)

    # операции с продажей/покупкой BUY, BUY ALL, SELL, SELL ALL
    def buy_money(self, amount: Union[str, int]) -> None:
        balance_uah = float(self.data_status['account_uah'])
        balance_usd = float(self.data_status['account_usd'])
        if float(amount) * self.data_status['course'] <= balance_uah:
            self.data_status['account_uah'] = balance_uah - float(amount) * self.data_status['course']
            self.data_status['account_usd'] = balance_usd + float(amount)
        else:
            self.get_balance(amount)

    def buy_all_money(self) -> None:
        residual = divmod(float(self.data_status['account_uah']), self.data_status['course'])
        self.data_status['account_uah'] = round(residual[1], 2)
        self.data_status['account_usd'] = float(self.data_status['account_usd']) + residual[0]

    def sell_money(self, amount: Union[str, int]) -> None:
        balance_uah = float(self.data_status['account_uah'])
        balance_usd = float(self.data_status['account_usd'])
        if float(amount) <= balance_usd:
            self.data_status['account_uah'] = balance_uah + float(amount) * self.data_status['course']
            self.data_status['account_usd'] = balance_usd - float(amount)
        else:
            self.get_balance(amount)

    def sell_all_money(self) -> None:
        uah_from_usd = float(self.data_status['account_usd']) * self.data_status['course']
        self.data_status['account_uah'] = float(self.data_status['account_uah']) + uah_from_usd
        self.data_status['account_usd'] = 0.0

    # напечатать баланс, если не хватает средств
    def get_balance(self, amount: Union[str, int]) -> None:
        print(f"UNAVAILABLE, REQUIRED BALANCE UAH {float(amount) * self.data_status['course']},"
              f"\nAVAILABLE {float(self.data_status['account_uah'])}")

    # операция RESTART
    def restart_trader(self) -> None:
        with open(self.filename_history, 'w'):
            pass
        self.data_status.clear()


def change_operation(data_worker, args: dict) -> None:
    if args['TypeOperation'] == 'RATE':     # операция RATE
        print(data_worker.data_status['course'])
    elif args['TypeOperation'] == 'AVAILABLE':     # операция AVAILABLE
        print(
            f"Account UAH: {data_worker.data_status['account_uah']} "
            f"\nAccount USD: {data_worker.data_status['account_usd']}")
    elif args['TypeOperation'] == 'BUY' and args['amount'] != 'ALL':
        data_worker.buy_money(args['amount'])
    elif args['TypeOperation'] == 'BUY' and args['amount'] == 'ALL':
        data_worker.buy_all_money()
    elif args['TypeOperation'] == 'SELL' and args['amount'] != 'ALL':
        data_worker.sell_money(args['amount'])
    elif args['TypeOperation'] == 'SELL' and args['amount'] == 'ALL':
        data_worker.sell_all_money()
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

data_worker = WorkWithData(filename_config, filename_current_status, filename_history)
change_operation(data_worker, args)
data_worker.write_status()
data_worker.write_history(args['TypeOperation'])
