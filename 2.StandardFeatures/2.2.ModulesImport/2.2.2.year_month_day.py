import redirect
import datetime

date = datetime.date(*map(int, input().split()))
days = int(input())
end_date = date + datetime.timedelta(days=days)
print(end_date.year, end_date.month, end_date.day)
