from collections import namedtuple
from itertools import batched

from parsel import Selector
from utils.fetch import fetch

Pathway = namedtuple("Pathway", ["kid", "integrations", "title", "href"])


async def get_pathways():
    html = await fetch("/kegg/pathway.html")

    results: list[Pathway] = []

    for dt, dd in batched(Selector(html).css("div.main").css("dl:has(a)").css("dt, dd"), 2):
        [kid] = dt.re(r"\d+")
        integrations = dt.re(r"[MRN]")
        [title, *_] = dd.css("a::text").extract()
        [href, *_] = dd.css("a::attr(href)").extract()
        results.append(Pathway(kid, integrations, title, href))

    return results
