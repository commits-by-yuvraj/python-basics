monthConversions = {
    "Jan": "January",
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


# dict["key"] → Use when you're sure the key exists. If it doesn't, Python raises a KeyError.
# dict.get("key") → Use when the key might not exist and you want to avoid an error.

print(monthConversions.get("Jan", 'not found')) # default value when key doesn't exist
print(monthConversions["Jan"])

