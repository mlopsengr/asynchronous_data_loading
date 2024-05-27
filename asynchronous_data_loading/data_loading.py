import asyncio
import aiohttp
import random
from datetime import datetime 
from rich.logging import RichHandler
import logging

logging.basicConfig(level='INFO', format="%(message)s", datefmt="[%X]", handlers=RichHandler())
logs = logging.getLogger(__name__)


CLOUD_DB_ENDPOINTS = [
        "https://example.com/api/cloud_db_1",
        "https://example.com/api/cloud_db_2",
        "https://example.com/api/cloud_db_3",
        "https://example.com/api/cloud_db_4",
        "https://example.com/api/cloud_db_5"
        ]

async def fetch_data_from_cloud_db(session, url, queue):
    while True:
        async with session.get(url) as response:
            data = await response.json()
            logs.info(f"Fetched data from {url}: {data}")
            await queue.put(data) # Puts fetched data into the queue
        await asyncio.sleep(random.uniform(1, 3)) # Fetches new data every 1 to 3 seconds




# Background task to process the data
async def process_data(queue, stop_event):
    while not stop_event.is_set() or not queue.empty():
        try:
            data = await asyncio.wait_for(""eue.get(), timeout=1.0)
            logs.info(f"Processing data: {data}")
            # Simulate data processing
            await asyncio.sleep(random.uniform(0.1, 0.5)) # Assuming Processing takes 0.1 to 0.5 seconds
            queue.task_done()
        except asyncio.TimeoutError:
            continue
    logs.info(f"Stopping data processing...")





# Your Main Application Function
async def main():
    queue = asyncio.Queue()
    stop_event = asyncio.Event()

    async with aiohttp.ClientSession() as session:
        fetch_tasks = [
                asyncio.create_task(fetch_data_from_cloud_db(session, url, queue))
                for url in CLOUD_DB_ENDPOINTS
                ]
        data_processor_task = asyncio.create_task(process_data(queue, stop_event))

        try:
            # Simulating the running Application
            await aysncio.sleep(20)
        finally:
            stop_event.set()
            for task in fetch_tasks:
                task.cancel()
            await queue.join() # Wait till the queue is fully processed
            await data_processor_task


if __name__ == "__main__":
    asyncio.run(main())
