from config.dbconfig import url
import psycopg2
import time
class AvailabilityAnnouncementsDAO:
    def __init__(self):
        self.conn = psycopg2.connect(
                                        database=url.path[1:],
                                        user=url.username,
                                        password=url.password,
                                        host=url.hostname,
                                        port=url.port
                                        )
    def getAllAnnouncements(self):
        cursor = self.conn.cursor()
        query = """
        select ann_id, sid, ann_date, qty, priceattime, rid, rname, catid, catname
        from availabilityannouncement natural inner join availabilityannouncementdetail natural inner join resource natural inner join category natural inner join supplier natural inner join appuser
        order by ann_id, rname;
        """
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementById(self, ann_id):
        cursor = self.conn.cursor()
        query = "select * from availabilityannouncement where ann_id=%s;"
        cursor.execute(query, (ann_id,))
        result = cursor.fetchone()
        return result

    def getAnnouncementBySIDWithDetails(self, sid):
        cursor = self.conn.cursor()
        query = """
        select ann_id, ann_date, qty, priceattime, rid, rname, catid, catname
        from availabilityannouncement natural inner join availabilityannouncementdetail natural inner join resource natural inner join category natural inner join supplier natural inner join appuser
        where sid = %s
        order by rname ;
        """
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementByIdWithDetails(self, ann_id):
        cursor = self.conn.cursor()
        query = """
        select ann_id, ann_date, sid, uid, username, lname, fname, isAdmin,email, phone, add_id, qty, priceattime, rid, rname, catid, catname
        from availabilityannouncement natural inner join availabilityannouncementdetail natural inner join resource natural inner join category natural inner join supplier natural inner join appuser
        where ann_id = %s
        """
        cursor.execute(query, (ann_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getAnnouncementsByParameters(self, args):

        cursor = self.conn.cursor()

        query ="""
        select ann_id, sid, ann_date, qty, priceattime, rid, rname, catid, catname
        from availabilityannouncement natural inner join availabilityannouncementdetail natural inner join resource natural inner join category
        where ann_id in
        """
        subquery = """
        select ann_id
        from availabilityannouncement natural inner join availabilityannouncementdetail natural inner join resource natural inner join category
		where
        """
        subquery+= "=%s AND ".join(args.keys())
        subquery+= "=%s order by ann_id"
        # TOOK OUT ISADMIN HERE -Kelvin
        query+= "(" + subquery + ") ORDER BY ann_id, rname;"

        cursor.execute(query, tuple(args.values()))
        result=[]
        for row in cursor:
            result.append(row)
        return result

    def insertAvailabilityAnnouncement(self, sid):
        cursor = self.conn.cursor()
        date = time.strftime("%Y/%m/%d")
        query = "insert into AvailabilityAnnouncement(sid, ann_date) values (%s,%s) returning ann_id;"
        cursor.execute(query, (sid, date))
        ann_id = cursor.fetchone()[0]
        self.conn.commit()
        return ann_id
