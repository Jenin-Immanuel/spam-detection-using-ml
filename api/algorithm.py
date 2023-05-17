import pickle

# Import the ML Model
f = open("spam_model.pickle", "rb")
mnb = pickle.load(f)
f.close()

f = open("vectorizer.pickle", "rb")
cv = pickle.load(f)
f.close()


"""
sms = pd.read_csv('spam.csv',encoding='ISO-8859-1')


# Dropping the unwanted cols
cols_to_drop = ['Unnamed: 2','Unnamed: 3','Unnamed: 4']
sms.drop(cols_to_drop,axis=1,inplace=True)
sms.columns = ['label','message']

# Converting the words into vectors 
cv = CountVectorizer(decode_error='ignore')
X = cv.fit_transform(sms['message'])

# Splitting the data into train and test datasets
# X_train, X_test, y_train, y_test = train_test_split(X, sms['label'], test_size=0.3, random_state=101)

# Train the model
mnb = MultinomialNB()
mnb.fit(X_train,y_train)
"""

def predict(message: str) -> str:
    # Transform into vecs
    vector = cv.transform([message])
    claass = mnb.predict(vector) 
    return claass[0]
