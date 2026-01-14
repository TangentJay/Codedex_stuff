import requests
import re

"""
Educational Penetration Testing Script for Video Privacy Controls
ONLY use on systems you own or have written permission to test!
"""

class VideoPrivacyTester:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
    
    def test_direct_url_access(self, video_id):
        """
        Test if private video URLs can be accessed directly
        Common issue: URLs are predictable but lack proper auth checks
        """
        print(f"\n[TEST 1] Testing direct URL access for video: {video_id}")
        
        # Try common URL patterns
        patterns = [
            f"{self.base_url}/video/{video_id}",
            f"{self.base_url}/videos/{video_id}.mp4",
            f"{self.base_url}/stream/{video_id}",
        ]
        
        for url in patterns:
            try:
                response = self.session.get(url)
                print(f"  URL: {url}")
                print(f"  Status: {response.status_code}")
                
                if response.status_code == 200:
                    print("  ⚠️  VULNERABLE: Direct access without authentication!")
                elif response.status_code == 403:
                    print("  ✓ Protected: Access forbidden")
                elif response.status_code == 401:
                    print("  ✓ Protected: Authentication required")
                    
            except requests.exceptions.RequestException as e:
                print(f"  Error: {e}")
    
    def test_referrer_check(self, video_url):
        """
        Test if video access relies only on Referer header
        Weakness: Referer can be spoofed
        """
        print(f"\n[TEST 2] Testing referrer-based protection")
        
        # Try without referer
        response1 = self.session.get(video_url)
        print(f"  Without Referer: {response1.status_code}")
        
        # Try with spoofed referer
        headers = {'Referer': f'{self.base_url}/authorized-page'}
        response2 = self.session.get(video_url, headers=headers)
        print(f"  With Referer: {response2.status_code}")
        
        if response1.status_code == 403 and response2.status_code == 200:
            print("  ⚠️  VULNERABLE: Only using Referer for auth (easily bypassed)")
        else:
            print("  ✓ Uses proper authentication beyond Referer")
    
    def test_token_validation(self, video_url_with_token):
        """
        Test if tokens in URLs are properly validated
        Common issues: expired tokens work, tokens not tied to user
        """
        print(f"\n[TEST 3] Testing token validation")
        
        # Extract token from URL
        token_match = re.search(r'token=([^&]+)', video_url_with_token)
        if not token_match:
            print("  No token found in URL")
            return
        
        token = token_match.group(1)
        
        # Try with modified token
        modified_url = video_url_with_token.replace(token, token[:-1] + 'X')
        response = self.session.get(modified_url)
        
        if response.status_code == 200:
            print("  ⚠️  VULNERABLE: Modified token still works!")
        else:
            print("  ✓ Token validation working properly")
    
    def test_idor(self, base_video_id):
        """
        Test for Insecure Direct Object Reference (IDOR)
        Can you access other videos by changing IDs?
        """
        print(f"\n[TEST 4] Testing for IDOR vulnerabilities")
        
        # Try sequential IDs
        test_ids = [
            int(base_video_id) - 1,
            int(base_video_id) + 1,
            int(base_video_id) + 100
        ]
        
        for vid_id in test_ids:
            url = f"{self.base_url}/video/{vid_id}"
            response = self.session.get(url)
            
            if response.status_code == 200:
                print(f"  Video ID {vid_id}: Accessible ⚠️")
            else:
                print(f"  Video ID {vid_id}: Blocked ✓")
    
    def test_metadata_leakage(self, video_id):
        """
        Test if private video metadata is exposed
        Even if video is blocked, metadata shouldn't leak
        """
        print(f"\n[TEST 5] Testing metadata leakage")
        
        endpoints = [
            f"{self.base_url}/api/video/{video_id}/info",
            f"{self.base_url}/api/video/{video_id}/thumbnail",
            f"{self.base_url}/oembed?url=video/{video_id}",
        ]
        
        for endpoint in endpoints:
            try:
                response = self.session.get(endpoint)
                if response.status_code == 200 and len(response.content) > 100:
                    print(f"  {endpoint}: ⚠️  Metadata exposed")
                else:
                    print(f"  {endpoint}: ✓ Protected")
            except:
                pass


# Example usage
if __name__ == "__main__":
    print("="*60)
    print("Video Privacy Penetration Testing Tool")
    print("For authorized testing only!")
    print("="*60)
    
    # Replace with your test environment
    tester = VideoPrivacyTester("http://localhost:5000/")
    
    # Run tests
    tester.test_direct_url_access("12345")
    tester.test_referrer_check("https://your-test-site.com/video/12345")
    tester.test_token_validation("https://your-test-site.com/video/12345?token=abc123")
    tester.test_idor("12345")
    tester.test_metadata_leakage("12345")
    
    print("\n" + "="*60)
    print("Testing complete!")