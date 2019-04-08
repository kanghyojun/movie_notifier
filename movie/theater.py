import dataclasses
import datetime
import enum
import typing
import urllib.parse

__all__ = 'MovieTheater',


@dataclasses.dataclass
class Movie:

    name: str

    time: typing.Sequence[str]


class MovieTheater:

    def get_movies(self, date: datetime.date) -> typing.List[Movie]:
        raise NotImplementedError()


class CGV(MovieTheater):

    base_url = 'http://www.cgv.co.kr/theaters/'

    class TheaterCode(enum.Enum):

        wangsimni: str = '0074'

        yongsan: str = '0013'

    class AreaCode(enum.Enum):

        seoul: str = '01'

    def __init__(self, theater_code: TheaterCode):
        self.theater_code = theater_code
        self.area_code = self.AreaCode.seoul

    def build_url(self, date: datetime.date) -> str:
        scheme, netloc, path, params, _, frag = urllib.parse.urlparse(
            self.base_url
        )
        qs = urllib.parse.urlencode({
            'areacode': self.area_code.value,
            'theaterCode': self.theater_code.value,
            'date': date.strftime('%Y%m%d')
        })
        return urllib.parse.urlunparse((
            scheme,
            netloc,
            path,
            params,
            qs,
            frag
        ))

    def get_movies(self, date: datetime.date) -> typing.List[Movie]:
        return []
