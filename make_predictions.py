import pandas as pd
import pickle  


# Create a function for making predictions
def make_predictions(model, data_path):

  df = pd.read_csv(data_path)

  id = df['id'].values

  df['BMI'] = (df['Weight'] / (df['Height']/100)**2).round(2)
  df = pd.get_dummies(df, columns= ['Sex'], dtype=int, drop_first=True)
  df.drop(['id'], axis=1, inplace=True)

  with open(model, 'rb') as f:
    model = pickle.load(f)

  pred = model.predict(df)

  pred = pd.DataFrame({
      'id':id,
      'Calories':pred
  })

  return pred