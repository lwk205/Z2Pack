"""Utilities to be used with quantum espresso calculations."""

import xml.etree.ElementTree as ET
import numpy as np
import scipy.linalg as la
from fsc.export import export

from ._general import to_reciprocal, find_local, round_to_zero
from ..shape import Plane


@export
def suggest_symmetry_surfaces(xml_path):
    """
    Returns a list of tuples (plane, symmetry) of planes and corresponding symmetry
    operations which leave each k-point on the plane invariant.

    Arguments
    ---------
    xml_path : str
        Path (absolute or relative to working directory) to the seendname.xml file produced by the SCF calculation.
    """
    surfaces = []
    symms = _symm_from_scf(xml_path)
    for symm in symms:
        if np.allclose(symm, np.eye(3)):
            continue
        ew, ev = la.eig(symm)
        ind = np.where(np.isclose(ew, -1))[0]
        # check that this is a simple reflection
        if np.isclose(ew, 1).any() and len(ind) == 1:
            v = ev[:, ind[0]]
            if np.isclose(np.angle(v) % np.pi, np.angle(v[0]) % np.pi).all():
                v = np.real(v / np.exp(1j * np.angle(v[0])))
                # construct orthogonal vectors
                i_max = np.argmax(v)
                v_orth = np.eye(3)[np.where(
                    np.logical_not(np.isclose([0, 1, 2], np.argmax(v)))
                )[0]]
                v_orth = [
                    vo - np.dot(vo, v) / v[i_max] * np.eye(3)[i_max]
                    for vo in v_orth
                ]
                # create surface
                surfaces.append((
                    Plane(
                        origin=np.array([0, 0, 0]),
                        spanning_vectors=v_orth,
                    ), symm
                ))
    return surfaces


@export
def generate_qe_sym_file(surface, xml_path, output_path):
    """
    Generates a .sym file to be used as input for the first-principles calculation
    for a given surface and QE SCF output.

    Arguments
    ---------
    surface : Callable
        Surface function (same format as for surface_run) for which local symmetries should be selected.
    xml_path : str
        Absolute or relative path to the seedname.xml file generated by the scf calculation.
    output_path : str
        Absolute or relative path to the output .sym file.
    """
    # get symmetries from scf file
    symms = _symm_from_scf(
        xml_path
    )  # this reads the symmetry matrices in the reduced basis
    symms = find_local(symms, surface)  # this selects the local symmetries
    # The .sym file has to be in cartesian coordinates
    basis_transform = _reduced_from_wannier(xml_path)
    symms_cart = []
    for s in symms:
        symms_cart.append(
            basis_transform.dot(s).dot(np.linalg.inv(basis_transform))
        )  # transform to cartesian basis
    _generate_pw_symm_file(symms_cart, output_path)


def _reduced_from_wannier(xml_path):
    """
    Get the basis transformation matrix from the reduced reciprocal space to cartesian basis from xml file
    """
    real_space = []
    cell = ET.parse(xml_path).find('output').find('atomic_structure'
                                                  ).find('cell')
    for vec in cell:
        real_space.append(np.fromstring(vec.text, sep=' '))
    return np.array(to_reciprocal(real_space)).T


def _symm_from_scf(xml_path):
    """
    Read symmetries from scf xml output file at xml path
    """
    tree = ET.parse(xml_path)
    symm_xml = tree.find('output').find('symmetries').findall('symmetry')
    symmetries = []
    for symm in symm_xml:
        s = np.fromstring(symm.find('rotation').text, sep=' ')
        n = int(round(np.sqrt(len(s))))

        if np.abs(np.sqrt(len(s)) - n) > 0.001:
            raise ValueError('Symmetry matrix not square')
        symmetries.append(s.reshape((n, n)))  # pylint: disable=too-many-function-args,useless-suppression
    return symmetries


def _generate_pw_symm_file(symmetries, output_path):
    """
    Write .sym file for use in pw2wannier90
    symmetries: matrix of real space symmetry matrices in cartesian basis
    output_path: Path to the file to which the local symmetries are written. The filename has to "seedname".sym.
    """

    with open(output_path, 'w') as f:
        f.write(str(len(symmetries)) + '\n')
        for symm in symmetries:
            symm = round_to_zero(symm)
            symm = np.vstack((symm, [0 for i in range(len(symm[0]))]))
            f.write('\n')
            f.write(
                '\n'.join(
                    map(lambda x: ' '.join(map('{:E}'.format, x)), symm)
                )
            )
            f.write('\n')
        f.close()