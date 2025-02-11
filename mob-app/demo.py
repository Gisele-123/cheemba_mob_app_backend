

# # PostgreSQL connection
# auth.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/cheembadb'
# auth.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# auth.config['SECRET_KEY'] = 'my_secret_key'

# db = SQLAlchemy(auth)
# bcrypt = Bcrypt(auth)

# # User model
# class User(db.Model):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=True, nullable=False)
#     password = db.Column(db.String(200), nullable=False)
#     email = db.Column(db.String(80), unique=True, nullable=False)
#     location = db.Column(db.String(200), unique=True, nullable=False)
#     ch_code = db.Column(db.String(250), unique=True, nullable=False)
#     marital_status = db.Column(db.String(30), unique=False, nullable=False)
#     phone_number = db.Column(db.String(15), unique=True, nullable=False)



# @auth.route('/signup', methods=['POST'])
# def signup():
#     # Extract and validate the required fields from the request body
#     data = request.json
#     name = data.get('name')
#     email = data.get('email')
#     marital_status = data.get('marital_status')
#     location = data.get('location')
#     password = data.get('password')
#     ch_code = data.get('ch_code')
#     phone_number = data.get('phone_number')

#     # Check if all required fields are provided
#     if not all([name, email, marital_status, location, password, ch_code, phone_number]):
#         return jsonify({'message': 'All fields are required'}), 400

#     # Check if the username or email already exists
#     if User.query.filter_by(name=name).first():
#         return jsonify({'message': 'Username already exists'}), 400
#     if User.query.filter_by(email=email).first():
#         return jsonify({'message': 'Email already exists'}), 400

#     # Hash the password
#     hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

#     # Create and save the new user
#     new_user = User(
#         name=name,
#         email=email,
#         marital_status=marital_status,
#         location=location,
#         password=hashed_password,
#         ch_code=ch_code,
#         phone_number=phone_number
#     )
#     db.session.add(new_user)
#     db.session.commit()

#     return jsonify({'message': 'User created successfully'}), 201

# @auth.route('/login', methods=['POST'])
# def login():
#     data = request.json
#     name = data.get('name')
#     password = data.get('password')

#     # Validate fields
#     if not name or not password:
#         return jsonify({'message': 'Username and password are required'}), 400

#     # Find the user by name
#     user = User.query.filter_by(name=name).first()

#     if not user or not bcrypt.check_password_hash(user.password, password):
#         return jsonify({'message': 'Invalid credentials'}), 401

#     # Set user session
#     session['user_id'] = user.id
#     return jsonify({'message': 'Login successful'}), 200

# @auth.route('/logout', methods=['POST'])
# def logout():
#     session.pop('user_id', None)
#     return jsonify({'message': 'Logged out successfully'}), 200

# if __name__ == '__main__':
#     auth.run(debug=True, host='localhost', port=5000)