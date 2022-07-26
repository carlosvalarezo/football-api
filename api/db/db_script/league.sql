SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

CREATE TABLE public.leagues (
    id integer NOT NULL,
    name text,
    country text,
    starting_date date,
    ending_date date,
    current_match integer,
    code text,
    league_flag text,
    country_flag text
);

ALTER TABLE public.leagues OWNER TO football;

CREATE SEQUENCE public.league_id_seq AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER TABLE public.league_id_seq OWNER TO football;

ALTER SEQUENCE public.league_id_seq OWNED BY public.leagues.id;

ALTER TABLE ONLY public.leagues ALTER COLUMN id SET DEFAULT nextval('public.league_id_seq'::regclass);

SELECT pg_catalog.setval('public.league_id_seq', 1, true);

ALTER TABLE ONLY public.leagues
    ADD CONSTRAINT league_id_pkey PRIMARY KEY (id);

