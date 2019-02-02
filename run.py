from app import create_app
from sqlalchemy.orm import scoped_session, sessionmaker, Query
import os
# if __name__=='__main__':
port = int(os.environ.get('PORT', 5000))
flask_app=create_app('config')
flask_app.run(host='0.0.0.0', port=port,debug=True)
# port = int(os.environ.get("PORT", 5010))
# flask_app.run(host='0.0.0.0', port=port)  