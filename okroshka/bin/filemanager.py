
import aiofiles as aiof
import os
import config


class LogCollector:
    _id = 0

    @classmethod
    async def count(cls):
        """
        Подсчет количества строк(событий) в нынешнем файле логов
        """
        lines_counter = 0
        files = os.listdir('./logs')
        if files:
            await LogCollector._get_current_id()
            async with aiof.open(f'logs/telegram_log{cls._id}.log', 'r', encoding='cp1251') as f:
                async for line in f:
                    lines_counter += 1
        return lines_counter

    @staticmethod
    async def _get_current_id():
        """
        Получение айди для нынешенго(последнего) файла с логами
        """
        files = os.listdir('./logs')
        if files:
            LogCollector._id = int([list(file.split('.')[0])[-1] for file in os.listdir('./logs')][-1])

    @staticmethod
    async def log_create(logs):
        """
        Создание лог-файла с описанием событий. Если файл есть - он дополняется.
        Если в файле больше 20 строк (1 строка - одно событие) - создается новый файл
        """
        lines_counter = await LogCollector.count()
        files = os.listdir('./logs')
        if files:
            if lines_counter == config.MAX_LOGFILE_LINES:
                LogCollector._id += 1
                with open(f'logs/telegram_log{LogCollector._id}.log', 'w+', encoding='cp1251') as f:
                    f.write(logs)
                    print('=' * 10, 'Новый лог-файл создан', '=' * 10)
            else:
                with open(f'logs/telegram_log{LogCollector._id}.log', 'a', encoding='cp1251') as f:
                    f.write('\n' + logs)
                    print('=' * 10, 'Лог-файл дополнен', '=' * 10)
        else:
            with open(f'logs/telegram_log{LogCollector._id}.log', 'w+', encoding='cp1251') as f:
                f.write(logs)
                print('=' * 10, 'Лог-файл создан', '=' * 10)
        lines_counter = await LogCollector.count()
        print('=' * 10, 'Количество строк в лог-файле - ', lines_counter, '=' * 10)
        print('=' * 10, 'Айди - ', LogCollector._id, '=' * 10)


