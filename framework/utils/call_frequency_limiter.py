import threading
from functools import wraps
from time import sleep


class CallFrequencyLimiter:
    """
    This class declares a feature that allow to limit time between function calls.
    It can be useful to avoid access block to some API due to process request limit.

    To use that, you just need to use allowed_frequency decorator that placed at the end of this file
    on your method.
    """

    wait_thread = None
    function_calls = {}

    @classmethod
    def get_wait_object(cls, method_identifier):
        try:
            return cls.function_calls[method_identifier]
        except KeyError:
            call_frequency_limiter_object = CallFrequencyLimiter()
            cls.function_calls[method_identifier] = call_frequency_limiter_object
            return call_frequency_limiter_object

    def wait(self, call_frequency: float):
        self.wait_thread = threading.Thread(target=sleep, args=(call_frequency,))
        self.wait_thread.start()

    def finish_wait(self):
        if self.wait_thread is None:
            return
        if self.wait_thread.is_alive():
            self.wait_thread.join()


def allowed_frequency(call_frequency: float):
    """
    Decorator for limiting call frequency of methods.
    """

    def inner_wrapper(method):

        @wraps(method)
        def wrapper(*args, **kwargs):
            wait_object = CallFrequencyLimiter.get_wait_object(id(method))
            wait_object.finish_wait()
            result = method(*args, **kwargs)
            wait_object.wait(call_frequency)
            return result

        return wrapper

    return inner_wrapper
