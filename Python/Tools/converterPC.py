#!/usr/bin/env python3
"""
Expert Base Converter
Convertisseur Binaire / Décimal / Hexadécimal avec implémentation algorithmique pure.
Auteur : Philippe
"""

import re
import argparse
import sys
from enum import Enum
from dataclasses import dataclass
from typing import Union

# ==========================================
# 1. MODÉLISATION DES DONNÉES (Typage fort)
# ==========================================

class BaseSystem(Enum):
    """Représentation des systèmes de base supportés."""
    BINARY = 2
    DECIMAL = 10
    HEXADECIMAL = 16

@dataclass(frozen=True)
class ConversionResult:
    """Structure de retour immuable pour les résultats de conversion."""
    raw_input: str
    source_base: BaseSystem
    target_base: BaseSystem
    decimal_equivalent: int
    formatted_output: str

# ==========================================
# 2. MOTEUR DE CONVERSION (Algorithmique & Bitwise)
# ==========================================

class NumberConverter:
    """
    Convertisseur expert. Utilise les built-ins Python pour la vitesse,
    mais inclut des méthodes manuelles pour démontrer la logique bitwise.
    """
    
    # Patterns Regex pour une validation stricte (Fail-Fast)
    _VALIDATORS = {
        BaseSystem.BINARY: re.compile(r'^-?(?:0[bB])?[01]+$'),
        BaseSystem.DECIMAL: re.compile(r'^-?[0-9]+$'),
        BaseSystem.HEXADECIMAL: re.compile(r'^-?(?:0[xX])?[0-9a-fA-F]+$')
    }

    @classmethod
    def parse(cls, value: str, source_base: BaseSystem) -> int:
        """Parse et valide une chaîne vers un entier décimal interne."""
        value = value.strip()
        if not cls._VALIDATORS[source_base].match(value):
            raise ValueError(f"Format invalide pour la base {source_base.name}: '{value}'")
        
        is_negative = value.startswith('-')
        clean_val = value.lstrip('-')
        
        # Nettoyage des préfixes (int() lève une erreur si on précise la base avec le préfixe)
        if source_base == BaseSystem.BINARY:
            clean_val = clean_val.removeprefix('0b').removeprefix('0B')
        elif source_base == BaseSystem.HEXADECIMAL:
            clean_val = clean_val.removeprefix('0x').removeprefix('0X')
        parsed = int(clean_val, source_base.value)
        return -parsed if is_negative else parsed

    @classmethod
    def _format_builtin(cls, value: int, target_base: BaseSystem) -> str:
        """Formatage rapide via les built-ins Python."""
        if target_base == BaseSystem.BINARY:
            return bin(value)
        elif target_base == BaseSystem.HEXADECIMAL:
            # On met en majuscules pour le standard hexadécimal
            return hex(value).replace('0x', '0X').replace('-0x', '-0X')
        return str(value)

    @classmethod
    def _format_bitwise(cls, value: int, target_base: BaseSystem) -> str:
        """
        [NIVEAU EXPERT] Formatage manuel via opérations bit à bit.
        Montre comment le processeur manipule les bits (masquage et décalage).
        """
        if value == 0:
            return "0b0" if target_base == BaseSystem.BINARY else "0x0"
        is_negative = value < 0
        n = abs(value)
        digits = []
        
        if target_base == BaseSystem.BINARY:
            while n > 0:
                digits.append(str(n & 1))  # Masque 1 bit (AND)
                n >>= 1                    # Décalage à droite de 1 bit
            prefix = "0b"
        else: # HEXADECIMAL
            hex_chars = "0123456789ABCDEF"
            while n > 0:
                digits.append(hex_chars[n & 0xF]) # Masque 4 bits (0xF = 15)
                n >>= 4                           # Décalage à droite de 4 bits
            prefix = "0X"
        result = prefix + ''.join(reversed(digits))
        return f"-{result}" if is_negative else result

    @classmethod
    def convert(cls, value: str, source_base: BaseSystem, target_base: BaseSystem, use_bitwise: bool = False) -> ConversionResult:
        """Méthode publique principale pour convertir une valeur."""
        decimal_val = cls.parse(value, source_base)
        
        if use_bitwise and target_base != BaseSystem.DECIMAL:
            formatted = cls._format_bitwise(decimal_val, target_base)
        else:
            formatted = cls._format_builtin(decimal_val, target_base)
            
        return ConversionResult(
            raw_input=value,
            source_base=source_base,
            target_base=target_base,
            decimal_equivalent=decimal_val,
            formatted_output=formatted
        )

# ==========================================
# 3. INTERFACE EN LIGNE DE COMMANDE (CLI)
# ==========================================

def build_cli() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convertisseur de bases expert (Binaire, Décimal, Hexadécimal)",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    # Arguments mutuellement exclusifs pour la source
    source_group = parser.add_mutually_exclusive_group(required=True)
    source_group.add_argument('-b', '--bin', type=str, help="Valeur binaire (ex: 1010 ou 0b1010)")
    source_group.add_argument('-d', '--dec', type=str, help="Valeur décimale (ex: 42)")
    source_group.add_argument('-x', '--hex', type=str, help="Valeur hexadécimale (ex: 2A ou 0x2A)")
    
    # Cible
    parser.add_argument('-t', '--to', type=str, required=True, choices=['bin', 'dec', 'hex'],
    help="Base de destination (bin, dec, hex)")
    
    # Option expert
    parser.add_argument('--bitwise', action='store_true', 
    help="Utilise l'algorithme bit à bit manuel au lieu des built-ins Python")
    
    return parser

def main():
    parser = build_cli()
    args = parser.parse_args()
    
    # Mapping des arguments
    base_map = {'bin': BaseSystem.BINARY, 'dec': BaseSystem.DECIMAL, 'hex': BaseSystem.HEXADECIMAL}
    
    if args.bin:
        val, src = args.bin, BaseSystem.BINARY
    elif args.dec:
        val, src = args.dec, BaseSystem.DECIMAL
    else:
        val, src = args.hex, BaseSystem.HEXADECIMAL
        
    target = base_map[args.to]
    
    try:
        result = NumberConverter.convert(val, src, target, use_bitwise=args.bitwise)
        
        # Affichage formaté (style Obsidian / Terminal)
        print("\n" + "="*40)
        print(f" 🔄 CONVERSION RÉUSSIE")
        print("="*40)
        print(f" Entrée ({result.source_base.name:<11}) : {result.raw_input}")
        print(f" Sortie ({result.target_base.name:<11}) : {result.formatted_output}")
        print(f" Équivalent Décimal     : {result.decimal_equivalent}")
        print("="*40 + "\n")
        
    except ValueError as e:
        print(f"\n❌ Erreur de validation : {e}\n", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
