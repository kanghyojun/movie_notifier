import datetime

from movie.theater import CGV, Movie


def test_movie():
    movie = Movie(name='Avengers', time=['00:00'])
    assert movie.name == 'Avengers'
    assert movie.time == ['00:00']


def test_cgv_theater_code():
    assert CGV.TheaterCode.wangsimni.value == '0074'
    assert CGV.TheaterCode.yongsan.value == '0013'


def test_cgv_build_url():
    cgv = CGV(CGV.TheaterCode.yongsan)
    expected = ('http://www.cgv.co.kr/theaters/'
                '?areacode=01&theaterCode=0013&date=20180101')
    assert cgv.build_url(datetime.date(2018, 1, 1)) == expected


def test_cgv():
    cgv = CGV(CGV.TheaterCode.yongsan)
    assert cgv.area_code == CGV.AreaCode.seoul
