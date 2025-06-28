import pandas as pd
import re
def preprocessor(data):
 pattern = r'(\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s(?:am|pm)\s-\s)(.*)'
 matches = re.findall(pattern, data)
 dates = [match[0] for match in matches]
 messages = [match[1] for match in matches]
 dates = re.findall(pattern, data)
 df = pd.DataFrame({'user_message': messages, 'message_date': dates})
 # Extract the date string from the tuple and replace the unicode character
 df['date_str'] = df['message_date'].apply(lambda x: x[0].replace('\u202f', ' '))
 # Convert the cleaned date string to datetime objects
 df['date'] = pd.to_datetime(df['date_str'], format='%d/%m/%y, %I:%M %p - ')
 # Drop the intermediate column and the original message_date column
 df.drop(columns=['message_date', 'date_str'], inplace=True)
 df.head()
 users_list = []
 messages_list = []
 for msg in df['user_message']:
     entry = re.split('([\w\W]+?):\s', msg)
     if entry[1:]:
         users_list.append(entry[1])
         messages_list.append(entry[2])
     else:
         users_list.append('group_notification')
         messages_list.append(entry[0])
 df['user'] = users_list
 df['message'] = messages_list
 df.drop(columns=['user_message'], inplace=True)
 df['year'] = df['date'].dt.year
 df['month'] = df['date'].dt.month_name()
 df['day'] = df['date'].dt.day
 df['hour'] = df['date'].dt.hour
 df['minute'] = df['date'].dt.minute
 return df
