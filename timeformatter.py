def min_to_hour(int):
    if int < 60:
        return int
    else:
        minut = int % 60
        hour = int-minut/60


def format_time(string):
    f_time = ["00"]
    if type(string) == float:
        # 00:00:00.00
        string = str(string)
        index = string.find(".")
        minutes = string[:index]
        if len(minutes) < 2:
            minutes = "0"+minutes+":"
        #if int(minutes) > 59:

        f_time.append(minutes)
        seconds = string[index+1:]
        if len(seconds) < 2:
            seconds += "0"
        f_time.append(seconds)
        return ":".join(f_time)+".00"