
monthConversions = {
    "Jan": "January",
    1: "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
print(monthConversions["Mar"])
print(monthConversions[1])
print(monthConversions.get("1", "Not a valid key"))

