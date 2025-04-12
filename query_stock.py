import requests
import json
import time
import re

def query_stock(stock_name):
    """Query information about a specific stock"""
    
    print(f"Querying information for {stock_name}...")
    
    try:
        # Make a POST request to the chat endpoint
        response = requests.post(
            "http://localhost:5000/api/chat",
            json={"message": f"Show me news for {stock_name}"},
            timeout=10
        )
        
        # Check if request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Print stock information
            print(f"\n{stock_name} Information:")
            print(f"Price: ₹{data.get('live_data', {}).get('price')}")
            print(f"Change: {data.get('live_data', {}).get('pChange')}%")
            
            # Save and print content
            content = data.get('content', '')
            print("\nContent:")
            print(content)
            
            # Extract and check news article links
            print("\nChecking News Article Links:")
            
            # Extract links using regex
            links = re.findall(r'Link: (https?://[^\s]+)', content)
            
            if links:
                print(f"Found {len(links)} news article links:")
                for i, link in enumerate(links):
                    print(f"{i+1}. {link}")
                    # Verify link format
                    if link.startswith("https://www."):
                        print("   ✅ Link format is correct with proper domain")
                    else:
                        print("   ❌ Link format is incorrect")
            else:
                print("No news article links found in the response")
                
                # Let's also try to get articles directly
                try:
                    article_response = requests.get(
                        f"http://localhost:5000/api/articles?entity={stock_name}",
                        timeout=10
                    )
                    
                    if article_response.status_code == 200:
                        article_data = article_response.json()
                        articles = article_data.get('articles', [])
                        
                        if articles:
                            print(f"\nFound {len(articles)} articles via direct API call:")
                            for i, article in enumerate(articles[:3]):
                                print(f"{i+1}. {article.get('title')}")
                                print(f"   URL: {article.get('url')}")
                                print(f"   Redirect URL: {article.get('redirect_url')}")
                                if article.get('redirect_url', '').startswith("https://www."):
                                    print("   ✅ Redirect URL format is correct")
                                else:
                                    print("   ❌ Redirect URL format is incorrect")
                    else:
                        print(f"Error getting articles: {article_response.status_code}")
                        
                except Exception as e:
                    print(f"Error getting articles directly: {str(e)}")
            
            return True
        else:
            print(f"Error: Received status code {response.status_code}")
            print(response.text)
            return False
            
    except Exception as e:
        print(f"Error querying {stock_name}: {str(e)}")
        return False

if __name__ == "__main__":
    # Test a specific stock
    company = "SWIGGY"  # Change to any stock you want to test
    
    success = query_stock(company)
    
    if success:
        print(f"\nSuccessfully retrieved {company} data!")
    else:
        print(f"\nFailed to retrieve {company} data.") 