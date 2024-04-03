import pprint
import json

profile = {
    "id": 2,
    "name": "john wick",
    "hobbies": ["playing with pencil"],
    "is_female": False,
}

print(f'profiles: {profile}')
print(f'len: {len(profile)}')

print(f'Hobbies: {profile["hobbies"]}')

print("=================================")

# pretty print dictionary
pprint.pprint(profile)

print("=================================")

print(json.dumps(profile, indent=4))
