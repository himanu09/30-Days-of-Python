import asyncio
from pydoc import text
import aiohttp
import aiofiles

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        responce = await session.get(url)
        html = await responce.text()
        return html

async def text_in_file(file,text):
    async with aiofiles.open(file,"w") as f:
        await f.write(text)

async def main(urls):
    tasks=[]
    for url in urls:
        file = f'{url.split("//")[-1]}.txt'
        html = await fetch(url)
        tasks.apppends(text_in_file(file,text))
    await asyncio.gather(*tasks)

urls= ("https://python.org","https://stackoverflow.com","https://google.com")
asyncio.run(main(urls))