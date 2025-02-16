from .base import *
from .utils import strtobool

DEBUG = strtobool(os.getenv("DEBUG", "n"))

INSTALLED_APPS += ["django_ses"]

# 許可するホスト名のリスト
ALLOWED_HOSTS = [s.strip() for s in os.getenv("ALLOWED_HOSTS", "").split(",")]

# 静的ファイルを配置する場所(本番環境ではWebサーバから配信)
STATIC_ROOT = "/usr/share/nginx/html/static"
MEDIA_ROOT = "/usr/share/nginx/html/media"

# Amazon SES関連設定
AWS_SES_ACCESS_KEY_ID = os.getenv("AWS_SES_ACCESS_KEY_ID")
AWS_SES_SECRET_ACCESS_KEY = os.getenv("AWS_SES_SECRET_ACCESS_KEY")
AWS_SES_REGION_NAME = "ap-northeast-1"
AWS_SES_REGION_ENDPOINT = f"email.{AWS_SES_REGION_NAME}.amazonaws.com"
EMAIL_BACKEND = "django_ses.SESBackend"

# AWS_SES_RETURN_PATH = os.getenv('AWS_SES_RETURN_PATH')

# 本番時のロギング設定
LOGGING = {
    "version": 1,  # 1固定
    "disable_existing_loggers": False,
    # ロガーの設定
    "loggers": {
        # Djangoが利用するロガー
        "django": {
            "handlers": ["file"],
            "level": "INFO",
        },
        # diaryアプリケーションが利用するロガー
        "diary": {
            "handlers": ["file"],
            "level": "INFO",
        },
    },
    # ハンドラの設定
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "logs/django.log"),
            "formatter": "prod",
            "when": "D",  # ログローテーション(新しいファイルへの切り替え)間隔の単位(D=日)
            "interval": 1,  # ログローテーション間隔(1日単位)
            "backupCount": 7,  # 保存しておくログファイル数
        },
    },
    # フォーマッタの設定
    "formatters": {
        "prod": {
            "format": "\t".join(
                [
                    "%(asctime)s",
                    "[%(levelname)s]",
                    "%(pathname)s(Line:%(lineno)d)",
                    "%(message)s",
                ]
            )
        },
    },
}
