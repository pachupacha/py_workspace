from datetime import datetime

print("Current Time in Different Timezones")

now = datetime.utcnow()
utc_hour = now.hour
utc_minute = now.minute
utc_second = now.second

new_york_hour = (utc_hour - 5) % 24
london_hour = (utc_hour + 0) % 24
tokyo_hour = (utc_hour + 9) % 24
sydney_hour = (utc_hour + 11) % 24
buenos_aires_hour = (utc_hour - 3) % 24

print(f"UTC: {utc_hour:02d}:{utc_minute:02d}:{utc_second:02d}")
print(f"New York: {new_york_hour:02d}:{utc_minute:02d}:{utc_second:02d}")
print(f"London: {london_hour:02d}:{utc_minute:02d}:{utc_second:02d}")
print(f"Tokyo: {tokyo_hour:02d}:{utc_minute:02d}:{utc_second:02d}")
print(f"Sydney: {sydney_hour:02d}:{utc_minute:02d}:{utc_second:02d}")
print(f"Buenos Aires: {buenos_aires_hour:02d}:{utc_minute:02d}:{utc_second:02d}")
