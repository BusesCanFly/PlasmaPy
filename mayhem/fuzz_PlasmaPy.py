#! /usr/bin/python3

import atheris
import sys

with atheris.instrument_imports():
    from plasmapy.particles.exceptions import *
    from plasmapy.particles import *
    from plasmapy.particles.particle_class import valid_categories


@atheris.instrument_func
def test_input(input_bytes):
    fdp = atheris.FuzzedDataProvider(input_bytes)
    input_string = fdp.ConsumeUnicodeNoSurrogates(sys.maxsize)
    # input_str_w_surrogates = fdp.ConsumeUnicode(sys.maxsize)
    input_int = fdp.ConsumeInt(sys.maxsize)
    
    try:
        atomic_number(input_string)
        element_name(input_int)
        particle_mass(input_string)
    except ParticleError:
        pass
    except AttributeError:
        pass

def main():
    atheris.Setup(sys.argv, test_input)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
