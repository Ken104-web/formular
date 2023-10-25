class SessionController(ApplicationController):
    def create(self):
        user = User.objects.get(email=params['email'])
        session['user_id'] = user.id
        if session['user_id']:
            return jsonify({'user_id': session['user_id']})
        else:
            return jsonify({'error': 'Invalid session'}), 401

    def destroy(self):
        session.pop('user_id', None)
        return '', 204

    def check(self):
        if session['user_id']:
            return jsonify({'isLoggedIn': True})
        else:
            return jsonify({'isLoggedIn': False})