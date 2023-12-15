import datetime

timezone=datetime.datetime.now()
timezone.hour

if (timezone.hour>=4 and timezone.hour<12):
    print("Good Morning")
elif (timezone.hour>=12 and timezone.hour<16):
    print("Good Afternoon")
elif (timezone.hour>=16 and timezone.hour<20):
    print("Good Evening")
else:
    print("Good Night")
