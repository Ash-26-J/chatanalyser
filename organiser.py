import emoji
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji

def fetch_stats(selected_user,df):
    if selected_user == 'overall':
        num_message= df.shape[0]
        verb = []
        for message in df['message']:
            verb.extend(message.split())

        num_media_message = df[df['message'] == '<Media omitted>'].shape[0]
        from urlextract import URLExtract
        extract = URLExtract()
        url = []
        for message in df['message']:
            url.extend(extract.find_urls(message))
        all_emoji = []

        for message in df['message']:
            emojis_in_messages = emoji.emoji_list(message)
            for emo_dict in emojis_in_messages:
                all_emoji.append(emo_dict['emoji'])

        return num_message, len(verb),num_media_message,len(all_emoji),len(url)

    else:
        df = df[df['user'] == selected_user]

    # fetch the number of messages
    num = df.shape[0]

    # fetch the total number of words
    words = []
    for message in df['message']:
        words.extend(message.split())

    # fetch number of media messages
    num_media_messages = df[df['message'] == '<Media omitted>'].shape[0]
    from urlextract import URLExtract
    extract = URLExtract()
    urls = []
    for message in df['message']:
        urls.extend(extract.find_urls(message))
    all_emojis = []

    for message in df['message']:
        emojis_in_message = emoji.emoji_list(message)
        for emo_dict in emojis_in_message:
            all_emojis.append(emo_dict['emoji'])

    return num,len(words),num_media_messages,len(urls),len(all_emojis)
def fetch_busy_users(df):
   x = df['user'].value_counts().head()
   ndf=round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'name', 'user': 'percent'})
   return x,ndf
def created_wordcloud(selected_user,df):
    if selected_user != 'overall':
        df = df[df['user'] == selected_user]
    wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    dfwc=wc.generate(df['message'].str.cat(sep=""))
    return dfwc
def most_common_words(selected_user,df):
    if selected_user != 'overall':
        df = df[df['user'] == selected_user]
    words=[]
    for message in df['message']:
        words.extend(message.split())
    word_counts = Counter(words)  # Count frequency of words
    most_common_20 = word_counts.most_common(20)  # List of (word, count) tuples

    most_common_df = pd.DataFrame(most_common_20, columns=['word', 'count'])
    return most_common_df


def emoji_analyse(selected_user, df):
    if selected_user != 'overall':
        df = df[df['user'] == selected_user]

    emojis = []
    for message in df['message']:
        # This line was missing proper indentation
        emojis.extend([c for c in message if emoji.is_emoji(c)])

    # This line was also missing proper indentation
    return pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
def monthly_timeline(selected_user, df):
    if selected_user != 'overall':
        df = df[df['user'] == selected_user]
    timeline = df.groupby(['year', 'month']).count()['message'].reset_index()
    time = []
    timeline = df.groupby(['year', 'month']).count()['message'].reset_index()
    for i in range(timeline.shape[0]):
        time.append(str(timeline['month'][i]) + "-" + str(timeline['year'][i]))

    timeline['time'] = time
    return timeline
def dailytimeline(selected_user,df):
    if selected_user != 'overall':
        df = df[df['user'] == selected_user]


    df['date_only'] = df['date'].dt.date
    dailyline = df.groupby('date_only').count()['message'].reset_index()
    return dailyline
def weekuser(selected_user,df):
    if selected_user != 'overall':
        df = df[df['user'] == selected_user]
    df['dayname'] = df['date'].dt.day_name()
    return df['dayname'].value_counts()
def monthactive(selected_user,df):
    if selected_user != 'overall':
        df = df[df['user'] == selected_user]
    return df['month'].value_counts()
def activityheatmep(selected_user,df):
    if selected_user != 'overall':
        df = df[df['user'] == selected_user]
    period = []
    for hour in df[['dayname', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))
    df['period'] = period
    active_heatmap=df.pivot_table(index='dayname', columns='period', values='message', aggfunc='count').fillna(0)
    return active_heatmap