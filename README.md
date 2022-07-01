# TIME CALCULATOR
The time calculator is a function that acts as a stopwatch. It adds duration time to a start time and returns a final time as the result. The starting time must be in 12-hour format and can end in AM or PM. The duration time must be in hours and minutes.
### What It Does
The time calculator takes three parameters; two required parameters and one optional parameter. The three parameters must be in string format. The parameters include:

a start time in the 12-hour clock format (ending in AM or PM)

a duration time that indicates the number of hours and minutes

(optional) a starting day of the week, case insensitive.

The function takes in the passed parameters and adds the duration time to the start time, returning the result. If the result will be the next day, it shows (next day) after the time. If the result will be more than one day later, it shows (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output displays the day of the week of the result. The day of the week in the output appears after the time and before the number of days later.

### Technologies used
The time calculator was built using python programming language.
