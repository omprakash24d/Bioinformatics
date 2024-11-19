import math
import csv
import Bio.PDB

def degrees(rad_angle):
    """Converts any angle in radians to degrees.

    If the input is None, it returns None.
    For numerical input, the output is mapped to [-180,180].
    """
    if rad_angle is None:
        return None
    angle = rad_angle * 180 / math.pi
    while angle > 180:
        angle -= 360
    while angle < -180:
        angle += 360
    return angle


pdb_code = "3gou"

print("About to load Bio.PDB and the PDB file...")
structure = Bio.PDB.PDBParser().get_structure(pdb_code, f"{pdb_code}.pdb")
print("Done")

print("About to save angles to file...")
with open(f"{pdb_code}_biopython.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Write the header row
    csvwriter.writerow(["PDB Code", "Chain ID", "Residue", "Residue ID", "Phi (°)", "Psi (°)"])
    
    # Iterate through the structure
    for model in structure:
        for chain in model:
            print(f"Chain {str(chain.id)}")
            polypeptides = Bio.PDB.CaPPBuilder().build_peptides(chain)
            for poly_index, poly in enumerate(polypeptides):
                phi_psi = poly.get_phi_psi_list()
                for res_index, residue in enumerate(poly):
                    next_residue = poly[res_index + 1] if res_index + 1 < len(poly) else None
                    phi, psi = phi_psi[res_index]
                    if phi and psi:
                        # Write the data row
                        csvwriter.writerow([
                            pdb_code,
                            chain.id,
                            residue.resname,
                            residue.id[1],
                            degrees(phi),
                            degrees(psi),
                            
                        ])
print("Done")
