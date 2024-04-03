# Return statements in a Python script
def calculate_fails(total_attempts, failed_attempts):
    fail_percentage = failed_attempts / total_attempts
    return fail_percentage

percentage = calculate_fails(1,2)

if (percentage >= .5):
    print("Account locked.")