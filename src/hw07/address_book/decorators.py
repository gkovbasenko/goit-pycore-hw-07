import functools


def input_error(func):
    """Turn user-input errors raised by a command handler into a reply string."""

    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e) if str(e) else "Invalid input. Please check your command."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid input. Please check your command."

    return inner
