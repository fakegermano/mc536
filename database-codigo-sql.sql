--
-- PostgreSQL database dump
--

-- Dumped from database version 10.4
-- Dumped by pg_dump version 10.4

-- Started on 2018-06-03 20:33:23

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 1 (class 3079 OID 12924)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2917 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 208 (class 1259 OID 24713)
-- Name: apita; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.apita (
    "num_ID" integer NOT NULL,
    "tipo_ID" character varying(30) NOT NULL,
    pais character varying(50) NOT NULL,
    pais1 character varying(50) NOT NULL,
    pais2 character varying(50) NOT NULL,
    rodada integer NOT NULL
);


ALTER TABLE public.apita OWNER TO postgres;

--
-- TOC entry 198 (class 1259 OID 24581)
-- Name: arbitro; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.arbitro (
    "num_ID" integer NOT NULL,
    "tipo_ID" character varying(30) NOT NULL,
    pais character varying(50) NOT NULL,
    funcao character varying(30) NOT NULL
);


ALTER TABLE public.arbitro OWNER TO postgres;

--
-- TOC entry 206 (class 1259 OID 24679)
-- Name: assiste; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.assiste (
    "num_ID" integer NOT NULL,
    "tipo_ID" character varying(30) NOT NULL,
    pais character varying(50) NOT NULL,
    pais1 character varying(50) NOT NULL,
    pais2 character varying(50) NOT NULL,
    rodada integer NOT NULL
);


ALTER TABLE public.assiste OWNER TO postgres;

--
-- TOC entry 197 (class 1259 OID 24576)
-- Name: comentarista; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.comentarista (
    "num_ID" integer NOT NULL,
    "tipo_ID" character varying(30) NOT NULL,
    pais character varying(50) NOT NULL,
    lingua character varying(50) NOT NULL
);


ALTER TABLE public.comentarista OWNER TO postgres;

--
-- TOC entry 200 (class 1259 OID 24591)
-- Name: estadio; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.estadio (
    cidade character varying(80) NOT NULL,
    estado character varying(50) NOT NULL,
    nome character varying(255) NOT NULL,
    capacidade integer NOT NULL
);


ALTER TABLE public.estadio OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 24601)
-- Name: jogador; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jogador (
    "num_ID" integer NOT NULL,
    "tipo_ID" character varying(30) NOT NULL,
    pais character varying(50) NOT NULL,
    num integer NOT NULL,
    cartoes_amarelos integer DEFAULT 0 NOT NULL,
    cartoes_vermelhos integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.jogador OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 24615)
-- Name: jogador_ataque; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jogador_ataque (
    "num_ID" integer NOT NULL,
    "tipo_ID" character varying(30) NOT NULL,
    pais character varying(50) NOT NULL,
    gols integer DEFAULT 0 NOT NULL,
    assistencias integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.jogador_ataque OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 24608)
-- Name: jogador_defesa; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jogador_defesa (
    "num_ID" integer NOT NULL,
    "tipo_ID" character varying(30) NOT NULL,
    pais character varying(50) NOT NULL,
    desarmes integer DEFAULT 0 NOT NULL,
    faltas integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.jogador_defesa OWNER TO postgres;

--
-- TOC entry 207 (class 1259 OID 24696)
-- Name: narra; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.narra (
    "num_ID" integer NOT NULL,
    "tipo_ID" character varying(30) NOT NULL,
    pais character varying(50) NOT NULL,
    pais1 character varying(50) NOT NULL,
    pais2 character varying(50) NOT NULL,
    rodada integer NOT NULL
);


ALTER TABLE public.narra OWNER TO postgres;

--
-- TOC entry 205 (class 1259 OID 24622)
-- Name: partida; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.partida (
    pais1 character varying(50) NOT NULL,
    pais2 character varying(50) NOT NULL,
    rodada integer NOT NULL,
    placar character varying(10),
    cidade character varying(80) NOT NULL,
    estado character varying(50) NOT NULL
);


ALTER TABLE public.partida OWNER TO postgres;

--
-- TOC entry 201 (class 1259 OID 24596)
-- Name: tecnico; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tecnico (
    "num_ID" integer NOT NULL,
    "tipo_ID" character varying(30) NOT NULL,
    pais character varying(50) NOT NULL
);


ALTER TABLE public.tecnico OWNER TO postgres;

--
-- TOC entry 199 (class 1259 OID 24586)
-- Name: time_futebol; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.time_futebol (
    pais character varying(50) NOT NULL,
    formacao character varying(30) NOT NULL
);


ALTER TABLE public.time_futebol OWNER TO postgres;

--
-- TOC entry 196 (class 1259 OID 16396)
-- Name: torcedor; Type: TABLE; Schema: public; Owner: grupo_mc536
--

CREATE TABLE public.torcedor (
    "num_ID" integer NOT NULL,
    "tipo_ID" character varying(30) NOT NULL,
    pais character varying(50) NOT NULL,
    torce_pais character varying(50)
);


ALTER TABLE public.torcedor OWNER TO grupo_mc536;

--
-- TOC entry 2909 (class 0 OID 24713)
-- Dependencies: 208
-- Data for Name: apita; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.apita ("num_ID", "tipo_ID", pais, pais1, pais2, rodada) FROM stdin;
\.


--
-- TOC entry 2899 (class 0 OID 24581)
-- Dependencies: 198
-- Data for Name: arbitro; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.arbitro ("num_ID", "tipo_ID", pais, funcao) FROM stdin;
\.


--
-- TOC entry 2907 (class 0 OID 24679)
-- Dependencies: 206
-- Data for Name: assiste; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.assiste ("num_ID", "tipo_ID", pais, pais1, pais2, rodada) FROM stdin;
\.


--
-- TOC entry 2898 (class 0 OID 24576)
-- Dependencies: 197
-- Data for Name: comentarista; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.comentarista ("num_ID", "tipo_ID", pais, lingua) FROM stdin;
\.


--
-- TOC entry 2901 (class 0 OID 24591)
-- Dependencies: 200
-- Data for Name: estadio; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.estadio (cidade, estado, nome, capacidade) FROM stdin;
\.


--
-- TOC entry 2903 (class 0 OID 24601)
-- Dependencies: 202
-- Data for Name: jogador; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jogador ("num_ID", "tipo_ID", pais, num, cartoes_amarelos, cartoes_vermelhos) FROM stdin;
\.


--
-- TOC entry 2905 (class 0 OID 24615)
-- Dependencies: 204
-- Data for Name: jogador_ataque; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jogador_ataque ("num_ID", "tipo_ID", pais, gols, assistencias) FROM stdin;
\.


--
-- TOC entry 2904 (class 0 OID 24608)
-- Dependencies: 203
-- Data for Name: jogador_defesa; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jogador_defesa ("num_ID", "tipo_ID", pais, desarmes, faltas) FROM stdin;
\.


--
-- TOC entry 2908 (class 0 OID 24696)
-- Dependencies: 207
-- Data for Name: narra; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.narra ("num_ID", "tipo_ID", pais, pais1, pais2, rodada) FROM stdin;
\.


--
-- TOC entry 2906 (class 0 OID 24622)
-- Dependencies: 205
-- Data for Name: partida; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.partida (pais1, pais2, rodada, placar, cidade, estado) FROM stdin;
\.


--
-- TOC entry 2902 (class 0 OID 24596)
-- Dependencies: 201
-- Data for Name: tecnico; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tecnico ("num_ID", "tipo_ID", pais) FROM stdin;
\.


--
-- TOC entry 2900 (class 0 OID 24586)
-- Dependencies: 199
-- Data for Name: time_futebol; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.time_futebol (pais, formacao) FROM stdin;
\.


--
-- TOC entry 2897 (class 0 OID 16396)
-- Dependencies: 196
-- Data for Name: torcedor; Type: TABLE DATA; Schema: public; Owner: grupo_mc536
--

COPY public.torcedor ("num_ID", "tipo_ID", pais, torce_pais) FROM stdin;
\.


--
-- TOC entry 2758 (class 2606 OID 24717)
-- Name: apita apita_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apita
    ADD CONSTRAINT apita_pkey PRIMARY KEY ("num_ID", "tipo_ID", pais, pais1, pais2, rodada);


--
-- TOC entry 2728 (class 2606 OID 24585)
-- Name: arbitro arbitro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.arbitro
    ADD CONSTRAINT arbitro_pkey PRIMARY KEY ("num_ID", "tipo_ID", pais);


--
-- TOC entry 2750 (class 2606 OID 24683)
-- Name: assiste assiste_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.assiste
    ADD CONSTRAINT assiste_pkey PRIMARY KEY ("num_ID", "tipo_ID", pais, pais1, pais2, rodada);


--
-- TOC entry 2726 (class 2606 OID 24580)
-- Name: comentarista comentarista_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comentarista
    ADD CONSTRAINT comentarista_pkey PRIMARY KEY ("num_ID", "tipo_ID", pais);


--
-- TOC entry 2732 (class 2606 OID 24595)
-- Name: estadio estadio_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estadio
    ADD CONSTRAINT estadio_pkey PRIMARY KEY (cidade, estado);


--
-- TOC entry 2743 (class 2606 OID 24619)
-- Name: jogador_ataque jogador_ataque_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jogador_ataque
    ADD CONSTRAINT jogador_ataque_pkey PRIMARY KEY ("num_ID", "tipo_ID");


--
-- TOC entry 2740 (class 2606 OID 24612)
-- Name: jogador_defesa jogador_defesa_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jogador_defesa
    ADD CONSTRAINT jogador_defesa_pkey PRIMARY KEY ("num_ID", "tipo_ID", pais);


--
-- TOC entry 2738 (class 2606 OID 24605)
-- Name: jogador jogador_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jogador
    ADD CONSTRAINT jogador_pkey PRIMARY KEY ("num_ID", "tipo_ID", pais);


--
-- TOC entry 2756 (class 2606 OID 24700)
-- Name: narra narra_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.narra
    ADD CONSTRAINT narra_pkey PRIMARY KEY ("num_ID", "tipo_ID", pais, pais1, pais2, rodada);


--
-- TOC entry 2748 (class 2606 OID 24626)
-- Name: partida partida_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.partida
    ADD CONSTRAINT partida_pkey PRIMARY KEY (pais1, pais2, rodada);


--
-- TOC entry 2735 (class 2606 OID 24600)
-- Name: tecnico tecnico_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tecnico
    ADD CONSTRAINT tecnico_pkey PRIMARY KEY ("num_ID", pais, "tipo_ID");


--
-- TOC entry 2730 (class 2606 OID 24590)
-- Name: time_futebol time_futebol_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.time_futebol
    ADD CONSTRAINT time_futebol_pkey PRIMARY KEY (pais);


--
-- TOC entry 2724 (class 2606 OID 16400)
-- Name: torcedor torcedor_pkey; Type: CONSTRAINT; Schema: public; Owner: grupo_mc536
--

ALTER TABLE ONLY public.torcedor
    ADD CONSTRAINT torcedor_pkey PRIMARY KEY ("num_ID", "tipo_ID", pais);


--
-- TOC entry 2759 (class 1259 OID 24723)
-- Name: fki_apita_arbitro; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_apita_arbitro ON public.apita USING btree ("num_ID", "tipo_ID", pais);


--
-- TOC entry 2760 (class 1259 OID 24729)
-- Name: fki_apita_partida; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_apita_partida ON public.apita USING btree (pais1, pais2, rodada);


--
-- TOC entry 2751 (class 1259 OID 24689)
-- Name: fki_assiste_partida; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_assiste_partida ON public.assiste USING btree (pais1, pais2, rodada);


--
-- TOC entry 2752 (class 1259 OID 24695)
-- Name: fki_assiste_torcedor; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_assiste_torcedor ON public.assiste USING btree ("num_ID", "tipo_ID", pais);


--
-- TOC entry 2741 (class 1259 OID 24660)
-- Name: fki_jogador_ataque; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_jogador_ataque ON public.jogador_ataque USING btree ("num_ID", "tipo_ID", pais);


--
-- TOC entry 2736 (class 1259 OID 24649)
-- Name: fki_jogador_pais; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_jogador_pais ON public.jogador USING btree (pais);


--
-- TOC entry 2753 (class 1259 OID 24706)
-- Name: fki_narra_comentarista; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_narra_comentarista ON public.narra USING btree ("num_ID", "tipo_ID", pais);


--
-- TOC entry 2754 (class 1259 OID 24712)
-- Name: fki_narra_partida; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_narra_partida ON public.narra USING btree (pais1, pais2, rodada);


--
-- TOC entry 2733 (class 1259 OID 24638)
-- Name: fki_pais; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_pais ON public.tecnico USING btree (pais);


--
-- TOC entry 2744 (class 1259 OID 24666)
-- Name: fki_pais1; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_pais1 ON public.partida USING btree (pais1);


--
-- TOC entry 2745 (class 1259 OID 24672)
-- Name: fki_pais2; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_pais2 ON public.partida USING btree (pais2);


--
-- TOC entry 2746 (class 1259 OID 24678)
-- Name: fki_partida_estadio; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_partida_estadio ON public.partida USING btree (cidade, estado);


--
-- TOC entry 2722 (class 1259 OID 24632)
-- Name: fki_torce_pais; Type: INDEX; Schema: public; Owner: grupo_mc536
--

CREATE INDEX fki_torce_pais ON public.torcedor USING btree (torce_pais);


--
-- TOC entry 2774 (class 2606 OID 24718)
-- Name: apita apita_num_ID_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apita
    ADD CONSTRAINT "apita_num_ID_fkey" FOREIGN KEY ("num_ID", "tipo_ID", pais) REFERENCES public.arbitro("num_ID", "tipo_ID", pais);


--
-- TOC entry 2775 (class 2606 OID 24724)
-- Name: apita apita_pais1_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apita
    ADD CONSTRAINT apita_pais1_fkey FOREIGN KEY (pais1, pais2, rodada) REFERENCES public.partida(pais1, pais2, rodada);


--
-- TOC entry 2771 (class 2606 OID 24690)
-- Name: assiste assiste_num_ID_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.assiste
    ADD CONSTRAINT "assiste_num_ID_fkey" FOREIGN KEY ("num_ID", "tipo_ID", pais) REFERENCES public.torcedor("num_ID", "tipo_ID", pais);


--
-- TOC entry 2770 (class 2606 OID 24684)
-- Name: assiste assiste_pais1_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.assiste
    ADD CONSTRAINT assiste_pais1_fkey FOREIGN KEY (pais1, pais2, rodada) REFERENCES public.partida(pais1, pais2, rodada);


--
-- TOC entry 2766 (class 2606 OID 24655)
-- Name: jogador_ataque jogador_ataque_num_ID_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jogador_ataque
    ADD CONSTRAINT "jogador_ataque_num_ID_fkey" FOREIGN KEY ("num_ID", "tipo_ID", pais) REFERENCES public.jogador("num_ID", "tipo_ID", pais);


--
-- TOC entry 2765 (class 2606 OID 24650)
-- Name: jogador_defesa jogador_defesa_num_ID_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jogador_defesa
    ADD CONSTRAINT "jogador_defesa_num_ID_fkey" FOREIGN KEY ("num_ID", "tipo_ID", pais) REFERENCES public.jogador("num_ID", "tipo_ID", pais);


--
-- TOC entry 2763 (class 2606 OID 24639)
-- Name: jogador jogador_pais_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jogador
    ADD CONSTRAINT jogador_pais_fkey FOREIGN KEY (pais) REFERENCES public.time_futebol(pais);


--
-- TOC entry 2764 (class 2606 OID 24644)
-- Name: jogador jogador_pais_fkey1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jogador
    ADD CONSTRAINT jogador_pais_fkey1 FOREIGN KEY (pais) REFERENCES public.time_futebol(pais);


--
-- TOC entry 2772 (class 2606 OID 24701)
-- Name: narra narra_num_ID_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.narra
    ADD CONSTRAINT "narra_num_ID_fkey" FOREIGN KEY ("num_ID", "tipo_ID", pais) REFERENCES public.comentarista("num_ID", "tipo_ID", pais);


--
-- TOC entry 2773 (class 2606 OID 24707)
-- Name: narra narra_pais1_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.narra
    ADD CONSTRAINT narra_pais1_fkey FOREIGN KEY (pais1, pais2, rodada) REFERENCES public.partida(pais1, pais2, rodada);


--
-- TOC entry 2769 (class 2606 OID 24673)
-- Name: partida partida_cidade_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.partida
    ADD CONSTRAINT partida_cidade_fkey FOREIGN KEY (cidade, estado) REFERENCES public.estadio(cidade, estado);


--
-- TOC entry 2767 (class 2606 OID 24661)
-- Name: partida partida_pais1_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.partida
    ADD CONSTRAINT partida_pais1_fkey FOREIGN KEY (pais1) REFERENCES public.time_futebol(pais);


--
-- TOC entry 2768 (class 2606 OID 24667)
-- Name: partida partida_pais2_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.partida
    ADD CONSTRAINT partida_pais2_fkey FOREIGN KEY (pais2) REFERENCES public.time_futebol(pais);


--
-- TOC entry 2762 (class 2606 OID 24633)
-- Name: tecnico tecnico_pais_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tecnico
    ADD CONSTRAINT tecnico_pais_fkey FOREIGN KEY (pais) REFERENCES public.time_futebol(pais);


--
-- TOC entry 2761 (class 2606 OID 24627)
-- Name: torcedor torcedor_torce_pais_fkey; Type: FK CONSTRAINT; Schema: public; Owner: grupo_mc536
--

ALTER TABLE ONLY public.torcedor
    ADD CONSTRAINT torcedor_torce_pais_fkey FOREIGN KEY (torce_pais) REFERENCES public.time_futebol(pais);


-- Completed on 2018-06-03 20:33:23

--
-- PostgreSQL database dump complete
--

