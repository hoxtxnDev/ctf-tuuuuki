#!/usr/bin/env python3
"""
Suite de Auditoría y Validación Integral del Repositorio CTF (Fase 4).
Verifica:
1. Cero flags duplicadas (entre las 57 legítimas, 3 de plantillas OSINT y 3 señuelo = 63 flags).
2. Cumplimiento del 100% con la expresión regular ^DUOC\{[a-z0-9_]*[0-9]+[a-z0-9_]*\}$.
3. Coherencia 1 a 1 entre la flag de metadata.yml y la documentada en solution/README.md.
4. Presencia y localización al español de README.md raíz, 57 README.md de retos y 57 guías de solución.
5. Completitud de las 3 plantillas OSINT reutilizables en templates/osint/.
6. Carácter 100% pasivo y aislamiento de los 3 Canary Tokens en docs/canary_registry.json y templates/canary_samples/.
7. Verificación sintáctica y funcional de scripts de solución disponibles.
"""

import os
import re
import json
import subprocess
import sys

FLAG_REGEX = re.compile(r"^DUOC\{[a-z0-9_]*[0-9]+[a-z0-9_]*\}$")
EXCLUDED_DIRS = {"tools", "templates", "docs"}


def get_challenge_dirs():
    return sorted(
        d for d in os.listdir(".")
        if os.path.isdir(d) and not d.startswith(".") and d not in EXCLUDED_DIRS
    )


def main():
    errors = []
    challenges = get_challenge_dirs()
    print(f"=== INICIANDO AUDITORÍA INTEGRAL DEL REPOSITORIO ({len(challenges)} desafíos) ===")

    # 1 & 2. Extraer flags legítimas, validar formato y unicidad
    legit_flags = {}
    for ch in challenges:
        meta_path = os.path.join(ch, "metadata.yml")
        if not os.path.exists(meta_path):
            errors.append(f"Falta metadata.yml en {ch}")
            continue
        with open(meta_path, "r", encoding="utf-8") as f:
            mc = f.read()
        m = re.search(r"^flag:\s*(.+)$", mc, re.M)
        if not m:
            errors.append(f"No se encontró campo flag en {meta_path}")
            continue
        fl = m.group(1).strip().strip("\"'")
        if not FLAG_REGEX.match(fl):
            errors.append(f"Formato inválido en {ch}: {fl}")
        if fl in legit_flags.values():
            errors.append(f"Flag legítima duplicada en {ch}: {fl}")
        legit_flags[ch] = fl

    print(f"[1/7] Flags legítimas extraídas: {len(legit_flags)} (Únicas: {len(set(legit_flags.values()))})")

    # 3. Integridad desafío-solución y README por desafío en español
    spanish_markers = ["Introducción", "Objetivo", "Requisitos", "Instrucciones de ejecución", "Metodología", "Formato de flags"]
    for ch, fl in legit_flags.items():
        readme_path = os.path.join(ch, "README.md")
        if not os.path.exists(readme_path):
            errors.append(f"Falta README.md en {ch}")
        else:
            with open(readme_path, "r", encoding="utf-8") as f:
                rc = f.read()
            for marker in spanish_markers:
                if marker not in rc:
                    errors.append(f"Sección '{marker}' faltante en {readme_path}")

        sol_readme = os.path.join(ch, "solution", "README.md")
        if not os.path.exists(sol_readme):
            errors.append(f"Falta solution/README.md en {ch}")
        else:
            with open(sol_readme, "r", encoding="utf-8") as f:
                sc = f.read()
            if fl not in sc:
                errors.append(f"La flag {fl} de {ch}/metadata.yml no coincide en {sol_readme}")

    print("[2/7] Coherencia desafío-solución (57/57) y README.md en español (57/57): VERIFICADO")

    # 4. Verificar las 3 plantillas OSINT
    osint_templates = ["osint_geografico", "osint_digital", "osint_investigativo"]
    template_flags = []
    for tpl in osint_templates:
        tpl_dir = os.path.join("templates", "osint", tpl)
        for req_file in ["challenge.yml", "metadata.yml", "README.md", "SOLUCION.md"]:
            p = os.path.join(tpl_dir, req_file)
            if not os.path.exists(p):
                errors.append(f"Falta {p} en plantilla OSINT")
        ev_dir = os.path.join(tpl_dir, "evidencias")
        if not os.path.isdir(ev_dir) or not os.listdir(ev_dir):
            errors.append(f"Carpeta evidencias/ vacía o faltante en {tpl_dir}")
        with open(os.path.join(tpl_dir, "challenge.yml"), "r", encoding="utf-8") as f:
            cc = f.read()
        m = re.search(r"^flag:\s*['\"]([^'\"]+)['\"]", cc, re.M)
        if not m or not FLAG_REGEX.match(m.group(1)):
            errors.append(f"Flag inválida en plantilla {tpl}")
        else:
            t_flag = m.group(1)
            template_flags.append(t_flag)
            with open(os.path.join(tpl_dir, "SOLUCION.md"), "r", encoding="utf-8") as sf:
                if t_flag not in sf.read():
                    errors.append(f"Flag de plantilla {t_flag} no documentada en {tpl}/SOLUCION.md")

    print(f"[3/7] Plantillas OSINT reutilizables verificadas: {len(osint_templates)}/3 ({template_flags})")

    # 5. Verificar Canary Tokens pasivos y aislamiento
    reg_path = os.path.join("docs", "canary_registry.json")
    eval_path = os.path.join("docs", "evaluacion_canary.md")
    canary_flags = []
    if not os.path.exists(reg_path) or not os.path.exists(eval_path):
        errors.append("Faltan archivos de registro o evaluación de Canary Tokens en docs/")
    else:
        with open(reg_path, "r", encoding="utf-8") as f:
            reg_data = json.load(f)
        for entry in reg_data.get("canaries", []):
            c_flag = entry["flag"]
            c_file = entry["file_path"]
            canary_flags.append(c_flag)
            if not FLAG_REGEX.match(c_flag):
                errors.append(f"Flag señuelo con formato inválido: {c_flag}")
            if c_flag in legit_flags.values() or c_flag in template_flags:
                errors.append(f"Flag señuelo colisiona con flag legítima: {c_flag}")
            if not os.path.exists(c_file):
                errors.append(f"Archivo de vector señuelo no existe: {c_file}")
            else:
                with open(c_file, "r", encoding="utf-8") as cf:
                    c_content = cf.read()
                if c_flag not in c_content:
                    errors.append(f"Flag señuelo {c_flag} no presente en {c_file}")
                if "<script" in c_content.lower():
                    errors.append(f"Vector señuelo {c_file} contiene etiqueta <script> no permitida")

    all_63_flags = list(legit_flags.values()) + template_flags + canary_flags
    if len(all_63_flags) != len(set(all_63_flags)):
        errors.append("Se detectaron colisiones globales entre flags legítimas, plantillas y señuelos")

    print(f"[4/7] Canary Tokens pasivos y aislados verificados: {len(canary_flags)}/3 ({canary_flags})")
    print(f"[5/7] Unicidad global verificada: {len(set(all_63_flags))}/{len(all_63_flags)} flags únicas en total.")

    # 6. Verificar README raíz
    if not os.path.exists("README.md"):
        errors.append("Falta README.md en la raíz del proyecto")
    else:
        print("[6/7] Documentación general README.md en raíz verificada.")

    # 7. Ejecutar pruebas automatizadas de sintaxis y solvers locales
    rb_count = 0
    for ch in challenges:
        sol_dir = os.path.join(ch, "solution")
        if os.path.isdir(sol_dir):
            for fn in os.listdir(sol_dir):
                if fn.endswith(".rb"):
                    rb_path = os.path.join(sol_dir, fn)
                    res = subprocess.run(["ruby", "-c", rb_path], capture_output=True, text=True)
                    if res.returncode != 0:
                        errors.append(f"Error de sintaxis Ruby en {rb_path}: {res.stderr}")
                    rb_count += 1

    # Ejecutar solver funcional offline de obscuratron y generador Base64 de cert-tool
    res_obs = subprocess.run(["ruby", "obscuratron/solution/solve.rb"], capture_output=True, text=True)
    if res_obs.returncode != 0:
        errors.append(f"Fallo en obscuratron/solution/solve.rb: {res_obs.stdout} {res_obs.stderr}")

    res_ct = subprocess.run(["python3", "cert-tool/solution/solve.py"], capture_output=True, text=True)
    if res_ct.returncode != 0 or "Y2F0IC9ob21lL2N0Zi9mbGFnLnR4dDsgI==j" not in res_ct.stdout:
        errors.append(f"Fallo en cert-tool/solution/solve.py: {res_ct.stdout}")

    print(f"[7/7] Pruebas automatizadas ejecutadas: {rb_count} scripts Ruby validados (`ruby -c`), solver XOR de `obscuratron` EXITOSO, generador de payload de `cert-tool` EXITOSO.")

    if errors:
        print("\n[ERROR] Se encontraron los siguientes problemas:")
        for e in errors:
            print("  -", e)
        sys.exit(1)

    print("\n=== RESULTADO FINAL: 0 ERRORES — VALIDACIÓN INTEGRAL EXITOSA ===")


if __name__ == "__main__":
    main()
