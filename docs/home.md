                              _____________________.___.____    .____     
                              \__    ___/\______   \   |    |   |    |    
                                |    |    |       _/   |    |   |    |    
                                |    |    |    |   \   |    |___|    |___ 
                                |____|    |____|_  /___|_______ \_______ \
                                                 \/            \/       \/

[![version](https://img.shields.io/pypi/v/trill-proteins?color=blueviolet&style=flat-square)](https://pypi.org/project/trill-proteins)
![Downloads](https://pepy.tech/badge/trill-proteins)
[![license](https://img.shields.io/pypi/l/trill-proteins?color=blueviolet&style=flat-square)](LICENSE)
[![Documentation Status](https://readthedocs.org/projects/trill/badge/?version=latest&style=flat-square)](https://trill.readthedocs.io/en/latest/?badge=latest)
<!-- ![status](https://github.com/martinez-zacharya/TRILL/workflows/CI/badge.svg?style=flat-square&color=blueviolet) -->
# Intro
TRILL (**TR**aining and **I**nference using the **L**anguage of **L**ife) is a sandbox for creative protein engineering and discovery. As a bioengineer myself, deep-learning based approaches for protein design and analysis are of great interest to me. However, many of these deep-learning models are rather unwieldy, especially for non ML-practitioners due to their sheer size. Not only does TRILL allow researchers to perform inference on their proteins of interest using a variety of models, but it also democratizes the efficient fine-tuning of large-language models. Whether using Google Colab with one GPU or a supercomputer with many, TRILL empowers scientists to leverage models with millions to billions of parameters without worrying (too much) about hardware constraints. Currently, TRILL supports using these models as of v1.9.0:

## Breakdown of TRILL's Commands

| **Command** | **Function** | **Available Models** |
|:-----------:|:------------:|:--------------------:|
| **Embed** | Generates numerical representations or "embeddings" of biological sequences for quantitative analysis and comparison. Can be Small-Molecule SMILES/RNA/DNA/Proteins dpending on the model. | [ESM2](https://doi.org/10.1101/2022.07.20.500902), [MMELLON](https://doi.org/10.48550/arXiv.2410.19704), [MolT5](https://doi.org/10.48550/arXiv.2204.11817), [ProtT5-XL](https://doi.org/10.1109/TPAMI.2021.3095381), [ProstT5](https://doi.org/10.1101/2023.07.23.550085), [Ankh](https://doi.org/10.48550/arXiv.2301.06568), [CaLM](https://doi.org/10.1038/s42256-024-00791-0), [mRNA-FM/RNA-FM](https://doi.org/10.48550/arXiv.2204.00300), [SaProt](https://doi.org/10.1101/2023.10.01.560349), [SELFIES-TED](https://openreview.net/forum?id=uPj9oBH80V), [SMI-TED](https://doi.org/10.48550/arXiv.2407.20267)|
| **Visualize** | Creates interactive 2D visualizations of embeddings for exploratory data analysis. | PCA, t-SNE, UMAP |
| **Finetune** | Finetunes protein language models for specific tasks. | [ESM2](https://doi.org/10.1101/2022.07.20.500902), [ProtGPT2](https://doi.org/10.1038/s41467-022-32007-7), [ZymCTRL](https://www.mlsb.io/papers_2022/ZymCTRL_a_conditional_language_model_for_the_controllable_generation_of_artificial_enzymes.pdf), [ProGen2](https://doi.org/10.1016/j.cels.2023.10.002)|
| **Language Model Protein Generation** | Generates proteins using pretrained language models. | [ESM2](https://doi.org/10.1101/2022.07.20.500902), [ProtGPT2](https://doi.org/10.1038/s41467-022-32007-7), [ZymCTRL](https://www.mlsb.io/papers_2022/ZymCTRL_a_conditional_language_model_for_the_controllable_generation_of_artificial_enzymes.pdf), [ProGen2](https://doi.org/10.1016/j.cels.2023.10.002)|
| **Inverse Folding Protein Generation** | Designs proteins to fold into specific 3D structures. | [ESM-IF1](https://doi.org/10.1101/2022.04.10.487779), [LigandMPNN](https://doi.org/10.1101/2023.12.22.573103), [ProstT5](https://doi.org/10.1101/2023.07.23.550085) |
| **Diffusion Based Protein Generation** | Uses denoising diffusion models to generate proteins. | [Genie2](https://doi.org/10.48550/arXiv.2405.15489), [RFDiffusion](https://doi.org/10.1101/2022.12.09.519842) |
| **Fold** | Predicts 3D protein structures. | [ESMFold](https://doi.org/10.1101/2022.07.20.500902), [ProstT5](https://doi.org/10.1101/2023.07.23.550085), [Chai-1](https://doi.org/10.1101/2024.10.10.615955), [Boltz-2](https://doi.org/10.1101/2025.06.14.659707) |
| **Dock** | Simulates protein-ligand interactions. | [DiffDock-L](https://doi.org/10.48550/arXiv.2210.01776), [Smina](https://doi.org/10.1021/ci300604z), [Autodock Vina](https://doi.org/10.1021/acs.jcim.1c00203), [Gnina](https://doi.org/10.1186/s13321-025-00973-x), [Lightdock](https://doi.org/10.1093/bioinformatics/btx555), [GeoDock](https://doi.org/10.1101/2023.06.29.547134) |
| **Classify** | Predicts properties with pretrained models or train custom classifiers | [CataPro](https://doi.org/10.1038/s41467-025-58038-4), [CatPred](https://doi.org/10.1038/s41467-025-57215-9), [M-Ionic](https://doi.org/10.1093/bioinformatics/btad782), [PSICHIC](https://doi.org/10.1038/s42256-024-00847-1), [PSALM](https://doi.org/10.1101/2024.06.04.596712), [TemStaPro](https://doi.org/10.1101/2023.03.27.534365), [EpHod](https://doi.org/10.1101/2023.06.22.544776), [ECPICK](https://doi.org/10.1093/bib/bbad401), [LightGBM](https://papers.nips.cc/paper_files/paper/2017/hash/6449f44a102fde848669bdd9eb6b76fa-Abstract.html), [XGBoost](https://doi.org/10.48550/arXiv.1603.02754), [Isolation Forest](https://doi.org/10.1109/ICDM.2008.17) [End-to-End Finetuning of ESM2 with a Multilayer perceptron head](https://huggingface.co/docs/transformers/en/model_doc/esm#transformers.EsmForSequenceClassification)|
| **Regress** | Train custom regression models. | [LightGBM](https://papers.nips.cc/paper_files/paper/2017/hash/6449f44a102fde848669bdd9eb6b76fa-Abstract.html), [Linear](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)|
| **Simulate** | Uses molecular dynamics to simulate biomolecular interactions followed by automated scoring | [OpenMM](https://doi.org/10.1371/journal.pcbi.1005659), [MMGBSA](https://doi.org/10.1021/acs.chemrev.9b00055), [ProLIF](https://doi.org/10.1186/s13321-021-00548-6) |
| **Score** | Utilize ESM1v or ESM2 to score protein sequences or ProteinMPNN/LigandMPNN/[SCASA](https://github.com/t-whalley/SCASA) to score protein structures/complexes in a zero-shot manner. | [COMPSS](https://www.nature.com/articles/s41587-024-02214-2#change-history), [SC](https://doi.org/10.1006/jmbi.1993.1648) |
| **Workflow** | Automated protein design workflows. | [Foldtuning](https://doi.org/10.1101/2023.12.22.573145)  |


## Set-Up
1. TRILL has only ever been tested on Linux machines, but it might work on Windows with WSL2. You can use TRILL with Google Colab by using the installation instructions from [this notebook](https://colab.research.google.com/drive/1eFJVh4tN3G2mz6w-G5hNUS6jb7JKMiQb?usp=sharing). For regular installations, I recommend using micromamba or mamba. If you don't have mamba installed, use this command
```shell
curl -fsSL https://pixi.sh/install.sh | sh

echo 'export PATH="$HOME/.pixi/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pixi completion --shell bash)"' >> ~/.bashrc

```
2. Once pixi environment is set up
```shell
cd trill
pixi run trill --help
```

## Use

```shell
usage: pixi run trill [-h] [--nodes NODES] [--logger LOGGER] [--profiler] [--RNG_seed RNG_SEED]
             [--outdir OUTDIR] [--n_workers N_WORKERS]
             name GPUs
             {classify,inv_fold_gen,dock,score,visualize,workflow,regress,embed,utils,lang_gen,fold,diff_gen,finetune,simulate}
             ...

positional arguments:
  name                  Name of run
  GPUs                  Input total number of GPUs per node
  {classify,inv_fold_gen,dock,score,visualize,workflow,regress,embed,utils,lang_gen,fold,diff_gen,finetune,simulate}
    classify            Classify proteins using either pretrained classifiers or train/test
                        your own.
    inv_fold_gen        Generate proteins using inverse folding
    dock                Perform molecular docking with proteins and ligands. Note that you
                        should relax your protein receptor with Simulate or another method
                        before docking.
    score               Use ESM-1v or ESM2 to score protein sequences, ProteinMPNN to score
                        protein structures and SC for protein complexes
    visualize           Reduce dimensionality of embeddings to 2D
    workflow            Perform workflow of interest
    regress             Train you own regressors on input protein sequences and some sort
                        of score.
    embed               Embed sequences/SMILES of interest
    utils               Misc utilities
    lang_gen            Generate proteins using large language models
    fold                Predict monomeric 3D protein structures using ESMFold, protein
                        complexes with ligands using Boltz-2/Chai-1, and obtain 3Di
                        structure for use with Foldseek to perform remote homology
                        detection
    diff_gen            Generate proteins using Denoising Diffusion models
    finetune            Finetune protein language models
    simulate            Use OpenMM to perform molecular dynamics

options:
  -h, --help            show this help message and exit
  --nodes NODES         Input total number of nodes. Default is 1
  --logger LOGGER       Enable Tensorboard logger. Default is None
  --profiler            Utilize PyTorchProfiler
  --RNG_seed RNG_SEED   Input RNG seed. Default is 123
  --outdir OUTDIR       Input full path to directory where you want the output from TRILL
  --n_workers N_WORKERS
                        Change number of CPU cores/'workers' TRILL uses


```


## Examples

In the examples below the string immediately after `trill` specifies the name of the run. This name will be preprended to all outputs. For example, `trill example` will prepend `example` to the filenames that are generated by the run. The second argument specifies the number of GPUs to use in the run. If you don't have access to GPUs, you can simply put 0 to run TRILL on the CPU only.

### 1. Finetune Protein Language Models
  The default mode for TRILL is to just fine-tune the selected model with the query input for 10 epochs with a learning rate of 0.0001.
  ```
  trill  1 finetune esm2_t12_35M trill/data/query.fasta
  ```
  By specifying --strategy, you can efficiently train large language models that would not normally be supported by your hardware. For example, if you run out of CUDA memory, you can try using Deepspeed or other strategies found [here](https://pytorch-lightning.readthedocs.io/en/stable/extensions/strategy.html). 
  ```
  trill  1 finetune esm2_t36_3B trill/data/query.fasta --strategy deepspeed_stage_2
  ```
  You can finetune ProtGPT2.
  ```
  trill  1 finetune ProtGPT2 trill/data/query.fasta
  ```
  You can also finetune ZymCTRL on certain a certain EC. Note that you must specify a EC tag that corresponds to ALL of the input proteins.
  ```
  trill  1 finetune ZymCTRL trill/data/query.fasta --ctrl_tag 1.2.3.4
  ```
### 2. Create embeddings
  Use the embed command to create high-dimensional representations of your proteins of interest. --avg returns the averaged, whole sequence embeddings, while --per_AA returns the per amino acid representation for each AA in each sequence.
  ```
  trill  1 embed esm2_t12_35M trill/data/query.fasta --avg --per_AA
  ```  
  If you wanted to change the batch_size and use a finetuned ESM2 model for embeddings, you can specify it with --batch_size and --finetuned respectively. Also note that you can opt to only return one type of representation.
  ```
  trill  1 embed esm2_t33_650M trill/data/query.fasta --batch_size 2 --finetuned /path/to/models/finetuned_esm2_t30_150M_UR50D.pt --avg
  ```
  For ESM2 exclusively for now, you can also pass '--poolparti' to also extract the [Pool PaRTI](https://doi.org/10.1101/2024.10.04.616701) representations.
  ```
  trill  1 embed esm2_t12_35M trill/data/query.fasta --poolparti
  ```
  In order to embed small-molecule SMILES, you first need to create a .smiles file that has the SMILES strings in fasta format. This means that headers start with ">" and every subsequent line until the next ">" is considered part of the prior sequence. Currently, only MolT5 models in TRILL allow for per-token embeddings, the rest are only the averaged, fixed-length vectors. 
  ```
  trill  1 embed SMI-TED trill/data/query.smiles --avg
  ```
### 3. Distributed Training/Inference
  In order to scale/speed up your analyses, you can distribute your training/inference across many GPUs with a few extra flags to your command. You can even fit models that do not normally fit on your GPUs with sharding, CPU-offloading etc. Below is an example slurm batch submission file. The list of strategies can be found here (https://pytorch-lightning.readthedocs.io/en/stable/extensions/strategy.html). The example below utilizes 16 GPUs in total (4(GPUs) * 4(--nodes)) with deepspeed_stage_2_offload and the 650M parameter ESM2 model.
  ```shell
  #!/bin/bash
  #SBATCH --time=8:00:00   # walltime
  #SBATCH --ntasks-per-node=4
  #SBATCH --nodes=4 # number of nodes
  #SBATCH --gres=gpu:4 # number of GPUs
  #SBATCH --mem-per-cpu=60G   # memory per CPU core
  #SBATCH -J "tutorial"   # job name
  #SBATCH --mail-user="" # change to your email
  #SBATCH --mail-type=BEGIN
  #SBATCH --mail-type=END
  #SBATCH --mail-type=FAIL
  #SBATCH --output=%x-%j.out
  master_addr=$(scontrol show hostnames "$SLURM_JOB_NODELIST" | head -n 1)
  export MASTER_ADDR=$master_addr
  export MASTER_PORT=13579
  
  srun trill  4 finetune esm2_t33_650M trill/data/query.fasta --nodes 4 --strategy deepspeed_stage_3_offload
  ```
  You can then submit this job with:
  ```
  sbatch distributed_example.slurm
  ```

### 4. Language Model Protein Generation
  You can use pretrained or finetuned protein language models to generate synthetic proteins with various hyperparameters.
  ProtGPT2: The command below generates 5 proteins. The default seed sequence is "M", but you can also change this. Check out the command-line arguments for more details.
  ```
  trill  1 lang_gen ProtGPT2 --num_return_sequences 5
  ```
  In case you wanted to generate certain "types" of proteins with ProtGPT2, below is an example of using a fine-tuned ProtGPT2 to generate proteins.
  ```
  trill  1 lang_gen ProtGPT2 --finetuned /path/to/FineTune_ProtGPT2_100.pt
  ```
  ESM2 Gibbs: Using Gibbs sampling, you can generate synthetic proteins from a finetuned ESM2 model. Note you must specify the ESM2 model architecture when doing gibbs sampling.
  ```
  trill  0 lang_gen ESM2 --finetuned /path/to/finetuned_model.pt --esm2_arch esm2_t30_150M_UR50D --num_return_sequences 5
  ```
  ZymCTRL: By specifying an EC tag, you can control the type of enzyme the model tries to generate. If it is a class of enzymes that was not well represented in the ZymCTRL training set, you can first finetune it and then proceed to generate bespoke enzymes by passing the finetuned model with --finetuned.
  ```
  trill  1 lang_gen ZymCTRL --num_return_sequences 5 --ctrl_tag 3.1.1.101
  ```
### 5. Inverse Folding Protein Generation
  ESM-IF1: When provided a protein structure the IF1 model is able to predict a sequence that might be able to fold into the input structure backbone. The example input are the backbone coordinates from DWARF14, a rice hydrolase. For every chain in the structure, 2 in 4ih9.pdb, the following command will generate 3 sequences. In total, 6 sequences will be generated.
  ```
  trill  1 inv_fold_gen ESM-IF1 trill/data/4ih9.pdb --num_return_sequences 3
  ```
  LigandMPNN: You can specify the max length you want your protein to be with --max_length. Note that max_length must be at least as long as the input structure. The .pdb input file can have a ligand, whether it be a small-molecule, protein or nucleic acid. The output will be sequences that are likely to fold with the same backbone as the input, as well as interface with the same ligands.
  ```
  trill  1 inv_fold_gen LigandMPNN 7t0r --max_length 1000 --num_return_sequences 5
  ```
  ProstT5: This bilingual protein language model is technically able to perform inverse folding. First, TRILL uses foldseek to extract 3Di tokens from the .pdb, and then ProstT5 translates the tokens into potential sequences. With this model, you can set hyperparameters such as --top_p in order to perform nucleus sampling and only the smallest set of most probable tokens with probabilities that add up to top_p or higher are kept for generation.
  ```
  trill  1 inv_fold_gen ProstT5 trill/data/4ih9.pdb --max_length 1000 --num_return_sequences 5 --top_p 0.9
  ```
### 6. Diffusion based Protein Generation
  RFDiffusion: You can perform a variety of protein design tasks, including designing binders! In the example below, you specify the target structure with --query, which in this case is an insulin receptor. The --contigs specify that we want residues 1-150 from chain A of the target structure, a chain break with /0 and a binder between 70-100 residues. We also specify residue hotspots, where we can tell the model to specifically target certain residues. Note that TRILL's implimentation of RFDiffusion does not yet have all of the knobs that the normal RFDiffusion has **yet**. I recommend checking out the examples for RFDiffusion on their [repo](https://github.com/RosettaCommons/RFdiffusion)
  ```
  trill  1 diff_gen RFDiffusion --query trill/data/insulin_target.pdb --contigs 'A1-150/0 70-100' --hotspots 'A59,A83,A91' --num_return_sequences 3
  ```
  Genie2: To perform motif scaffolding, you can provide a .pdb file with the desired motifs. The following line will attempt to make a protein backbone with a minimum length of 300 amino acids and maximum of 350. It will also try to include two motifs from the input --query .pdb file, residues 15 through 100 on chain A and 100 through 150 from chain B.
  ```
  trill  1 diff_gen Genie2 --query path/to/example.pdb --contigs 300-350 --motifs 'A-15-100 B-100-150'
  ```
### 7. Predicting protein 3D structures
  You can predict 3D protein structures rapidly in bulk using ESMFold. The output will be PDB files.
  ```
  trill  1 fold ESMFold trill/data/query.fasta
  ```
  With co-folding models like Chai and Boltz, you are able to predict the 3D structure of protein sequences in complex with the input ligands, which can be nucleic acids or small-molecules. These ligands are passed as .fasta files and examples of how to format that are found in trill/data/chai_example_input.fasta and trill/data/boltz_example_input.fasta respectively. 
  ```
  trill  1 fold Chai-1 trill/data/chai_example_input.fasta
  ```
  By default, Chai/Boltz run in single-sequence mode, which might not be as reliable as running in MSA mode. In order to do this, you simply just need to provide '--msa' to the fold command. Note that currently the MSA creation is performed on colabfold's shared server, you might face bottlenecks.
  ```
  trill  1 fold Chai-1 trill/data/chai_example_input.fasta --msa
  ```
  While not technically returning a 3D structure, ProstT5 is able to predict 3Di tokens from sequence alone, which can then be used with Foldseek!
  ```
  trill  1 fold ProstT5 trill/data/query.fasta
  ```
### 8. Docking
  DiffDock: Uses deep-learning to dock small-molecules to proteins. The output is ranked poses of the ligand.
  ```
  trill  1 dock DiffDock trill/data/4ih9.pdb trill/data/NAG_ideal.sdf
  ```
  Lightdock: Dock proteins to proteins using physics-based glowworm swarm optimization 
  ```
  trill  1 dock LightDock trill/data/4ih9.pdb trill/data/peptide.pdb
  ```
  Autodock Vina: Dock small-molecule(s) to a protein. Not only can you perform blind docking, but in TRILL, you are able to dock multiple ligands at once!
  ```
  trill  1 dock Vina trill/data/4ih9.pdb ligand_1.sdf ligand_2.sdf --blind
  ```
  For Smina/Vina/Gnina, note that if you don't provide --blind, TRILL will first predict potential binding pockets using [Fpocket](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-10-168) and attempt docking the ligands to all of them. You can adjust some parameters for pocket hunting like '--min_alpha_spheres', which can be lowered to try and only attempt to dock the ligand into smaller pockets.
  ```
  trill  1 dock Vina trill/data/4ih9.pdb ligand_1.sdf --min_alpha_spheres 25
  ```
  Also note that after docking with Vina/Gnina, automated [ProLIF](https://doi.org/10.1186/s13321-021-00548-6) interaction fingerprints will be computed and includes info such as HBond donors/acceptors, Van der Waals contacts etc. for each pose.
### 9. Visualize your embeddings
  Create interactive, queryable visualizations for your output embeddings in 2D. TRILL uses PCA by default, but you can specify tSNE or UMAP with --method.
  ```
  trill  1 visualize /path/to/embeddings.csv
  ```
### 10. Perform molecular simulations.
  Using OpenMM, TRILL is able to relax protein structures, which is often needed before performing docking.
  ```
  trill  1 simulate /path/to/protein.pdb --just_relax
  ```
  You are also able to perform MD simulations to probe protein-ligand interactions. By default, the amber14 forcefield is used and the Hawkins-Cramer-Truhlar GBSA implicit solvent model. After the simulation, binding energies are predicted with MMGBSA, ProLIF fingerprints are computed, RMSD over the whole trajectory in reference to the first frame, and RMSF for each residue.
  ```
  trill  1 simulate /path/to/protein.pdb --ligand /path/to/ligand.sdf
  ```
  To perform your simulation with explicit solvent, simply provide one of the options for solvents. The example below uses the [TIP3P](http://docs.openmm.org/latest/userguide/zbibliography.html#id22) water model and ions. The same downstream analysis in the example above is performed on this simulation too. Currently, MMGBSA is computed by stripping the solvent and associated ions. Please let me know if MMPBSA is something of interest, I have chosen to not include it for now due to how time-consuming the calculations are.
  ```
  trill  1 simulate /path/to/protein.pdb --ligand /path/to/ligand.sdf --solvent ‘amber14/tip3p.xml’
  ```
  You can also provide the raw .pdbqt output file from Smina/Vina/Gnina docking that contain the top-predicted poses and provide it as input for --ligand. This will automatically parse the .pdbqt input and perform a simulation with each pose.
  ```
  trill  1 simulate /path/to/protein.pdb --ligand /path/to/ligand.sdf --solvent ‘amber14/tip3p.xml’
  ```
### 11. Leverage pretrained classifiers or train your own custom ones.
  Currently, TRILL offers several pretrained protein classifiers. These include EpHod (optimal pH for enzymatic activity), TemStaPro (thermostability), M-Ionic (metal-ion binding), ECPICK (enzyme commission), PSALM (PFAM domain and clan), CatPred (kcat, kM and kI), CataPro (kcat, kM), and PSICHIC (binding affinity, agonist/antagonist, and non-binding). The predictions from the models will be saved as .csv files. Note that for CatPred, CataPro and PSICHIC, --smiles is required. 
  ```
  trill  1 classify EpHod trill/data/query.fasta
  ```
  TRILL also allows users to train custom LightGBM/XGBoost classifiers or Isolation Forest anomaly detectors with the average sequence representation extracted with a protein language model. While XGBoost benefits from a balanced training set, the iForest only needs one label and it predicts whether a protein is an anomaly or not. To train a model, you only need to provide protein sequences in fasta form, as well as a csv that contains the class mappings. First, you can use the utils command to prepare the class key by either passing a directory with --dir and your desired classes should be separated into different fasta files according to their class. If there are 5 fasta files, there will be 5 classes. You can also pass a .txt file with absolute paths to fasta files separated by new lines and every fasta file will be treated as a unique class.
  ```
  trill  0 utils prepare_class_key --fasta_paths_txt my_classes.txt
  ```
  Once you have your key, you can train your custom XGBoost model! TRILL automatically partitions your sequences into training and validation sets, you can adjust the ratio with --train_split. After training, the model is evaluated on a held-out validation set and metrics such as F-score are calculated.
  ```
  trill  1 classify XGBoost train_master.fasta --train_split .8 --key my_key.csv 
  ```
  The XGBoost model will be saved as a .json, which can be loaded with --preTrained to predict the classes of new sequences. Note that if you have already embedded your sequences, you can pass the csv with --preComputed_Embs and the corresponding model that was used to create the embeddings with --emb_model. The preComputed_Embs must be extracted from the same model that the XGBoost model was trained on to begin with. Regardless, the predictions will be saved as a csv. 
  ```
  trill  1 classify XGBoost test_master.fasta --preTrained my_xgboost.json
  ```
  You can also pass '--sweep' when training a LightGBM/XGBoost model in order to perform a hyperparameter sweep over '--sweep_iters' trials, with the default being 10. 
  ```
  trill  1 classify XGBoost train_test.fasta --train_split .8 --key my_key.csv 
  ```
  With ESM2 only for now, you can perform end-to-end fine-tuning with a multilayer perceptron classification head. This differs from training other custom classifiers in TRILL, since those involve using frozen pre-trained models like ESM2 to extract the protein embeddings, which are then fed into a downstream classifier. With ESM2+MLP, you are able to perform masked-language modeling on your input sequences with ESM2 while simultaneously training the classifier, hopefully leading to optimized performance since the embeddings can actually change over the course of training in order to optimize the classification success.
  ```
  test 1 classify ESM2+MLP train.fasta --key key.csv --epochs 1 --train_split 0.9
  ```
  You might find yourself in a situation where you have a protein classification of interest, but there isn't an obvious way to find negative examples of this classification. Using just one type of label, you can train an Isolation Forest to predict whether new sequences are anomalies. 
  ```
  trill  1 classify iForest train.fasta --emb_model esm2_t30_150M
  trill  1 classify iForest test.fasta --emb_model esm2_t30_150M --preTrained my_iforest.skops
  ```
### 12. Use end-to-end workflows.
  While TRILL is mostly "choose your own adventure", as in you can chain together commands to achieve workflow, there is a "workflow" command that can perform these procedures with just one command. The only workflow currently included in TRILL is [Foldtuning](https://doi.org/10.1101/2023.12.22.573145). This automated pipeline takes as input just protein sequences and through an iterative process, generates protein sequences that are predicted to have similar fold/function to the inputs, but with decreasing sequence similarity over each round of fine-tuning. By default, five rounds of foldtuning will be performed on your inputs.
  ```
  trill test 1 workflow foldtune example.fasta
  ```
  While currently not experimentally validated, TRILL also offers "fast-foldtuning", which skips the time-consuming structural prediction with ESMFold step by extract 3Di tokens with ProstT5 instead to perform structural comparisons. In limited testing, this sped-up version of foldtuning can be ~7x faster than the original version.
  ```
  trill test 1 workflow foldtune example.fasta --fast_folding 
  ```
## Misc. Tips

- **Safetensors Support**: TRILL now supports safer model loading with safetensors format. When loading PyTorch models (.pt files), TRILL will automatically:
  - Look for a corresponding .safetensors file first (safer format)
  - Fall back to torch.load with security warnings if only .pt files are available
  - Recommend upgrading to PyTorch 2.6+ if using .pt files due to security vulnerabilities (CVE-2025-32434)
  - You can convert existing .pt files to safetensors format using the utils command:
    ```
    trill 0 utils convert_to_safetensors --pt_file model.pt
    ```
- Make sure there are no "\*" in the protein sequences
- After finetuning and trying to save a model using deepspeed, if all the CPU RAM is used the application can crash and not finish saving, leaving you a directory similar to "your_model.pt". You can rescue your model by running this python script
  ```  python
  from pytorch_lightning.utilities.deepspeed import convert_zero_checkpoint_to_fp32_state_dict
  convert_zero_checkpoint_to_fp32_state_dict(“your_model.pt”, “rescued_model.pt”)
  ```  
- If you are using TRILL on Google Colab, you need to start your commands with an "!".
  ```
  !trill  1 embed esm2_t12_35M trill/data/query.fasta
  ```
- If you recieve this error when trying to use deepspeed CPU offloading
  ```
  AttributeError: 'DeepSpeedCPUAdam' object has no attribute 'ds_opt_adam'
  ```
  you can potentially fix the issue by using mamba or micromamba to install -c "nvidia/label/cuda-11.7.0" cuda-nvcc
