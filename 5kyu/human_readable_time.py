def make_readable(seconds):
    second = 0
    minute = 0
    hour = 0
    second = seconds % 60
    if seconds // 60:
        seconds = seconds // 60
        minute = seconds % 60
    if seconds // 60:
        hour = seconds // 60
    return f'{hour:0>2}:{minute:0>2}:{second:0>2}'

print(make_readable(1200))