from urllib.parse import urljoin

from niquests import AsyncSession

from .env import dev


async def fetch(url: str):
    async with AsyncSession(happy_eyeballs=dev) as session:
        res = await session.get(urljoin("https://www.genome.jp/", url))
        res.raise_for_status()
        assert res.text is not None, res
        return res.text
