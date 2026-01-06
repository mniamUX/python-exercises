# variable stores an HTTP response code
response_code = 200

# adding a condition
if response_code == 200:
    print("PASS")
else:
    print("FAIL")

# this condition says that only the response_code variable with value 200
# will show "PASS" as a result in the terminal,
# every other value for this variable will show "FAIL"
# important side note: = → assigns a value // == → compares values
