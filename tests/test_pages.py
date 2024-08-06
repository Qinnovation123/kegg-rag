from kegg.index import get_pathways


async def test_index_page():
    pathways = await get_pathways()
    print(f"{len(pathways) = }")
