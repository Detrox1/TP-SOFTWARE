PGDMP      
        
        |            TP-IntroSoftware    16.3    16.3     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16397    TP-IntroSoftware    DATABASE     �   CREATE DATABASE "TP-IntroSoftware" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Argentina.1252';
 "   DROP DATABASE "TP-IntroSoftware";
                postgres    false            �            1259    16412    Ciudad    TABLE     �   CREATE TABLE public."Ciudad" (
    "Id" numeric NOT NULL,
    "Nombre" character varying NOT NULL,
    "Descripcion" character varying,
    "Nivel" numeric NOT NULL,
    "Plata" numeric NOT NULL
);
    DROP TABLE public."Ciudad";
       public         heap    postgres    false            �            1259    16419 	   Edificios    TABLE     B  CREATE TABLE public."Edificios" (
    "Id" numeric NOT NULL,
    "Nombre" character varying NOT NULL,
    "Descripcion" character varying NOT NULL,
    "Foto" character varying NOT NULL,
    "PlataPasiva" numeric NOT NULL,
    "Costo" numeric NOT NULL,
    "Poblacion" numeric NOT NULL,
    "IdCiudad" numeric NOT NULL
);
    DROP TABLE public."Edificios";
       public         heap    postgres    false            �            1259    16405    Usuarios    TABLE     �   CREATE TABLE public."Usuarios" (
    "Id" numeric NOT NULL,
    "NombreUsuario" character varying NOT NULL,
    "Contraseña" character varying NOT NULL,
    "Imagen" character varying
);
    DROP TABLE public."Usuarios";
       public         heap    postgres    false            �          0    16412    Ciudad 
   TABLE DATA           S   COPY public."Ciudad" ("Id", "Nombre", "Descripcion", "Nivel", "Plata") FROM stdin;
    public          postgres    false    216   4       �          0    16419 	   Edificios 
   TABLE DATA           }   COPY public."Edificios" ("Id", "Nombre", "Descripcion", "Foto", "PlataPasiva", "Costo", "Poblacion", "IdCiudad") FROM stdin;
    public          postgres    false    217   t       �          0    16405    Usuarios 
   TABLE DATA           T   COPY public."Usuarios" ("Id", "NombreUsuario", "Contraseña", "Imagen") FROM stdin;
    public          postgres    false    215   �       $           2606    16418    Ciudad Ciudad_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public."Ciudad"
    ADD CONSTRAINT "Ciudad_pkey" PRIMARY KEY ("Id");
 @   ALTER TABLE ONLY public."Ciudad" DROP CONSTRAINT "Ciudad_pkey";
       public            postgres    false    216            &           2606    16425    Edificios Id 
   CONSTRAINT     P   ALTER TABLE ONLY public."Edificios"
    ADD CONSTRAINT "Id" PRIMARY KEY ("Id");
 :   ALTER TABLE ONLY public."Edificios" DROP CONSTRAINT "Id";
       public            postgres    false    217            "           2606    16411    Usuarios Usuarios_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public."Usuarios"
    ADD CONSTRAINT "Usuarios_pkey" PRIMARY KEY ("Id");
 D   ALTER TABLE ONLY public."Usuarios" DROP CONSTRAINT "Usuarios_pkey";
       public            postgres    false    215            (           2606    16426    Edificios IdCiudad    FK CONSTRAINT     }   ALTER TABLE ONLY public."Edificios"
    ADD CONSTRAINT "IdCiudad" FOREIGN KEY ("IdCiudad") REFERENCES public."Ciudad"("Id");
 @   ALTER TABLE ONLY public."Edificios" DROP CONSTRAINT "IdCiudad";
       public          postgres    false    217    4644    216            '           2606    16431    Usuarios IdCiudad    FK CONSTRAINT     �   ALTER TABLE ONLY public."Usuarios"
    ADD CONSTRAINT "IdCiudad" FOREIGN KEY ("Id") REFERENCES public."Ciudad"("Id") NOT VALID;
 ?   ALTER TABLE ONLY public."Usuarios" DROP CONSTRAINT "IdCiudad";
       public          postgres    false    215    216    4644            �   0   x�3�t�J�-��w�,MIL��KTH3r2�R9�8����b���� C!�      �      x������ � �      �      x������ � �     