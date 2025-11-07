import pandas as pd
import jieba
from snownlp import SnowNLP


def nlpdemo(df):
    with open('stopwords.txt', 'r', encoding='utf-8') as f:
        stopwords = [line.strip() for line in f]
    # 存储结果
    scores = []
    segmented_comments = []  # 分词结果

    for comment in df['评论内容']:
        comment = str(comment)

        words = jieba.cut(comment)

        filtered_words = [word for word in words if word not in stopwords or word in ["不", "没", "非常", "特别"]]

        filtered_text = ''.join(filtered_words)
        segmented_comments.append(' '.join(filtered_words))
        if not filtered_text.strip():
            scores.append(0.5)
        else:
            s = SnowNLP(filtered_text)
            scores.append(s.sentiments)

    df['scores'] = scores
    df['segmented'] = segmented_comments

    df.to_csv('nlp_result.csv', index=False)


if __name__ == "__main__":
    df = pd.read_csv('comment_data.csv')
    nlpdemo(df)
