from tikapi import TikAPI, ValidationException, ResponseException
import json

api = TikAPI("9sFIFLPbURQmvFJiAiwqqvt019Tw8prbJ9VEAh5efWLhfF07")

try:
    response = api.public.hashtag(name="coronavirus")
    hashtagId = response.json()['challengeInfo']['challenge']['id']

    response = api.public.hashtag(id=hashtagId)
    json_data: dict = response.json()
    filename = "test_5.json"
    
    with open(filename, 'w') as file:
        file.write("[\n")
        iteration = 30
        while response:
            
            cursor = response.json().get('cursor')
            print("Getting next items ", cursor)
            num_vid = int(cursor)
            video_index = 1
            
            while 1:
                try:
                    author_data = json_data["itemList"][video_index]["author"]
                    author_data.pop("avatarLarger", None)
                    author_data.pop("avatarMedium", None)
                    author_data.pop("avatarThumb", None)

                    author_stat = json_data["itemList"][video_index]["authorStats"]

                    hashtag = [{"hashtagId": item["hashtagId"], "hashtagName": item["hashtagName"]} 
                               for item in  json_data["itemList"][video_index].get("textExtra", [])
                    ]

                    meta_data = {
                        "author": author_data, 
                        "author_stat": author_stat,
                        "createTime": json_data["itemList"][video_index]["createTime"],
                        "desc": json_data["itemList"][video_index]["desc"],
                        "digged": json_data["itemList"][video_index]["digged"],
                        "duetDisplay": json_data["itemList"][video_index]["duetDisplay"],
                        "duetEnabled": json_data["itemList"][video_index]["duetEnabled"],
                        "officalItem": json_data["itemList"][video_index]["officalItem"],
                        "originalItem": json_data["itemList"][video_index]["originalItem"],
                        "stats": json_data["itemList"][video_index]["stats"],
                        "stickersOnItem": json_data["itemList"][video_index].get("stickersOnItem", None),
                        "stitchDisplay": json_data["itemList"][video_index]["stitchDisplay"],
                        "stitchEnabled": json_data["itemList"][video_index]["stitchEnabled"],
                        "hashtagInfo": hashtag,
                        "videoURL": json_data['itemList'][video_index]['video']['downloadAddr'],
                    } 
                    json.dump(meta_data, file, indent=4)
                    file.write(",\n")
                    video_index += 1
                except IndexError:
                    # If video_index exceeds the available range, break the loop and get new response
                    break
            iteration = iteration - 1
            if iteration < 0: break
            response = response.next_items()
        
        file.write("]")
        

except ValidationException as e:
    print(e, e.field)

except ResponseException as e:
    print(e, e.response.status_code)
