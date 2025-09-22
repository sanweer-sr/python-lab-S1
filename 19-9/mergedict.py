capitals = {'Russia': 'Moscow',
            'Ukraine': 'Kiev',
            'USA': 'Washington'}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964

}

new=capitals.copy()
new.update(thisdict)
print(new)


