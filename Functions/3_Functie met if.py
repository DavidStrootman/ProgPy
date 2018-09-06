def lang_genoeg(lengte):
    if 120 <= lengte:
        return 'Je bent lang genoeg voor de attractie!'
    else:
        return 'Sorry, je bent te klein!'


print(lang_genoeg(120))
