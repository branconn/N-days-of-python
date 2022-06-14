import colorgram
colors = colorgram.extract("image.jpg", 12)
listed_colors = []
for color in colors:
    tup = (color.rgb.r, color.rgb.g, color.rgb.b)
    listed_colors.append(tup)
listed_colors = listed_colors[4:12]
print(listed_colors)


