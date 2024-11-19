from Bio.PDB import PDBParser, calc_dihedral
import math

# Function to calculate phi and psi angles from a PDB file
def calculate_phi_psi(pdb_file):
    # Load the PDB structure
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure('protein', pdb_file)
    
    # List to store the phi and psi angles for each residue
    angles = []

    # Loop through each model, chain, and residue
    for model in structure:
        for chain in model:
            # Get the list of residues in this chain
            residues = list(chain)
            n_residues = len(residues)

            # Loop through each residue
            for i, residue in enumerate(residues):
                # Skip non-standard residues or those missing atoms
                if residue.id[0] != " ":
                    continue

                try:
                    # Get backbone atoms for the current residue
                    n_atom = residue['N']
                    ca_atom = residue['CA']
                    c_atom = residue['C']
                except KeyError:
                    # Skip if any backbone atom is missing
                    continue

                # Calculate phi angle (using previous residue’s C atom)
                phi = None  # Default to None if phi cannot be calculated
                if i > 0:  # Ensure there’s a previous residue
                    prev_residue = residues[i - 1]
                    try:
                        prev_c_atom = prev_residue['C']
                        phi = math.degrees(calc_dihedral(
                            prev_c_atom.get_vector(),
                            n_atom.get_vector(),
                            ca_atom.get_vector(),
                            c_atom.get_vector()
                        ))
                    except KeyError:
                        pass  # Skip if previous residue’s C atom is missing

                # Calculate psi angle (using next residue’s N atom)
                psi = None  # Default to None if psi cannot be calculated
                if i < (n_residues - 1):  # Ensure there’s a next residue
                    next_residue = residues[i + 1]
                    try:
                        next_n_atom = next_residue['N']
                        psi = math.degrees(calc_dihedral(
                            n_atom.get_vector(),
                            ca_atom.get_vector(),
                            c_atom.get_vector(),
                            next_n_atom.get_vector()
                        ))
                    except KeyError:
                        pass  # Skip if next residue’s N atom is missing

                # Save the angles for this residue
                angles.append({
                    'Residue': f"{residue.resname} {residue.id[1]}",
                    'Phi': phi,
                    'Psi': psi
                })

    return angles

# Run the function on a PDB file
pdb_file = "P:\Linux&Python\Maths\3gou.pdb"  # Replace with the path to your PDB file
phi_psi_angles = calculate_phi_psi(pdb_file)

# Print the results for each residue
for angle in phi_psi_angles:
    print(f"Residue: {angle['Residue']}, Phi: {angle['Phi']}, Psi: {angle['Psi']}")
