profile = {
    "id": 2,
    "name": "mario",
    "hobbies": ("playing with luigi", "saving the mushroom kingdom"),
    "is_female": False,
    "affliations": [
        {
            "name": "luigi",
            "affliation": "brother"
        },
        {
            "name": "mushroom kingdom",
            "affliation": "protector"
        },
    ]
}

profile.pop("hobbies")
print(profile)

del profile["id"]
print(profile)