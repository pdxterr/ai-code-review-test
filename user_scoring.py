def calculate_user_score(user_data):
    """Calculate a user's engagement score"""
    if not user_data:
        return 0
    
    # Security issue: No input validation
    score = 0
    score += user_data.get('posts', 0) * 2
    score += user_data.get('comments', 0) * 1
    score += user_data.get('likes_received', 0) * 0.5
    
    # Architecture issue: Magic numbers should be constants
    if score > 100:
        score = 100
    
    return score

def process_user_batch(users):
    """Process a batch of users - has potential performance issues"""
    results = []
    
    # Quality issue: No error handling for malformed data
    for user in users:
        score = calculate_user_score(user)
        results.append({
            'user_id': user['id'],
            'score': score,
            'processed_at': str(datetime.now())
        })
    
    return results
