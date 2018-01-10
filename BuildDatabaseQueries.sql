--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.10
-- Dumped by pg_dump version 9.5.10

-- Started on 2018-01-07 17:04:50 AST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 187 (class 1259 OID 16547)
-- Name: address; Type: TABLE; Schema: public; Owner: appusr
--

CREATE TABLE address (
    add_id integer NOT NULL,
    address1 character varying(30) NOT NULL,
    address2 character varying(30),
    zipcode character varying(5) NOT NULL,
    region character varying(20) NOT NULL,
    country character varying(20) NOT NULL,
    city character varying(20) NOT NULL
);


ALTER TABLE address OWNER TO appusr;

--
-- TOC entry 186 (class 1259 OID 16545)
-- Name: address_add_id_seq; Type: SEQUENCE; Schema: public; Owner: appusr
--

CREATE SEQUENCE address_add_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE address_add_id_seq OWNER TO appusr;

--
-- TOC entry 2206 (class 0 OID 0)
-- Dependencies: 186
-- Name: address_add_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: appusr
--

ALTER SEQUENCE address_add_id_seq OWNED BY address.add_id;


--
-- TOC entry 2083 (class 2604 OID 16550)
-- Name: add_id; Type: DEFAULT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY address ALTER COLUMN add_id SET DEFAULT nextval('address_add_id_seq'::regclass);


--
-- TOC entry 2201 (class 0 OID 16547)
-- Dependencies: 187
-- Data for Name: address; Type: TABLE DATA; Schema: public; Owner: appusr
--

INSERT INTO address VALUES (1, 'calle 367, km 1.6', NULL, '00637', 'Mayaguez', 'Puerto Rico', 'Sabana Grande');
INSERT INTO address VALUES (4, 'some random house', NULL, '00000', 'Ponce', 'Puerto Rico', 'Barranquitas');
INSERT INTO address VALUES (6, 'another random house', NULL, '11111', 'San Juan', 'Puerto Rico', 'San Juan');
INSERT INTO address VALUES (7, 'colegio', NULL, '22222', 'Mayaguez', 'Puerto Rico', 'Mayaguez');
INSERT INTO address VALUES (9, 'UPI', NULL, '23324', 'San Juan', 'Puerto Rico', 'San Juan');


--
-- TOC entry 2207 (class 0 OID 0)
-- Dependencies: 186
-- Name: address_add_id_seq; Type: SEQUENCE SET; Schema: public; Owner: appusr
--

SELECT pg_catalog.setval('address_add_id_seq', 9, true);


--
-- TOC entry 2085 (class 2606 OID 16552)
-- Name: address_pkey; Type: CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY address
    ADD CONSTRAINT address_pkey PRIMARY KEY (add_id);


-- Completed on 2018-01-07 17:04:51 AST

--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.10
-- Dumped by pg_dump version 9.5.10

-- Started on 2018-01-07 17:11:25 AST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 189 (class 1259 OID 16555)
-- Name: appuser; Type: TABLE; Schema: public; Owner: appusr
--

CREATE TABLE appuser (
    uid integer NOT NULL,
    username character varying(20) NOT NULL,
    password character varying(20) NOT NULL,
    fname character varying(20) NOT NULL,
    lname character varying(20) NOT NULL,
    add_id integer NOT NULL,
    isadmin boolean DEFAULT false
);


ALTER TABLE appuser OWNER TO appusr;

--
-- TOC entry 188 (class 1259 OID 16553)
-- Name: users_uid_seq; Type: SEQUENCE; Schema: public; Owner: appusr
--

CREATE SEQUENCE users_uid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE users_uid_seq OWNER TO appusr;

--
-- TOC entry 2208 (class 0 OID 0)
-- Dependencies: 188
-- Name: users_uid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: appusr
--

ALTER SEQUENCE users_uid_seq OWNED BY appuser.uid;


--
-- TOC entry 2083 (class 2604 OID 16558)
-- Name: uid; Type: DEFAULT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY appuser ALTER COLUMN uid SET DEFAULT nextval('users_uid_seq'::regclass);


--
-- TOC entry 2203 (class 0 OID 16555)
-- Dependencies: 189
-- Data for Name: appuser; Type: TABLE DATA; Schema: public; Owner: appusr
--

INSERT INTO appuser VALUES (4, 'theherbertperez', 'somepassword', 'Herbert', 'Perez', 1, false);
INSERT INTO appuser VALUES (6, 'k3rmoon', 'anotherpassword', 'Kelvin', 'Roche', 4, false);
INSERT INTO appuser VALUES (7, 'captainyuca', 'thepassword', 'Manuel', 'Baez', 6, true);
INSERT INTO appuser VALUES (9, 'Batman', 'martha', 'Bruce', 'Wayne', 7, true);
INSERT INTO appuser VALUES (11, 'thetester', 'atest', 'a', 'b', 7, false);


--
-- TOC entry 2209 (class 0 OID 0)
-- Dependencies: 188
-- Name: users_uid_seq; Type: SEQUENCE SET; Schema: public; Owner: appusr
--

SELECT pg_catalog.setval('users_uid_seq', 11, true);


--
-- TOC entry 2086 (class 2606 OID 16561)
-- Name: users_pkey; Type: CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY appuser
    ADD CONSTRAINT users_pkey PRIMARY KEY (uid);


--
-- TOC entry 2087 (class 2606 OID 16562)
-- Name: users_add_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY appuser
    ADD CONSTRAINT users_add_id_fkey FOREIGN KEY (add_id) REFERENCES address(add_id);


-- Completed on 2018-01-07 17:11:25 AST

--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.10
-- Dumped by pg_dump version 9.5.10

-- Started on 2018-01-07 17:10:58 AST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 195 (class 1259 OID 16730)
-- Name: supplier; Type: TABLE; Schema: public; Owner: appusr
--

CREATE TABLE supplier (
    sid integer NOT NULL,
    uid integer
);


ALTER TABLE supplier OWNER TO appusr;

--
-- TOC entry 194 (class 1259 OID 16728)
-- Name: suppliers_sid_seq; Type: SEQUENCE; Schema: public; Owner: appusr
--

CREATE SEQUENCE suppliers_sid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE suppliers_sid_seq OWNER TO appusr;

--
-- TOC entry 2207 (class 0 OID 0)
-- Dependencies: 194
-- Name: suppliers_sid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: appusr
--

ALTER SEQUENCE suppliers_sid_seq OWNED BY supplier.sid;


--
-- TOC entry 2083 (class 2604 OID 16733)
-- Name: sid; Type: DEFAULT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY supplier ALTER COLUMN sid SET DEFAULT nextval('suppliers_sid_seq'::regclass);


--
-- TOC entry 2202 (class 0 OID 16730)
-- Dependencies: 195
-- Data for Name: supplier; Type: TABLE DATA; Schema: public; Owner: appusr
--

INSERT INTO supplier VALUES (1, 4);
INSERT INTO supplier VALUES (2, 7);
INSERT INTO supplier VALUES (3, 9);
INSERT INTO supplier VALUES (4, 11);


--
-- TOC entry 2208 (class 0 OID 0)
-- Dependencies: 194
-- Name: suppliers_sid_seq; Type: SEQUENCE SET; Schema: public; Owner: appusr
--

SELECT pg_catalog.setval('suppliers_sid_seq', 6, true);


--
-- TOC entry 2085 (class 2606 OID 16735)
-- Name: suppliers_pkey; Type: CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY supplier
    ADD CONSTRAINT suppliers_pkey PRIMARY KEY (sid);


--
-- TOC entry 2086 (class 2606 OID 16736)
-- Name: suppliers_uid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY supplier
    ADD CONSTRAINT suppliers_uid_fkey FOREIGN KEY (uid) REFERENCES appuser(uid);


-- Completed on 2018-01-07 17:10:58 AST

--
-- PostgreSQL database dump complete
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.10
-- Dumped by pg_dump version 9.5.10

-- Started on 2018-01-07 17:07:58 AST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 193 (class 1259 OID 16717)
-- Name: requester; Type: TABLE; Schema: public; Owner: appusr
--

CREATE TABLE requester (
    nid integer NOT NULL,
    uid integer
);


ALTER TABLE requester OWNER TO appusr;

--
-- TOC entry 192 (class 1259 OID 16715)
-- Name: requesters_nid_seq; Type: SEQUENCE; Schema: public; Owner: appusr
--

CREATE SEQUENCE requesters_nid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE requesters_nid_seq OWNER TO appusr;

--
-- TOC entry 2207 (class 0 OID 0)
-- Dependencies: 192
-- Name: requesters_nid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: appusr
--

ALTER SEQUENCE requesters_nid_seq OWNED BY requester.nid;


--
-- TOC entry 2083 (class 2604 OID 16720)
-- Name: nid; Type: DEFAULT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY requester ALTER COLUMN nid SET DEFAULT nextval('requesters_nid_seq'::regclass);


--
-- TOC entry 2202 (class 0 OID 16717)
-- Dependencies: 193
-- Data for Name: requester; Type: TABLE DATA; Schema: public; Owner: appusr
--

INSERT INTO requester VALUES (1, 4);
INSERT INTO requester VALUES (2, 6);
INSERT INTO requester VALUES (3, 7);


--
-- TOC entry 2208 (class 0 OID 0)
-- Dependencies: 192
-- Name: requesters_nid_seq; Type: SEQUENCE SET; Schema: public; Owner: appusr
--

SELECT pg_catalog.setval('requesters_nid_seq', 6, true);


--
-- TOC entry 2085 (class 2606 OID 16722)
-- Name: requesters_pkey; Type: CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY requester
    ADD CONSTRAINT requesters_pkey PRIMARY KEY (nid);


--
-- TOC entry 2086 (class 2606 OID 16723)
-- Name: requesters_uid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY requester
    ADD CONSTRAINT requesters_uid_fkey FOREIGN KEY (uid) REFERENCES appuser(uid);


-- Completed on 2018-01-07 17:07:58 AST

--
-- PostgreSQL database dump complete
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.10
-- Dumped by pg_dump version 9.5.10

-- Started on 2018-01-07 17:06:04 AST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 199 (class 1259 OID 16775)
-- Name: availabilityannouncement; Type: TABLE; Schema: public; Owner: appusr
--

CREATE TABLE availabilityannouncement (
    ann_id integer NOT NULL,
    sid integer,
    ann_date date NOT NULL
);


ALTER TABLE availabilityannouncement OWNER TO appusr;

--
-- TOC entry 198 (class 1259 OID 16773)
-- Name: availabilityannouncement_ann_id_seq; Type: SEQUENCE; Schema: public; Owner: appusr
--

CREATE SEQUENCE availabilityannouncement_ann_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE availabilityannouncement_ann_id_seq OWNER TO appusr;

--
-- TOC entry 2207 (class 0 OID 0)
-- Dependencies: 198
-- Name: availabilityannouncement_ann_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: appusr
--

ALTER SEQUENCE availabilityannouncement_ann_id_seq OWNED BY availabilityannouncement.ann_id;


--
-- TOC entry 2083 (class 2604 OID 16778)
-- Name: ann_id; Type: DEFAULT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY availabilityannouncement ALTER COLUMN ann_id SET DEFAULT nextval('availabilityannouncement_ann_id_seq'::regclass);


--
-- TOC entry 2202 (class 0 OID 16775)
-- Dependencies: 199
-- Data for Name: availabilityannouncement; Type: TABLE DATA; Schema: public; Owner: appusr
--

INSERT INTO availabilityannouncement VALUES (1, 1, '2017-12-12');
INSERT INTO availabilityannouncement VALUES (2, 1, '2017-11-11');
INSERT INTO availabilityannouncement VALUES (3, 2, '2017-12-12');


--
-- TOC entry 2208 (class 0 OID 0)
-- Dependencies: 198
-- Name: availabilityannouncement_ann_id_seq; Type: SEQUENCE SET; Schema: public; Owner: appusr
--

SELECT pg_catalog.setval('availabilityannouncement_ann_id_seq', 3, true);


--
-- TOC entry 2085 (class 2606 OID 16780)
-- Name: availabilityannouncement_pkey; Type: CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY availabilityannouncement
    ADD CONSTRAINT availabilityannouncement_pkey PRIMARY KEY (ann_id);


--
-- TOC entry 2086 (class 2606 OID 16781)
-- Name: availabilityannouncement_sid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY availabilityannouncement
    ADD CONSTRAINT availabilityannouncement_sid_fkey FOREIGN KEY (sid) REFERENCES supplier(sid);


-- Completed on 2018-01-07 17:06:04 AST

--
-- PostgreSQL database dump complete
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.10
-- Dumped by pg_dump version 9.5.10

-- Started on 2018-01-07 17:08:29 AST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 197 (class 1259 OID 16760)
-- Name: resourcerequest; Type: TABLE; Schema: public; Owner: appusr
--

CREATE TABLE resourcerequest (
    req_id integer NOT NULL,
    nid integer,
    req_date date NOT NULL
);


ALTER TABLE resourcerequest OWNER TO appusr;

--
-- TOC entry 196 (class 1259 OID 16758)
-- Name: resourcerequest_req_id_seq; Type: SEQUENCE; Schema: public; Owner: appusr
--

CREATE SEQUENCE resourcerequest_req_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE resourcerequest_req_id_seq OWNER TO appusr;

--
-- TOC entry 2207 (class 0 OID 0)
-- Dependencies: 196
-- Name: resourcerequest_req_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: appusr
--

ALTER SEQUENCE resourcerequest_req_id_seq OWNED BY resourcerequest.req_id;


--
-- TOC entry 2083 (class 2604 OID 16763)
-- Name: req_id; Type: DEFAULT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY resourcerequest ALTER COLUMN req_id SET DEFAULT nextval('resourcerequest_req_id_seq'::regclass);


--
-- TOC entry 2202 (class 0 OID 16760)
-- Dependencies: 197
-- Data for Name: resourcerequest; Type: TABLE DATA; Schema: public; Owner: appusr
--

INSERT INTO resourcerequest VALUES (3, 2, '2018-03-01');
INSERT INTO resourcerequest VALUES (5, 2, '2018-02-01');
INSERT INTO resourcerequest VALUES (7, 3, '2017-12-31');


--
-- TOC entry 2208 (class 0 OID 0)
-- Dependencies: 196
-- Name: resourcerequest_req_id_seq; Type: SEQUENCE SET; Schema: public; Owner: appusr
--

SELECT pg_catalog.setval('resourcerequest_req_id_seq', 7, true);


--
-- TOC entry 2085 (class 2606 OID 16765)
-- Name: resourcerequest_pkey; Type: CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY resourcerequest
    ADD CONSTRAINT resourcerequest_pkey PRIMARY KEY (req_id);


--
-- TOC entry 2086 (class 2606 OID 16766)
-- Name: resourcerequest_nid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY resourcerequest
    ADD CONSTRAINT resourcerequest_nid_fkey FOREIGN KEY (nid) REFERENCES requester(nid);


-- Completed on 2018-01-07 17:08:29 AST

--
-- PostgreSQL database dump complete
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.10
-- Dumped by pg_dump version 9.5.10

-- Started on 2018-01-07 17:06:51 AST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 182 (class 1259 OID 16428)
-- Name: category; Type: TABLE; Schema: public; Owner: appusr
--

CREATE TABLE category (
    catid integer NOT NULL,
    catname character varying(20) NOT NULL
);


ALTER TABLE category OWNER TO appusr;

--
-- TOC entry 181 (class 1259 OID 16426)
-- Name: category_catid_seq; Type: SEQUENCE; Schema: public; Owner: appusr
--

CREATE SEQUENCE category_catid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE category_catid_seq OWNER TO appusr;

--
-- TOC entry 2206 (class 0 OID 0)
-- Dependencies: 181
-- Name: category_catid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: appusr
--

ALTER SEQUENCE category_catid_seq OWNED BY category.catid;


--
-- TOC entry 2083 (class 2604 OID 16431)
-- Name: catid; Type: DEFAULT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY category ALTER COLUMN catid SET DEFAULT nextval('category_catid_seq'::regclass);


--
-- TOC entry 2201 (class 0 OID 16428)
-- Dependencies: 182
-- Data for Name: category; Type: TABLE DATA; Schema: public; Owner: appusr
--

INSERT INTO category VALUES (1, 'water');
INSERT INTO category VALUES (2, 'small bottles');
INSERT INTO category VALUES (3, '1 gallon bottles');
INSERT INTO category VALUES (4, 'medications');
INSERT INTO category VALUES (5, 'baby food');
INSERT INTO category VALUES (6, 'canned food');
INSERT INTO category VALUES (7, 'dry food');
INSERT INTO category VALUES (8, 'ice');
INSERT INTO category VALUES (9, 'fuel');
INSERT INTO category VALUES (10, 'diesel');
INSERT INTO category VALUES (11, 'propane');
INSERT INTO category VALUES (12, 'gasoline');
INSERT INTO category VALUES (13, 'medical devices');
INSERT INTO category VALUES (14, 'heavy equipment');
INSERT INTO category VALUES (15, 'tools');
INSERT INTO category VALUES (16, 'clothing');
INSERT INTO category VALUES (17, 'power generators');
INSERT INTO category VALUES (18, 'batteries');


--
-- TOC entry 2207 (class 0 OID 0)
-- Dependencies: 181
-- Name: category_catid_seq; Type: SEQUENCE SET; Schema: public; Owner: appusr
--

SELECT pg_catalog.setval('category_catid_seq', 18, true);


--
-- TOC entry 2085 (class 2606 OID 16433)
-- Name: category_pkey; Type: CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY category
    ADD CONSTRAINT category_pkey PRIMARY KEY (catid);


-- Completed on 2018-01-07 17:06:51 AST

--
-- PostgreSQL database dump complete
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.10
-- Dumped by pg_dump version 9.5.10

-- Started on 2018-01-07 17:10:37 AST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 183 (class 1259 OID 16449)
-- Name: subcategory; Type: TABLE; Schema: public; Owner: appusr
--

CREATE TABLE subcategory (
    parent_id integer NOT NULL,
    subcat_id integer NOT NULL
);


ALTER TABLE subcategory OWNER TO appusr;

--
-- TOC entry 2201 (class 0 OID 16449)
-- Dependencies: 183
-- Data for Name: subcategory; Type: TABLE DATA; Schema: public; Owner: appusr
--

INSERT INTO subcategory VALUES (1, 2);
INSERT INTO subcategory VALUES (1, 3);
INSERT INTO subcategory VALUES (9, 10);
INSERT INTO subcategory VALUES (9, 11);
INSERT INTO subcategory VALUES (9, 12);


--
-- TOC entry 2084 (class 2606 OID 16453)
-- Name: subcategories_pkey; Type: CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY subcategory
    ADD CONSTRAINT subcategories_pkey PRIMARY KEY (parent_id, subcat_id);


--
-- TOC entry 2085 (class 2606 OID 16454)
-- Name: subcategories_parent_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY subcategory
    ADD CONSTRAINT subcategories_parent_id_fkey FOREIGN KEY (parent_id) REFERENCES category(catid);


--
-- TOC entry 2086 (class 2606 OID 16459)
-- Name: subcategories_subcat_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY subcategory
    ADD CONSTRAINT subcategories_subcat_id_fkey FOREIGN KEY (subcat_id) REFERENCES category(catid);


-- Completed on 2018-01-07 17:10:37 AST

--
-- PostgreSQL database dump complete
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.10
-- Dumped by pg_dump version 9.5.10

-- Started on 2018-01-07 17:09:00 AST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 185 (class 1259 OID 16466)
-- Name: resource; Type: TABLE; Schema: public; Owner: appusr
--

CREATE TABLE resource (
    rid integer NOT NULL,
    rname character varying(20) NOT NULL,
    catid integer NOT NULL
);


ALTER TABLE resource OWNER TO appusr;

--
-- TOC entry 184 (class 1259 OID 16464)
-- Name: resources_rid_seq; Type: SEQUENCE; Schema: public; Owner: appusr
--

CREATE SEQUENCE resources_rid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE resources_rid_seq OWNER TO appusr;

--
-- TOC entry 2207 (class 0 OID 0)
-- Dependencies: 184
-- Name: resources_rid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: appusr
--

ALTER SEQUENCE resources_rid_seq OWNED BY resource.rid;


--
-- TOC entry 2083 (class 2604 OID 16469)
-- Name: rid; Type: DEFAULT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY resource ALTER COLUMN rid SET DEFAULT nextval('resources_rid_seq'::regclass);


--
-- TOC entry 2202 (class 0 OID 16466)
-- Dependencies: 185
-- Data for Name: resource; Type: TABLE DATA; Schema: public; Owner: appusr
--

INSERT INTO resource VALUES (3, 'panadol', 4);
INSERT INTO resource VALUES (4, 'advil', 4);
INSERT INTO resource VALUES (5, 'gerber mixed vegetab', 5);
INSERT INTO resource VALUES (6, 'oatmeal', 7);
INSERT INTO resource VALUES (7, 'freeze-dried ice cre', 7);
INSERT INTO resource VALUES (9, 'libby''s mixed vegeta', 6);
INSERT INTO resource VALUES (10, 'green giant cut gree', 6);
INSERT INTO resource VALUES (11, 'del monte sliced bee', 6);
INSERT INTO resource VALUES (12, 'ReadyIce 10lb bag', 8);
INSERT INTO resource VALUES (13, 'puma diesel', 10);
INSERT INTO resource VALUES (14, 'shell diesel', 10);
INSERT INTO resource VALUES (15, 'puma gasoline', 12);
INSERT INTO resource VALUES (16, 'shell gasoline', 12);
INSERT INTO resource VALUES (17, 'blue rhino propane c', 11);
INSERT INTO resource VALUES (18, 'duracel AA', 18);
INSERT INTO resource VALUES (19, 'energizer AA', 18);
INSERT INTO resource VALUES (20, 'duracel AAA', 18);
INSERT INTO resource VALUES (21, 'energizer AAA', 18);
INSERT INTO resource VALUES (22, 'pacemaker', 13);
INSERT INTO resource VALUES (23, 'hearing aids', 13);
INSERT INTO resource VALUES (24, 'tshirt', 16);
INSERT INTO resource VALUES (25, 'size 10 shoes', 16);
INSERT INTO resource VALUES (27, '7500W Generator', 17);
INSERT INTO resource VALUES (28, '2000W Generator', 17);
INSERT INTO resource VALUES (29, 'Craftsman Hammer', 15);
INSERT INTO resource VALUES (30, 'Craftsman Drill', 15);
INSERT INTO resource VALUES (31, 'DeWalt 25ft Tape Mea', 15);
INSERT INTO resource VALUES (32, 'Excavator', 14);
INSERT INTO resource VALUES (33, 'Bulldozer', 14);
INSERT INTO resource VALUES (34, 'Dump Truck', 14);
INSERT INTO resource VALUES (35, 'Tractor', 14);
INSERT INTO resource VALUES (36, 'nikini 24 bottle pkg', 2);
INSERT INTO resource VALUES (1, 'dasani 30 bottle pkg', 2);
INSERT INTO resource VALUES (2, 'ricura 4 bottle pkg', 3);


--
-- TOC entry 2208 (class 0 OID 0)
-- Dependencies: 184
-- Name: resources_rid_seq; Type: SEQUENCE SET; Schema: public; Owner: appusr
--

SELECT pg_catalog.setval('resources_rid_seq', 36, true);


--
-- TOC entry 2085 (class 2606 OID 16471)
-- Name: resources_pkey; Type: CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY resource
    ADD CONSTRAINT resources_pkey PRIMARY KEY (rid);


--
-- TOC entry 2086 (class 2606 OID 16472)
-- Name: resources_catid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY resource
    ADD CONSTRAINT resources_catid_fkey FOREIGN KEY (catid) REFERENCES category(catid);


-- Completed on 2018-01-07 17:09:00 AST

--
-- PostgreSQL database dump complete
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.10
-- Dumped by pg_dump version 9.5.10

-- Started on 2018-01-07 17:14:44 AST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 205 (class 1259 OID 16913)
-- Name: resourcerequestdetail; Type: TABLE; Schema: public; Owner: appusr
--

CREATE TABLE resourcerequestdetail (
    qty integer NOT NULL,
    req_id integer NOT NULL,
    rid integer NOT NULL
);


ALTER TABLE resourcerequestdetail OWNER TO appusr;

--
-- TOC entry 2201 (class 0 OID 16913)
-- Dependencies: 205
-- Data for Name: resourcerequestdetail; Type: TABLE DATA; Schema: public; Owner: appusr
--

INSERT INTO resourcerequestdetail VALUES (50, 3, 24);
INSERT INTO resourcerequestdetail VALUES (100, 3, 20);
INSERT INTO resourcerequestdetail VALUES (30, 3, 13);
INSERT INTO resourcerequestdetail VALUES (1, 5, 4);
INSERT INTO resourcerequestdetail VALUES (2, 7, 12);


--
-- TOC entry 2084 (class 2606 OID 16917)
-- Name: resourcerequestdetail_pkey; Type: CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY resourcerequestdetail
    ADD CONSTRAINT resourcerequestdetail_pkey PRIMARY KEY (req_id, rid);


--
-- TOC entry 2085 (class 2606 OID 16918)
-- Name: resourcerequestdetail_req_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY resourcerequestdetail
    ADD CONSTRAINT resourcerequestdetail_req_id_fkey FOREIGN KEY (req_id) REFERENCES resourcerequest(req_id);


--
-- TOC entry 2086 (class 2606 OID 16923)
-- Name: resourcerequestdetail_rid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY resourcerequestdetail
    ADD CONSTRAINT resourcerequestdetail_rid_fkey FOREIGN KEY (rid) REFERENCES resource(rid);


-- Completed on 2018-01-07 17:14:44 AST

--
-- PostgreSQL database dump complete
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.10
-- Dumped by pg_dump version 9.5.10

-- Started on 2018-01-07 17:06:31 AST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 204 (class 1259 OID 16898)
-- Name: availabilityannouncementdetail; Type: TABLE; Schema: public; Owner: appusr
--

CREATE TABLE availabilityannouncementdetail (
    qty integer NOT NULL,
    priceattime double precision NOT NULL,
    ann_id integer NOT NULL,
    rid integer NOT NULL
);


ALTER TABLE availabilityannouncementdetail OWNER TO appusr;

--
-- TOC entry 2201 (class 0 OID 16898)
-- Dependencies: 204
-- Data for Name: availabilityannouncementdetail; Type: TABLE DATA; Schema: public; Owner: appusr
--

INSERT INTO availabilityannouncementdetail VALUES (25, 2, 1, 3);
INSERT INTO availabilityannouncementdetail VALUES (10, 5, 1, 18);
INSERT INTO availabilityannouncementdetail VALUES (10, 5, 1, 20);
INSERT INTO availabilityannouncementdetail VALUES (4, 10, 2, 24);
INSERT INTO availabilityannouncementdetail VALUES (1, 1500, 3, 27);
INSERT INTO availabilityannouncementdetail VALUES (1, 700, 3, 28);


--
-- TOC entry 2084 (class 2606 OID 16902)
-- Name: availabilityannouncementdetails_pkey; Type: CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY availabilityannouncementdetail
    ADD CONSTRAINT availabilityannouncementdetails_pkey PRIMARY KEY (ann_id, rid);


--
-- TOC entry 2085 (class 2606 OID 16903)
-- Name: availabilityannouncementdetails_ann_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY availabilityannouncementdetail
    ADD CONSTRAINT availabilityannouncementdetails_ann_id_fkey FOREIGN KEY (ann_id) REFERENCES availabilityannouncement(ann_id);


--
-- TOC entry 2086 (class 2606 OID 16908)
-- Name: availabilityannouncementdetails_rid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY availabilityannouncementdetail
    ADD CONSTRAINT availabilityannouncementdetails_rid_fkey FOREIGN KEY (rid) REFERENCES resource(rid);


-- Completed on 2018-01-07 17:06:31 AST

--
-- PostgreSQL database dump complete
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.10
-- Dumped by pg_dump version 9.5.10

-- Started on 2018-01-07 17:09:57 AST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 206 (class 1259 OID 16962)
-- Name: stock; Type: TABLE; Schema: public; Owner: appusr
--

CREATE TABLE stock (
    currentpriceperitem double precision NOT NULL,
    rid integer NOT NULL,
    sid integer NOT NULL,
    qtysum integer NOT NULL
);


ALTER TABLE stock OWNER TO appusr;

--
-- TOC entry 2201 (class 0 OID 16962)
-- Dependencies: 206
-- Data for Name: stock; Type: TABLE DATA; Schema: public; Owner: appusr
--

INSERT INTO stock VALUES (10, 24, 1, 4);
INSERT INTO stock VALUES (1500, 27, 2, 1);
INSERT INTO stock VALUES (5, 18, 1, 5);
INSERT INTO stock VALUES (5, 20, 1, 5);
INSERT INTO stock VALUES (700, 28, 2, 0);
INSERT INTO stock VALUES (2, 3, 1, 3);


--
-- TOC entry 2084 (class 2606 OID 16966)
-- Name: stock_pkey; Type: CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY stock
    ADD CONSTRAINT stock_pkey PRIMARY KEY (rid, sid);


--
-- TOC entry 2085 (class 2606 OID 16967)
-- Name: stock_rid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY stock
    ADD CONSTRAINT stock_rid_fkey FOREIGN KEY (rid) REFERENCES resource(rid);


--
-- TOC entry 2086 (class 2606 OID 16972)
-- Name: stock_sid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY stock
    ADD CONSTRAINT stock_sid_fkey FOREIGN KEY (sid) REFERENCES supplier(sid);


-- Completed on 2018-01-07 17:09:57 AST

--
-- PostgreSQL database dump complete
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.10
-- Dumped by pg_dump version 9.5.10

-- Started on 2018-01-07 17:07:14 AST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 191 (class 1259 OID 16569)
-- Name: paymentinfo; Type: TABLE; Schema: public; Owner: appusr
--

CREATE TABLE paymentinfo (
    pi_id integer NOT NULL,
    ccnum character varying(16) NOT NULL,
    expirationdate date NOT NULL,
    uid integer,
    add_id integer
);


ALTER TABLE paymentinfo OWNER TO appusr;

--
-- TOC entry 190 (class 1259 OID 16567)
-- Name: paymentinfo_pi_id_seq; Type: SEQUENCE; Schema: public; Owner: appusr
--

CREATE SEQUENCE paymentinfo_pi_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE paymentinfo_pi_id_seq OWNER TO appusr;

--
-- TOC entry 2208 (class 0 OID 0)
-- Dependencies: 190
-- Name: paymentinfo_pi_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: appusr
--

ALTER SEQUENCE paymentinfo_pi_id_seq OWNED BY paymentinfo.pi_id;


--
-- TOC entry 2083 (class 2604 OID 16572)
-- Name: pi_id; Type: DEFAULT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY paymentinfo ALTER COLUMN pi_id SET DEFAULT nextval('paymentinfo_pi_id_seq'::regclass);


--
-- TOC entry 2203 (class 0 OID 16569)
-- Dependencies: 191
-- Data for Name: paymentinfo; Type: TABLE DATA; Schema: public; Owner: appusr
--

INSERT INTO paymentinfo VALUES (3, '3456123412345678', '2028-02-02', 4, 1);
INSERT INTO paymentinfo VALUES (4, '0987654321098765', '2039-02-26', 7, 6);
INSERT INTO paymentinfo VALUES (9, '1234123412341234', '2025-05-05', 9, 1);
INSERT INTO paymentinfo VALUES (5, '0428079824709817', '2020-08-08', 6, 4);


--
-- TOC entry 2209 (class 0 OID 0)
-- Dependencies: 190
-- Name: paymentinfo_pi_id_seq; Type: SEQUENCE SET; Schema: public; Owner: appusr
--

SELECT pg_catalog.setval('paymentinfo_pi_id_seq', 5, true);


--
-- TOC entry 2085 (class 2606 OID 16574)
-- Name: paymentinfo_pkey; Type: CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY paymentinfo
    ADD CONSTRAINT paymentinfo_pkey PRIMARY KEY (pi_id);


--
-- TOC entry 2087 (class 2606 OID 16580)
-- Name: paymentinfo_billing_add_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY paymentinfo
    ADD CONSTRAINT paymentinfo_billing_add_id_fkey FOREIGN KEY (add_id) REFERENCES address(add_id);


--
-- TOC entry 2086 (class 2606 OID 16575)
-- Name: paymentinfo_uid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY paymentinfo
    ADD CONSTRAINT paymentinfo_uid_fkey FOREIGN KEY (uid) REFERENCES appuser(uid);


-- Completed on 2018-01-07 17:07:14 AST

--
-- PostgreSQL database dump complete
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.10
-- Dumped by pg_dump version 9.5.10

-- Started on 2018-01-07 17:07:32 AST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 201 (class 1259 OID 16837)
-- Name: purchase; Type: TABLE; Schema: public; Owner: appusr
--

CREATE TABLE purchase (
    purchase_id integer NOT NULL,
    purchase_date date NOT NULL,
    purchase_total double precision NOT NULL,
    uid integer NOT NULL,
    buyer_pi_id integer
);


ALTER TABLE purchase OWNER TO appusr;

--
-- TOC entry 200 (class 1259 OID 16835)
-- Name: purchase_purchase_id_seq; Type: SEQUENCE; Schema: public; Owner: appusr
--

CREATE SEQUENCE purchase_purchase_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE purchase_purchase_id_seq OWNER TO appusr;

--
-- TOC entry 2208 (class 0 OID 0)
-- Dependencies: 200
-- Name: purchase_purchase_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: appusr
--

ALTER SEQUENCE purchase_purchase_id_seq OWNED BY purchase.purchase_id;


--
-- TOC entry 2083 (class 2604 OID 16840)
-- Name: purchase_id; Type: DEFAULT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY purchase ALTER COLUMN purchase_id SET DEFAULT nextval('purchase_purchase_id_seq'::regclass);


--
-- TOC entry 2203 (class 0 OID 16837)
-- Dependencies: 201
-- Data for Name: purchase; Type: TABLE DATA; Schema: public; Owner: appusr
--

INSERT INTO purchase VALUES (1, '2018-01-01', 790, 6, 4);
INSERT INTO purchase VALUES (3, '2018-01-02', 4, 9, 9);


--
-- TOC entry 2209 (class 0 OID 0)
-- Dependencies: 200
-- Name: purchase_purchase_id_seq; Type: SEQUENCE SET; Schema: public; Owner: appusr
--

SELECT pg_catalog.setval('purchase_purchase_id_seq', 3, true);


--
-- TOC entry 2085 (class 2606 OID 16842)
-- Name: purchase_pkey; Type: CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY purchase
    ADD CONSTRAINT purchase_pkey PRIMARY KEY (purchase_id);


--
-- TOC entry 2087 (class 2606 OID 16848)
-- Name: purchase_buyer_pi_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY purchase
    ADD CONSTRAINT purchase_buyer_pi_id_fkey FOREIGN KEY (buyer_pi_id) REFERENCES paymentinfo(pi_id);


--
-- TOC entry 2086 (class 2606 OID 16843)
-- Name: purchase_uid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY purchase
    ADD CONSTRAINT purchase_uid_fkey FOREIGN KEY (uid) REFERENCES appuser(uid);


-- Completed on 2018-01-07 17:07:32 AST

--
-- PostgreSQL database dump complete
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.10
-- Dumped by pg_dump version 9.5.10

-- Started on 2018-01-07 17:09:16 AST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 203 (class 1259 OID 16863)
-- Name: resourcetransaction; Type: TABLE; Schema: public; Owner: appusr
--

CREATE TABLE resourcetransaction (
    tid integer NOT NULL,
    sid integer NOT NULL,
    transactionammount double precision NOT NULL,
    purchase_id integer NOT NULL,
    supplier_pi_id integer
);


ALTER TABLE resourcetransaction OWNER TO appusr;

--
-- TOC entry 202 (class 1259 OID 16861)
-- Name: resourcetransaction_tid_seq; Type: SEQUENCE; Schema: public; Owner: appusr
--

CREATE SEQUENCE resourcetransaction_tid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE resourcetransaction_tid_seq OWNER TO appusr;

--
-- TOC entry 2209 (class 0 OID 0)
-- Dependencies: 202
-- Name: resourcetransaction_tid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: appusr
--

ALTER SEQUENCE resourcetransaction_tid_seq OWNED BY resourcetransaction.tid;


--
-- TOC entry 2083 (class 2604 OID 16866)
-- Name: tid; Type: DEFAULT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY resourcetransaction ALTER COLUMN tid SET DEFAULT nextval('resourcetransaction_tid_seq'::regclass);


--
-- TOC entry 2204 (class 0 OID 16863)
-- Dependencies: 203
-- Data for Name: resourcetransaction; Type: TABLE DATA; Schema: public; Owner: appusr
--

INSERT INTO resourcetransaction VALUES (2, 1, 90, 1, 3);
INSERT INTO resourcetransaction VALUES (9, 2, 700, 1, 4);
INSERT INTO resourcetransaction VALUES (10, 1, 4, 3, 3);


--
-- TOC entry 2210 (class 0 OID 0)
-- Dependencies: 202
-- Name: resourcetransaction_tid_seq; Type: SEQUENCE SET; Schema: public; Owner: appusr
--

SELECT pg_catalog.setval('resourcetransaction_tid_seq', 10, true);


--
-- TOC entry 2085 (class 2606 OID 16868)
-- Name: resourcetransaction_pkey; Type: CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY resourcetransaction
    ADD CONSTRAINT resourcetransaction_pkey PRIMARY KEY (tid);


--
-- TOC entry 2087 (class 2606 OID 16874)
-- Name: resourcetransaction_purchase_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY resourcetransaction
    ADD CONSTRAINT resourcetransaction_purchase_id_fkey FOREIGN KEY (purchase_id) REFERENCES purchase(purchase_id);


--
-- TOC entry 2086 (class 2606 OID 16869)
-- Name: resourcetransaction_sid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY resourcetransaction
    ADD CONSTRAINT resourcetransaction_sid_fkey FOREIGN KEY (sid) REFERENCES supplier(sid);


--
-- TOC entry 2088 (class 2606 OID 16879)
-- Name: resourcetransaction_supplier_pi_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY resourcetransaction
    ADD CONSTRAINT resourcetransaction_supplier_pi_id_fkey FOREIGN KEY (supplier_pi_id) REFERENCES paymentinfo(pi_id);


-- Completed on 2018-01-07 17:09:16 AST

--
-- PostgreSQL database dump complete
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.10
-- Dumped by pg_dump version 9.5.10

-- Started on 2018-01-07 17:09:37 AST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 207 (class 1259 OID 16977)
-- Name: resourcetransactiondetail; Type: TABLE; Schema: public; Owner: appusr
--

CREATE TABLE resourcetransactiondetail (
    qty integer NOT NULL,
    purchaseprice double precision NOT NULL,
    rid integer NOT NULL,
    tid integer NOT NULL
);


ALTER TABLE resourcetransactiondetail OWNER TO appusr;

--
-- TOC entry 2201 (class 0 OID 16977)
-- Dependencies: 207
-- Data for Name: resourcetransactiondetail; Type: TABLE DATA; Schema: public; Owner: appusr
--

INSERT INTO resourcetransactiondetail VALUES (20, 2, 3, 2);
INSERT INTO resourcetransactiondetail VALUES (5, 5, 20, 2);
INSERT INTO resourcetransactiondetail VALUES (5, 5, 18, 2);
INSERT INTO resourcetransactiondetail VALUES (1, 700, 28, 9);
INSERT INTO resourcetransactiondetail VALUES (2, 2, 3, 10);


--
-- TOC entry 2084 (class 2606 OID 16981)
-- Name: resourcetransactiondetails_pkey; Type: CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY resourcetransactiondetail
    ADD CONSTRAINT resourcetransactiondetails_pkey PRIMARY KEY (rid, tid);


--
-- TOC entry 2085 (class 2606 OID 16982)
-- Name: resourcetransactiondetails_rid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY resourcetransactiondetail
    ADD CONSTRAINT resourcetransactiondetails_rid_fkey FOREIGN KEY (rid) REFERENCES resource(rid);


--
-- TOC entry 2086 (class 2606 OID 16987)
-- Name: resourcetransactiondetails_tid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: appusr
--

ALTER TABLE ONLY resourcetransactiondetail
    ADD CONSTRAINT resourcetransactiondetails_tid_fkey FOREIGN KEY (tid) REFERENCES resourcetransaction(tid);


-- Completed on 2018-01-07 17:09:37 AST

--
-- PostgreSQL database dump complete
--
