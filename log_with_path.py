import json
import time

def logs_with_path(path):
    def foo_logs(total_foo):
        path_to_logs = path
        def log_foo(*args, **kwargs):
            nonlocal path_to_logs
            local_time = time.localtime()
            date_today = time.strftime("%d.%m.%Y", local_time)
            time_start = time.strftime("%H:%M:%S", local_time)
            run_foo = total_foo(*args, **kwargs)
            logs = {'date':date_today, 'start':time_start, 'name':total_foo.__name__, 'args':args,
                    'kwargs':kwargs, 'return':run_foo}
            with open(path_to_logs, 'a') as f:
                json.dump(logs, f, indent=2)
            return run_foo
        return log_foo
    return foo_logs


@logs_with_path('log_file2.json')
def test_foo(*arg, **kwarg):
    print(arg)
    return kwarg


