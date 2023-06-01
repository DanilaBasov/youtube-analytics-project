from src.channel import Channel


def test_print_info():
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')

    assert moscowpython.print_info() == {'etag': '271grJ8hNCh7MtMrY5vgbqBM9ks',
     'items': [{'etag': 'AoNJLKi85KxHhLdeei-tLjmOKd4',
                'id': 'UC-OVMPlMA3-YCIeg4z5z23A',
                'kind': 'youtube#channel',
                'snippet': {'country': 'RU',
                            'customUrl': '@moscowdjangoru',
                            'description': 'Видеозаписи со встреч питонистов и '
                                           'джангистов в Москве и не только. :)\n'
                                           'Присоединяйтесь: '
                                           'https://www.facebook.com/groups/MoscowDjango! '
                                           ':)',
                            'localized': {'description': 'Видеозаписи со встреч '
                                                         'питонистов и джангистов '
                                                         'в Москве и не только. '
                                                         ':)\n'
                                                         'Присоединяйтесь: '
                                                         'https://www.facebook.com/groups/MoscowDjango! '
                                                         ':)',
                                          'title': 'MoscowPython'},
                            'publishedAt': '2012-07-13T09:48:44Z',
                            'thumbnails': {'default': {'height': 88,
                                                       'url': 'https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s88-c-k-c0x00ffffff-no-rj',
                                                       'width': 88},
                                           'high': {'height': 800,
                                                    'url': 'https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s800-c-k-c0x00ffffff-no-rj',
                                                    'width': 800},
                                           'medium': {'height': 240,
                                                      'url': 'https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s240-c-k-c0x00ffffff-no-rj',
                                                      'width': 240}},
                            'title': 'MoscowPython'},
                'statistics': {'hiddenSubscriberCount': False,
                               'subscriberCount': '26000',
                               'videoCount': '686',
                               'viewCount': '2316562'}}],
     'kind': 'youtube#channelListResponse',
     'pageInfo': {'resultsPerPage': 5, 'totalResults': 1}}

