
# HPC WEEKLY TASK AND HABIT TRACKER
# This program reads ten dictionary files and prints a weekly report
# for each file using the reporting logic from my Jupyter notebook.

from asteval import Interpreter

aeval = Interpreter()

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday']


# Generate a weekly report using the dictionaries from one file.
def report_week(habits, activities, file_name):

    # Show which dataset is being processed.
    print(f"\n===== REPORT FOR {file_name} =====")
    print("===== WEEKLY PROGRESS REPORT =====")

    # Display how many days each habit was completed.
    print("\nHABIT PROGRESS:")

    if not habits:
        print("No habits are currently being tracked.")
    else:
        for habit_name, daily_status in habits.items():
            completed_days = sum(
                1 for status in daily_status.values() if status
            )
            print(f"{habit_name}: {completed_days}/7 days complete")

    # Separate completed activities from incomplete activities.
    completed_activities = []
    incomplete_activities = []

    # Check the activities for each day of the week.
    for weekday in days:
        for activity_name, completed in activities[weekday].items():
            activity_record = f"{activity_name} ({weekday})"

            if completed:
                completed_activities.append(activity_record)
            else:
                incomplete_activities.append(activity_record)

    # Print the completed activities.
    print("\nCOMPLETED ACTIVITIES:")

    if completed_activities:
        for activity in completed_activities:
            print("ACCEPT", activity)
    else:
        print("No completed activities recorded.")

    # Print the incomplete activities.
    print("\nINCOMPLETE ACTIVITIES:")

    if incomplete_activities:
        for activity in incomplete_activities:
            print("REJECT", activity)
    else:
        print("No incomplete activities recorded.")

    if not completed_activities and not incomplete_activities:
        print("\nNo activities have been recorded for the week.")


# List all ten files that the HPC program will process.
file_list = [
    f"dictionaries_{number}.txt"
    for number in range(1, 11)
]


# Read each file and generate its weekly report.
for file_name in file_list:
    with open(file_name) as f:
        content = f.read()

        # Convert the file contents into Python dictionaries.
        data = aeval(content)

        # The first dictionary contains habits.
        # The second dictionary contains activities.
        report_week(data[0], data[1], file_name)
