profile = {
    "id": 2,
    "name": "mario",
    "hobbies": ("playing with luigi", "saving the mushroom kingdom"),
    "is_female": False,
}
print("name:", profile["name"])

profile["name"] = "mario mario"
print("name:", profile["name"])
