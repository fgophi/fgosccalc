"""
    twitter 関連の共通するルーチンをまとめたモジュール
"""
from pathlib import Path
import re
from io import BytesIO
import logging

import tweepy
import cv2

from . import setting

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

def img2media_id(api, img):
    res = api.media_upload(filename='fgo_screenshot.jpg', file=BytesIO(img))
    logger.info('res.media_id: %s', res.media_id)
    return res.media_id


def file2media_id(api, file):
    quality = 85
    f = Path(file)
    img = cv2.imread(file)
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
    _, encimg = cv2.imencode(".jpg", img, encode_param)
    return img2media_id(api, encimg)


def set_twitter():
    ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET = setting.get_twitter_key()
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    return tweepy.API(auth)


def do_upload(befores, afters, owneds, func) -> str:
    api = set_twitter()
    media_ids = []

    text = '画像のテスト投稿'
    for before in befores:
        media_ids.append(func(api, before))
    for after in afters:
        media_ids.append(func(api, after))
    if len(befores) == 1:
        logger.debug('owneds: %s', owneds)
        if owneds is not None:
            if len(owneds) > 0:
                for owned in owneds:
                    media_ids.append(func(api, owned))

    logger.debug('media_ids: %s', media_ids)
    status_img = api.update_status(status=text, media_ids=media_ids)
    status_text = api.get_status(status_img.id, tweet_mode="extended")
    logger.debug('%s', status_text.full_text)
    pattern = "(?P<url>https://t.co/.+)$"
    m1 = re.search(pattern, status_text.full_text)
    if not m1:
        url = ""
    else:
        url = re.sub(pattern, r"\g<url>", m1.group())

    return url

def upload_file(args) -> str:
    return do_upload(args.before, args.after,
                     args.owned, file2media_id)


def upload_webfile(encoded_image_pairs, owneds) -> str:
    if len(encoded_image_pairs) == 2:
        befores = [encoded_image_pairs[0][0], encoded_image_pairs[1][0]]
        afters = [encoded_image_pairs[0][1], encoded_image_pairs[1][1]]
    else:
        befores = [encoded_image_pairs[0][0]]
        afters = [encoded_image_pairs[0][1]]
    return do_upload(befores, afters,
                     owneds, img2media_id)