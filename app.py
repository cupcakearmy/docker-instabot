import os
import time

from src import InstaBot

bot = InstaBot(
    login="myusername",
    password="mypass",
    like_per_day=1000,
    comments_per_day=5,
    tag_list=['food', 'weed', 'smoke', 'smoking', 'party',
              'health', 'food', 'fit', 'wasted', 'fml', 'drugs', 'drug'],
    max_like_for_one_tag=50,
    follow_per_day=300,
    follow_time=24*60*60,
    unfollow_per_day=280,
    unfollow_break_min=15,
    unfollow_break_max=30,
    log_mod=0,
    comment_list=[["sweet", "nice"],
                  ["..", "...", "!!", "👌", "💪"]],
    unwanted_username_list=[
        'second', 'stuff', 'art', 'project', 'love', 'life', 'food', 'blog',
        'free', 'keren', 'photo', 'graphy', 'indo', 'travel', 'art', 'shop',
        'store', 'sex', 'toko', 'jual', 'online', 'murah', 'jam', 'kaos',
        'case', 'baju', 'fashion', 'corp', 'tas', 'butik', 'grosir', 'karpet',
        'sosis', 'salon', 'skin', 'care', 'cloth', 'tech', 'rental', 'kamera',
        'beauty', 'express', 'kredit', 'collection', 'impor', 'preloved',
        'follow', 'follower', 'gain', '.id', '_id', 'bags'
    ])

while True:
	bot.new_auto_mod()