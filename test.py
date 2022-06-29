from spotify import db, app, bcrypt
from spotify.models import User, Tracks
import pandas as pd
from flask_migrate import Migrate

df = pd.read_csv("/Users/saumyamundra/Documents/Python for Machine Learning/Projects/Spotify Project/A_Playlist.csv")
uri_series = df.iloc[:,5].str.split(':').str[-1].dropna()
migrate = Migrate(app, db)
db.create_all()
users = User.query.all()
uri_prefix = 'https://open.spotify.com/track/'
#uri = ['https://open.spotify.com/track/7BuzJmV2h6eBbSDdRaDY7C', 'https://open.spotify.com/track/4d1CG5ei1E2vGbvmgf5KKv', 'https://open.spotify.com/track/63JU4kHsgytIKkSM4tedme', 'https://open.spotify.com/track/4j3obTRIyR7QzvdeQz9vaO']
tracks = []
for i in range(1, 8):
    for j in range(i+1, 8):
        uri = uri_series.sample(n=4).to_list()
        for k in range(4):
            db.session.add(Tracks(name=f'{users[i].username}_{k}_{users[j].username}', user1=users[i].username, user2=users[j].username, uri=uri[k], link=uri_prefix+uri[k]))
# # track2 = Tracks(name=f'{users[8].username}_2_{users[5].username}', user1=users[8].username, user2=users[5].username, uri='https://open.spotify.com/track/4d1CG5ei1E2vGbvmgf5KKv')
# # track3 = Tracks(name=f'{users[8].username}_3_{users[5].username}', user1=users[8].username, user2=users[5].username, uri='https://open.spotify.com/track/4d1CG5ei1E2vGbvmgf5KKv')
# # track4 = Tracks(name=f'{users[8].username}_4_{users[5].username}', user1=users[8].username, user2=users[5].username, uri='https://open.spotify.com/track/4d1CG5ei1E2vGbvmgf5KKv')
# # # user3 = User(username='hello', email='hello@test.com', password='testing')
# # # users = [user3]
# # tracks = [track2,track3, track4]
def add_user():
    test_users = []
    for i in range(1, 11):
        test_users.append('test'+str(i))

    for user in test_users:
        hashed_password = bcrypt.generate_password_hash('testing').decode('utf-8')
        user = User(username=user, email=user+'@test.com', password=hashed_password)
        db.session.add(user)

    db.session.commit()
# for user in users:
#     db.session.add(user)
#     print(0)

# # for track in tracks:
# #     db.session.add(track)
# #     print(0)
db.session.commit()
