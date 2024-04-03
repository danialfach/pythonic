profile1 = {
    "id": 2,
    "name": "john wick",
    "hobbies": ["playing with pencil"],
    "is_female": False,
}

profile2 = dict(
    set="id",
    name="john wick",
    hobbies=["playing with pencil"],
    is_female=False,
)

profile3 = dict([
    ('set', "id"),
    ('name', "john wick"),
    ('hobbies', ["playing with pencil"]),
    ('is_female', False)
])

print(profile1,profile2,profile3)

# empty dict
profile = dict()
print(profile)

profile = {}
print(profile)
