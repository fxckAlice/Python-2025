from core.repository.news_repository import fetch_latest_news


def get_latest_news(limit=5):
    news = fetch_latest_news()
    news = sorted(news, key=lambda n: n["date"], reverse=True)
    return news[:limit]
