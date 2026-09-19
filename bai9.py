

list_data = [
    {
        "id":1,
        "plate":"ABC"
    },
    {
        "id":2,
        "plate":"ERT"
    },
]

# list_data.pop(0)

list_data.append({
    "id":list_data[-1]['id']+1,
    "plate": "DCB"
})
print(list_data)