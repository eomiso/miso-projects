import functools

# Decorator factory example


def task(task_id):
    def decorator(func):
        print(f"Task {task_id}: registering {func.__name__}")

        def wrapper(*args, **kwargs):
            print(f"Task {task_id}: running {func.__name__}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


def hello_world(*args, **kwargs):
    print("Hello World!")


partial_func = functools.partial(task(task_id=3)(hello_world))

partial_func("123", "!23")
