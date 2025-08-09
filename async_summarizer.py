import asyncio
import time

class MockAsyncModel:
    async def generate_content(self, prompt):
        print(f"[Async Processing prompt: {prompt[:50]}]")
        await asyncio.sleep(3)
        return f"Summary of: {prompt[:100]}"

class MockAsyncClient:
    def __init__(self):
        self.models=MockAsyncModel()
        self.aio = self

async_client = MockAsyncClient()

async def summarize_article_async(article_text:str, request_id: int):
    start_time=time.time()
    print(f"Request{request_id}]")
    summary = await async_client.models.generate_content(article_text)

    end_time = time.time()
    duration=end_time-start_time
    print(f"[Request {request_id}] Finished asynchronous summarization in {duration:.2f}s. Summary: {summary[:50]}...")
    return summary

async def simulate_async_server():
    print("async server simulation")
    requests=["The recent study on climate change reveals alarming trends...",
        "Quantum computing is rapidly advancing, promising breakthroughs...",
        "The history of artificial intelligence dates back decades...",
        "New discoveries in space exploration are reshaping our understanding..."
    ]

    tasks = []
    for i, article in enumerate(requests):
        task=summarize_article_async(article,i+1)
        tasks.append(task)

    await asyncio.gather(*tasks)

print("--- Asynchronous Server Simulation Finished ---")

if __name__ == "__main__":
    # This is the entry point for running async code
    asyncio.run(simulate_async_server())