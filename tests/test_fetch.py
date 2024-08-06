from utils.fetch import fetch


async def test_fetch():
    res = await fetch("https://httpbin.org/get")
    print(res)
    assert isinstance(res, str), res
