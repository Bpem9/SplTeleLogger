
import aiofiles as aiof
import os
import config


class LogCollector:
    _id = 0

    @classmethod
    async def count(cls):
        """
        Calculating the amount of lines(events) in current log-file
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
        Receiving of the ID of the current (last created) log-file
        """
        files = os.listdir('./logs')
        if files:
            LogCollector._id = int([list(file.split('.')[0])[-1] for file in os.listdir('./logs')][-1])

    @staticmethod
    async def log_create(logs):
        """
        Handles the creating of a log file in ./logs directory. If the file exists - it is complementing.
        If the log file includes more than 20 lines (1 line - 1 event) - the new file is creating
        """
        lines_counter = await LogCollector.count()
        files = os.listdir('./logs')
        if files:
            if lines_counter == config.MAX_LOGFILE_LINES:
                LogCollector._id += 1
                with open(f'logs/telegram_log{LogCollector._id}.log', 'w+', encoding='cp1251') as f:
                    f.write(logs)
                    print('=' * 10, 'A new log-file created', '=' * 10)
            else:
                with open(f'logs/telegram_log{LogCollector._id}.log', 'a', encoding='cp1251') as f:
                    f.write('\n' + logs)
                    print('=' * 10, 'The existing log-file complemented', '=' * 10)
        else:
            with open(f'logs/telegram_log{LogCollector._id}.log', 'w+', encoding='cp1251') as f:
                f.write(logs)
                print('=' * 10, 'A log-file created', '=' * 10)
        lines_counter = await LogCollector.count()
        print('=' * 10, 'The full amount of lines in a current log-file- ', lines_counter, '=' * 10)


