@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    user_id = data.get('id')
    password = data.get('password')
    
    if not user_id or not password:
        return jsonify({"error": "ID and Password required"}), 400
        
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, password, tier FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
        conn.close()
        
        if user and user['password'] == password:
            return jsonify({"success": True, "tier": user['tier']})
        else:
            return jsonify({"error": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500
