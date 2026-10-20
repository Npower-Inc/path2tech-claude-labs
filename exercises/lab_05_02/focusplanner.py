# focusplanner.py — starter version (intentionally fragile)

work_minutes = float(input("Enter work block length in minutes: "))
break_minutes = float(input("Enter break length in minutes: "))
num_sessions = int(input("Enter number of sessions: "))

total_study_time = work_minutes * num_sessions
total_break_time = break_minutes * (num_sessions - 1)  # no break after the last session
total_elapsed_time = total_study_time + total_break_time

print(f"Total study time: {total_study_time:.0f} minutes")
print(f"Total elapsed time (including breaks): {total_elapsed_time:.0f} minutes")
