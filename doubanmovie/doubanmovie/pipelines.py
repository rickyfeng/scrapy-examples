# -*- coding: utf-8 -*-

from scrapy import log
from twisted.enterprise import adbapi
from settings import MYSQL_HOST,MYSQL_DB,MYSQL_USER,MYSQL_PASSWD,MYSQL_CHARSET

import MySQLdb
import MySQLdb.cursors

class DoubanmoviePipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool(
            'MySQLdb',
            host=MYSQL_HOST,
            db=MYSQL_DB,
            user=MYSQL_USER,
            passwd=MYSQL_PASSWD,
            cursorclass=MySQLdb.cursors.DictCursor,
            charset=MYSQL_CHARSET,
            use_unicode=False
        )

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)
        return item

    def _conditional_insert(self, tx, item):
        subject_id = item['subject_id'][0]
        title = item['title'][0]
        director = '/'.join(item['director'])
        scriptwriter = '/'.join(item['scriptwriter'])
        actor = '/'.join(item['actor'])
        category = '/'.join(item['category'])
        area = '/'.join(item['area'])
        language = '/'.join(item['language'])
        released_date= '/'.join(item['released_date'])
        length = '/'.join(item['length'])
        imdb = item['imdb'][0]
        score = item['score'][0]
        alias = item['alias'][0]
        introduce = item['introduce'][0].strip()
        top_order = item['top_order'][0][3:]

        tx.execute("select id from movie where subject_id = %s", (subject_id,))
        result = tx.fetchone()
        if result:
            tx.execute("UPDATE movie SET top_order = 0 WHERE top_order = %s" , (top_order))
            tx.execute("UPDATE movie SET top_order = %s, score= %s WHERE subject_id=%s" , (top_order, score, subject_id) )
        else:
            tx.execute(\
                "REPLACE INTO movie (subject_id, title, director, scriptwriter, actor, category, area, language, released_date, length, imdb, score, alias, introduce, top_order) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",\
                (subject_id, title, director, scriptwriter, actor, category,area,language,released_date,length,imdb,score,alias,introduce,top_order)
            )

        log.msg("Item stored in db: %s" % item, level=log.DEBUG)

    def handle_error(self, e):
        log.err(e)
