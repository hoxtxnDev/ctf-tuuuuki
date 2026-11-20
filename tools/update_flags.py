#!/usr/bin/env python3
"""
Script determinista de estandarización de flags (Fase 1A).
Actualiza únicamente archivos de configuración (metadata.yml), archivos de texto
plano de flags, referencias textuales en código/soluciones y verificadores de texto,
sin alterar artefactos binarios, imágenes, capturas PCAP ni archivos compilados.
"""

import os
import re
import glob

# Mapeo de los 57 desafíos:
# carpeta -> (flag_anterior, flag_nueva, requiere_reconstruccion_binaria, archivos_texto_adicionales)
FLAG_MAPPING = {
    "acaan": (
        "CTF{changing-memories}",
        "DUOC{escritura_memoria_proc_48291}",
        False,
        ["acaan/challenge/src/flag.txt"],
    ),
    "amd": (
        "CTF{zen_and_the_art_of_bad_crypto}",
        "DUOC{preimagen_cmac_microcodigo_73920}",
        False,
        ["amd/challenge/flag.txt", "amd/solution/README.md"],
    ),
    "arrow-of-time": (
        "CTF{reverse_time_polarity}",
        "DUOC{ciclo_colision_brent_59184}",
        False,
        ["arrow-of-time/challenge/flag.txt", "arrow-of-time/solution/README.md"],
    ),
    "block-cipher": (
        "CTF{subterrenaceous_hyperencryption_misconfigurate_transmutational_deobfuscation}",
        "DUOC{codificacion_radix_mixta_84619}",
        True,
        ["block-cipher/solution/README.md"],
    ),
    "boxy": (
        "YouCrackedTheCode",
        "DUOC{combinacion_candado_fisico_31749}",
        False,
        [],
    ),
    "bug-me": (
        "CTF{hope-you-enjoyed-this-one}",
        "DUOC{residuos_teorema_chino_62841}",
        True,
        ["bug-me/challenge/src/embed.rb", "bug-me/solution/solve.rb"],
    ),
    "cardx": (
        "CTF{plsverifynow}",
        "DUOC{matriz_puntos_amarillos_95173}",
        True,
        ["cardx/solution/README.md", "cardx/challenge/dot_patterns/make_dot_pattern.pl"],
    ),
    "cert-tool": (
        "CTF{dont_look_behind_you}",
        "DUOC{retroceso_relleno_base64_27465}",
        False,
        ["cert-tool/challenge/flag.txt"],
    ),
    "cipher-block-corruption": (
        "CTF{is_my_flag_showing}",
        "DUOC{cabecera_png_sin_iv_41827}",
        True,
        ["cipher-block-corruption/solution/README.md"],
    ),
    "crossworthy": (
        "CTF{bugbounty}",
        "DUOC{recompensa_vulnerabilidad_53918}",
        True,
        [],
    ),
    "dating": (
        "CTF{helping-dragons-find-love-since-2025}",
        "DUOC{deserializacion_xmldecoder_86429}",
        False,
        ["dating/challenge/flag.txt"],
    ),
    "detector": (
        "CTF{tharr-be-draggggons}",
        "DUOC{inyeccion_consola_directa_19574}",
        False,
        ["detector/challenge/app/dragon-detector-ai"],
    ),
    "detector-2": (
        "CTF{tharr-be-MORE-draggggons}",
        "DUOC{sustitucion_subshell_filtro_74832}",
        False,
        ["detector-2/challenge/app/dragon-detector-ai"],
    ),
    "digital-citizen": (
        "CTF{never_trust_a_black_box}",
        "DUOC{factores_primos_compartidos_38516}",
        False,
        ["digital-citizen/challenge/flag_1.txt", "digital-citizen/solution/README.md"],
    ),
    "digital-citizen-2": (
        "CTF{for_bits_location_is_everything}",
        "DUOC{raices_pequenas_coppersmith_92647}",
        False,
        ["digital-citizen/challenge/flag_2.txt", "digital-citizen/solution/README.md"],
    ),
    "drago-daction": (
        "CTF{file-writing-is-fun}",
        "DUOC{desbordamiento_puntero_archivo_67391}",
        False,
        ["drago-daction/challenge/flag.txt"],
    ),
    "dragon-name": (
        "CTF{w3akT0Fa1ryTyp3}",
        "DUOC{debilidad_elemental_hada_45928}",
        True,
        ["dragon-name/solution/README.md"],
    ),
    "dragon-spell": (
        "CTF{viridian}",
        "DUOC{sustitucion_runas_esmeralda_81354}",
        True,
        ["dragon-spell/solution/README.md", "dragon-spell/challenge/spell.txt"],
    ),
    "evidence": (
        "CTF{aha-found-em}",
        "DUOC{entidad_externa_xml_29483}",
        False,
        ["evidence/challenge/flag.txt"],
    ),
    "extinction": (
        "CTF{i-saved-the-dragons-and-all-i-got-was-this-stupid-flag}",
        "DUOC{maleabilidad_bits_base64_57294}",
        False,
        ["extinction/challenge/flag.txt"],
    ),
    "extra-effed-system": (
        "CTF{ticktock_upwarp}",
        "DUOC{reconstruccion_extents_xfs_63819}",
        True,
        ["extra-effed-system/solution/solution.txt"],
    ),
    "flag-search": (
        "CTF{bctrckngftw}",
        "DUOC{poda_backtracking_bits_49182}",
        True,
        ["flag-search/solution/README.md", "flag-search/challenge/search.py"],
    ),
    "go-back": (
        "CTF{told-you-its-not-timing}",
        "DUOC{oraculo_codigo_retorno_83715}",
        False,
        ["go-back/challenge/src/flag.txt"],
    ),
    "go-git-it": (
        "CTF{g0tt4_g!t_th4t}",
        "DUOC{historial_commits_expuesto_26491}",
        True,
        ["go-git-it/challenge/docker-compose.yml"],
    ),
    "goto-zero": (
        "CTF{i-solved-by-returning-to-main}",
        "DUOC{cadena_rop_retorno_main_71538}",
        False,
        ["goto-zero/challenge/flag.txt"],
    ),
    "hangman-one": (
        "CTF{hangm4nw1thfr1end5andf03s}",
        "DUOC{palabra_estatica_compartida_34982}",
        True,
        [],
    ),
    "hangman-two": (
        "CTF{h4ngmanr0ulett3w1n}",
        "DUOC{persistencia_cookie_estado_58271}",
        False,
        ["hangman-two/challenge/server.py"],
    ),
    "hangman-three": (
        "CTF{hangm4nW1thW3akJWTK3y}",
        "DUOC{secreto_jwt_diccionario_91463}",
        False,
        ["hangman-three/challenge/server.py"],
    ),
    "hidden-reports": (
        "CTF{select-or-one-equals-one}",
        "DUOC{tautologia_booleana_sql_47289}",
        False,
        ["hidden-reports/challenge/app/index.php"],
    ),
    "hoard": (
        "CTF{a-dragons-hoard-is-all-he-has-dont-take-it-away}",
        "DUOC{escape_comillas_parametro_69145}",
        False,
        ["hoard/challenge/flag.txt"],
    ),
    "last": (
        "CTF{auth_auth_bypass_bypass}",
        "DUOC{cabecera_subrequest_interna_82537}",
        False,
        [],
    ),
    "locky": (
        "make_me_a_secret",
        "DUOC{apertura_cilindro_fisico_15948}",
        False,
        [],
    ),
    "magic": (
        "CTF{g0t_th3_p0w3r_u_n33d}",
        "DUOC{reparacion_firma_cabecera_76392}",
        True,
        [],
    ),
    "matryoshkafs": (
        "CTF{warranty_void_if_layers_removed}",
        "DUOC{particiones_anidadas_multiple_54829}",
        True,
        [],
    ),
    "meow": (
        "CTF{DontBeACheatAh}",
        "DUOC{lectura_consola_remota_39174}",
        False,
        ["meow/challenge/flag.txt"],
    ),
    "moa-station": (
        "CTF{TRUST_BUT_VER1FY}",
        "DUOC{eventos_teclado_extension_61839}",
        False,
        ["moa-station/challenge/extension/background.js"],
    ),
    "nearest-neighbor": (
        "CTF{incredible_shrinking_flag}",
        "DUOC{interpolacion_submuestreo_28594}",
        True,
        [],
    ),
    "obscuratron": (
        "CTF{xor-by-next-letter-isnt-crypto}",
        "DUOC{flujo_xor_encadenado_94716}",
        True,
        ["obscuratron/challenge/src/memo.html"],
    ),
    "oh-say-can-you-see": (
        "CTF{draigon}",
        "DUOC{inversion_gradiente_red_43681}",
        True,
        [],
    ),
    "oh-the-places-youll-go": (
        "CTF{i_kill_where_i_wish_and_none_dare_resist}",
        "DUOC{triangulacion_visual_urbana_78245}",
        True,
        [],
    ),
    "oh-the-places-youll-go-2": (
        "CTF{681742030869784848529051269297481582042587446976}",
        "DUOC{coordenadas_681742030869784848529051269297481582042587446976}",
        True,
        [],
    ),
    "pascals-homomorphism": (
        "CTF{wut_not_rsa}",
        "DUOC{factorizacion_modulo_debil_35792}",
        False,
        ["pascals-homomorphism/challenge/src/flag_1.txt", "pascals-homomorphism/solution/README.md"],
    ),
    "pascals-homomorphism-2": (
        "CTF{homomorphisms_for_the_win}",
        "DUOC{maleabilidad_aditiva_oraculo_89417}",
        False,
        ["pascals-homomorphism/challenge/src/flag_2.txt", "pascals-homomorphism/solution/README.md"],
    ),
    "pathing": (
        "CTF{dotslashdotdotslashdotslashes}",
        "DUOC{navegacion_relativa_raiz_52683}",
        False,
        ["pathing/challenge/flag.txt"],
    ),
    "qr-decomp": (
        "CTF{punny_codes}",
        "DUOC{producto_matricial_ortogonal_64928}",
        True,
        ["qr-decomp/challenge/flag.txt", "qr-decomp/solution/README.md"],
    ),
    "ruthless-dot-flag": (
        "CTF{oldie_but_goodie}",
        "DUOC{decodificacion_pixel_rgb555_17385}",
        True,
        ["ruthless-dot-flag/solution/solution.txt"],
    ),
    "ruthless-dot-flag-2": (
        "CTF{evilcorp_won}",
        "DUOC{extraccion_bit_transparencia_83942}",
        True,
        ["ruthless-dot-flag/solution/solution.txt"],
    ),
    "sighting": (
        "CTF{dotdotslashdotdot}",
        "DUOC{inclusion_archivo_local_46197}",
        False,
        ["sighting/challenge/flag.txt"],
    ),
    "slackblock-steg": (
        "CTF{slack_space_not_just_for_filesystems}",
        "DUOC{relleno_bloques_dimension_72518}",
        True,
        ["slackblock-steg/solution/README.md"],
    ),
    "soothsayer": (
        "CTF{S33dth3tw1st3r}",
        "DUOC{prediccion_semilla_aleatoria_39846}",
        False,
        ["soothsayer/challenge/server/server.py"],
    ),
    "subprime": (
        "CTF{n0n_0pt!m@l_pR!m3$}",
        "DUOC{exponente_privado_factorizado_51739}",
        True,
        ["subprime/solution/README.md"],
    ),
    "tarnation": (
        "CTF{tarrible_format}",
        "DUOC{ocurrencia_archivo_concatenado_96284}",
        True,
        ["tarnation/solution/README.md"],
    ),
    "taxonomy": (
        "CTF{those-are-the-types-of-dragons}",
        "DUOC{evasion_filtro_clasificado_24861}",
        True,
        ["taxonomy/challenge/dragons.sql"],
    ),
    "toothless": (
        "CTF{y0u_us3l3ss_r3pt1l3}",
        "DUOC{carga_icmp_huerfana_68352}",
        True,
        [],
    ),
    "web-tutorial-1": (
        "CTF{X55-1s-back-aga1n}",
        "DUOC{exfiltracion_script_inline_41975}",
        False,
        ["web-tutorial-1/challenge/server.py"],
    ),
    "web-tutorial-2": (
        "CTF{Cl0udyFunct10n5F0rA11}",
        "DUOC{dominio_autorizado_politica_85329}",
        False,
        ["web-tutorial-2/challenge/server.py"],
    ),
    "your-browser-hates-you": (
        "CTF{shh-its-a-secret}",
        "DUOC{omision_certificado_autofirmado_37614}",
        False,
        ["your-browser-hates-you/challenge/app/index.html"],
    ),
}

FLAG_REGEX = re.compile(r"^DUOC\{[a-z0-9_]*[0-9]+[a-z0-9_]*\}$")


def validate_mapping():
    seen = set()
    for ch, (old_f, new_f, is_bin, extra_files) in FLAG_MAPPING.items():
        assert FLAG_REGEX.match(new_f), f"Formato inválido en {ch}: {new_f}"
        assert new_f not in seen, f"Flag duplicada: {new_f}"
        seen.add(new_f)
    print(f"[OK] {len(seen)} flags únicas validadas contra {FLAG_REGEX.pattern}")


def apply_updates():
    updated_summary = {}
    for ch, (old_f, new_f, is_bin, extra_files) in sorted(FLAG_MAPPING.items()):
        updated_files = []
        meta_path = os.path.join(ch, "metadata.yml")
        if os.path.exists(meta_path):
            with open(meta_path, "r", encoding="utf-8") as f:
                content = f.read()
            if old_f in content:
                content = content.replace(old_f, new_f)
            else:
                content = re.sub(r"^(flag:\s*['\"]?)DUOC\{[^}]+\}(['\"]?)$", rf"\g<1>{new_f}\g<2>", content, flags=re.M)
            if ch == "oh-the-places-youll-go-2" and "DUOC{coordenadas_" not in content.split("description:")[1]:
                content = content.replace(
                    "(Uses the files found from solving part 1)",
                    "(Uses the files found from solving part 1. Format: DUOC{coordenadas_<48_digitos>})",
                )
            with open(meta_path, "w", encoding="utf-8") as f:
                f.write(content)
            updated_files.append(meta_path)

        for fp in extra_files:
            if os.path.exists(fp):
                with open(fp, "r", encoding="utf-8") as f:
                    c = f.read()
                if old_f in c:
                    c = c.replace(old_f, new_f)
                elif ch == "dragon-spell" and "CTF{Viridian}" in c:
                    c = c.replace("CTF{Viridian}", new_f)
                with open(fp, "w", encoding="utf-8") as f:
                    f.write(c)
                updated_files.append(fp)

        # Actualizar verificadores libronsolve.rb / solve.rb si existen y el reto es de texto plano
        lib_path = os.path.join(ch, "solution", "libronsolve.rb")
        if os.path.exists(lib_path):
            with open(lib_path, "r", encoding="utf-8") as f:
                lc = f.read()
            if "CTF{" in lc:
                lc = lc.replace("/(CTF{[^}]*})/", "/(DUOC{[^}]*})/")
                with open(lib_path, "w", encoding="utf-8") as f:
                    f.write(lc)
            updated_files.append(lib_path)

        if ch == "your-browser-hates-you":
            s_path = "your-browser-hates-you/solution/solve.rb"
            with open(s_path, "r", encoding="utf-8") as f:
                sc = f.read()
            sc = sc.replace("/(CTF{[^}]*})/", "/(DUOC{[^}]*})/")
            with open(s_path, "w", encoding="utf-8") as f:
                f.write(sc)
            updated_files.append(s_path)

        if ch == "extinction":
            s_path = "extinction/solution/solve.rb"
            with open(s_path, "r", encoding="utf-8") as f:
                sc = f.read()
            sc = sc.replace("include?('CTF')", "include?('DUOC')")
            with open(s_path, "w", encoding="utf-8") as f:
                f.write(sc)
            updated_files.append(s_path)

        updated_summary[ch] = (old_f, new_f, updated_files, "Pendiente manual (artefacto binario/imagen)" if is_bin else "Actualizado")

    print(f"[OK] Actualizados {len(updated_summary)} desafíos.")


if __name__ == "__main__":
    validate_mapping()
    apply_updates()
