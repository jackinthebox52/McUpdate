from crontab import CronTab

def Scheduler(srvname):
    cron = CronTab(user='root')
    job = cron.new(command='mcupdate update name={0}'.format(srvname))
    job.day.every(1)
    cron.write()