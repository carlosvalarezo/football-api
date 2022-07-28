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
-- public.leagues
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
-- public.leagues
-- public.teams
CREATE TABLE public.teams (
    id integer NOT NULL,
    name text,
    team_flag text,
    venue text,
    code text,
    coach integer
);

ALTER TABLE public.teams OWNER TO football;

CREATE SEQUENCE public.team_id_seq AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER TABLE public.team_id_seq OWNER TO football;

ALTER SEQUENCE public.team_id_seq OWNED BY public.teams.id;

ALTER TABLE ONLY public.teams ALTER COLUMN id SET DEFAULT nextval('public.team_id_seq'::regclass);

SELECT pg_catalog.setval('public.team_id_seq', 1, true);

ALTER TABLE ONLY public.teams
    ADD CONSTRAINT team_id_pkey PRIMARY KEY (id);
-- public.teams
-- public.coaches
CREATE TABLE public.coaches (
    id integer NOT NULL,
    name text,
    nationality text,
    code text
);

ALTER TABLE public.coaches OWNER TO football;

CREATE SEQUENCE public.coach_id_seq AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER TABLE public.coach_id_seq OWNER TO football;

ALTER SEQUENCE public.coach_id_seq OWNED BY public.coaches.id;

ALTER TABLE ONLY public.coaches ALTER COLUMN id SET DEFAULT nextval('public.coach_id_seq'::regclass);

SELECT pg_catalog.setval('public.coach_id_seq', 1, true);

ALTER TABLE ONLY public.coaches
    ADD CONSTRAINT coach_id_pkey PRIMARY KEY (id);
-- public.coaches
-- public.players
CREATE TABLE public.players (
    id integer NOT NULL,
    name text,
    nationality text,
    date_of_birth date,
    position text,
    team integer,
    code text
);

ALTER TABLE public.players OWNER TO football;

CREATE SEQUENCE public.player_id_seq AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER TABLE public.player_id_seq OWNER TO football;

ALTER SEQUENCE public.player_id_seq OWNED BY public.players.id;

ALTER TABLE ONLY public.players ALTER COLUMN id SET DEFAULT nextval('public.player_id_seq'::regclass);

SELECT pg_catalog.setval('public.player_id_seq', 1, true);

ALTER TABLE ONLY public.players
    ADD CONSTRAINT player_id_pkey PRIMARY KEY (id);
-- public.players
-- table league_teams
CREATE TABLE public.league_teams (
    league integer NOT NULL,
    team integer NOT NULL
);

ALTER TABLE public.league_teams OWNER TO football;

ALTER TABLE ONLY public.league_teams
    ADD CONSTRAINT league_teams_id_pkey PRIMARY KEY (league, team);
-- table league_teams

-- foreign keys
ALTER TABLE ONLY public.teams
    ADD CONSTRAINT coach FOREIGN KEY (coach) REFERENCES public.coaches(id) ON UPDATE CASCADE ON DELETE SET NULL;

ALTER TABLE ONLY public.players
    ADD CONSTRAINT team FOREIGN KEY (team) REFERENCES public.teams(id) ON UPDATE CASCADE ON DELETE SET NULL;

ALTER TABLE ONLY public.league_teams
    ADD CONSTRAINT league FOREIGN KEY (league) REFERENCES public.leagues(id) ON UPDATE CASCADE ON DELETE SET NULL;

ALTER TABLE ONLY public.league_teams
    ADD CONSTRAINT team FOREIGN KEY (team) REFERENCES public.teams(id) ON UPDATE CASCADE ON DELETE SET NULL;
