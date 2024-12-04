import os
import asyncio  # Add this import
from datetime import datetime
from crawl4ai import AsyncWebCrawler, CacheMode
from fastapi import FastAPI
app = FastAPI()

@app.post("/crawl")
async def crawl_webpage(weburl: str):
   async with AsyncWebCrawler(verbose=True) as crawler:
      result = await crawler.arun(url=weburl)
   
      filename = "results"
      # Ensure 'results' directory exists
      os.makedirs('results', exist_ok=True)
      
      # Save the results in a structured format
      with open(f"results/{filename}", 'w', encoding='utf-8') as f:
         f.write("=" * 50 + "\n")
         f.write("Web Crawl Results\n")
         f.write(f"URL: {weburl}\n")
         f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
         f.write("=" * 50 + "\n\n")
         
         # Write the markdown content with proper formatting
         f.write("Content:\n")
         f.write("-" * 50 + "\n")
         f.write(result.markdown)
         f.write("\n" + "-" * 50 + "\n")
      
      print(f"Results saved to: results/{filename}")
      print(f"First 500 characters of crawl result: {result.markdown[:500]}")
      return {"message": "Crawl completed successfully"}



if __name__ == "__main__":
    asyncio.run(main())