import requests

data = requests.get("https://sheet.best/api/sheets/3a149976-7f49-4bc2-9b60-d57e118c5dfc")

print(data.content)

# requests.post(
#     "https://sheet.best/api/sheets/3a149976-7f49-4bc2-9b60-d57e118c5dfc",
#     json={
#         'Name': 'Ram',
#         'Branch': 'AI',
#         'Email': 'ram@ram.com',
#         '': "99944320",
#     },
# )



# requests.delete("https://sheet.best/api/sheets/cf969697-682a-40e3-bad4-d54803eeeacf/Name/*Raghav*")
# requests.delete("https://sheet.best/api/sheets/cf969697-682a-40e3-bad4-d54803eeeacf/Row Number")



# # Update first row setting the name to "Jack Doe"
# requests.patch(
#     "https://sheet.best/api/sheets/cf969697-682a-40e3-bad4-d54803eeeacf/1",
#     json={
#         'Name': 'Jack Doe',
#     },
# )

# # Update the first row setting the name to "Jack Doe" and erasing other columns data
# requests.put(
#     "https://sheet.best/api/sheets/cf969697-682a-40e3-bad4-d54803eeeacf/1",
#     json={
#         'Name': 'Jack Doe',
#     },
# )


# Filtered Update
# Update all rows that have "John" inside the name column and change it to "Jack Doe"

# requests.patch(
#     "https://sheet.best/api/sheets/cf969697-682a-40e3-bad4-d54803eeeacf/Name/*John*",
#     json={
#         'Name': 'Jack Doe',
#     },
# )

# requests.put(
#     "https://sheet.best/api/sheets/cf969697-682a-40e3-bad4-d54803eeeacf/1",
#     json={
#         'Name': 'Jack Doe',
#     },
# )