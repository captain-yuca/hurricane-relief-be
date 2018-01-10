from config.dbconfig import pg_config
import psycopg2
class AvailabilityAnnouncementsDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllAnnouncements(self):
        cursor = self.conn.cursor()
        query = """
        select ann_id, ann_date, qty, rid, rname, catid, catname
        from availabilityannouncement natural inner join availabilityannouncementdetail natural inner join resource natural inner join category
        order by rname
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

    def getAnnouncementByIdWithDetails(self, ann_id):
        cursor = self.conn.cursor()
        query = """
        select ann_id, ann_date, sid, uid, username, lname, fname, isAdmin, add_id, qty, priceattime, rid, rname, catid, catname
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
        select ann_id, ann_date, qty, rid, rname, catid, catname
        from availabilityannouncement natural inner join availabilityannouncementdetail natural inner join resource natural inner join category
        where
        """ # TOOK OUT ISADMIN HERE -Kelvin
        query+= "=%s AND ".join(args.keys())
        query+= "=%s"

        cursor.execute(query, tuple(args.values()))
        result=[]
        for row in cursor:
            result.append(row)
        return result
