import streamlit as st
import preprocessor
import organiser
import matplotlib.pyplot as plt
import seaborn as sn
from organiser import most_common_words

st.sidebar.title('Chat- Analyzer')

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df =preprocessor.preprocessor(data)
    userdetails = df['user'].unique().tolist()
    userdetails.remove('group_notification')
    userdetails.sort()
    userdetails.insert(0,'overall')
    selected_user =st.sidebar.selectbox("show analysis with respect to ",userdetails)
    if st.sidebar.button("Show Analysis"):
       num,words, num_meadia_msg,urls,all_emojis= organiser.fetch_stats( selected_user,df)
       st.title("Top Statistics")
       col1, col2, col3, col4, col5 = st.columns(5)  # Changed st.beta_columns to st.columns
       with col1:
        st.header(" Total  Messages")
        st.title(num)
       with col2:
        st.header(" Total Words ")
        st.title(words)
       with col3:
        st.header(" Total Media Shared")
        st.title(num_meadia_msg)
        with col4:
            st.header(" Total Urls Shared")
            st.title(urls)
        with col5:
            st.header(" Total Number of Emojis")
            st.title(all_emojis)
    st.title("Monthly Usage Analysis")
    timeline = organiser.monthly_timeline(selected_user,df)
    fig,ax = plt.subplots()
    ax.plot(timeline['time'], timeline['message'],color='blue')
    plt.xticks(rotation='vertical')
    st.pyplot(fig)
    st.title("Daily Usage Analysis")
    dailyline = organiser.dailytimeline(selected_user, df)
    fig, ax = plt.subplots()
    ax.plot(dailyline['date_only'], dailyline['message'], color='orange')
    plt.xticks(rotation='vertical')
    st.pyplot(fig)
    st.title('Activity Mapping')
    col1,col2=st.columns(2)
    with col1:
        st.header("most busy day")
        busy=organiser.weekuser(selected_user, df)
        fig,ax=plt.subplots()
        ax.bar(busy.index, busy.values,color='orange')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)
    with col2:
        st.title("most busy month")
        busy = organiser.monthactive(selected_user, df)
        fig, ax = plt.subplots()
        ax.bar(busy.index, busy.values,color='blue')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)
    st.title("Weekly Activity Map")
    active = organiser.activityheatmep(selected_user, df)
    fig,ax = plt.subplots()
    ax=sn.heatmap(active)
    st.pyplot(fig)



    if selected_user == 'overall':
       st.title('Most busy users')
       x,ndf=organiser.fetch_busy_users(df)
       fig, ax = plt.subplots()
       col1, col2 = st.columns(2)
       with col1:
        ax.bar(x.index, x.values,color='red')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)
       with col2:
           st.dataframe(ndf)
    st.title("wordcloud")
    dfwc = organiser.created_wordcloud(selected_user,df)
    fig, ax = plt.subplots()
    ax.imshow(dfwc)
    plt.imshow(dfwc)
    st.pyplot(fig)
    most_common_df=organiser.most_common_words(selected_user, df)
    fig, ax = plt.subplots()
    x = most_common_df.iloc[:, 0].astype(str)
    y = most_common_df.iloc[:, 1]
    ax.bar(x, y,color='green')

    plt.xticks(rotation='vertical')

    st.title('Most commmon words')
    st.pyplot(fig)

    emoji_df = organiser.emoji_analyse(selected_user,df)
    st.title("Chat-Emojis Analysis")
    col1,col2 =st.columns(2)
    with col1:
        st.dataframe(emoji_df)
    with col2:
         fig,ax =plt.subplots()
         ax.pie(emoji_df[1].head(), labels=emoji_df[0].head(),autopct="%0.2f")

         st.pyplot(fig)