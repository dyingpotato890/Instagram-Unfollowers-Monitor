import json
import pandas as pd

# Getting JSON file paths
followers_path = input("Enter The Path for 'followers_1.json': ").replace('"', "").replace('\\', '/')
following_path = input("Enter The Path for 'following.json': ").replace('"', "").replace('\\', '/')

# Opening the files
followers =  open(followers_path, "r")
followers_data = json.load(followers)

following =  open(following_path, "r")
following_data = json.load(following)

# Pulling User ID And Link For Followers And Following
followers_list = [i["string_list_data"][0]['value'] for i in followers_data]

following_list = [i["string_list_data"][0]['value'] for i in following_data["relationships_following"]]
following_href = [i["string_list_data"][0]['href'] for i in following_data["relationships_following"]]

unfollow = {"Username": [],
            "Link": []}

# Append to Dictionary If They Have Unfollowed
for i in following_list:
    if i not in followers_list:
        unfollow["Username"].append(i)
        unfollow["Link"].append(following_href[following_list.index(i)])

# Convert Dictionary To An Excel File
df = pd.DataFrame(unfollow)
try:
    df.to_excel("unfollow.xlsx", index = False)
    print("\nAn Excel File Has Been Created Successfully!")
except:
    print("\nThere Was Some Error In Creating The Excel File")