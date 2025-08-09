import time, threading

class MockSyncModel:
    def generate_content(self, prompt):
        print(f"Processing Prompt:{prompt[:50]}")
        time.sleep(3) # Simulating 3 seconds AI processing time
        return f"Summary of: {prompt[:100]}"

class MockSyncClient:
    def __init__(self):
        self.models= MockSyncModel()

sync_client = MockSyncClient()

def summarize_article_sync(article_text: str, request_id: int):
    start_time = time.time()
    print(f"[Request {request_id}] received article for synchronous summary")
    summary = sync_client.models.generate_content(article_text)
    end_time=time.time()
    duration=end_time-start_time
    print(f"[Reqeust{request_id}] Finished syncronous summarization in {duration: .2f}s.")
    return summary

def simulate_sync_server():
    print("Starting Synchronous Server Simulation")
    requests=[
        "The recent study on climate change reveals alarming trends...",
        "Quantum computing is rapidly advancing, promising breakthroughs...",
        "The history of artificial intelligence dates back decades...",
        "New discoveries in space exploration are reshaping our understanding..."
    ]
    threads = []
    for i, article in enumerate(requests):
        thread=threading.Thread(target=summarize_article_sync, args=(article, i+1))
        threads.append(thread)
        thread.start()
        time.sleep(0.5)
    for thread in threads:
        thread.join() # wait for all threads to complete
    
    print("---Synchronous Server Simulation Finished ---")


if __name__ == "__main__":
    simulate_sync_server()