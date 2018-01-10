from config.dbconfig import pg_config
import psycopg2
class ResourceRequestsDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect('postgres://ebwyoylyofgguf:bce5e728f4d5504e7a83ba37ece6f608483572bb56baa5700c90dab37d151295@ec2-54-83-59-144.compute-1.amazonaws.com:5432/de320ggpcvnl39')

    def getAllRequests(self):
        cursor = self.conn.cursor()
        query = """
        select req_id, req_date, qty, rid, rname, catid, catname
        from resourcerequest natural inner join requester natural inner join appuser natural inner join resourcerequestdetail natural inner join resource natural inner join category
        order by rname;
        """
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByIdWithDetails(self, req_id):
        cursor = self.conn.cursor()
        query = """select req_id, req_date, nid, uid, username, lname, fname, isAdmin, add_id, qty, rid, rname, catid, catname
        from resourcerequest natural inner join requester natural inner join appuser natural inner join resourcerequestdetail natural inner join resource natural inner join category
        where req_id=%s
        order by rname;
        """
        cursor.execute(query,(req_id,))
        result = []
        for row in cursor:
            result.append(row)
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
        select req_id, req_date, qty, rid, rname, catid, catname
        from resourcerequest natural inner join requester natural inner join appuser natural inner join resourcerequestdetail natural inner join resource natural inner join category
        where
        """ # TOOK OUT ISADMIN HERE -Kelvin
        query+= "=%s AND ".join(args.keys())
        query+= "=%s order by rname;"


        cursor.execute(query, tuple(args.values()))
        result=[]
        for row in cursor:
            result.append(row)
        return result
