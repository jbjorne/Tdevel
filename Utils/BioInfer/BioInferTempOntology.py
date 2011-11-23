g_Ontology = None

def addOscEdge(parent, child):
    global g_Ontology
    assert not child in g_Ontology
    g_Ontology[child] = parent

def getBioInferTempOntology():
    global g_Ontology
    if g_Ontology == None:
        initOntology()
    return g_Ontology

def initOntology():
    global g_Ontology
    g_Ontology = {}
    
    addOscEdge('universal','Relationship')
    addOscEdge('universal','Physical_entity')
    addOscEdge('universal','Property_entity')
    
    addOscEdge('Addition','ACETYLATE')
    addOscEdge('Addition','ADD')
    addOscEdge('Addition','PHOSPHORYLATE')
    addOscEdge('Amino_acid','Amino_acid_monomer')
    addOscEdge('Amino_acid','Peptide')
    addOscEdge('Amino_acid','Protein')
    addOscEdge('Amount','DECREASE')
    addOscEdge('Amount','INCREASE')
    addOscEdge('Artificial','Cell_line')
    addOscEdge('Artificial','Other_artificial_source')
    addOscEdge('Assembly','ASSEMBLE')
    addOscEdge('Assembly','ATTACH')
    addOscEdge('Assembly','BIND')
    addOscEdge('Assembly','CROSS-LINK')
    addOscEdge('Assembly','CROSS-LINK-AP')
    addOscEdge('Assembly','POLYMERIZE')
    addOscEdge('Break-Down','CLEAVE')
    addOscEdge('Break-Down','DEPOLYMERIZE')
    addOscEdge('Break-Down','DISASSEMBLE')
    addOscEdge('Break-Down','DISRUPT')
    addOscEdge('Break-Down','UNBIND')
    addOscEdge('Causal','CAUSE')
    addOscEdge('Causal','Change')
    addOscEdge('Causal','Condition')
    addOscEdge('Causal','PARTICIPATE')
    addOscEdge('Causal','XOR')
    addOscEdge('Change','AFFECT')
    addOscEdge('Change','Amount')
    addOscEdge('Change','Dynamics')
    addOscEdge('Change','INTERACT')
    addOscEdge('Change','Location')
    addOscEdge('Change','MUTUAL-AFFECT')
    addOscEdge('Change','Physical')
    addOscEdge('Collection:Member','MEMBER')
    addOscEdge('Compound','Carbohydrate')
    addOscEdge('Compound','Inorganic')
    addOscEdge('Compound','Organic')
    addOscEdge('Condition','CONDITION')
    addOscEdge('Condition','MUTUALCONDITION')
    addOscEdge('Condition','PREVENT')
    addOscEdge('DNA','DNA_family_or_group')
    addOscEdge('DNA','Domain_or_region_of_DNA')
    addOscEdge('DNA','Individual_DNA_molecule')
    addOscEdge('Domain_or_region_of_DNA','Gene')
    addOscEdge('Dynamics','Full-Stop')
    addOscEdge('Dynamics','Negative')
    addOscEdge('Dynamics','Positive')
    addOscEdge('Dynamics_property','Activity')
    addOscEdge('Dynamics_property','Expression')
    addOscEdge('Dynamics','Start')
    addOscEdge('Dynamics','Unspecified')
    addOscEdge('Equality','COREFER')
    addOscEdge('Equality','ENCODE')
    addOscEdge('Equality','EQUAL')
    addOscEdge('Full-Stop','HALT')
    addOscEdge('Full-Stop','INACTIVATE')
    addOscEdge('Functional-Similarity','FNSIMILAR')
    addOscEdge('Function_property','Function')
    addOscEdge('Function_property','Signal')
    addOscEdge('Individual_protein','Antibody')
    addOscEdge('Individual_protein','Fusion_protein')
    addOscEdge('Individual_protein','Protein_complex')
    addOscEdge('IS_A','Equality')
    addOscEdge('IS_A','Similarity')
    addOscEdge('Lipid','Steroid')
    addOscEdge('Location','LOCALIZE')
    addOscEdge('Location','LOCALIZE-TO')
    addOscEdge('Modification','Addition')
    addOscEdge('Modification','MODIFY')
    addOscEdge('Modification','Removal')
    addOscEdge('Natural','Body_part')
    addOscEdge('Natural','Cell_component')
    addOscEdge('Natural','Cell_type')
    addOscEdge('Natural','Organism')
    addOscEdge('Natural','Other_natural_source')
    addOscEdge('Natural','Tissue')
    addOscEdge('Negative','DOWNREGULATE')
    addOscEdge('Negative','INHIBIT')
    addOscEdge('Negative','SUPPRESS')
    addOscEdge('Nucleic_acid','DNA')
    addOscEdge('Nucleic_acid','Nucleotide')
    addOscEdge('Nucleic_acid','Polynucleotide')
    addOscEdge('Nucleic_acid','RNA')
    addOscEdge('Object:Component','CONTAIN')
    addOscEdge('Object:Component','F-CONTAIN')
    addOscEdge('Object:Component','MUTUALCOMPLEX')
    addOscEdge('Object:Component','SUBSTRUCTURE')
    addOscEdge('Observation','COREGULATE')
    addOscEdge('Observation','CORELATE')
    addOscEdge('Observation','Spatial')
    addOscEdge('Observation','Temporal')
    addOscEdge('Organic','Amino_acid')
    addOscEdge('Organic','Gene/protein/RNA')
    addOscEdge('Organic','Lipid')
    addOscEdge('Organic','Nucleic_acid')
    addOscEdge('Organic','Other_organic_compounds')
    addOscEdge('Organism','Mono-cell_organism')
    addOscEdge('Organism','Multi-cell_organism')
    addOscEdge('Organism','Virus')
    addOscEdge('PART_OF','Collection:Member')
    addOscEdge('PART_OF','Object:Component')
    addOscEdge('Physical','Assembly')
    addOscEdge('Physical','Break-Down')
    addOscEdge('Physical_entity','Analog')
    addOscEdge('Physical_entity','Homolog')
    addOscEdge('Physical_entity','Mutant')
    addOscEdge('Physical_entity','Other')
    addOscEdge('Physical_entity','Source')
    addOscEdge('Physical_entity','Substance')
    addOscEdge('Physical','Modification')
    addOscEdge('Physical-Similarity','SQSIMILAR')
    addOscEdge('Physical-Similarity','STSIMILAR')
    addOscEdge('Positive','ACTIVATE')
    addOscEdge('Positive','CATALYZE')
    addOscEdge('Positive','MEDIATE')
    addOscEdge('Positive','STIMULATE')
    addOscEdge('Positive','UPREGULATE')
    addOscEdge('Property_entity','Amount_property')
    addOscEdge('Property_entity','Dynamics_property')
    addOscEdge('Property_entity','Function_property')
    addOscEdge('Property_entity','Location_property')
    addOscEdge('Property_entity','Physical_property')
    addOscEdge('Protein','Individual_protein')
    addOscEdge('Protein','Protein_family_or_group')
    addOscEdge('Protein','Substructure_of_protein')
    addOscEdge('Relationship','Causal')
    addOscEdge('Relationship','HUMANMADE')
    addOscEdge('Relationship','IS_A')
    addOscEdge('Relationship','NOT')
    addOscEdge('Relationship','Observation')
    addOscEdge('Relationship','PART_OF')
    addOscEdge('Relationship','RELATE')
    addOscEdge('Relationship','REL-ENT')
    addOscEdge('Removal','DEPHOSPHORYLATE')
    addOscEdge('Removal','REMOVE')
    addOscEdge('RNA','Domain_or_region_of_RNA')
    addOscEdge('RNA','Individual_RNA_molecule')
    addOscEdge('RNA','RNA_family_or_group')
    addOscEdge('Similarity','Functional-Similarity')
    addOscEdge('Similarity','Physical-Similarity')
    addOscEdge('Similarity','SIMILAR')
    addOscEdge('Source','Artificial')
    addOscEdge('Source','Natural')
    addOscEdge('Spatial','ABSENCE')
    addOscEdge('Spatial','COLOCALIZE')
    addOscEdge('Spatial','COPRECIPITATE')
    addOscEdge('Spatial','PRESENCE')
    addOscEdge('Start','INITIATE')
    addOscEdge('Substance','Atom')
    addOscEdge('Substance','Compound')
    addOscEdge('Temporal','COEXPRESS')
    addOscEdge('Temporal','COOCCUR')
    addOscEdge('Unspecified','CONTROL')
    addOscEdge('Unspecified','MODULATE')
    addOscEdge('Unspecified','REGULATE')