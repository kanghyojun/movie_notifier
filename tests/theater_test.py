import datetime

from movie.theater import CGV, Movie

from pytest import fixture


@fixture
def fx_cgv():
    return CGV(CGV.TheaterCode.yongsan)


def test_movie():
    movie = Movie(name='Avengers', time=['00:00'])
    assert movie.name == 'Avengers'
    assert movie.time == ['00:00']


def test_cgv_theater_code():
    assert CGV.TheaterCode.wangsimni.value == '0074'
    assert CGV.TheaterCode.yongsan.value == '0013'


def test_cgv_build_url(fx_cgv: CGV):
    expected = ('http://www.cgv.co.kr/theaters/'
                '?areacode=01&theaterCode=0013&date=20180101')
    assert fx_cgv.build_url(datetime.date(2018, 1, 1)) == expected


def test_cgv(fx_cgv: CGV):
    assert fx_cgv.area_code == CGV.AreaCode.seoul


def test_cgv_movies(fx_cgv):
    pass
