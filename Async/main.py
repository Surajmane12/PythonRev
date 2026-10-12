
import time
import httpx
import asyncio

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_post(client,post_id):
    response = await client.get(f"{BASE_URL}/{post_id}", timeout=10)
    response.raise_for_status()
    post = response.json()

    print(f"Fetched post {post_id}: {post['title']}")


async def main():
    start = time.perf_counter()

    async with httpx.AsyncClient(timeout=10) as client:
        posts = await asyncio.gather(
            fetch_post(client, 1),
            fetch_post(client, 2),
            fetch_post(client, 3)
        )
    print(f"Total time: {time.perf_counter() - start:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
