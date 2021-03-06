import time

from config.dbconfig import url
import psycopg2
class ResourceRequestsDAO:
    def __init__(self):
        self.conn = psycopg2.connect(
                                        database=url.path[1:],
                                        user=url.username,
                                        password=url.password,
                                        host=url.hostname,
                                        port=url.port
                                        )
    def getAllRequests(self):
        cursor = self.conn.cursor()
        query = """
        select req_id, nid, req_date, qty, rid, rname, catid, catname
        from resourcerequest natural inner join requester natural inner join appuser natural inner join resourcerequestdetail natural inner join resource natural inner join category
        where f_date is null order by req_id, rname;
        """
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByIdWithDetails(self, req_id):
        cursor = self.conn.cursor()
        query = """select req_id, req_date, nid, uid, username, lname, fname, email, phone, add_id, qty, rid, rname, catid, catname
        from resourcerequest natural inner join requester natural inner join appuser natural inner join resourcerequestdetail natural inner join resource natural inner join category
        where req_id=%s
        order by rname;
        """
        cursor.execute(query,(req_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByIdWithDetailsNoReq(self, req_id):
        cursor = self.conn.cursor()
        query = """select req_id, req_date, qty, rid, rname, catid, catname
        from resourcerequest natural inner join requester natural inner join appuser natural inner join resourcerequestdetail natural inner join resource natural inner join category
        where req_id=%s
        order by rname;
        """
        cursor.execute(query,(req_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByIdWithDetails2(self, req_id):
        cursor = self.conn.cursor()
        query = """select req_id, req_date, qty, rid, rname, catid, catname
        from resourcerequest natural inner join requester natural inner join appuser natural inner join resourcerequestdetail natural inner join resource natural inner join category
        where req_id=%s
        order by rname;
        """
        cursor.execute(query, (req_id,))
        result = cursor.fetchone()
        return result

    #created by herbert to get all resources requeste dby users, sorted by nane
    def getRequestedResources(self):
        cursor = self.conn.cursor()
        query = """
                select req_id, rid, rname, catname, qty, nid, uid, username, lname, fname, add_id, req_date
                from resourcerequest natural inner join appuser natural inner join
                resourcerequestdetail natural inner join requester natural inner join
                category natural inner join resource
                order by rname;
                """
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestsByParameters(self, args):

        cursor = self.conn.cursor()

        query ="""
        select req_id, nid, req_date, qty, rid, rname, catid, catname
        from resourcerequest natural inner join requester natural inner join appuser natural inner join resourcerequestdetail natural inner join resource natural inner join category
        where req_id in
        """ # TOOK OUT ISADMIN HERE -Kelvin

        subquery = """
        select req_id
        from resourcerequest natural inner join requester natural inner join appuser natural inner join resourcerequestdetail natural inner join resource natural inner join category
		where
        """
        subquery+= "=%s AND ".join(args.keys())
        subquery+= "=%s order by req_id"

        query+= "(" + subquery + ") ORDER BY req_id, rname;"


        cursor.execute(query, tuple(args.values()))
        result=[]
        for row in cursor:
            result.append(row)
        return result

    def insertRequest(self, nid):
        cursor = self.conn.cursor()
        date = time.strftime("%Y/%m/%d")
        query = "insert into resourcerequest(nid, req_date) values(%s, %s) returning req_id;"
        cursor.execute(query, (nid, date,))
        req_id = cursor.fetchone()[0]
        self.conn.commit()
        return req_id

    def getRequestsByNid(self, nid):
        cursor = self.conn.cursor()
        query ="""
        select req_id, req_date, qty, rid, rname, catid, catname
        from resourcerequest natural inner join requester natural inner join appuser natural inner join resourcerequestdetail natural inner join resource natural inner join category
        where req_id in
        """ # TOOK OUT ISADMIN HERE -Kelvin

        subquery = """
        select req_id
        from resourcerequest natural inner join requester natural inner join appuser natural inner join resourcerequestdetail natural inner join resource natural inner join category
		where nid = %s ORDER BY req_id
        """

        query+= "(" + subquery + ") ORDER BY req_id, rname;"


        cursor.execute(query, (nid,))
        result=[]
        for row in cursor:
            result.append(row)
        return result
