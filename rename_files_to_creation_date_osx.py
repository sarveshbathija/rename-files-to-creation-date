import glob, os, time, datetime, commands

def get_osx_creation_time(filename):
    """Accepts a filename as a string. Gets the OS X creation date/time by parsing "mdls" output.
    Returns file creation date as a float; float is creation date as seconds-since-epoch.
    """
    status, output = commands.getstatusoutput('/usr/bin/mdls -name kMDItemFSCreationDate "%s"' % (filename))
    if status != 0:
        print('Error getting OS X metadata for %s. Error was %d. Error text was: <%s>.' %
              (filename, status, output))
        sys.exit(3)
    datestring = output.split('=')[1].strip()
    datestring_split = datestring.split(' ')
    datestr = datestring_split[0]
    timestr = datestring_split[1]
    # At present, we're ignoring timezone.
    date_split = datestr.split('-')
    year = int(date_split[0])
    month = int(date_split[1])
    day = int(date_split[2])

    time_split = timestr.split(':')
    hour = int(time_split[0])
    minute = int(time_split[1])
    second = int(time_split[2])

    # convert to "seconds since epoch" to be compatible with os.path.getctime and os.path.getmtime.
    return time.mktime([year, month, day, hour, minute, second, 0, 0, -1])


os.chdir("/path/to/folder")
for file in glob.glob("*.mov"):
   date = datetime.datetime.fromtimestamp(get_osx_creation_time(file))
   month = date.month
   day = date.month
   hour = date.hour
   minute = date.minute
   second = date.second
   if month < 10:
       month = '0%s' % (month)
   if day < 10:
       day = '0%s' % (day)
   if hour < 10:
       hour = '0%s' % (hour)
   if minute < 10:
       minute = '0%s' % (minute)
   if second < 10:
       second = '0%s' % (second)
   filename = ('%s-%s-%s_%s-%s-%s.mov' % (date.year, month, day, hour, minute, second))
   os.rename(file, filename)
   print (filename)
