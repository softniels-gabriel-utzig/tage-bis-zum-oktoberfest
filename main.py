import datetime
def get_date_difference():
    date_now = datetime.datetime.now()
    oktoberfest = datetime.datetime(2023, 10, 12)
    diff_date = oktoberfest - date_now
    days = diff_date.days
    diff_date = diff_date.total_seconds()
    hours = diff_date / 3600
    diff_date = diff_date % 3600
    minutes = diff_date / 60
    diff_date = diff_date % 60
    return (days, hours, minutes, diff_date)

def get_music():
    with open('.\musics.txt', 'r') as f:
        musics = f.readlines()
        music = musics[0]
        musics = musics[1:]
        
    with open('.\musics.txt', 'w') as f:
        f.writelines(musics)
    return music

def main():
    days_remaning, hours_remaning, minutes_remaning, seconds_remaning = get_date_difference()
    txt = "Olá, faltam {days} dias, {hours} horas, {minutes} minutos e {seconds} segundos para a Softniels ir para a Oktoberfest!"
    print(txt.format(days = round(days_remaning), hours = round(hours_remaning), minutes= round(minutes_remaning), seconds = round(seconds_remaning)))
    music = get_music()

if __name__ == '__main__':
    main()