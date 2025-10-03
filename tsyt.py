from flask import Flask, request, jsonify, send_file
import os

app = Flask(__name__)

# Fake database of videos
# In real life, this would be a real database
videos = {
    "1": {"title": "Public Cat Video", "private": False, "owner": "user1"},
    "2": {"title": "Private Birthday Party", "private": True, "owner": "user1"},
    "3": {"title": "Secret Company Meeting", "private": True, "owner": "user2"},
    "4": {"title": "Public Tutorial", "private": False, "owner": "user2"},
}

# Fake users (normally you'd have real authentication)
current_user = None


@app.route('/')
def home():
    return """
    <h1>Vulnerable Video Site - For Testing Only!</h1>
    <p>This site has intentional security flaws for learning.</p>
    <h2>Available Videos:</h2>
    <ul>
        <li><a href="/video/1">Video 1 - Public Cat Video</a></li>
        <li><a href="/video/2">Video 2 - Private Birthday Party</a></li>
        <li><a href="/video/3">Video 3 - Secret Company Meeting</a></li>
        <li><a href="/video/4">Video 4 - Public Tutorial</a></li>
    </ul>
    <h2>API Endpoints to Test:</h2>
    <ul>
        <li>/video/[id] - View video</li>
        <li>/videos/[id].mp4 - Direct video file</li>
        <li>/stream/[id] - Stream video</li>
        <li>/api/video/[id]/info - Get video metadata</li>
    </ul>
    """


@app.route('/video/<video_id>')
def view_video(video_id):
    """
    VULNERABILITY #1: No authentication check!
    Anyone can view any video by knowing the ID
    """
    if video_id not in videos:
        return "Video not found", 404
    
    video = videos[video_id]
    
    # BUG: We check if it's private but don't actually block access!
    if video["private"]:
        print(f"Warning: Private video {video_id} being accessed!")
    
    return f"""
    <h1>{video['title']}</h1>
    <p>Video ID: {video_id}</p>
    <p>Owner: {video['owner']}</p>
    <p>Private: {video['private']}</p>
    <video width="320" height="240" controls>
        <source src="/videos/{video_id}.mp4" type="video/mp4">
    </video>
    """


@app.route('/videos/<video_id>.mp4')
def direct_video(video_id):
    """
    VULNERABILITY #2: Direct file access without auth
    """
    # Remove the .mp4 extension to get the ID
    vid_id = video_id.replace('.mp4', '')
    
    if vid_id not in videos:
        return "Video not found", 404
    
    # No check if video is private or if user has access!
    return f"[This would be video file data for video {vid_id}]", 200


@app.route('/stream/<video_id>')
def stream_video(video_id):
    """
    VULNERABILITY #3: Only checks Referer header (can be spoofed)
    """
    if video_id not in videos:
        return "Video not found", 404
    
    video = videos[video_id]
    
    # Weak security: only checking referer
    referer = request.headers.get('Referer', '')
    
    if video["private"] and 'localhost' not in referer:
        return "Access denied - no referer", 403
    
    # If referer contains localhost, allow access (easily spoofed!)
    return f"[Streaming video {video_id}: {video['title']}]", 200


@app.route('/api/video/<video_id>/info')
def video_info(video_id):
    """
    VULNERABILITY #4: Metadata leakage
    Private video info is exposed even without access
    """
    if video_id not in videos:
        return jsonify({"error": "Not found"}), 404
    
    video = videos[video_id]
    
    # BUG: Returning full info even for private videos!
    return jsonify({
        "id": video_id,
        "title": video["title"],
        "owner": video["owner"],
        "private": video["private"],
        "views": 1337,
        "upload_date": "2024-01-15"
    })


@app.route('/api/video/<video_id>/thumbnail')
def video_thumbnail(video_id):
    """
    VULNERABILITY #5: Thumbnails leak for private videos
    """
    if video_id not in videos:
        return "Not found", 404
    
    # Should check if video is private and user has access, but doesn't!
    return f"[Thumbnail image for video {video_id}]", 200


if __name__ == '__main__':
    print("\n" + "="*60)
    print("VULNERABLE TEST WEBSITE")
    print("Running on: http://localhost:5000")
    print("="*60)
    print("\nThis site has intentional vulnerabilities:")
    print("1. No authentication on private videos")
    print("2. Direct file access without checks")
    print("3. Weak referer-based protection")
    print("4. Metadata leakage")
    print("5. Thumbnail leakage")
    print("\nUse the penetration testing script to find these flaws!")
    print("="*60 + "\n")
    
    app.run(debug=True, port=5000)