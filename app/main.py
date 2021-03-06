import download_metadata

# Ask the user to distinguish if they want to download a playlist or URL
def set_URL_options(URL_options_list = []):
    URL_options = {}
    while True:
        playlist_bool = input("Do you wish to download a playlist or individual video (1 for playlist 0 for single video) ")
        if playlist_bool not in ["0", "1"]:
            print("Sorry, please input either a 1 or a 0")
            continue
        else:
            URL_options["playlist_bool"] = playlist_bool
            break

    URL = input("Please enter the URL: ")
    URL_options["URL"] = URL

    # Ask the user if the playlist/URL contains only songs, only non-songs, or mixed videos
    while True:
        type = "playlist" if playlist_bool == "1" else "single video"
        URL_options['type'] = type
        SongsOrNotOrMixed = input(f"Does this {type} contain only songs ( 1 ) only non-songs ( 0 ) or a mix ( 2 )? ")
        if SongsOrNotOrMixed not in ["0", "1", "2"]:
            print("Sorry, please input either a 0 if it's only songs, a 1 if there's only non-songs, or a 2 if it's a mix")
            continue
        else:
            URL_options["SongsOrNotOrMixed"] = SongsOrNotOrMixed
            break

    name = input(f"Please input the name of this {type}: ")
    URL_options['Name'] = name

    # Append specified options to list
    URL_options_list.append(URL_options)

    ### TO WORK ON: allow multiple playlists/urls to be entered
    while True:
        multiple = input(f"Do you want to input another URL to download? (0 for no, 1 for yes) ")
        if multiple not in ["0", "1"]:
            print("Sorry, please input either a 0, or a 1")
            continue
        elif multiple == "1":
            URL_options_list = set_URL_options(URL_options_list)
            break
        else:
            break
    return URL_options_list


def set_URL_options_helper(URL_options_list=[]):
    pass

if __name__ == "__main__":
    # Ask the user what type of URL is being input
    options = set_URL_options()
    print([i for i in options])
    number_of_downloads = len(options)
    counter = 1
    downloaded = 0
    for option in options:
        # Save the video metadata in the appropriate places
        if option['SongsOrNotOrMixed'] == "1":
            path = f"../data/music_data/{option['Name']}.csv"
        elif option['SongsOrNotOrMixed'] == "0":
            path = f"../data/non_music_data/{option['Name']}.csv"
        else:
            path = f"../data/mixed_data/{option['Name']}.csv"

        if option['playlist_bool'] == "0":
            print('Sorry, the functionality to classify/download an individual video URL hasn\'nt been built yet')
            counter += 1
        else:
            df = download_metadata.playlist_features_csv(option['URL'], 'ALL')
            df.to_csv(path)
            print(f"COMPLETED DOWNLOAD OF METADATA: {option['type']} {counter} of {number_of_downloads} saved in {path}")
            counter += 1
            downloaded += 1

    print(f"DOWNLOADS COMPLETED: SUCCESSFULLY DOWNLOADED {downloaded} out of {number_of_downloads} playlists")


### YouTube playlist URLs:
"""
NON-MUSIC
Daily dose of internet science videos (x67)
https://www.youtube.com/playlist?list=PLlUZ3i-FUgHodW67Vr0YxU_5G_CaHI27G
Short memes (x67)
https://www.youtube.com/playlist?list=PLFr3c472VstyuniFqFD6KBtzQhLuT_BKO
Favorite podcasts (x25)
https://www.youtube.com/playlist?list=PLjsZNSbnATzpFuhFvUsUecDVRfV6h9gZ5
Deep learning lectures
https://www.youtube.com/playlist?list=PLjsZNSbnATzpX4RRhizQPmlmd8FOmLg2K

MUSIC
Peaceful piano
https://www.youtube.com/playlist?list=PLRpbxz3LvOYCQU6qBvtEcj9Boof7Y8Al3

"""