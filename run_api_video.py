from tikapi import TikAPI, ValidationException, ResponseException

api = TikAPI("9sFIFLPbURQmvFJiAiwqqvt019Tw8prbJ9VEAh5efWLhfF07")

try:
    response = api.public.hashtag(
        name="coronavirus"
    )

    hashtagId = response.json()['challengeInfo']['challenge']['id']

    response = api.public.hashtag(
        id=hashtagId
    )

    json: dict = response.json()
    
    print(json)
    while(response):
        cursor = response.json().get('cursor')
        print("Getting next items ", cursor)
        video_index = 1
        while video_index < 30:
            response.save_video(json['itemList'][video_index]['video']['downloadAddr'], f'video_{video_index}.mp4')
            video_index += 1
            break
        response = response.next_items()
        break

except ValidationException as e:
    print(e, e.field)

except ResponseException as e:
    print(e, e.response.status_code)