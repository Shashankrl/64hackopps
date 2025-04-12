import requests
import json

def check_articles_endpoint(entity="SWIGGY"):
    """Check the articles endpoint for proper URL formatting"""
    
    print(f"Checking articles for {entity}...")
    
    try:
        # Make a request to the articles endpoint
        response = requests.get(
            f"http://localhost:5000/api/articles?entity={entity}",
            timeout=10
        )
        
        # Check if request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            articles = data.get('articles', [])
            
            print(f"\nFound {len(articles)} articles for {entity}")
            
            all_correct = True
            
            for i, article in enumerate(articles[:5]):  # Check first 5 articles
                print(f"\nArticle {i+1}: {article.get('title')}")
                print(f"Source: {article.get('source')}")
                
                # Check URL format
                url = article.get('url', '')
                redirect_url = article.get('redirect_url', '')
                
                print(f"URL: {url}")
                if url.startswith("https://www."):
                    print("✅ URL format is correct")
                else:
                    print("❌ URL format is incorrect")
                    all_correct = False
                
                print(f"Redirect URL: {redirect_url}")
                if redirect_url.startswith("https://www."):
                    print("✅ Redirect URL format is correct")
                else:
                    print("❌ Redirect URL format is incorrect")
                    all_correct = False
            
            if all_correct:
                print("\n✅ All article URLs are correctly formatted!")
            else:
                print("\n❌ Some article URLs have incorrect formatting")
            
            return True
            
        else:
            print(f"Error: Received status code {response.status_code}")
            print(response.text)
            return False
            
    except Exception as e:
        print(f"Error checking articles: {str(e)}")
        return False

if __name__ == "__main__":
    # Test articles for a specific entity
    check_articles_endpoint("SWIGGY")
    
    # Also check without entity parameter to get general articles
    print("\n" + "="*50 + "\n")
    check_articles_endpoint("")  # Empty string to check general articles 