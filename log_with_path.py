import json
import time


def logs_with_path(path):
    def foo_logs(total_foo):
        file_path = path
        def log_foo(*args, **kwargs):
            nonlocal file_path
            local_time = time.localtime()
            date_today = time.strftime("%d.%m.%Y", local_time)
            time_start = time.strftime("%H:%M:%S", local_time)
            run_foo = total_foo(*args, **kwargs)
            logs = {'date': date_today, 'start': time_start, 'name':total_foo.__name__, 'args': args,
                    'kwargs': kwargs, 'return': run_foo}
            with open(file_path, 'a') as f:
                json.dump(logs, f, indent=2)
            return run_foo

        return log_foo

    return foo_logs