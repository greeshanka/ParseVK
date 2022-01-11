import requests
import datetime


from config import API_TOKEN, ACCESS_TOKEN, VERSION


def search_wall(group_name: str, search_word: str) -> List[str]:
    """Функция отпраляет запрос по поиску групп в вк.
    После, циклом, добавляет нужное кол-во screen_name-групп в пустой список.
    И далее отправляет по каждой найденной группе циклом запрос на нужные нам объявления.
    Далее всю нужную информацию добавялет в новый пустой список и вот уже этот список нам возвращает.
    """
    all_info = []
    all_screen_name_group = []
    group_name += ' объявления'

    group = requests.get(METHOD_GROUP_SEARCH,
                         params={
                             'access_token': ACCESS_TOKEN_VK,
                             'v': VERSION,
                             'q': group_name,
                             'type': 'group',
                             'count': 1,
                             'sort': 6,
                         }).json()['response']['items']
    for i in group:
        all_screen_name_group.append(i['screen_name'])
    print(all_screen_name_group)

    for i in all_screen_name_group:
        sear = requests.get(METHOD_WALL_SEARCH,
                            params={
                                'access_token': API_TOKEN_VK,
                                'v': VERSION,
                                'domain': i,
                                'count': 1,
                                'offset': 0,
                                'query': search_word,
                                'owners_only': 1
                            }
                            )

        data = sear.json()['response']['items']

        for post in data:
            text = post['text'] + '\n'
            all_info.append(text)
            all_info.append("\n")
            try:
                if post['attachments'][0]['type'] not in all_info:
                    url_photo = post['attachments'][-1]['photo']['sizes'][-1]['url']
                    all_info.append(url_photo)
                else:
                    print('pass')
            except KeyError:
                print('Нет фото')
    return all_info

if __name__=='__main__':
        html = search_wall(group_name=str(input('Введите имя групп: ')), search_word=str(input('Введите нужное слово: ')))










