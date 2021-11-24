def add_time(p1, p2, day=None):
  x = p1.split(':')
  s_hour = int(x[0])
  y = p2.split(':')
  d_hour = int(y[0])
  second_split = x[1].split()
  text = second_split[1]
  s_minutes = int(second_split[0])
  d_minutes = int(y[1])
#converting the time from 12-hour format to 24-hour format.
  if 'A' in text:
    if s_hour == 12:
      s_hour = 0
    else:
      pass
  if 'P' in text:
    if s_hour == 12:
      s_hour = 12
    else:
      s_hour = s_hour + 12
#ensuring the duration minutes will add up with starting minutes to less than 60. If not, one hour is added to duration hour.
  if 60 - s_minutes < d_minutes:
    d_hour += 1
#new time is computed in the 24-hour format.
  new_hour = (s_hour + d_hour) % 24
  new_minutes = (s_minutes + d_minutes) % 60
#ensuring the new minutes remains 2-digit.
  new_minutes = str(new_minutes)
  if len(new_minutes) < 2:
    new_minutes = new_minutes.rjust(2,'0')
#converting back to 12-hour format while simultaneously determining whether the time is AM or PM.
  if new_hour == 0:
    new_hour = 12
    new_time = str(new_hour) + ':' + new_minutes + ' AM'
  elif new_hour == 12:
    new_time = str(new_hour) + ':' + new_minutes + ' PM'
  elif new_hour > 12:
    new_hour = new_hour - 12
    new_time = str(new_hour) + ':' + new_minutes + ' PM'
  else:
    new_time = str(new_hour) + ':' + new_minutes + ' AM'
#calculating the number of days.
  if ((24 - s_hour) < d_hour % 24) or (s_hour == 23 and ((60 - s_minutes) < d_minutes)):
    num_of_days = d_hour // 24 + 1
  else: 
    num_of_days = d_hour // 24
#determining the final day if given. Else, returning the new time without the day.
  if day is not None:
    day = day.lower() # in order to make the third parameter (starting day) case insensitive.
    week = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    f_day_index = week.index(day)
    if num_of_days < 1:
      return new_time + ',' + ' ' + week[f_day_index].title()
    elif num_of_days == 1:
      return new_time + ',' + ' ' + week[f_day_index + num_of_days].title() + ' ' + '(next day)'
    elif num_of_days > 1:
      return new_time + ',' + ' ' + week[f_day_index + (num_of_days % 7)].title() + ' ' + '(' + str(num_of_days) + ' days later)'
  else:
    if num_of_days < 1:
      return new_time
    elif num_of_days == 1:
      return new_time + ' ' + '(next day)'
    elif num_of_days > 1:
      return new_time + ' ' + '(' + str(num_of_days) + ' days later)'
