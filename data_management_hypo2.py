import pandas as pd

df = pd.read_csv('output1.csv')

nickname_counts = df['author.nickname'].value_counts()


grouped_df = df.groupby('author.nickname').agg({
    'createTime': 'count',             # Count of videos
    'stats.diggCount': 'sum',          # Sum of diggCount
    'stats.commentCount': 'sum',       # Sum of commentCount
    'stats.playCount': 'sum',          # Sum of playCount
    'stats.shareCount': 'sum',         # Sum of shareCount
    'author_stat.followerCount': 'first'
    # Add more aggregation functions for other columns as needed
})

# Rename the columns for clarity
grouped_df.rename(columns={
    'createTime': 'video_count',
    'stats.diggCount': 'total_digg_count',
    'stats.commentCount': 'total_comment_count',
    'stats.playCount': 'total_play_count',
    'stats.shareCount': 'total_share_count',
    'author_stat.followerCount': 'follower_count'
}, inplace=True)

ranked_df = grouped_df.sort_values(by="total_play_count", ascending=False)
ranked_df.to_csv('most_viral.csv', index=True)

