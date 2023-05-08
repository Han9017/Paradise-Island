#this is a nested dictionary that contains all the place and their descriptions
tile = ["Start", "A swampy land", "A charred jungle", "Bloody Lake", 
        "Demon Flower Field", "sacrificial altar", "broken church", 
        "land of cracks"]
tiles = {
  tile[0]: {
    "Description": "There's only despair here."
  },
  tile[1]: {
    "Description": "I believe that the sun will shine on this land again."
  },
  tile[2]: {
    "Description": "I believe this place used to be beautiful."
  },
  tile[3]: {
    "Description": "My teacher said he once fished here, and he said the" 
    +" lake water here was clear and bottomless."
  },
  tile[4]: {
    "Description": "Everything here makes me uneasy, why those flowers have a"
    +" human face?."
  },
  tile[5]: {
    "Description": "I can feel him here, the most evil being in this land."
  },
  tile[6]: {
    "Description": "I miss the beauty of the past."
  },
  tile[7]: {
    "Description": "I can hear the sound of hell here."
  },
}

#map------------------------------------------------------------------
map = [[tile[0], tile[1], tile[2], tile[6]],
       [tile[1], tile[4], tile[7], tile[1]],
       [tile[2], tile[1], tile[4], tile[2]],
       [tile[3], tile[2], tile[1], tile[5]]]

max_row = 3
max_col = 3
