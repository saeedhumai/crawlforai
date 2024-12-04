import os
import asyncio  # Add this import
from datetime import datetime
from crawl4ai import AsyncWebCrawler, CacheMode
async def main():
   async with AsyncWebCrawler(verbose=True) as crawler:
      result = await crawler.arun(url="https://www.saeedanwar.pro")
      
      # Create a timestamp for the filename
      timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
      filename = f"crawl_result_{timestamp}.txt"
      
      # Ensure 'results' directory exists
      os.makedirs('results', exist_ok=True)
      
      # Save the results in a structured format
      with open(f"results/{filename}", 'w', encoding='utf-8') as f:
         f.write("=" * 50 + "\n")
         f.write("Web Crawl Results\n")
         f.write(f"URL: https://www.saeedanwar.pro\n")
         f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
         f.write("=" * 50 + "\n\n")
         
         # Write the markdown content with proper formatting
         f.write("Content:\n")
         f.write("-" * 50 + "\n")
         f.write(result.markdown)
         f.write("\n" + "-" * 50 + "\n")
      
      print(f"Results saved to: results/{filename}")
      print(f"First 500 characters of crawl result: {result.markdown[:500]}")



if __name__ == "__main__":
    asyncio.run(main())