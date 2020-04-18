import json
import time


def foo_logs(total_foo):
    def log_foo(*args, **kwargs):
        local_time = time.localtime()
        date_today = time.strftime("%d.%m.%Y", local_time)
        time_start = time.strftime("%H:%M:%S", local_time)
        run_foo = total_foo(*args, **kwargs)
        logs = {'date':date_today, 'start':time_start, 'name':total_foo.__name__, 'args':args,
                'kwargs':kwargs, 'return':run_foo}
        with open('log_file.json', 'a') as f:
            json.dump(logs, f, indent=2)
        return run_foo
    return log_foo


@foo_logs
def test_foo(arg, kwarg='some'):

    print(f"Test {arg}, {kwarg}")
    return kwarg


test_foo("arg")
