TIME_TYPE = [
                ['year', 31556926],
                ['day', 86400],
                ['hour', 3600],
                ['minute', 60],
                ['second', 1]
]

def format_duration(seconds):
    if seconds == 0:
        return "now"

    result = []
    for name, time in TIME_TYPE:
        curr = seconds // time
        if curr:
            if curr > 1:
                name += 's'
            result.append(f"{curr} {name}")
        seconds %= time
    return ', '.join(result[:-1]) + ' and ' +  result[-1]

print(format_duration(132113944))
